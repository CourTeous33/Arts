def permute_list(num=6, random_number=0, idx=0):
    
    num_list = [i for i in range(num)]
    tmp = []
    for i in range(num):
        tmp.append(num_list.pop(random_number[idx]%len(num_list)))
        idx += 1

    return tmp

def gen_permute_sets(sets=5, ran=6, random_number=0, idx=0):
    '''
    sets: Number of permutations to generate? (1–50)
    ran: Number of objects in each permutation? (1–200)
    '''
    if ran > 200:
        ran = 200
    num_lists = {}
    for i in range(sets):
        num_lists[f"set {i}"] = permute_list(ran, random_number=random_number, idx=idx)
        idx += 1
    return num_lists, idx

if __name__ == "__main__":
    print(gen_permute_sets(sets=6, ran=3))