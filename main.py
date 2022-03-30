import signals


def menu():
    choice = int(input("1. Encoding\n"
                       "2. Decoding\n"
                       "Enter Your Choice : "))
    if choice == 1:
        signal = input("Enter The Signal : ")
        sign = input('Enter The First Sign (+,-):')
        return signal, sign, choice
    elif choice == 2:
        signal = input("Enter The Signal : ").split()
        sign = '+'
        return signal, sign, choice


if __name__ == "__main__":
    RawSignal, sign, choice = menu()

    signalTest = signals.Signal(RawSignal, sign)

    if choice == 1:
        signalTest.encode()
    elif choice == 2:
        signalTest.decode()
