import matplotlib.pyplot as plt
import numpy as np


def printSignal(signal, orig):
    orig = [int(bit) for bit in orig]

    # Figure 1
    xs = np.repeat(range(len(orig)), 2)
    ys = np.repeat(orig, 2)
    xs = xs[1:]
    ys = ys[:-1]
    xs = np.append(xs, xs[-1] + 1)
    ys = np.append(ys, ys[-1])
    plt.subplot(2, 1, 1)
    plt.plot(xs, ys)
    plt.grid(linewidth=0.5)
    plt.title("Original Signal")

    # Figure 2
    xs = np.repeat(range(len(signal)), 2)
    ys = np.repeat(signal, 2)
    xs = xs[1:]
    ys = ys[:-1]
    xs = np.append(xs, xs[-1] + 1)
    ys = np.append(ys, ys[-1])
    plt.subplot(2, 1, 2)
    plt.grid(linewidth=0.5)
    plt.title("B8ZS Signal")
    plt.plot(xs, ys)

    # plt.gcf().set_size_inches(30, 8)
    # plt.title(f"{signal}\n{orig}")
    # plt.ylim(-1.5, 1.5)
    plt.show()


def changeZeros(signal, sign):
    temp = "".join(signal)
    print(sign)
    if temp.find("00000000") == -1:
        print("ERROR: No sequence of 8 bits detected")
    else:
        if(sign == '+'):
            temp = temp.replace('00000000', '000+-0-+')
        else:
            temp = temp.replace('00000000', '000-+0+-')

    return temp


def changeSign(sign):
    return '-' if sign == '+' else '+'


def changeOnes(signal, sign):
    signal = [bit for bit in signalList]

    for i in range(len(signal)):
        if int(signal[i]) == 1:
            if sign == '+':
                signal[i] = '+'
                sign = changeSign(sign)
            elif sign == '-':
                signal[i] = '-'
                sign = changeSign(sign)
        else:
            continue
    signal = changeZeros(signal, sign)
    return signal


def menu():
    bits = input("Enter The Bits : ")
    sign = input("Enter First Sign (+,-): ")
    # choice = int(input("1. Encoding\n"
    #                    "2. Decoding\n"
    #                    "Enter You Choice : "))
    return bits, sign


if __name__ == "__main__":
    signalList, sign = "011010000000011011", '+'

    signal = changeOnes(signalList, sign)
    finalSignal = []

    for bit in signal:
        if bit == '+':
            finalSignal.append(1)
        elif bit == '-':
            finalSignal.append(-1)
        else:
            finalSignal.append(0)

    printSignal(finalSignal, signalList)
    print(finalSignal)
