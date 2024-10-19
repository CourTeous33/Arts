import random

def check_num(num):
    condition_num = num >= ord('0') and num <= ord('9')
    condition_alpha = num >= ord('A') and num <= ord('Z')
    condition_alpha2 = num >= ord('a') and num <= ord('z')
    condition_3 = num == ord('_')
    condition = condition_num or condition_alpha or condition_alpha2 or condition_3
    return condition

def gen_alphabet():
    num = random.randint(0, 255)
    condition = check_num(num)
    while not condition:
        num = random.randint(0, 255)
        condition = check_num(num)
    output = chr(num)

    return output

if __name__ == "__main__":
    for i in range(1024):
        print(gen_alphabet(), end="")