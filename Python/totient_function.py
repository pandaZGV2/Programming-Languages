import math
import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as sns

sns.set_theme()
sns.set_style('darkgrid')

def gcd(a, b):

    if (a == 0):
        return b
    return gcd(b % a, a)


def phi(n):

    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result += 1
    return result


x=list()
y=list()
for i in range(1, 1001):
    x.append(i)
    y.append(phi(i))
# print(x, y)
# plt.set_xscale(3, 'linear')
plt.scatter(x, y, c='g')
plt.xlim(0,1100)
x1=np.arange(1,1001)
y1=x1-1
plt.plot(x1,y1,'r--',lw='3')
plt.savefig('Python/totient_function.png', format='png');
plt.show()