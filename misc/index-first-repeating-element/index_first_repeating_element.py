def findIndexOfFirstRepeatingElement(arr = []):
    for index, elem in enumerate(arr):
        if arr.count(elem) >= 2:
            return index
    return -1

if __name__ == "__main__":
    print(findIndexOfFirstRepeatingElement(
        [1,3,5,2,52,5]
    ))

    print(findIndexOfFirstRepeatingElement(
        [1,3,5,2,10,25,15,0]
    ))