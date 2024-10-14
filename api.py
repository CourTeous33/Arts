import requests
import json
import pandas as pd

if __name__ == "__main__":
    # 呼叫 10 個變數
    for i in range(10):
        res = requests.post('http://127.0.0.1:8080/Generate', json={"Type": "hexadecimal"})
        if res.ok:
            print(res.json())
