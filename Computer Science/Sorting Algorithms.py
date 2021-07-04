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
