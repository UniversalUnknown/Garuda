import requests
from bs4 import BeautifulSoup

url = "https://vitcolab945.examly.io/mycourses/details?id=..&type=mylabs"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    paragraphs = soup.find_all('p')
    extracted_text = '\n'.join([para.get_text() for para in paragraphs])
    
    print("Extracted Text from Webpage:")
    print(extracted_text)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
