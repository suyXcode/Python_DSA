def insertion_sort_asc(nums):
    print(f"Original Array : {nums}")
    for i in range(len(nums)):
        pivot=nums[i]
        j=i-1
        while j>=0 and nums[j]>pivot:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=pivot
    print(f"Sorted Array : {nums}")
print(f"\n*** Insertion Sort Algorithm in ascending order. ***\n")
insertion_sort_asc([1,45,3,34,2,1])




def insertion_sort_dsc(nums):
    print(f"Original Array : {nums}")
    for i in range(len(nums)):
        pivot=nums[i]
        j=i-1
        while j>=0 and nums[j]<pivot:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=pivot
    print(f"Sorted Array : {nums}")
print(f"\n*** Insertion Sort Algorithm in Descending order. ***\n")
insertion_sort_dsc([1,45,3,34,2,1])