import numpy as np
rate = 1.0936835844379738

sum = -285 + 41/rate + 74/rate**2 + 123/rate**3+ 90/rate**4+ 55/rate**5+ 20/rate**6- 31/rate**6


a = 1.01091999
n = 60
arr = np.arange(1, n+1)
sum = np.sum(1 / np.power(a, arr))

# 计算整个表达式的值
result = -96000 + 1028.61 * sum + 97662.97 / np.power(a, n)
print(result)