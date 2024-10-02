import random

def gen(Type="string"):
    '''
    Generate a random number between 1 and 100
    Type: str, default "string"
    Help: Type of output, "string",
                          "int",
                          "binary",
                          "octal",
                          "hexadecimal",
    '''
    # output = str(random.randint(1, 100))
    if Type == "string":
        output = str(random.randint(1, 100))
    elif Type == "int":
        output = random.randint(1, 100)
    elif Type == "binary":
        output = bin(random.randint(1, 100))
    elif Type == "octal":
        output = oct(random.randint(1, 100))
    elif Type == "hexadecimal":
        output = hex(random.randint(1, 100))
    else:
        output = output = str(random.randint(1, 100))
        
    return output