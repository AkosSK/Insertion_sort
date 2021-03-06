def insertion_sort(array):

    # We start from 1 since the first element is sorted
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition - 1

        array[currentPosition] = currentValue

array = [4, 22, 41, 40, 27]
insertion_sort(array)
print("sorted array: " + str(array))