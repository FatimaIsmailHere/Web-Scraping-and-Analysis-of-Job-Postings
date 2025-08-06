# Web-Scraping-and-Analysis-of-Job-Postings
This Python script scrapes job postings from a fake jobs website, extracts key information, and analyzes the most in-demand skills by city.

📌 Features
--Scrapes job title, company, location, and date posted
--Saves the data to a CSV file
--Extracts keywords from job titles (used as “skills”)
--Analyzes the most frequent skills per city
--Visualizes top 10 most frequent skill-city pairs using a horizontal bar chart
--Cleancode using only requests, BeautifulSoup, pandas, and matplotlib

📦 Requirements
Install the following Python packages:
pip install requests beautifulsoup4 pandas matplotlib

🚀 How to Run
python job_scraper.py

This will:
--Scrape data from the site
--Save a CSV file named jobs.csv
--Show a bar chart of the most common skills by city
--Print the most in-demand skills globally


