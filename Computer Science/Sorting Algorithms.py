array = [1, 5, -13, -5, 0, 99, 85, 17, 25, 5, 6, 9, 101, 55, 13, 17, 99, 56, 76, 4]

def selectionSort(array):

    """
    The selection sort algorithm sorts an array 
    by repeatedly finding the minimum element 
    (considering ascending order) from unsorted part 
    and putting it at the beginning.

    Worst time complexity: n^2
    Average time complexity: n^2
    Best time complexity: n^2
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

    Worst time complexity: n^2
    Average time complexity: n^2
    Best time complexity: n
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

def insertionSortInterleaved(array, startIdx, gap):

    """
    Helper function for Shell sort algorithm

    parameters
    ----------
    array : array
        unsorted array
    startIdx : integer
        index of a value from which to start
        sorting algorithm
    gap : integer
        gap between compairing values
    """

    for i in range(startIdx + gap, len(array), gap):
        j = i

        while (j - gap >= startIdx) and (array[j] < array[j - gap]):
            temp = array[j]
            array[j] = array[j - gap]
            array[j - gap] = temp
            j = j - gap

def shellSort(array, gapValues):
    """
    Shell sort method starts by sorting pairs of elements 
    far apart from each other, then progressively reducing
    the gap between elements to be compared.

    Worst complexity: Depends on gap sequence
    Average complexity: n*log(n)^2 or n^(3/2)
    Best complexity: n
    Space complexity: 1

    parameters
    ----------
    array : array
        unsorted array
    gapValues : array
        Number of indexes between compairing values in
        an array.
        Gap values are often chosen in decreasing order. 
        A gap value of 1 is equivalent to the regular 
        insertion sort algorithm.
        Usual gap values: 
            powers of 2 minus 1 is a common choice, 
            in decreasing order. 1 should be the last value.
        The sum of gapValues is the number of times
        insertionSortInterleaved is called.

    returns
    ----------
    array : =/=
        sorted array
    """

    for gapValue in gapValues:

        for startIdx in range(gapValue):
            
            insertionSortInterleaved(array, startIdx, gapValue)
        
    return array