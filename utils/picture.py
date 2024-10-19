import random
import numpy as np
from matplotlib import pyplot as plt

def gen_img():
    '''
    Generate a random image
    '''
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    # # Display the image
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    # # ax.set_title('Random Image')
    # ax.imshow([[[R, G, B]]])
    # # print(np.array([[[R, G, B]]]).shape)
    return [[[R, G, B]]]

if __name__ == "__main__":
    fig = gen_img()
    plt.show()