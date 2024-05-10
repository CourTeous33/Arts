import requests
import json
import pandas as pd

# response = requests.get("http://127.0.0.1:8080/")
# resultText = response.text

# print(resultText)

for i in range(10):
    res = requests.post('http://127.0.0.1:8080/Generate', json={"Type": "int"})
    if res.ok:
        print(res.json())

# 呼叫 10 個變數