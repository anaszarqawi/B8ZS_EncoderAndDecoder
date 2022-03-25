import matplotlib.pyplot as plt
import numpy as np


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
    plt.title("".join(original).replace('', '    '))

    # Figure 2
    xs = np.repeat(range(len(finalSignal)), 2)
    ys = np.repeat(finalSignal, 2)
    xs = xs[1:]
    ys = ys[:-1]
    xs = np.append(xs, xs[-1] + 1)
    ys = np.append(ys, ys[-1])
    plt.subplot(2, 1, 2)
    plt.grid(linewidth=0.5)
    plt.title("".join(signal).replace('', '    '))
    plt.plot(xs, ys)

    # plt.gcf().set_size_inches(30, 8)
    # plt.title(f"{signal}\n{orig}")
    # plt.ylim(-1.5, 1.5)
    plt.show()


def getIndexOfZeros():
    return signal.find("00000000")


def changeSign():
    global sign
    return '-' if sign == '+' else '+'


def changeZeros():
    global i
    global signal
    global sign
    i += 7
    signal = "".join(newSignal)
    sign = changeSign()
    if signal.find("00000000") == -1:
        print("ERROR: No sequence of 8 bits detected")
    else:
        if(sign == '+'):
            signal = signal.replace('00000000', '000+-0-+')
        else:
            signal = signal.replace('00000000', '000-+0+-')

    sign = changeSign()
    return [bit for bit in signal]


def changeOnes():
    global sign
    global i
    if int(signal[i]) == 1:
        if sign == '+':
            newSignal[i] = '+'
            sign = changeSign()
        elif sign == '-':
            newSignal[i] = '-'
            sign = changeSign()
        else:
            return


def convert():
    for bit in newSignal:
        if bit == '+':
            finalSignal.append(1)
        elif bit == '-':
            finalSignal.append(-1)
        else:
            finalSignal.append(0)

    return finalSignal


def generate():
    global i
    global newSignal
    while i < len(newSignal):
        if getIndexOfZeros() == -1:
            changeOnes()
        elif i < getIndexOfZeros():
            changeOnes()
        else:
            newSignal = changeZeros()
        i += 1

    signal = "".join(newSignal)
    convert()
    printSignal()


if __name__ == "__main__":
    signal = input("Enter The Bits :")
    sign = input('Enter The First Sign (+,-):')

    original = [bit for bit in signal]
    newSignal = [bit for bit in signal]
    finalSignal = []
    i = 0
    generate()
