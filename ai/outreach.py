from transformers import pipeline


generator = pipeline(
    "text-generation",
    model="distilgpt2"
)


def generate_outreach(job):

    prompt = f"""
Write a concise professional LinkedIn outreach message.

Candidate:
AI/ML student interested in fintech and startups.

Job:
{job['title']}

Type:
{job['type']}

Source:
{job['source']}

Message:
"""

    result = generator(
        prompt,
        max_length=120,
        num_return_sequences=1
    )

    generated_text = (
        result[0]["generated_text"]
    )

    return generated_text