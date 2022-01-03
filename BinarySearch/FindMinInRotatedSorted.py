def findMin(nums):
    l, r = 0, len(nums)-1

    result = nums[0]

    while l <= r:
        if nums[l] < nums[r]:
            result = nums[l]
            break

        mid = l + (r-l)//2

        if nums[mid] >= nums[l]:
            result = min(result, nums[l])
            l = mid+1
        else:
            r = mid-1

    return result

assert(findMin([4,5,6,7,0,1,2]) == 0)
assert(findMin([4,5,6,7]) == 4)
assert(findMin([1,2,3,0]) == 0)
assert(findMin([1]) == 1)
assert(findMin([1,2]) == 1)
assert(findMin([2,1]) == 1)