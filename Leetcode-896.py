nums = list(map(int,input().split()))
mantiq = True
for i in range(len(nums)-1):
               if nums[i]<nums[i+1]:
                    mantiq = False
                    break
if mantiq == False:
    mantiq = True
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            mantiq = False
            break
print(mantiq)