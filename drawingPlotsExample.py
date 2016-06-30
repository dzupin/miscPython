import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0., 5., 0.2)
plt.plot(x, x**4, 'r', x, x*90, 'bs', x, x**3, 'g^')
plt.show()


x1 = np.arange(0., 5., 0.2)
x2 = np.arange(0., 5., 0.1)
plt.figure(1)
plt.subplot(211)
plt.plot(x1, x1**4, 'r', x1, x1*90, 'bs', x1, x1**3, 'g^',linewidth=2.0)
plt.subplot(212)
plt.plot(x2,np.cos(2*np.pi*x2), 'k')
plt.show()

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(1000)
n, bins, patches = plt.hist(x, 10, normed=1, facecolor='g')
plt.xlabel('Frequency')
plt.ylabel('Probability')
plt.title('Histogram Example')
plt.text(40,.028, 'mean=100 std.dev.=15')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

N = 100
x = np.random.rand(N)
y = np.random.rand(N)
#colors = np.random.rand(N)
colors=('r','b','g')
area = np.pi * (10 * np.random.rand(N))**2
# 0 to 10 point radiuses
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()