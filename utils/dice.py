import random

def gen_list(num=6, min_num=1, max_num=6):
    
    num_list = [i for i in range(min_num, max_num+1)]
    tmp = []
    for i in range(num):
        tmp.append(num_list.pop(random.randint(0, 255)%len(num_list)))

    return tmp

def gen_dice_sets(sets=5, ran=6, min_num=1, max_num=6):
    '''
    sets: Number of permutations to generate? (1–50)
    ran: Number of objects in each permutation? (1–200)
    min_num: Minimum number of dice? (0–254)
    max_num: Maximum number of dice? (1–255)
    '''
    if max_num < ran:
        return {"sets 0": "Input is not valid. Not enough numbers to generate set."}
    elif min_num > max_num:
        return {"sets 0": "Input is not valid. Minimum number is greater than maximum number."}
    
    if ran > 200:
        ran = 200
    num_lists = {}
    for i in range(sets):
        num_lists[f"set {i}"] = gen_list(ran, min_num, max_num)
    
    return num_lists

if __name__ == "__main__":
    print(gen_dice_sets(sets=6, ran=2, min_num=2, max_num=3))