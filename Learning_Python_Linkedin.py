## Chapter 2 Python Basics ##
## 2.1 Functions ##
## Build Function ##
def main():
    print("Hello World")
    name = input("What is your name?")
    print("Nice to meet you", name)
## Execute Function ##
if __name__ == "__main__":
     main()
## Variables and Data Types ##
myint = 5 ## Creating integer variable ##
myfloat = 13.2 ## Creating float variable ##
mystr = "This is a string" ## Creating string variable ##
mybool = True ## Creating boolean variable ##
mylist = [0, 1, "Two", 3.2, False] ## Creating list variable ##
mytuple = (0,1,2) ## Creating tuple variable ##
mydict= {"one" : 1, "two" : 2} ## Creating dict variable ##
## Displaying above variables ##
print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

## Access a member of a sequence (it is a 0 based index) ##
print(mylist[2]) # Show 3rd record of mylist #
print(mytuple[0]) # Show 1st record of mytuple#

## Access a part of a sequence ##
print(mylist[1:5]) # give me the values 1 through 5 based on the 0 based index ##
print(mylist[1:5:2]) # give me the values 1 through 5 but skip every second #

## Using slices to reverse a sequence ##
print(mylist[::-1])

## Accessing values of dictionaries ##
print(mydict["one"])

## Combining variables of different types ##
print("string type " + str(123))

#Global vs Local Variables#
mystr = "This is a string"  ## Global Variable ##

def someFunction():  # Creating new Function #
     mystr = "def" # Creating new local variable #
     print(mystr) # print local variable #

someFunction() # prints local variable #
print(mystr) # prints global variable #

def someFunction():  # Creating new Function #
     global mystr ## denotes change global variable #
     mystr = "def" # Creating new global variable #
     print(mystr) # print global variable #

someFunction() ## print the new global variable ##
print(mystr) ## prints the same variable ##

### Comments in code ##

## 1. Example of a single line comment ##
# Example of a single line comment #

## 2.Example of a multi-line comment ##
# Example of a #
# multi #
# line # 
# comment #

## 3. Example of a multi-line comment
"""
Example of a 
multi-line
comment
"""

## Deleting Variables ##
Craig = "Craig" ## New Variable ##
del Craig ## Delete Variable ##
print(Craig) ## Variable will not print as it is deleted ##

