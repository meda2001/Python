# let discuss about datatypes in python

# before that what is data type?

'''
A data type is a classification that dictates what a variable or object can hold in computer programming.
'''
'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''

# you no need to declare which type of data python will automatically detect

#for example

myInt=5
myFloat=7.8
myComplex=1+2j

myString = "Test Message"
myBool = True

myList=[1,"test",7.6] # allow duplicates and changed

myTuple=(1,2,3,1,2) # allows duplicate and unchanged

mySet={1,2,3} #no dupilcates allows and unchanged

myDict=[
    {"name":"Test message"},
    {"name":"test message 2"}
]    # allows duplicate and changed

print(myInt,type(myInt)) # to get class type of data types
print(myFloat)
print(myComplex)
print(myString)
print(myBool)
print(myList)
print(myTuple)
print(mySet)
print(myDict)
