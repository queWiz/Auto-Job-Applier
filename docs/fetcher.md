# Fetcher Module (Scraper)

## IndeedScraper

Scrapes Indeed job listings using `requests` and `BeautifulSoup`.

### Key points

- Builds search URL from keywords & locations
- Parses job cards for title, company, link, salary, and easy-apply indicator
- Returns `JobListing` dataclasses to the pipeline
