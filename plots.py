

from typing import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc


def filledfuncplot(x,
    y=None, border : Optional[bool]=True, color=None, alpha : Optional[float]=None,
    borderalpha : Optional[float]=None, bordersize : Optional[int]=None) -> None:

    if y is None:
        y = x
        x = np.arange(0, len(y))
    elif callable(y):
        y = y(x)

    xf = np.concatenate(([x[0]], x, [x[-1]]))
    yf = np.concatenate(([0], y, [0]))

    if color is None:
        if alpha is None:
            alpha = 0.35 if border is False else 0.2
        if borderalpha is None:
            borderalpha = 0.9

        color = 'blue'

    if alpha is not None:
        if borderalpha is None:
            borderalpha = 1
        else:
            if borderalpha <= alpha:
                border = False
            else:
                borderalpha -= alpha

    plt.fill(xf, yf, color=color, alpha=alpha)

    if border:
        plt.plot(x, y, color=color, alpha=borderalpha, linewidth=bordersize, label='_nolegend_')


def diffplot(y, x=None,
    marker=None, markersize=None, pointcolors=None, pointsalpha=None,
    linewidths=1, linecolors=None, linestyles='-', linesalpha=None):

    y = np.array(y)

    if x is None:
        x = np.arange(0, len(a))

    if pointcolors is None and pointsalpha is None:
        pointalpha = 1

    if linecolors is None and linesalpha is None:
        linesalpha = 0.5

    if linecolors is None:
        linecolors = 'black'

    # Plot lines
    lines = mc.LineCollection(
        list(zip(np.stack([x, y[0]], axis=1), np.stack([x, y[1]], axis=1))),
        linestyles=linestyles, linewidths=linewidths, colors=linecolors, alpha=linesalpha, label='_nolegend_')
    plt.gca().add_collection(lines)

    # Plot points
    for k in (0, 1):
        plt.scatter(x, y[k], marker=marker, s=markersize, c=pointcolors, alpha=pointsalpha)


if __name__ == '__main__':
    a = np.random.random(10)
    b = np.random.random(10)
    diffplot((a, b), linewidths=1, pointcolors='blue', pointsalpha=1)
    #plt.plot(a, b, None)
    #plt.legend(['f'])
    plt.show()
