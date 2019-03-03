# Sorts a linked list using merge sort. A new head reference is returned.

def llistMergeSort( theList ):
    # Split the linked list into two sublists of equal size.
    rightList = _splitLinkedList( theList )
    leftList = theList

    # Perform the same operation on the left half
    leftList = llistMergeSort( leftList )

    # and the right half.
    rightList = llistMergeSort( rightList )

    # Merge the two ordered sublists.
    theList = _mergeLinkedLists( leftList, rightList )

    # Return the head pointer of the ordered sublist.
    return theList

    # Splits a linked list
