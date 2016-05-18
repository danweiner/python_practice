def ArithGeo(arr):

    # create a function to loop through array to find if diffs are the same

    def arrayDiffs(diff, arr, subtract):

        # loop through the array starting at i = 2 and check if every diff is same

        for i in range(2, len(arr)):

            # store a temporary difference to check against diff param
            if subtract:
                tempDiff = arr[i] - arr[i-1]
            else:
                tempDiff = arr[i] / arr[i-1]

            # if diffs do not match return false
            if (tempDiff != diff):
                return False
            # if we reach the end of the array and all diffs matched, return True
            elif(i == len(arr)-1 and tempDiff == diff):
                return True


    diffArith = arr[1] - arr[0]

    diffGeo = arr[1] / arr[0]

    isArithSeq = arrayDiffs(diffArith, arr, True)

    if isArithSeq:
        return 'Arithmetic'

    else:
        isGeoSeq = arrayDiffs(diffGeo, arr, False)
        if isGeoSeq:
            return 'Geometric'
        else:
            return -1

print(ArithGeo([5,15,46])) 
