# Import modules
import numpy as np
import math
import pandas as pd
from scipy.optimize import curve_fit
from scipy.linalg import toeplitz, matmul_toeplitz
import time

# get the start time
t_start = time.time()

### Program structure

    ## Parameters section
        # Data length
        # Input voltage
        # ADC info

    ## Fuction section
        # dec2bin
        # sortbin
        # Gauss
        # min_entropy
        # digit_array
        # Toe_hash
        # combine_array
        # chunk2str

    ## Main program
        # Data read
        # Convert data type to array
        # Dec2bin
        # Data sort
        # Executing curve_fit
        # Calculate quantum_SD and min_entropy
        # Prepare data chunk
        # Toeplitz hashing
        # Turn hashed chunk back to string
        # Hashed data sort
        # Output random number

### End of structure table

## Parameters section

# Data length
N = pow(10, 6) # input data length
SD = 1/math.sqrt(N) # standard deviation
# Input voltage
VR = 1 # voltage range of the data (+0.5V ~ -0.5V)
V_min = -0.5
V_max = 0.5
# ADC info
ADCRB = 12 # ADC resolution bits
min_diff = VR/pow(2, ADCRB) # minimum voltage difference
n = 200 # chunk unit number

## Fuction section

# dec2bin_string
def dec2bin(data, N, bits, diff, min):

    bit_string = [] 
    for i in data:
        value_dec = int((i.item()-min)/diff)
        bit_string.append(np.binary_repr(value_dec, bits))

    return bit_string

# Sort data into bins
def sortbin(data, bits):
    
    bin = np.array([0]*pow(2, bits))
    for i in data:
        n = int(i, 2)-1
        bin[n] = bin[n]+1

    return bin

# Define the Gaussian function 
def Gauss(x, a, x0, sigma): 
    y = a*(1/(math.sqrt(2*math.pi)*sigma))*np.exp(-0.5*((x-x0)/sigma)**2)
    return y 

# Calculate min entropy
def min_entropy(sigma, x, nbin):

    prob = [0]*nbin
    for i in x:
        prob[i] = 0.5*math.erf((x[i]-nbin/2+0.5)/(math.sqrt(2)*sigma))-0.5*math.erf((x[i]-nbin/2-0.5)/(math.sqrt(2)*sigma))

    entropy = -math.log(max(prob),2)
    return entropy

# String list to element array
def digit_array(string_list, N, bits, n):

    digit_list = [[int(d) for d in element] for element in string_list]
    digit_list = np.array(digit_list)
    digit_list = digit_list.transpose()
    digit_list = digit_list.reshape(bits*n, int(N/n))

    return digit_list

# Toeplitz hashing
def Toe_hash(chunk, m, n):

    c = np.random.randint(2, size=m)
    r = np.random.randint(2, size=n)
    hashed_chunk = (toeplitz(c, r) @ chunk) % 2

    return hashed_chunk

# element array to string list
def combine_array(digit_list, N, bits):

    combine = [] 
    for i in range(N):
        bit_string = ''
        for j in range(bits):
            bit_string = bit_string + str(digit_list[i, j])
        combine.append(bit_string)

    return combine

# chunk2string
def chunk2str(chunk, N, bits):

    string_list = chunk.reshape(bits, N)
    string_list = string_list.transpose()
    string_list = combine_array(string_list, N, bits)

    return string_list


## Main program
if __name__ == "__main__":
    # Data read
    data_VS_1 = pd.read_csv("Moku_20240522_1300.csv",
                    sep=',',index_col=0,skiprows=9,nrows=N)
    data_DN_1 = pd.read_csv("Moku_20240522_darknoise.csv",
                    sep=',',index_col=0,skiprows=9,nrows=N)
    # VS = Vacuum State
    # DN = Dark Noise

    # Convert data type to array
    data_VS_2 = np.asarray(data_VS_1)
    data_DN_2 = np.asarray(data_DN_1)

    # dec2bin
    data_VS_3 = dec2bin(data_VS_2, N, ADCRB, min_diff, V_min)
    data_DN_3 = dec2bin(data_DN_2, N, ADCRB, min_diff, V_min)

    # Data sort
    prob_VS = sortbin(data_VS_3, ADCRB)
    prob_DN = sortbin(data_DN_3, ADCRB)
    # prob = probability distribution

    # Executing curve_fit
    x = np.array(np.arange(pow(2, ADCRB)))
    # popt = optimal parameters 
    # pcov = covariance of popt
    popt_VS, pcov_VS = curve_fit(Gauss, x, prob_VS, p0 = (0 ,1 ,pow(2, ADCRB)/2))
    popt_DN, pcov_DN = curve_fit(Gauss, x, prob_DN, p0 = (0 ,1 ,pow(2, ADCRB)/2))
    fit_y_VS = Gauss(x, popt_VS[0], popt_VS[1], popt_VS[2])
    fit_y_DN = Gauss(x, popt_DN[0], popt_DN[1], popt_DN[2]) 

    # Calculate quantum_SD and min_entropy
    quantum_sigma = math.sqrt(popt_VS[2]**2-popt_DN[2]**2)
    #print('quantum signal:',quantum_sigma)
    #print('minimum entropy:',min_entropy(quantum_sigma, x, pow(2, ADCRB)))
    output_bit = math.floor(min_entropy(quantum_sigma, x, pow(2, ADCRB)))

    # Prepare data chunk
    data_chunk_VS = digit_array(data_VS_3, N, ADCRB, n)

    # Toeplitz hashing
    hashed_chunk = Toe_hash(data_chunk_VS, output_bit*n, ADCRB*n)

    # Turn hashed chunk back to string
    output_string = chunk2str(hashed_chunk, N, output_bit)

    # Hashed data sort
    prob_hashed = sortbin(output_string, output_bit)
    xh = np.array(np.arange(pow(2, output_bit)))

    # Output random number
    RN_out = [int(s, 2) for s in output_string]
    print(RN_out)

    # get the end time
    t_end = time.time()

    # execution time
    t_elapsed = t_end - t_start
    print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(t_elapsed)))

    ### End of CODE