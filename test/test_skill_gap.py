from ai.skill_gap import *

profile = [
    "Python",
    "TensorFlow",
    "Machine Learning"
]

job = [
    "Python",
    "PyTorch",
    "Docker",
    "Machine Learning"
]

print(
    find_skill_gaps(
        profile,
        job
    )
)