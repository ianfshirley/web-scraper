import requests
from web_scraper.parser import parse


if __name__ == "__main__":
  url = "https://testing-www.codefellows.org/course-calendar/?filters=400:%20Advance,code-python-401"
  response = requests.get(url)
  results = parse(response.text)

