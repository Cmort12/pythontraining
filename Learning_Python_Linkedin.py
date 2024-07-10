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

## define a basic function ##
def func1(): ## define function ##
     print("I am a function") ## indentation to denote that it is in function and denote print ##
func1() ## will print function ##
print(func1()) ## will print function prints "None" because the print is already in function ##

## Functions that take arguments ##
def func2(arg1,arg2): ## create function and denote two variables arg1 and arg2 ##
     print(arg1, "", arg2) ## print arg1 and arg2

func2(10,20) ##function with arg1 = 10 and arg2 = 20 #

## Functions that return a value##
def cube(x): ## create new function with variable x
     return x*x*x ## print the value x^3 for calculation of cube

cube(3) #prints x^3
print(cube(3)) #also prints x^3

## Functions with default value for an argument ##
def multiplication(num, x=1): ## new function with two variables. Denotes x =1 when there is no assignment for x. ##
    return num * x #return the value of num * x (the two variables in the function)

multiplication(3) # returns 3 * 1(the default value for x)
multiplication(3,3) #returns 3*3

## Functions with variable number of arguments ##
def multi_add(*args): ## deonte multiple variables in function
     result = 0 ## result at the start = 0
     for x in args: ## this is a loop it will be covered later, essentially it means do this for all values of x ##
         result = result + x ## means add all the values of x. 0 + x1 = x1, x1 +x2 = sum1 then sum1 +x3 abd so forth ##
     return result ## return the sum of all values of x achieved before ##

multi_add(1,2,3,4,5,6) ## returns the sum of the variables ##
multi_add(10,20,30,30) ## returns the sum of the variables ##

## Chater 2.4 Conditional Structures ##
 ## ELIF ##
def main(): # Create new function ##
     x, y = 10, 100 # Values for x and y respectively
     if x < y: ## check if x is less than y ##
          result = "x is less than y" ## result if x is less than y ##
     elif x == y: ## check if x is equal to y ##
          result = "x is equal to y" ## result if x equals y ##
     else: ## denotes creation of result if above are false ##
        result = "x is greater than y" ## result if above two conditions are false ##
     print(result) ## print result of above rules and conditions ##
main() ## use function ##

def main1():# Create new function ##
     x, y = 1000, 100  # Values for x and y respectively
     if x < y: ## check if x is less than y ##
          result = "x is less than y" ## result if x is less than y ##
     elif x == y: ## check if x is equal to y ##
          result = "x is equal to y" ## result if x equals y ##
     else: ## denotes creation of result if above are false ##
        result = "x is greater than y" ## result if above two conditions are false ##
     print(result) ## print result of above rules and conditions ##
main1() ## use function ##

def main2(): # Create new function ##
     x, y = 100, 100 # Values for x and y respectively
     if x < y: ## check if x is less than y ##
          result = "x is less than y" ## result if x is less than y ##
     elif x == y: ## check if x is equal to y ##
          result = "x is equal to y" ## result if x equals y ##
     else: ## denotes creation of result if above are false ##
        result = "x is greater than y" ## result if above two conditions are false ##
     print(result) ## print result of above rules and conditions ##
main2() ## use function ##


## Conditional Statements Let you use "a if C else b". ##
x, y = 10, 100 ## assign values for x and y ##
result1 = "x is less than y" if x < y else "x is greater to or equal to y" ## denote result for x is less than y and other ##
print(result1) ## print result ##
x, y = 1000, 100 ## assign new values for x and y ##
result2 = "x is less than y" if x < y else "x is greater to or equal to y" ## denote result for x is less than y and other ##
print(result2) ## print result ##