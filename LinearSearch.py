def LinearSearch(lst,key):
  length=len(lst)
  for i in range(0,length):
    if lst[i]==key:
      return i
  return -1
lst=[10,20,30,60,50,40,70,90,80,100]
a=int(input("Select a no."))
ans=LinearSearch(lst,a)
if ans!= -1:
  print(a," is found at index ",ans)
else:
  print("Element not Found")
