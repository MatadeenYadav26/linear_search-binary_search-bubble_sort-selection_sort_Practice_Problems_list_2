#Problem-1: Searhing Algorithm: Linear Search :-
# search = int(input("What you want to search: "))
# a = [10,14,16,15,26,36,42,35,32,77,98]

# for i in range (len(a)-1):
#     if a[i] == search:
#         print(f"{search} is present in a , at index {i}.")
#         break
# else: 
#     print(f"{search} is not present in a.")

#Problem-2: Search Algorithm : Binary Search :- Divide and Conquer: we need a sorted list

# a = [10,12,14,16,22.33,44,66,88,100]

# search = int(input("Tell what to Search: "))

# start = 0
# end = len(a)-1
# mid = (start + end) // 2

# while start <= end :
#     if a[mid] == search:
#         print(f"Element found at index {mid}.")
#         break
#     elif a[mid] < search:
#         start = mid + 1
#         mid = (start+end)//2
#     elif a[mid] > search:
#         end = mid-1
#         mid = (start+end)//2
# else:
#     print("Sorry , No Such Elements Exist.")


#Problem - 3 :  Bubble Sort : Swap the list if they are in wrong order : You take the largest element in bubble and put it at the last by running loop for one lesser time/element.

# a = [10,24,16,75,46,66,92,45,452,37,8]

# for j in range(len(a)-1):
#     for i in range(len(a)-1-j):
#         if a[i] > a[i+1]:
#             a[i],a[i+1] = a[i+1],a[i]

# print(a)

#Problem - 4 : Selection Sort : 2 pointers at a time , one selects the minimum or stays at first 2nd finds the minimum element , then both swap each other then , index value increases by 1 then then same process is repeated until , complete list isn't sorted.

a = [10,24,16,35,86,66,92,45,452,37,8]

for i in range (len(a)-1):
    j = i+1
    min = i 
    for k in range (j,len(a)):
        if  a[k] < a[min]:
            min = k 
    
    a[i],a[min] = a[min] ,a[i]

print(a)