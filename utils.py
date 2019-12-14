import numpy as np
import math
import matplotlib.pyplot as plt


# prints formatted price
def formatPrice(n):
    return ("-%" if n < 0 else " %") + "{0:.3f}".format(abs(n))


# returns the sigmoid
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# returns the vector containing stock data from a fixed file
def getStockDataVec(key):
    vec = []
    lines = open("files/input/" + key + ".csv", "r").read().splitlines()
    column_close_price = 4
    for line in lines[1:]:
        vec.append(float(line.split(",")[column_close_price]))

    return vec


def plot_histogram(x, bins, title, xlabel, ylabel, xmin=None, xmax=None):
    plt.clf()
    plt.hist(x, bins=bins)
    if xmin != None:
        plt.xlim(xmin, xmax)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig('files/output/' + title + '.png')


def plot_barchart(list, file="BT", title='BT', ylabel="Price", xlabel="Date", colors='green'):
    l = len(list)
    x = range(l)
    # font = {'family': 'serif',
    # 		'color':  'black',
    # 		'weight': 'normal',
    # 		'size': 8,
    # 		}
    myarray = np.asarray(list)
    colors = colors  # 'green'#np.array([(1,0,0)]*l)
    # colors[myarray > 0.0] = (0,0,1)
    plt.clf()
    plt.bar(x, myarray, color=colors)
    # plt.text(0, 0,text,  fontdict=font)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig('files/output/' + file + '.png')
