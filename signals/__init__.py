import matplotlib.pyplot as plt
import numpy as np


class Signal:
    finalSignal = []
    i = 0

    # constructor to initialize data
    def __init__(self, RawSignal, sign):
        self.RawSignal = RawSignal
        self.original = [int(bit) for bit in RawSignal]
        self.signal = [bit for bit in RawSignal]
        self.sign = sign

    # Function to print two signals
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

    # this function converts a signal from ['+', '-', '1', '0'] to [1, -1, 1, 0]
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

    # Start Encodeing Functions ----------
    # This function searches for 8 zeros and returns their index
    def getIndexOfZeros(self):
        temp = "".join(self.signal)
        return temp.find("00000000")

    # This function reverses the sign
    def changeSign(self):
        return '-' if self.sign == '+' else '+'

    # This function changes each 8 zeros to B8ZS form
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

    # This function change each one according to sign
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

    def encode(self):
        while self.i < len(self.signal):
            if self.getIndexOfZeros() == -1 or self.i < self.getIndexOfZeros():
                self.changeOnes()
            else:
                self.signal = self.changeZeros()
            self.i += 1

        self.finalSignal = self.convert(self.signal).copy()
        print(f"\nThe Signal after Encoding : {self.finalSignal}")
        self.printSignal(self.original, self.finalSignal)

    # End Encodeing Functions ----------

    # Decodeing Functions
    def changeB8ZS(self, s):
        if s.find("0001-10-11") == -1 and s.find("000-1101-1") == -1:
            print("ERROR: No B8ZS a line coding detected")
            exit(-1)
        else:
            s = s.replace('0001-10-11', '00000000')
            s = s.replace('000-1101-1', '00000000')
            s = s.replace('-1', '1')
            s = s.replace('1', '1')

        return s

    def decode(self):
        strSignal = "".join(self.RawSignal)
        strSignal = self.changeB8ZS(strSignal)
        self.finalSignal = self.convert(strSignal).copy()
        print(f"\nThe Signal after Decoding : {self.finalSignal}")
        self.printSignal(self.original, self.finalSignal)
