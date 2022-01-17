nums = [3,4,5,1,2]
nums.append(6)
print(nums[0]) // 1
print(len(nums)) // 6
print(nums[1:3]) // 3,4

nums.sort()
print(nums) // [1,2,3,4,5,6]

print(nums.index(3)) //2
nums.pop(4)

nums.pop(nums.index(3))
nums.remove(4)
del nums[1]
nums.pop() // delets -1

