def bin_search(array,n):
    if (len(array)<2 and array[0]==n):
        return 0
    elif (len(array)<2 and array[0]!=n):
        return None
    else:
        low = 0
        max = len(array)-1
        while low <= max:
            mid = low+max
            guess = array[mid]
            if(guess==n):
                return mid
            if(guess>n):
                max = mid -1
            if(guess<n):
                low= mid + 1
        return None
print(bin_search([1,3,5,6,8,10,16],16))