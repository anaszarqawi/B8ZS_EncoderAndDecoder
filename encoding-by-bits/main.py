import matplotlib.pyplot as plt
import numpy as np


def printSignal(s1, s2):
    # Figure 1
    xs = np.repeat(range(len(s1)), 2)
    ys = np.repeat(s1, 2)
    xs = xs[1:]
    ys = ys[:-1]
    xs = np.append(xs, xs[-1] + 1)
    ys = np.append(ys, ys[-1])
    plt.subplot(2, 1, 1)
    plt.plot(xs, ys)
    plt.grid(linewidth=0.5)
    plt.title(s1)

    # Figure 2
    xs = np.repeat(range(len(s2)), 2)
    ys = np.repeat(s2, 2)
    xs = xs[1:]
    ys = ys[:-1]
    xs = np.append(xs, xs[-1] + 1)
    ys = np.append(ys, ys[-1])
    plt.subplot(2, 1, 2)
    plt.grid(linewidth=0.5)
    plt.title(s2)
    plt.plot(xs, ys)

    # plt.gcf().set_size_inches(30, 8)
    # plt.title(f"{signal}\n{orig}")
    # plt.ylim(-1.5, 1.5)
    plt.show()


def convert(s):
    temp = []
    for bit in s:
        if bit == '+':
            temp.append(1)
        elif bit == '-':
            temp.append(-1)
        elif bit == '1':
            temp.append(1)
        else:
            temp.append(0)
    return temp


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


def changeB8ZS():
    global RawSignal
    if RawSignal.find("000+-0-+") == -1 and RawSignal.find("000-+0+-") == -1:
        print("ERROR: No B8ZS a line coding detected")
        exit(-1)
    else:
        RawSignal = RawSignal.replace('000+-0-+', '00000000')
        RawSignal = RawSignal.replace('000-+0+-', '00000000')
        RawSignal = RawSignal.replace('-', '1')
        RawSignal = RawSignal.replace('+', '1')


def encode():
    global i
    global signal

    while i < len(signal):
        if getIndexOfZeros() == -1 or i < getIndexOfZeros():
            changeOnes()
            print(signal)
        else:
            signal = changeZeros()
        i += 1

    finalSignal = convert(signal).copy()
    printSignal(original, finalSignal)


def decode():
    global RawSignal
    global finalSignal
    global original
    changeB8ZS()
    finalSignal = convert(RawSignal).copy()
    original = convert(original).copy()
    printSignal(original, finalSignal)


def menu():
    choice = int(input("1. Encoding\n"
                       "2. Decoding\n"
                       "Enter You Choice : "))
    signal = input("Enter The Signal : ")
    if choice == 1:
        sign = input('Enter The First Sign (+,-):')
        return signal, sign, choice
    elif choice == 2:
        sign = '+'
        return signal, sign, choice


if __name__ == "__main__":
    # signal => "01010011"
    RawSignal, sign, choice = menu()

    original = [bit for bit in RawSignal]
    signal = [bit for bit in RawSignal]
    finalSignal = []
    i = 0

    if choice == 1:
        encode()
    elif choice == 2:
        decode()

    print(RawSignal)
