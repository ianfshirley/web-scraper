import requests
from bs4 import BeautifulSoup

def parse(markup):
  soup = BeautifulSoup(markup, "html.parser")

  # need to inspect the website you're scraping to find where the data you want it. Class names, html elements etc.
  courses = soup.select(".calendar-event")

  course_info = "Course Info\n"

  for course in courses:
    if "Python" in course.h1.text:
      course_info += course.h1.text + "\n"
      course_info += course.h1.text + "\n"
      course_info += "\n"

  return course_info