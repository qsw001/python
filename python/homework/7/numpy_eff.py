import numpy as np
import time
import timeit

def NativeTest():
    python_list = list(range(1000000))

    start_time = time.time()
    result = [x*2 for x in python_list]
    end_time = time.time()

    print("python:",end_time-start_time)

def NumpyTest():
    numpy_array = np.arange(1000000)

    start_time = time.time()
    result = numpy_array*2
    end_time = time.time()

    print("numpy:",end_time-start_time)

if __name__ == "__main__":
    accurateTime = timeit.timeit(NativeTest, number=20)
    print("python:",accurateTime/20)

    accurateTime = timeit.timeit(NumpyTest, number=20)
    print("numpy",accurateTime/20)
