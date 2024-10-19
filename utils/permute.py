import random

def permute_list(num=6):
    
    num_list = [i for i in range(num)]
    tmp = []
    for i in range(num):
        tmp.append(num_list.pop(random.randint(0, 255)%len(num_list)))

    return tmp

def gen_permute_sets(sets=5, ran=6):
    '''
    sets: Number of permutations to generate? (1–50)
    ran: Number of objects in each permutation? (1–200)
    '''
    if ran > 200:
        ran = 200
    num_lists = {}
    for i in range(sets):
        num_lists[f"set {i}"] = permute_list(ran)
    
    return num_lists

if __name__ == "__main__":
    print(gen_permute_sets(sets=6, ran=3))