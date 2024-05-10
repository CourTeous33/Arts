import random

def gen(Type="string"):
    # output = str(random.randint(1, 100))
    if Type == "string":
        output = str(random.randint(1, 100))
    else:
        output = random.randint(1, 100)
    return output