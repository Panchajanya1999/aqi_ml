import csv
import requests
from bs4 import BeautifulSoup

# Define the URL of the website to scrape
url = "https://www.airnow.gov/index.cfm?action=airnow.city&zipcode=94103"

# Send a GET request to the website
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the relevant elements containing the air quality data
air_quality_elements = soup.find_all("div", class_="air-quality")

# Create a list to store the extracted data
data = []

# Extract the air quality data and append it to the list
for element in air_quality_elements:
    city = element.find("span", class_="city").text.strip()
    quality = element.find("span", class_="quality").text.strip()
    data.append([city, quality])

# Define the path and filename for the CSV file
csv_file = "air_quality_data.csv"

# Write the data to the CSV file
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["City", "Air Quality"])  # Write header row
    writer.writerows(data)

print(f"Air quality data has been scraped and saved to {csv_file}.")
