
import requests

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

data = requests.get(url,headers=header)
print(data)
print(data.text)