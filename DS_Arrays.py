#Arrays is a container which can hold a fix number of items and these items should be of same type
#Element- Each item stored in array
#Index - Each location of an element in an array has a numerical index

from array import *

array1= array('i',[10,100,1000,10000])

for i in array1:
    count = 0
    print(id(array1[count]))
    print(i)
    count= count + 1

#Array methods
#Insertion element into array

array2 = array('i',[1,2,3,4,5,6,7,8,9])

array2.insert(9,10)


def insertelement(arr,value,position):
    arr2 = array('i',[value])
    return (arr[0:position - 1] + arr2 + arr[position - 1:len(arr)])

print(insertelement(array2,0,5))

#deletion an element from array

array2.remove(9)
print(array2)

def removelement(arr,value):
    count=0;
    for i in arr:
      if(i == value):
            break;
      count = count + 1
    return (arr[0:count]+arr[count + 1:len(arr)])

print(removelement(array2,8))

#Searching an element in an array

print(array2.index(10))

def searchelement(arr,value):
    count = 0;
    for i in arr:
        if(i == value):
            break
        count = count + 1;
    return count

print(searchelement(array2,10))



#Updating array elemnts

array2[1] = 1
print(array2)

def updateelement(arr,value,index):
    count = 0;
    for i in arr:
        if(count == index):
            arr[index] = value
            break
        count = count + 1
    return arr

print(updateelement(array2,9,6))
