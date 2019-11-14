import math
def linearSearch(namelist,nameSought);
    index = -1
    i = 0
    found = False
    while i < len(namelist) and not found:
        if namelist[i] == nameSought:
            index = i
            found = True
        #endif
        i = i + 1
    #endwhile
    return index
#endfunction

        
    
