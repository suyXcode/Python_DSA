def selection_sort_asc(nums):
    print(f"Original array: {nums}")
    n=len(nums)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if nums[j]<nums[min_index]:
                min_index=j 
            nums[i],nums[min_index]=nums[min_index],nums[i]
    print(f"Sorted array: {nums}")

print("\n*** Selection Sort Algorithm in ascending order. ***\n")
selection_sort_asc([34, 12, 24, 9, 5])



def selection_sort_dsc(nums):
    print(f"Original array: {nums}")
    n=len(nums)
    for i in range(0,n):
        max_index=i
        for j in range(i+1,n):
            if nums[j]>nums[max_index]:
                max_index=j 
            nums[i],nums[max_index]=nums[max_index],nums[i]
    print(f"Sorted array: {nums}")

print("\n*** Selection Sort Algorithm in descending order. ***\n")
selection_sort_dsc([34, 12, 24, 9, 5])