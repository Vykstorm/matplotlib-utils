

from typing import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc


def filledplot(x,
    y=None, border : Optional[bool]=True, color=None, alpha : Optional[float]=None,
    borderalpha : Optional[float]=None, bordersize : Optional[int]=None) -> None:
    '''
    Creates a plot that paints the area behind the given function (its similar to fill_between
    function)

    The next signatures are valid:
    filledplot(y)
    filledplot(x, y)

    :param x: 1D array with the coordinates on the x-axis if specified (if only y is set, it will
    be by default np.arange(0, len(y)))

    :param y: 1D array with the coordinates on the y-axis or a callable function
    If its a 1D array and x is also set, both vectors must have the same length
    If its a callable (x must be set first), it ill be called with x as argument and it must return a 1D array with the same
    length as x

    :param border: If it is true, plot the function also
    :param color: Color to be used to paint the function and its enclosed area
    :param alpha: Alpha value to be used when painting the area
    :param borderalpha: Alpha value to be used when painting the function (only used if border is True)
    :param bordersize: Size of the lines when plotting the function (only used if border is True)
    '''
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
