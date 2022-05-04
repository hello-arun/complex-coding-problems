from math import sin, cos, pi
from timeit import timeit
# Recursive function of FFT


def fft(a):
    n = len(a)
    # if input contains just one element
    if n == 1:
        return [a[0]]
    # For storing n complex nth roots of unity
    theta = 2*pi/n
    w = list(complex(cos(theta*i), sin(theta*i)) for i in range(n))
    # print(w)
    # Separate coefficients
    Aeven = a[0::2]
    Aodd = a[1::2]
    # Recursive call for even indexed coefficients
    Yeven = fft(Aeven)
    # Recursive call for odd indexed coefficients
    Yodd = fft(Aodd)
    # for storing values of y0, y1, y2, ..., yn-1.
    Y = [0]*n
    middle = n//2
    for k in range(n//2):
        w_yodd_k = w[k] * Yodd[k]
        yeven_k = Yeven[k]
        Y[k] = yeven_k + w_yodd_k
        Y[k + middle] = yeven_k - w_yodd_k
    return Y


def direct(a):
    # convert from a0+a1*x+a2*xx+a3*xxx => a3*xxx+a2*xx+a1*x+a0
    a = a[::-1]
    n = len(a)
    Y = [0]*n
    theta = 2*pi/n
    n_roots = list(complex(cos(theta*i), sin(theta*i)) for i in range(n))
    for i, root in enumerate(n_roots):
        result = a[0]
        # Evaluate value of polynomial using Horner's method
        for i in range(1, n):
            result = result*root + a[i]
        Y[i] = result
    return Y


# Driver code
if __name__ == '__main__':
    # Poly a_n(x^n) => n range from 0 to n-1
    a = [1]*512
    time_direct = timeit(lambda: direct(a), number=10000)
    time_fft = timeit(lambda: fft(a), number=10000)
    print(f"Time for direct evaluation : {time_direct:0.5f}")
    print(f"Time for fastFT evaluation : {time_fft:0.5f}")
    # for value in values_fft:
    # print(value)
    # for value in values_direct:
    # print(value)
