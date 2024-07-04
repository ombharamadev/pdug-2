
import pandas as pd

js_data = [
    {
        "name":"aryan",
        "age":"21"
    },{
        "name":"kalki",
        "age":"1500"
    }
]

df  = pd.DataFrame(js_data)
df.to_csv("out.csv")