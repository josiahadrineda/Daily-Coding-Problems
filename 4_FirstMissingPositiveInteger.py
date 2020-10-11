#Must be completed in O(n) time and O(1) space
def find_integer(nums):
    #Base case
    if 1 not in nums:
        return 1

    #Differentiate between positive and negative
    #- = left, + = right
    def filter(nums, n):
        j = 0
        for i in range(n):
            if nums[i] <= 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return j

    #Grunt work
    #Return value range: [1, n+1]
    def find_positive(nums, n):
        for i in range(n):
            if abs(nums[i])-1 < n and nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]

        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1

    #Culminates into the solution/RESult
    def res(nums, n):
        start = filter(nums, n)
        return find_positive(nums[start:], n-start)

    return res(nums, len(nums))

#Driver code
nums = [1 for i in range(100000)]
print(find_integer(nums))