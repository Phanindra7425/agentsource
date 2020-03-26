#Data Structrues is a particular way of organizing data ina a computer so that it can used effectively

def lengthofarray(arr):
    #length of the  array
    count = 0
    for i in arr:
          count = count + 1
    return count

def insertlist(index,value,arr):
    count = lengthofarray(arr)
    return  arr[0:index] + [value] + arr[index+1:count]

def appendlist(value,arr):
    count = lengthofarray(arr)
    return arr[0:count] + [value]

def removeelement(value,arr):
    count = lengthofarray(arr)
    for i in arr:
        if(i == value):
            break
    return arr[0:i] + arr[i + 1:count]

def popelement(index,arr):
    count = lengthofarray(arr)
    return arr[0:index] + arr[index + 1 :count]

def clearlist(arr):
    for i in arr:
        count = lengthofarray(arr)
        if(count != 0):
            arr = arr[i:count]
    return arr

def indexofvalue(value,arr):
    count = 0
    for i in arr:
        count = count + 1
        if i == value:
            break
    return count - 1

def sortlist(arr,reverse):
    count = lengthofarray(arr)
    if reverse != True:
        for i in range(0,count):
            for j in arr:
                if indexofvalue(j,arr) < count - 1:
                    nextpos = indexofvalue(j,arr) + 1
                    if (j > arr[nextpos]):
                        temp = arr[nextpos]
                        arr[nextpos] = arr[nextpos - 1]
                        arr[nextpos -1] = temp
        return arr
    else:
        for i in range(0,count):
            for j in arr:
                if indexofvalue(j,arr) < count - 1:
                    nextpos = indexofvalue(j, arr) + 1
                    if j < arr[nextpos]:
                        temp = arr[nextpos]
                        arr[nextpos] = arr[nextpos - 1]
                        arr[nextpos - 1] = temp
        return arr

def reversinglist(arr):
    count = lengthofarray(arr) + 1
    return arr[-1:-(count):-1]



arr = [10,20,3,4,5,1]
print(lengthofarray(arr))
print(insertlist(2,10,arr))
print(appendlist([1,2],arr))
print(removeelement(3,arr))
print(popelement(3,arr))
print(clearlist(arr))
print(indexofvalue(10,arr))
print(sortlist([1,2,10,29,15],False))
print(sortlist([1,2,10,29,15],True))
print(reversinglist(arr))

