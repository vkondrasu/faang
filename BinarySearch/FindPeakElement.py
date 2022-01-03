def findPeak(nums):
    n = len(nums)

    l, r = 0, n-1

    while l < r:
        mid = l + (r-l)//2

        if nums[mid] > nums[mid+1]:
            r = mid
        else:
            l = mid+1

    return l

assert(findPeak([1,2,3,1]) == 2)
assert(findPeak([1,2,1,3,5,6,4]) in [1,5])
assert(findPeak([3,2,3,1]) in [0,2])