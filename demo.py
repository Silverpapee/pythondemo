
def sort(nums):
  for i in range(5):
    # 5 is the high index from nums
    minpos = i
    for j in range(i,6):
       if nums[j] < nums[minpos]:
         minpos = j


    temp = nums[i]
    nums[i] = nums[minpos]
    nums[minpos] = temp

    print(nums)






#(len(num)): this means the length of num inside the range

nums = [5,3,6,8,7,2]
sort(nums)
print(nums)
