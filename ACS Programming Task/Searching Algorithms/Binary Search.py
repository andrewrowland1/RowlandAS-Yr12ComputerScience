import math
def BinarySearch (aList, itemSought):
    found = False
    index = -1
    first = 0
    last = len(aList)-1
    while first <= last and found == False:
        midpoint = int((first + last) / 2)
        if aList[midpoint] == itemSought :
            found = True
            index = midpoint
        else:
            if aList[midpoint] < itemSough:
                first = midpoint + 1
            else:
                last = midpoint - 1
            #endif
        #endif
    #endwhile
    return index
#endfunction

