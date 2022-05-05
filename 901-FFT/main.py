from math import sin, cos, pi
from timeit import timeit


def fft(a):
    # Recursive function of FFT
    n = len(a)
    # if input contains just one element
    if n == 1:
        return a
    # For storing n complex nth roots of unity
    theta = 2*pi/n
    w = list(complex(cos(theta*i), sin(theta*i)) for i in range(n))
    # Separate coefficients
    Aeven, Aodd = a[0::2], a[1::2]
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


def ifft(a):
    # Part of the code is refernced from https://rosettacode.org/wiki/Fast_Fourier_transform#Python
    N = len(a)
    iN = 1 / N
    # // Conjugate nums in a
    a = [num.conjugate() for num in a]
    # Apply Fourier Transform
    a = fft(a)
    a = [num.conjugate()*iN for num in a]
    return a


if __name__ == '__main__':
    # Driver code
    # Poly a_n(x^n) => n range from 0 to n-1
    a = [1, 2, 3, 4]
    print(a)

    fft_a = fft(a)
    # Rounding complex nums
    fft_a = [complex(round(i.real, 8), round(i.imag, 8)) for i in fft_a]
    print(fft_a)

    ifft_fft_a = ifft(fft_a)
    # Rounding complex nums
    ifft_fft_a = [complex(round(i.real, 8), round(i.imag, 8))
                  for i in ifft_fft_a]
    print(ifft_fft_a)
