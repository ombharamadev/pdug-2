import pandas as pd
import requests
import json



date = "2024-07-07"
url = "https://vegetablemarketprice.com/api/dataapi/market/himachalpradesh/daywisedata?date="+str(date)+""

header = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ga=GA1.1.579592366.1719805178; JSESSIONID=D40CEFB8547AFB0C60996DA07E91FEAC; __gads=ID=d417311b4ca58bd6:T=1719805164:RT=1720413465:S=ALNI_MZBDVVGHlSQqR5k0P8vj4Ymc9foyA; __gpi=UID=00000e6d610639a0:T=1719805164:RT=1720413465:S=ALNI_MbOlZIJQSQMot2btmDNHhDbbUpTNw; __eoi=ID=5fb93107935acbae:T=1719805164:RT=1720413465:S=AA-Afjbak2cMxgawT7R_UvUzAL3n; FCNEC=%5B%5B%22AKsRol9_WQtqgnXbtabRnQoMZGwDjtiSlSfxjTFRiv4a38syp1kJUToWOHXPJ1nfMr_jp3P4FLJHeazx66XTVOBe9c2MdztBl7yluLoApveZyZseQLeAmigsS-MVktEWVvDJAB6DxSPGdqvjAPXCoijqnx9ZmBNBGQ%3D%3D%22%5D%5D; _ga_2RYZG7Y4NC=GS1.1.1720413452.3.1.1720413488.0.0.0",
    "Referer": "https://vegetablemarketprice.com/market/himachalpradesh/today",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }

data = requests.get(url,headers=header)
print(data)

js_data = json.loads(data.text)

js_arr = []
for api in js_data["data"]:
    print(api)
    veg_name = str(api["vegetablename"])
    price = str(api["price"])
    retail_price = str(api["retailprice"])
    unit = str(api["units"])
    mall_price = str(api["shopingmallprice"])
    new_js = {
        "date":str(date),
        "veg_name":veg_name,
        "price":price,
        "retail_price":retail_price,
        "mall_price":mall_price,
        "unit":unit,
    }
    js_arr.append(new_js)

df = pd.DataFrame(js_arr)
df.to_csv("out.csv")