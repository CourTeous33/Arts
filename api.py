import requests

from matplotlib import pyplot as plt

if __name__ == "__main__":
    # 呼叫 10 個變數
    print("Random Number")
    for i in range(3):
        res = requests.post('http://127.0.0.1:8080/Generate', json={"Type": "hexadecimal"})
        if res.ok:
            num = res.json()["Random Number"]
            print(num, end="")
    print() # 換行
    
    
    # 更新 10 個色塊
    fig = plt.figure(figsize=(1, 1))
    ax = fig.gca()
    img = ax.imshow([[[0, 0, 0]]])
    ax.axis('off')
    plt.show(block=False)
    plt.pause(0.5)

    for i in range(10):
        res = requests.post('http://127.0.0.1:8080/Picture', json={})
        if res.ok:
            rgb = res.json()["pixel"]
            img.set_data(rgb)
            plt.pause(0.1)
            ax.draw_artist(img)
        # fig.canvas.draw_idle()
    plt.close()

    # 呼叫1024個字元
    print("Alphabet")
    for i in range(1024):
        res = requests.post('http://127.0.0.1:8080/Alphabet', json={})
        if res.ok:
            word = res.json()["Random Alphabet"]
            print(word, end="")
    
    print() # 換行
    
    # 呼叫5個排列
    print("Permute")
    res = requests.post('http://127.0.0.1:8080/Permute', json={"sets": 5, "ran": 6})
    if res.ok:
        sets = len(res.json().keys())
        for i in range(sets):
            word = res.json()[f"set {i}"]
            print(f"set {i}:", word)
    else:
        print("Error")


    # 呼叫6個骰子
    print("Dice")
    res = requests.post('http://127.0.0.1:8080/Dice', json={"sets": 4, "ran": 6, "min_num": 1, "max_num": 49})
    if res.ok:
        sets = len(res.json().keys())
        for i in range(sets):
            word = res.json()[f"set {i}"]
            print(f"set {i}:", word)
    else:
        print("Error")