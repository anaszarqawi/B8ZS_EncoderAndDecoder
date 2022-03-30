import matplotlib.pyplot as plt
import numpy as np


class Signal:
    finalSignal = []
    i = 0

    def __init__(self, RawSignal, sign):
        self.RawSignal = RawSignal
        self.original = [bit for bit in RawSignal]
        self.signal = [bit for bit in RawSignal]
        self.sign = sign

    def printSignal(self, s1, s2):
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
        plt.plot(xs, ys)
        plt.grid(linewidth=0.5)
        plt.title(s2)

        # Show 2 Figs
        plt.show()

    def convert(self, s):
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

    def getIndexOfZeros(self):
        temp = "".join(self.signal)
        return temp.find("00000000")

    def changeSign(self):
        return '-' if self.sign == '+' else '+'

    def changeZeros(self):
        self.i += 7
        self.signal = "".join(self.signal)
        self.sign = self.changeSign()
        if self.signal.find("00000000") == -1:
            print("ERROR: No sequence of 8 bits detected")
        else:
            if(self.sign == '+'):
                self.signal = self.signal.replace('00000000', '000+-0-+')
            else:
                self.signal = self.signal.replace('00000000', '000-+0+-')

        self.sign = self.changeSign()
        return [bit for bit in self.signal]

    def changeOnes(self):
        if int(self.signal[self.i]) == 1:
            if self.sign == '+':
                self.signal[self.i] = '+'
                self.sign = self.changeSign()

            elif self.sign == '-':
                self.signal[self.i] = '-'
                self.sign = self.changeSign()

            else:
                return

    def changeB8ZS(self):
        if self.RawSignal.find("000+-0-+") == -1 and self.RawSignal.find("000-+0+-") == -1:
            print("ERROR: No B8ZS a line coding detected")
            exit(-1)
        else:
            self.RawSignal = self.RawSignal.replace('000+-0-+', '00000000')
            self.RawSignal = self.RawSignal.replace('000-+0+-', '00000000')
            self.RawSignal = self.RawSignal.replace('-', '1')
            self.RawSignal = self.RawSignal.replace('+', '1')

    def encode(self):
        while self.i < len(self.signal):
            if self.getIndexOfZeros() == -1 or self.i < self.getIndexOfZeros():
                self.changeOnes()
            else:
                self.signal = self.changeZeros()
            self.i += 1

        self.finalSignal = self.convert(self.signal).copy()
        self.printSignal(self.original, self.finalSignal)

    def decode(self):
        self.changeB8ZS()
        self.finalSignal = self.convert(self.RawSignal).copy()
        self.original = self.convert(self.original).copy()
        self.printSignal(self.original, self.finalSignal)
