import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://vitcolab945.examly.io/mycourses/details?id=e3c4baa7-838c-41a6-84d6-087b0fc7acc5&type=mylabs"  # Replace with the URL you want to scrape

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract text from the webpage (you can customize this to target specific elements)
    # For example, extracting all paragraph text
    paragraphs = soup.find_all('p')
    extracted_text = '\n'.join([para.get_text() for para in paragraphs])
    
    # Print the extracted text
    print("Extracted Text from Webpage:")
    print(extracted_text)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
