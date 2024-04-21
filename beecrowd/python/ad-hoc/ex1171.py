nums = list()
n = int(input())
for i in range(n):
    nums.append(int(input()))
nums.sort()
i=0
while i < len(nums):
    rep = nums.count(nums[i])
    print("{} aparece {} vez(es)".format(nums[i], rep))
    i += rep