                                        #CREATING SETS
# 1. using { }
set0 = {1,2,"aar",True}
print(set0)
# 2. using set()
set2 = set((1,2,3,4,5))
print(set2)
# -> duplicate elements are removed 
# -> can contain differenet datatypes , even other sets

                                        # ACCCESSING SETS
# -> accessing sets is not possible using index - they are unordered
# -> using for loop , list comprehension , using subset

                                        # ADDING ELEMENTS
# 1. using add() method - give element to be added in parameter ~ can only add single element
set_X = {1,2,5.0,"aaa"}
print(set_X)
set_X.add(False)
print(set_X)
# 2. using update() - give elements or swquense as parameer ~ to add multiple elements or sequece of elements
set_Y = { 10 , 89.0 , 1 , "CCC"} 
set_X.update(set_Y)
print(set_X)
# -> a different example
str = set("Hello")
str.update("World")
print(str)
# 3. using union - can use union() method [ another set as parameter] OR use '|' bwtween two sets 
setA = { 1,2,3,4,5}
setB = { 5,6,7,8,9}
setC = { 7,8,9,10}
joinedSet1 = setA.union(setB)
joinedSet2 = setB | setC
print(joinedSet1)
print(joinedSet2)
# 4. using set comprehension

                                        #REMOVE ELEMENTS
# 1. remove() - element as parameter
setA.remove(4)
print(setA)
# 2.  discard() - same as remove() , diff - dont produce error even if element is not present
setA.discard(3)
print(setA)