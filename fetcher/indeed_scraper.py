import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dataclasses import dataclass

@dataclass
class JobListing:
    title: str
    company: str
    url: str
    date_posted: datetime.date
    salary: int
    easy_apply: bool

class IndeedScraper:
    BASE_URL = "https://sg.indeed.com/jobs"

    def __init__(self, user_agent: str, proxy: str=None):
        self.headers = {"User-Agent": user_agent}
        self.proxies = {"http": proxy, "https": proxy} if proxy else None

    def search(self, keywords, locations):
        listings = []
        q = "+".join(keywords)
        l = "+".join(locations)
        url = f"{self.BASE_URL}?q={q}&l={l}"
        resp = requests.get(url, headers=self.headers, proxies=self.proxies)
        soup = BeautifulSoup(resp.text, "html.parser")

        for card in soup.select("div.jobsearch-SerpJobCard"):
            title = card.select_one("h2.title a")["title"].strip()
            company = card.select_one("span.company").get_text(strip=True)
            link = "https://sg.indeed.com" + card.select_one("h2.title a")["href"]
            date_txt = card.select_one("span.date").get_text(strip=True)
            salary_tag = card.select_one("span.salaryText")
            salary = int(salary_tag.get_text(strip=True)
                          .replace("SGD","")
                          .replace(",","")
                          .split()[0]) if salary_tag else 0
            easy = bool(card.select_one("span.iaLabel"))
            listings.append(JobListing(title, company, link, datetime.today().date(), salary, easy))
        return listings
