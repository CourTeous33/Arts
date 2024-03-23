import time
import numpy as np

if __name__ == "__main__":
    while True:
        # Generate a random number
        with open("test.json", "w") as f:
            f.write(str(np.random.randint(1, 100)))
        time.sleep(100)