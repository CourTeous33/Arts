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
    # compare = [0, 2, 4, 8, 16, 32, 64, 128]
    # num = [random.randint(0, 1) for i in range(8)]
    num = random.randint(0, 255)

    if Type == "string":
        output = f'{num:0b}'
        output = output.zfill(8)
    elif Type == "int":
        output = str(num)
        output = output.zfill(3)
    elif Type == "binary":
        output = f'{num:0b}'
        output = output.zfill(8)
    elif Type == "octal":
        output = f'{num:0o}'
        output = output.zfill(4)
    elif Type == "hexadecimal":
        output = f'{num:0x}'
        output = output.zfill(2)
    else:
        output = str(num)
        
    return output