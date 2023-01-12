import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")

  citation_needed = soup.find_all(class_='noprint Inline-Template Template-Fact')

  citation_count = len(citation_needed)
  print(f"There are {citation_count} passages that need citations.\n")
  return citation_count

def get_citations_needed_report(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")

  citation_needed = soup.find_all(class_='noprint Inline-Template Template-Fact')

  citation_report = "Passages Needing Citations:\n\n"

  for c in citation_needed:
    paragraph = c.parent.text
    citation_report += "\n"
    citation_report += paragraph
    citation_report += "\n"

  print(citation_report)
  return(citation_report)

if __name__ == "__main__":
  url = "https://en.wikipedia.org/wiki/Babylon"
  get_citations_needed_count(url)
  get_citations_needed_report(url)
