from playwright.sync_api import sync_playwright
from parser import parse


def main():
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    page = browser.new_page()
    page.goto("https://testing-www.codefellows.org")

    
    browser.close()

if __name__ == "__main__":
  main()
