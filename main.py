import signals


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
    RawSignal, sign, choice = menu()

    signalTest = signals.Signal(RawSignal, sign)

    if choice == 1:
        signalTest.encode()
    elif choice == 2:
        signalTest.decode()
