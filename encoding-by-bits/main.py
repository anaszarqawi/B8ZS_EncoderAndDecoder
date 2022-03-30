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

    # plt.gcf().set_size_inches(30, 8)
    # plt.title(f"{signal}\n{orig}")
    # plt.ylim(-1.5, 1.5)
    plt.show()


def getIndexOfZeros():
    temp = "".join(signal)
    return temp.find("00000000")


def changeSign():
    global sign
    return '-' if sign == '+' else '+'


def changeZeros():
    global i
    global signal
    global sign
    i += 7
    signal = "".join(signal)
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
            signal[i] = '+'
            sign = changeSign()

        elif sign == '-':
            signal[i] = '-'
            sign = changeSign()

        else:
            return


def convert():
    for bit in signal:
        if bit == '+':
            finalSignal.append(1)
        elif bit == '-':
            finalSignal.append(-1)
        else:
            finalSignal.append(0)

    return finalSignal


def encode():
    global i
    global signal

    while i < len(signal):
        if getIndexOfZeros() == -1 or i < getIndexOfZeros():
            changeOnes()
        else:
            signal = changeZeros()
        i += 1

    signal = convert()
    printSignal()


def menu():
    signal = input("Enter The Signal : ")
    sign = input('Enter The First Sign (+,-):')
    choice = int(input("1. Encoding\n"
                       "2. Decoding\n"
                       "Enter You Choice : "))

    return signal, sign, choice


if __name__ == "__main__":
    # signal => "01010011"
    RawSignal, sign, choice = menu()

    original = [int(bit) for bit in RawSignal]
    signal = [bit for bit in RawSignal]
    finalSignal = []
    i = 0

    if choice == 1:
        encode()
    elif choice == 2:
        decode()
