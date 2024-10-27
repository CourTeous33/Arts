from matplotlib import pyplot as plt

def gen_img(random_number=0, idx=0):
    '''
    Generate a random image
    '''
    R = int(random_number[idx])
    idx += 1
    G = int(random_number[idx])
    idx += 1
    B = int(random_number[idx])
    idx += 1

    # # Display the image
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    # # ax.set_title('Random Image')
    # ax.imshow([[[R, G, B]]])
    # # print(np.array([[[R, G, B]]]).shape)
    return [[[R, G, B]]], idx

if __name__ == "__main__":
    color = [10,100,188] 
    idx = 0
    fig, idx = gen_img(color, idx)
    print(fig)
    # plt.show()