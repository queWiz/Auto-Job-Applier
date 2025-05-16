# 🧠 Job Scraper & Auto-Apply Bot

An automated job/internship application tool built with Python, BeautifulSoup, and Selenium.

## 🔍 What It Does

- **Scrapes** job listings from Indeed based on:
  - Keywords (e.g. Software Engineer Intern, Data Analyst Intern)
  - Location (Singapore / Remote)
  - Salary threshold (if provided)

- **Automatically applies** to jobs that:
  - Only require resume uploads (i.e. "Easy Apply")

- **Saves** complex listings (e.g., multi-step forms) to a CSV for manual follow-up.

## 📂 Structure

- `fetcher/` — Scrapes listings from job boards (IndeedScraper)
- `filter_queue/` — Filters listings by salary, keywords, recency
- `applier/` — Uses Selenium to auto-apply to jobs
- `utils/` — Logging and history tracking
- `templates/` — Cover letter template
- `data/` — Auto and manual queues (`to_apply.json`, `skipped.csv`, `applied.db`)
- `docs/` — Component documentation for Cursor AI
- `.github/workflows/` — GitHub Actions workflow

## ⚙️ Technologies

- Python
- requests, BeautifulSoup
- Selenium
- YAML config
- GitHub Actions (optional)
- CSV / JSON logging

## 📅 How to Run

1. Edit `config.yaml` to match your keywords, location, salary, and resume paths  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```  
3. Run:
   ```bash
   python main.py
   ```  
4. Optionally schedule it via GitHub Actions or run manually.

