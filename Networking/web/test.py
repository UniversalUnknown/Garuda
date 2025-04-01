import requests
THINGSPEAK_CHANNEL_ID = "2874616"
WRITE_API_KEY = "WI18D2PC7EW6CC8B"
READ_API_KEY = "YYHRGB8OL7VTH9H8"
def read_latest_data():
    url = f"https://api.thingspeak.com/channels/2874616/feeds.json?api_key=YYHRGB8OL7VTH9H8&results=2"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("Latest Data:", data['feeds'][0])  # Print latest sensor readings
    else:
        print("Error fetching data:", response.status_code)
def write_data(field1_value, field2_value=None, field3_value=None):
    url = f"https://api.thingspeak.com/update?api_key=WI18D2PC7EW6CC8B&field1=0"
    payload = {
        'field1': field1_value,
        'field2': field2_value,
        'field3': field3_value
    }
    response = requests.post(url, params=payload)
    if response.status_code == 200:
        print("Data written successfully. Response:", response.json())
    else:
        print("Error writing data:", response.status_code)
def main():
    read_latest_data()
    write_data(field1_value=25.5, field2_value=60.0, field3_value=1013.0)  # Example values

if __name__ == "__main__":
    main()