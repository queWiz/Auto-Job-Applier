from fetcher.indeed_scraper import IndeedScraper
from filter_queue.filter import filter_and_queue
from applier.selenium_apply import SeleniumApplier
from utils.logger import log_success
from config import CFG
import json

def main():
    # 1. Scrape listings
    fetcher = IndeedScraper(
        user_agent=CFG['user_agent'],
        proxy=CFG.get('proxy')
    )
    raw_listings = fetcher.search(CFG['keywords'], CFG['locations'])

    # 2. Filter & queue
    filter_and_queue(raw_listings)

    # 3. Apply to easy-apply jobs
    with open('data/to_apply.json') as f:
        to_apply = json.load(f)
    applier = SeleniumApplier(headless=True)
    for job in to_apply:
        resume = CFG['resume_variants'][0]
        cover = "Automated cover letter for {role} at {company}".format(
            role=job['title'], company=job['company']
        )
        applier.apply(job, resume, cover)
        log_success(job['url'])

if __name__ == '__main__':
    main()
