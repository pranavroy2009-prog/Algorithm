lst=[1,2,3,4,5,6,7,8,9,10]
length=len(lst)
def BinarySearch(lst,key,low,high):
  if low>high:
    return -1
  mid=int((low+high)/2)
  if key==lst[mid]:
    return mid
  if key>lst[mid]:
    return BinarySearch(lst,key,mid+1,high)
  else:
    return BinarySearch(lst,key,low,mid-1)
    
  
a=int(input("enter a no. to search : "))
ans=BinarySearch(lst,a,0,length-1)
if ans !=-1:
  print("element found at index ",ans )
else:
  print("element not found")
