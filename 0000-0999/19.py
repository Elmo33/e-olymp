nums = input()
first_half = nums[0:len(nums)//2]
second_half = nums[len(nums)//2:][::-1]
count = 0

if len(nums)%2 ==1:
    count +=1
for i in range(len(first_half)):
    if first_half[i] == second_half[i]:
        count+=1

print(count)
