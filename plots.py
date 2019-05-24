

from typing import *
import numpy as np
import matplotlib.pyplot as plt


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



if __name__ == '__main__':
    hist, edges = np.histogram(np.random.randn(1000), bins=30)

    filledfuncplot(hist, color='blue', alpha=0.25, border=True, bordersize=1)
    plt.legend(['f'])
    plt.show()
