import numpy as np
from numpy import fft 

fft_a=fft.fft([1,2,3,4])
ifft_a=fft.ifft(fft_a)

print(fft_a)
print(ifft_a)