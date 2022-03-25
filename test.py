
def test(list1):
    list1[1] = 10
    return list1


def main():
    arr = [1, 2, 3, 4, 5, 6]
    test(arr)
    print(arr)


main()
