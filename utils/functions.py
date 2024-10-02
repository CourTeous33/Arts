import random

def gen(Type="string", num=0):
    '''
    Generate a random number between 1 and 100
    Type: str, default "string"
    Help: Type of output, "string",
                          "int",
                          "binary",
                          "octal",
                          "hexadecimal",
    '''
    num = random.randint(1, 10000)

    if Type == "string":
        output = str(num)
    elif Type == "int":
        output = num
    elif Type == "binary":
        output = bin(num)
    elif Type == "octal":
        output = oct(num)
    elif Type == "hexadecimal":
        output = hex(num)
    else:
        output = str(num)
        
    return output