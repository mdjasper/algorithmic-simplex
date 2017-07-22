def getMatrixInput ():
    print("Enter the coefficients for a matrix row-by-row")
    print("For example \"1 3 -6\"")
    print("Enter \"q\" to quit")
    print("===")
    inputMatrix = list()
    while True:
        input = raw_input('Enter a row: ')
        if input == "q":
            break
        else:
            arr = [int(num) for num in input.split(' ')]
            inputMatrix.append(arr)

    return inputMatrix