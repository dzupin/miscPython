from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
def knnDemo(X,y, n): #cresates the the classifier and fits it to the data
    res=0.05
    k1 = knn(n_neighbors=n,p=2,metric='minkowski')
    k1.fit(X,y)
    #sets up the grid
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, res),np.arange(x2_min, x2_max, res))
    # makes the prediction
    Z = k1.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    # creates the color map
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
    # Plots the decision surface
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap_light)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    # plots the samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    plt.show()
iris = datasets.load_iris()
X1 = iris.data[:, 0:3:2]
X2 = iris.data[:, 0:2]
X3 = iris.data[:, 1:3]
y = iris.target
knnDemo(X2, y, 15)



###############################################################
from sklearn.linear_model import Ridge
import numpy as np
def ridgeReg(alpha):
    n_samples, n_features = 10, 5
    y = np.random.randn(n_samples)
    X = np.random.randn(n_samples, n_features)
    clf = Ridge(.001)
    res=clf.fit(X, y)
    return(res)
res= ridgeReg(0.001)
print (res.coef_)
print (res.intercept_)
#################################################################

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
def normal(mean = 0, var = 1):
    sigma = np.sqrt(var)
    x = np.linspace(-3,3,100)
    plt.plot(x,mlab.normpdf(x,mean,sigma))
    plt.show()
normal(1,0.5)
###############################################################################################



from scipy.stats import binom
def binomial(x=10,n=10, p=0.5):
    fig, ax = plt.subplots(1, 1)
    x=range(x)
    rv = binom(n, p)
    plt.vlines(x, 0, (rv.pmf(x)), colors='k', linestyles='-')
    plt.show()
binomial()
#####################################################################################


from scipy.stats import poisson
def pois(x=1000):
    xr=range(x)
    ps=poisson(xr)
    plt.plot(ps.pmf(x/2))
pois()
###########################################################

import scipy.stats as stats
def cdf(s1=50,s2=0.2):
    x = np.linspace(0,s2 * 100,s1 *2)
    cd = stats.binom.cdf
    plt.plot(x,cd(x, s1, s2))
plt.show()
###########################################################


import numpy as np
import random
import matplotlib.pyplot as plt
def gradientDescent(x, y, alpha, numIterations):
    xTrans = x.transpose()
    m, n = np.shape(x)
    theta = np.ones(n)
    for i in range(0, numIterations):
        hwx = np.dot(x, theta)
        loss = hwx - y
        cost = np.sum(loss ** 2) / (2 * m)
        print("Iteration %d | Cost: %f " % (i, cost))
        gradient = np.dot(xTrans, loss) / m
        theta = theta - alpha * gradient
    return theta
def genData(numPoints, bias, variance):
    x = np.zeros(shape=(numPoints, 2))
    y = np.zeros(shape=numPoints)
    for i in range(0, numPoints):
        x[i][0] = 1
        x[i][1] = i
        y[i] = (i + bias) + random.uniform(0, 1) * variance
    return x, y
def plotData(x,y,theta):
    plt.scatter(x[...,1],y)
    plt.plot(x[...,1],[theta[0] + theta[1]*xi for xi in x[...,1]])
    x, y = genData(20, 25, 10)
    iterations= 10000
    alpha = 0.001
    theta=gradientDescent(x,y,alpha,iterations)
    plotData(x,y,theta)




















