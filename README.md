# 🚀 InternPilot

**AI-Powered Internship Discovery & Matching Platform**

InternPilot is an intelligent internship discovery platform that automates the process of finding, filtering, ranking, and tracking internship opportunities. Instead of manually searching across multiple job boards, InternPilot aggregates internships from various sources, applies AI-powered semantic matching based on a candidate's profile, generates recruiter outreach suggestions, and delivers real-time notifications.

---

## 🎯 Problem Statement

Students often spend hours searching through multiple job portals, evaluating opportunities, and manually tracking applications. Most opportunities are either missed or discovered too late.

InternPilot solves this by:

* Aggregating internships from multiple sources
* Ranking opportunities using AI-powered semantic similarity
* Generating recruiter discovery links
* Drafting outreach messages
* Sending real-time alerts for relevant opportunities
* Providing a foundation for application tracking and skill-gap analysis

---

## ✨ Features

### Multi-Source Internship Aggregation

* Y Combinator Work at a Startup
* Wellfound
* Internshala
* Extensible architecture for additional job sources

### AI-Powered Matching

* Sentence Transformers embeddings
* Cosine similarity scoring
* Profile-based opportunity ranking
* Personalized recommendations

### Smart Notifications

* Telegram Bot integration
* Instant internship alerts
* Match-score-based notifications

### Recruiter Discovery

* Automated recruiter search generation
* LinkedIn-focused search workflows
* Outreach support

### Outreach Generation

* AI-assisted recruiter messaging
* Personalized outreach templates
* Cold outreach workflow support

### Data Management

* Job deduplication
* Historical storage
* Modular JSON-based architecture

---

## 🏗️ System Architecture

```text
                 ┌──────────────────┐
                 │ Job Sources      │
                 │ YC / Wellfound   │
                 │ Internshala      │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Scrapers         │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Job Aggregator   │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ AI Matching      │
                 │ Sentence         │
                 │ Transformers     │
                 └────────┬─────────┘
                          │
          ┌───────────────┼───────────────┐
          ▼                               ▼
 ┌─────────────────┐            ┌─────────────────┐
 │ Recruiter       │            │ Telegram Alerts │
 │ Discovery       │            │ Notifications   │
 └─────────────────┘            └─────────────────┘
```

---

## 🧠 Tech Stack

### Programming

* Python

### AI / Machine Learning

* Sentence Transformers
* Scikit-learn
* Cosine Similarity

### Automation

* Playwright

### Notifications

* Telegram Bot API

### Data Storage

* JSON

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
internpilot/

├── ai/
│   ├── embedder.py
│   ├── scorer.py
│   ├── outreach.py
│   ├── recruiter_finder.py
│   └── skill_gap.py
│
├── scrapers/
│   ├── yc.py
│   ├── wellfound.py
│   └── internshala.py
│
├── notifier/
│   └── telegram_bot.py
│
├── tracker/
│   └── application_tracker.py
│
├── data/
│   ├── profile.json
│   ├── jobs.json
│   ├── applications.json
│   └── seen_jobs.json
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/internpilot.git

cd internpilot
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright Browsers

```bash
playwright install
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

---

## ▶️ Running the Project

```bash
python main.py
```

InternPilot will:

1. Scrape internships
2. Aggregate opportunities
3. Calculate AI match scores
4. Generate recruiter discovery links
5. Create outreach suggestions
6. Send Telegram alerts

---

## 📈 Future Roadmap

### Planned Features

* Streamlit Dashboard
* Resume Matching Engine
* Skill Gap Analysis
* Company Watchlists
* LinkedIn Hiring Post Detection
* Application Tracking Dashboard
* Daily Automated Execution
* Recruiter Email Discovery
* Advanced Ranking Models

---

## 🎓 Learning Outcomes

Through InternPilot, I explored:

* Web Automation
* Information Retrieval
* Recommendation Systems
* NLP Embeddings
* Semantic Search
* Software Architecture
* Automation Pipelines
* Product-Oriented AI Development

---

## 👨‍💻 Author

**Yashas Raina**

B.Tech Artificial Intelligence & Machine Learning

GitHub: https://github.com/yashasnot

LinkedIn: www.linkedin.com/in/yashas-raina-985910292
