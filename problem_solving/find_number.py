nums = [0,0,1,1,1,2,2,3,3,4]

def find_num(nums, value):
    for i in range(len(nums)):
        if nums[i] == value:
            return i
    return -1


def removeDuplicates(nums):
        if len(nums) <= 1:
            return nums
        max_num = nums[-1]
        min_num = nums[0]

        i = 0
        counter = 0
        while counter < len(nums):
            added = 1
            j = find_num(nums, i+added)
            while j < 0:
                if added >= max_num - min_num:
                     added = -1
                     break
                added+=1
                j = find_num(nums, i+added)
            if added == -1:
                 break
            nums[i+1] = nums[j]
            i+=1
            counter+=1
        return nums

print(removeDuplicates(nums))    