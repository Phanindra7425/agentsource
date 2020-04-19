# Dictionaries -- Sequence of Key:value pairs seperated with comma(,) declared inside { }...

a={"username":"ramesh","password":"ramesh123",'emails':["ramesh123@gmail.com","ramesh@gmail.com"],'username':"suresh",1:21,(11,1):"Django"}

# Limitation for Dictionaries:
    # Dictionaries may contain duplicate keys. But while exectuion it will consider only lastest key:value pair into consideration.......
    # Dictionary keys should be immutable only......(definite)
print(a)

# immutable datatypes -- numbers,string,tuple
# mutuable datatypes-- list,dictionary,sets.

# accessing inside the dictinarise will be using key-name...
print(a['emails'])

# print(a['city']) #- it will return error as key name is not present in dictionary

#
# # .get() -- will retunr None if the key is not present inside the dictionary...
#
print(a.get('emails'))
print(a.get('city'))
#
#
# # Dictionaries are Mutubale...
#
b={"username":"ramesh","password":"ramesh123",'emails':["ramesh123@gmail.com","ramesh@gmail.com"]}
#
#
# # if key is present already it will update the value of the particular key...
b['username'] ="Suresh"
print(b)
# # if the key is not present it is adding it as new key:values pari into the dictionary..
print(b)
b['city']="Hyderabad"
print(b)
#
# print(dir(dict))
#
#
# # Dictionary Methods:-
#
# # update() -- It for adding a dictionary with other dictionary..

c={"username":"ramesh","password":"ramesh"}
print(c)
d={"email":"ramesh@gmail.com","city":"hyderabad"}
print(d)
#Appending the c and d dictinary
c.update(d)
print(c)
#
#
# # Removal Methods
#     # pop
#     # popitem
#     # clear
#
# # pop -- It for removing a key:value pair from the dictionary..
#
e={"username":"ramesh","password":"ramesh123","username":"suresh",'emails':["ramesh123@gmail.com","ramesh@gmail.com"]}
#
#
f=["emails","password"]
#
print(e)
for j in f:
    e.pop(j)

print(e)
e.pop('username')
print(e)

# # popitem() -- for removing a single key:value pair at atime by default the last key:value pair..
g={"username":"ramesh","password":"ramesh123","username":"suresh",'emails':["ramesh123@gmail.com","ramesh@gmail.com"]}
print(g)
g.popitem()
print(g)
# # clear() -- for removing everything and make it as empty dictionary..
g.clear()
print(g)

# # keys() -- it will return all the keys present inside the dictionary()...
h={"one":'1',"two":'2',"three":'3'}
print(h.keys())

# # values()() -- it will return all the values present inside the dictionary..

print(h.values())

# # item() -- It will retunr the key:value pair present inside the dictionary..

print(h.items())

# # copy() --

j=h # assigning the memory allocation of A value..
print(j)
k=j.copy()
print(k)

print(a)
a['email']="ramesh@gmail.com"

print(a)
print(b)

# print(dir(dict))


a=["username","password","city","emails"]

b={}

for j in a:
    b[j]=None

print(b)
#
# # fromkeys() -- updating the values to all keys presesnt in the dictinoary

print({}.fromkeys(a,['ramesh',"ramesh123"]))

l={}
l.setdefault('username')
print(l)


# # dictionary Comprehension
#
# # {key:values for elments in sequence} -1
# # {key:values for elment in sequence if condition} -2
# # {key:values if condition else values for elments in sequence}
#
range(1,11)
# { 1:2,2:4,3:6,4:8,5:10,6:12 }
print({j:j*2 for j in range(1,11)})

b= {}

for j in range(1,11):
    b[j]=j*2

print(b)
#{3:9,6:18,9:27}
print({j:j*3 for j in range(1,11) if j%3==0})

b={}

for j in range(1,11):
    if j%3==0:
        b[j]=j*3

print(b)


#{1: 4, 2: 4, 3: 12, 4: 8, 5: 20, 6: 12, 7: 28, 8: 16, 9: 36, 10: 20}
print({j:j*2 if j%2==0 else j*4 for j in range(1,11)})

b={}

for j in range(1,11):
    if(j%2 ==0):
        b[j]=j*2
    else:
        b[j]=j*4

print(b)


