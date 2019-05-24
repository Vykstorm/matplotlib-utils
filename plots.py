

from typing import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc


def filledplot(x,
    y=None, border : Optional[bool]=True, color=None, alpha : Optional[float]=None,
    borderalpha : Optional[float]=None, bordersize : Optional[int]=None) -> None:

    if x is not None:
        x = np.array(x)

    if y is None:
        y = x
        x = np.arange(0, len(y))
    elif callable(y):
        y = y(x)
    else:
        y = np.array(y)

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

    plt.fill_between(x, y, color=color, alpha=alpha)

    if border:
        plt.plot(x, y, color=color, alpha=borderalpha, linewidth=bordersize, label='_nolegend_')


def diffplot(y, x=None,
    marker : Optional[str]=None, markersize : Optional[int]=None,
    colors=None, alpha : Optional[float]=None,
    matchmarker : Optional[str]=None, matchmarkersize : Optional[float]=None,
    matchcolor=None, matchalpha : Optional[float]=None,

    linewidths : Optional[int]=1, linecolors=None, linestyles : Optional[str]='-',
    linesalpha : Optional[float]=None,) -> None:

    y = np.array(y)

    if x is None:
        x = np.arange(0, len(a))
    else:
        x = np.array(x)

    if colors is None and alpha is None:
        alpha = 1

    if linecolors is None and linesalpha is None:
        linesalpha = 0.5

    if linecolors is None:
        linecolors = 'black'

    if matchmarker is None and marker is not None:
        matchmarker = marker

    if matchmarkersize is None and markersize is not None:
        matchmarkersize = markersize

    if matchalpha is None and alpha is not None:
        matchalpha = alpha

    if colors is not None and matchcolor is None:
        matchcolor = 'black'

    indices = np.abs(y[1] - y[0]) > 0
    xd, yd = x[indices], y[:, indices]
    xnd, ynd = x[~indices], y[:, ~indices]

    # Plot lines
    lines = mc.LineCollection(
        list(zip(np.stack([xd, yd[0]], axis=1), np.stack([xd, yd[1]], axis=1))),
        linestyles=linestyles, linewidths=linewidths, colors=linecolors, alpha=linesalpha, label='_nolegend_')
    plt.gca().add_collection(lines)

    # Plot points
    for k in (0, 1):
        plt.scatter(xd, yd[k],
            marker=marker, s=markersize, c=colors, alpha=alpha)

    # Plot matching points
    plt.scatter(xnd, ynd[0, :], marker=matchmarker, c=matchcolor, s=matchmarkersize, alpha=matchalpha)

if __name__ == '__main__':
    a = np.random.randint(0, 4, size=10)
    b = np.random.randint(0, 4, size=10)


    diffplot((a, b))
    plt.show()
