import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Loading the website
url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Finding all job listings
job_cards = soup.find_all('div', class_='card-content')

# Extracting data and saving into lists
titles = []
companies = []
locations = []
dates = []

for job in job_cards:
    title = job.find('h2', class_='title').text.strip()
    company = job.find('h3', class_='company').text.strip()
    location = job.find('p', class_='location').text.strip()
    date_posted = job.find('time')['datetime'].strip()

    titles.append(title)
    companies.append(company)
    locations.append(location)
    dates.append(date_posted)

# Creating DataFrame
df = pd.DataFrame({
    'Job Title': titles,
    'Company': companies,
    'Location': locations,
    'Date Posted': dates
})

# Saving to CSV
df.to_csv('jobs.csv', index=False)

print("Scraping done.Saved to 'jobs.csv'")
print(df.head())

# Analyzing the most in-demand job roles
most_common_roles = df['Job Title'].value_counts().reset_index()
most_common_roles.columns = ['Job Title', 'Count']

print("Top 10 Most In-Demand Job Roles:")
print(most_common_roles.head(10))
# Visualize all common skills (words from job titles) by city

# Combining job title and location into one DataFrame
df2= df[['Job Title', 'Location']]

# Converting to lowercase and spliting words from job titles
skill_city = []

for i, row in df2.iterrows():
    words = row['Job Title'].lower().split()
    for word in words:
        if len(word) > 2:
            skill_city.append([row['Location'], word])

# Making a DataFrame
skill_df = pd.DataFrame(skill_city, columns=['City', 'Skill'])

# Counting occurrences
skill_counts = skill_df.groupby(['City', 'Skill']).size().reset_index(name='Count')
skill_counts = skill_counts.sort_values('Count', ascending=False)

# Limit to top 10 rows
top10 = skill_counts.head(10)

# plotting
plt.figure(figsize=(12, 6))
top10.loc[:, 'Label'] = top10['City'] + " | " + top10['Skill']
plt.barh(top10['Label'], top10['Count'])

plt.xlabel('Count')
plt.title('Most Frequent Skills by City (All)')
plt.tight_layout()
plt.show()
