import matplotlib.pyplot as plt
import numpy as np


def changeZeros():
    global signal
    if signal.find("00000000") == -1:
        print("ERROR: No sequence of 8 bits detected")
    else:
        if(sign == '+'):
            signal = signal.replace('00000000', '000+-0-+')
        else:
            signal = signal.replace('00000000', '000-+0+-')


def convert(s):
    temp = []
    for bit in s:
        if bit == '+':
            temp.append(1)
        elif bit == '-':
            temp.append(-1)
        else:
            temp.append(0)
    return temp


def printSignal():
    # Figure 1
    xs = np.repeat(range(len(original)), 2)
    ys = np.repeat(original, 2)
    xs = xs[1:]
    ys = ys[:-1]
    xs = np.append(xs, xs[-1] + 1)
    ys = np.append(ys, ys[-1])
    plt.subplot(2, 1, 1)
    plt.plot(xs, ys)
    plt.grid(linewidth=0.5)
    plt.title(original)

    # Figure 2
    xs = np.repeat(range(len(finalSignal)), 2)
    ys = np.repeat(finalSignal, 2)
    xs = xs[1:]
    ys = ys[:-1]
    xs = np.append(xs, xs[-1] + 1)
    ys = np.append(ys, ys[-1])
    plt.subplot(2, 1, 2)
    plt.grid(linewidth=0.5)
    plt.title(finalSignal)
    plt.plot(xs, ys)
    plt.show()


def encodeing():
    global original
    global finalSignal

    changeZeros()
    finalSignal = convert(signal).copy()
    original = convert(original).copy()
    printSignal()


if __name__ == "__main__":
    signal = '+-+-+0-+-+00000000-+-'
    original = signal
    finalSignal = []
    zerosIndex = signal.find('00000000')
    sign = signal[zerosIndex-1]
    encodeing()
