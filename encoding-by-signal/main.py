import matplotlib.pyplot as plt
import numpy as np


def changeZeros():
    global signal
    if signal.find("00000000") == -1:
        print("ERROR: No sequence of 8 bits detected")
        exit(-1)
    else:
        if(sign == '+'):
            signal = signal.replace('00000000', '000+-0-+')
        else:
            signal = signal.replace('00000000', '000-+0+-')


def changeB8ZS():
    global signal
    if signal.find("000+-0-+") == -1 and signal.find("000-+0+-") == -1:
        print("ERROR: No B8ZS a line coding detected")
        exit(-1)
    else:
        signal = signal.replace('000+-0-+', '00000000')
        signal = signal.replace('000-+0+-', '00000000')


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
    plt.grid(linewidth=0.5, solid_capstyle='butt')
    plt.title(finalSignal)
    plt.plot(xs, ys)
    plt.show()


def encode():
    global original
    global finalSignal

    changeZeros()
    finalSignal = convert(signal).copy()
    original = convert(original).copy()
    printSignal()


def decode():
    global original
    global finalSignal

    changeB8ZS()
    finalSignal = convert(signal).copy()
    original = convert(original).copy()
    printSignal()


def menu():
    signal = input("Enter The Signal : ")
    choice = int(input("1. Encoding\n"
                       "2. Decoding\n"
                       "Enter You Choice : "))

    return signal, choice


if __name__ == "__main__":
    signal, choice = menu()
    original = signal
    finalSignal = []

    zerosIndex = signal.find('00000000')
    sign = signal[zerosIndex-1]

    if choice == 1:
        encode()
    elif choice == 2:
        decode()

    print(signal)
