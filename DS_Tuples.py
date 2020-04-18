#Tuples are sequences of multiples values separated by , written inside ()

a = (1,4,5,'python',[5.6,78])

print(type(a))

b = 1,4,5 # () is not andatory but recommended

print(type(b))

c = (4,)

print(type(c)) # single value tuple

#Accessing element inside the tuple -- Indexing

d = (1,2.4,4,5,'python')

#index will start from 0 to length-1
print(d[4])

#slicing starts from left hand side element and last with right hand side element -1
print(d[0:4])

#2 jumps everytime
print(d[0:4:2])

#negative indexing
print(d[-1:-6:-1])

#nested index
print(a[4][1])

#Mutable and Immutable -- Tuples are immutable datatypes (not possible to make single change inside tuple elements)
#methods
#index -- to find the index value of particular element in tuple
#count -- to find how many time particular element is repeated in the tuple

e = (1,2,3,4,5,1,2,3)

print(e.index(1))

def indexoftuple(value,e):
    index = 0;
    for i in e:
        index = index + 1
        if i == value:
            break;
    return index - 1;

print(indexoftuple(1,e))

print(e.count(1))

def countoftuple(value,e):
    count = 0;
    for i in e:
        if i == value:
            count = count + 1
    return count;

print(countoftuple(2,e))

#Operations
#Concatnation (+)
print((11,12,13) + (13,12,11))


def lengthoftuple(t):
    count=0;
    for i in t:
        count=count+1
    return count

tup1=11,12,13
tup2=15,16,17,18

print(lengthoftuple(tup1))
print(lengthoftuple(tup2))

#repetition (*)
print((11,12,13)*3)

#if element inside tuple is mutablee datatype it is possible to make changes to that particular datatype value
a[4][1] = 97
print(a)

#looping
f = ('9642221228','8886527425','9885822090','8500939822')
g = tuple();
for i in f:
    if len(i) ==10:
        g = g + (i,)
print(g)

