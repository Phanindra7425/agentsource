#sets -- Sequence of values separated by ',' declare inside {}

a = {1,2,'python',4.5,4.5,3,2,1}

print(a)
print(type(a))

#methods
#add -- adding a single element
a.add('django')
a.add((9,10,11))
print(a)
#update -- updating a multiple element
a.update(("framework",11,12),[9,99])
print(a)
remove -- Remove the value from the set
a.remove(1)
print(a)
# a.remove(24)
# print(a)
#del
#discard -- removes  the value
print(a)
a.discard(2)
print(a)
a.discard(24)
print(a)
#pop -- remove starrting element from the set
a.pop()
print(a)
a.pop()
print(a)
#clear -- clears the sets
a.clear()
print(a)

#Advanced Set Operations
#union (|) -- add both sets and remove duplicates
a = {1,2,3}
b= {5,6,2,1}
print(a.union(b))
print(a|b)
#intersection (&) -- duplicates elements will be printed
print(a.intersection(b))
print(a&b)
#difference (-)
print(a.difference(b))
print(a-b)
print(b-a)
#symmetric_Difference (^) -- uncommon elements of both sets
print(a.symmetric_difference(b))
print(a^b)
print(a.issuperset(b)) # is all elements of a present in b or not
print({1,2,3}.issuperset({1,2,3}))
print(a.issubset(b))
print(a.isdisjoint(b)) #if there is no common elements between both sets return true
print({1,2,3}.isdisjoint({11,12}))
