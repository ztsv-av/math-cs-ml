def selectionSort(array):
    """
    The selection sort algorithm sorts an array 
    by repeatedly finding the minimum element 
    (considering ascending order) from unsorted part 
    and putting it at the beginning.

    Worst complexity: n^2
    Average complexity: n^2
    Best complexity: n^2
    Space complexity: 1

    parameters
    ----------
    array : unsorted array

    returns
    ----------
    array : =/=
        sorted array
    """

    for i in range(len(array) - 1):

        smallestIdx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallestIdx]:
                smallestIdx = j
            
        temp = array[i]
        array[i] = array[smallestIdx]
        array[smallestIdx] = temp

    return array

def insertionSort(array):
    """
    Insertion sort is a simple sorting algorithm 
    that builds the final sorted array (or list) 
    one item at a time.

    Worst complexity: n^2
    Average complexity: n^2
    Best complexity: n
    Space complexity: 1

    parameters
    ----------
    array : unsorted array

    returns
    ----------
    array : =/=
        sorted array
    """

    for i in range(1, len(array)):

        j = i
        while j > 0 and array[j] < array[j - 1]:
            temp = array[j]
            array[j] = array[j - 1]
            array[j - 1] = temp
            j -= 1
        
    return array