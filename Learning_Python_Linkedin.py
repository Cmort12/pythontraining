git config
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

## Match Case Statements (compare multiple values) ##
value = "one" ## value that will be matched ##
match value: ## create match and denote which value ##
     case "one": ## match this value ##
          result = 1 ## result if matched ##
     case "two": ## match this value ##
          result = 2 ## result if matched ##
     case "three" | "four": ## match either of these values ##
          result =(3,4) ## result if either of above matched ##
     case _: ## If no match ##
          result = -1 ## result if no match ##
print(result) ## result = 1 ##

value = "three" ## value that will be matched ##
match value: ## create match and denote which value ##
     case "one":  ## match this value ##
          result = 1 ## result if matched ##
     case "two":  ## match this value ##
          result = 2 ## result if matched ##
     case "three" | "four": ## match either of these values ##
          result =(3,4) ## result if either of above matched ##
     case _: ## If no match ##
          result = -1 ## result if no match ##
print(result) ## result = (3,4) ##

value = "42" ## value that will be matched ##
match value: ## create match and denote which value ##
     case "one": ## match this value ##
          result = 1 ## result if matched ##
     case "two": ## match this value ##
          result = 2 ## result if matched ##
     case "three" | "four": ## match either of these values ##
          result =(3,4) ## result if either of above matched ##
     case _: ## If no match ##
          result = -1 ## result if no match ##
print(result) ## result = -1 ##

## Loops ##

## A while Loop ##
def whilefunc(): ## Create new function ##
     x = 0 ## value of x is 0 ##
     while(x < 5): ## perform this loop while x is still less than 5 ##
          print(x) ## print the value of x ##
          x = x + 1 ## print all the values of x from the original definition to the max it is still less than 5 ##
whilefunc() ## Run the created function.

## A for Loop with a range of numbers ##
def forfunc(): ## create function ##
     for x in range(5,10): ## define the range ##
        print(x) ## print the defined range ##
forfunc() ## run the function ##

## A for loop over a collection ##
days = ["Mon", "Tues" , "Wed", "Thu", "Fri" , "Sat" , "Sun"] ## create the string collection ##
for d in days: ## define d as all values in collection ##
     print(d) ## print d being the collection ##

## Range() example ##
x = range(1,10,2) ## define the range ##
for n in x: ## set all values of n as the values of the range ##
     print(n) ## print n which is all values of the range

# Break Statement #
for x in range(5,10): # define x as range(5,10)
     if x == 7: # Set condition where x = 7 #
          break # break the loop when the above condition is met #
     print(x) # print values of x they meet above condition which will be 5,6 #

## Continue Statement ##
for x in range(5,10): # define x as range(5,10)
     if x % 2 == 0: #Set condition when divided by 2 there are no remainders (even number)##
          continue # skip the loop when the condition is met #
     print(x) ## Print the loop ##

## Using the enumerate( ) function to get an index ##
days = ["Mon" , "Tues" , "Wed" , "Thurs" , "Fri" , "Sat", "Sun"] # Create Variable #
for i,d in enumerate(days): ## enumerate retuns item and the index of the item in question
     print(i,d) # print both the item and the index ##

## Creating Classes ##
class vehicle(): ## create the bass class vehicle ##
     def __init__(self, body_style): ## details the parameters that will need to be passed in for the class vehicle()##
         #self is always passed in the init() method. It represents the object of the class itself #
         self.body_style = body_style ## denotes that the variable is unique to each instance and is passed in through a parameter ##

     def drive(self,speed): ## new function called drive passed into the class vehicle ()  and defines the parameters that will need to be passed in##
          self.mode = "driving" # a defined property for the drive function shared by all instances
          self.speed = speed # this property is passed in through a parameter and is unique for each instance

class car(vehicle): ## creates a sub class for vehicle()
     def __init__(self,engine_type): # defines the parameters that need to passed in for the function car(). #
          super().__init__("Car") # defines the body_style parameter for car() and init is required to add parameters for car()
          self.wheels = 4 # creates a defined property for wheels for all cars #
          self.doors = 4 # creates a defined property for door for all cars #
          self.engine_type = engine_type # this property is passed in through a parameter and is unique for each instance #

     def drive(self,speed): # defines the function for the drive class #
          super().drive(speed) # defines the class the function is dependent on and the parameter that needs to be passed in #
          print("Driving my", self.engine_type, "car at", self.speed) # print the following result based on the parameter in the class and function

class motorcycle(vehicle): ## creates a subclass for vehicle() called motorcycle()
     def __init__(self,engine_type, has_side_car): # defines the parameters for the motorcycle() class 
          super().__init__("Motorcycle") # defines the body_style parameter for motorcycle() and init is required to add parameters for motorcycle()
          if (has_side_car): # defines the condition if true
               self.wheels = 3 #result if true
          else:
               self.wheels = 2 #result if false #
          self.doors = 0 # defined parameter for all motorcycle() results
          self.engine_type = engine_type # property that requires a parameter to be passed through
     
     def drive(self,speed): # defines the function for the drive class #
          super().drive(speed) # defines the class the function is dependent on and the parameter that needs to be passed in #
          print("Driving my", self.engine_type, "motorcycle at", self.speed) # print the following result based on the parameter in the class and function

car1 = car("gas") # car1 has a engine_type gas
car2 = car("electric") # car2 has a engine_type electric
mc1 = motorcycle("gas", True) #mc1 has a gas engine type and a sidecar

print(mc1.wheels) # displays 3 as it has a side car
print(car1.engine_type) #prints gas as it is defined above
print(car2.doors) #prints 4 as all cars have 4 doors
print(car1.body_style) # prints Car as all car have a body_style Car

car1.drive(30) #Prints "driving my gas car at 30" as a result of drive() class and value defined for car1 and parameter passed through
car2.drive(40) #Prints "driving my electric car at 40" as a result of drive() class and value defined for car2 and parameter passed through
mc1.drive(50) #Prints "driving my gas motorcycle at 50" as a result of drive() class and value defined for mc1 and parameter passed through


## Importing and using modules ##
import math ### import of the math module ##
print("The square root of 16 is", math.sqrt(16))## math.sqrt produces the square root of a value ##
print(math.pi) ## produces the pi value ##
print(math.ceil(27.4)) #rounds numbers up to the nearest integer being 28 in this case ##
print(math.floor(27.6)) #rounds number down to the nearest integer being 27 in this case #
print(math.log(100)) # produces the natural logarithim of the number being 4.605 in this case##


# Exception Handling #

# Traditional code with error that will error ##
x = 10/0 # write a code to produce an error #

## Code that tells you how to better present error ##
try: ## condition = no error##
     x= 10/0  #result if there is no error
except: ## condition = error  ##
     print("Well that didn't work") ## result if there is error

## code that handles communicates the type of errors ##
try: ## condition =  no error ##
     answer = input("What should i divide by 10 by?") ## answer is the input to this question #
     num = int(answer) # the number trys to convert the answer to a integer
     print(10/num) # if no error print 10/num
except ZeroDivisionError as e: # condition = divide by zero error
     print("You can't divide by 0") # print if above condition met
except ValueError as e: # condition = cannot be converted to integer
     print("You didn't give me a valid number") # print if above condition met
     print(e) # detail error if condition (cannot be converted to integer met)
finally: ## print all the time
     print("This code always runs") # print all the time

### Palindrome test ###
## Palindromes are words that when punctuation and capitalisation is removed they have the same letters ## 

test_words = ["Hellow World!", "Radar", "Mama?", "Madam i'm adam", "Race Car!"]
total = 3

def is_palindrome(teststr):
     # convert the string to all lowercase #
     temp = teststr.lower()
     ## strip all the spaces and punctuation from the string ##
     newstr = ""
     for c in temp:
          if c.isalnum():
               newstr += c ##add to string ##
     ## now calculate the reverse of the string ##
     reversestr = ""
     strindx = len(newstr) - 1
     while (strindx >= 0):
           reversestr += newstr[strindx]
           strindx -= 1
     
     if newstr == reversestr:
          return True
     return False

for word in test_words:
     is_palindrome(word)


## Working with files ##
def main(): ## create new function ##
     ## for file called textfile.txt have write permission and open if not created ## 
     myfile = open("textfile.txt","w+")
     for i in range(10): ## write this many lines of data in the file
          myfile.write("This is some text\n") ## write this line
     myfile.close() ##close the file when done
main()  ## run the function

def main2(): ## create new function ##
     myfile = open("textfile.txt" , "a+") ## append the file (add to the end)  ##
     for i in range(10): ## write this mny lines of data in the file
          myfile.write("This is some new text\n") ## write this text in the file
     myfile.close() ## close the file

main2()

def main3(): ## create new function
     myfile = open("textfile.txt", "r")  ## open with read permissions only
     if myfile.mode == 'r': ## if open with correct permissions
          contents = myfile.read() ## read the file
          print(contents) ## print out the relevant lines
main3()

def main4(): ## create new function ##
     myfile = open("textfile.txt", "r") ## open with read permissions only
     if myfile.mode == "r": # if open with the correct permssions 
          fl = myfile.readlines() ## returns each line of the file 
          for x in fl: ## loop for each line in the new file
               print(x) ## print each line

main4()

### Finding information about a file ##
import os
from os import path
import datetime 
from datetime import date, time, timedelta
import time

# Print the name of the OS (Operating System)
def os_function(): ## create new function ##
     print(os.name) ## call module os and name to reference operating system name

os_function() ## run the function

## Check for item existence and type ##
def item_exists(): ## Create new function ##
     print("Item exists:", str(path.exists("textfile.txt"))) ## check if item exists
     print("Item is a file:", path.isfile("textfile.txt")) ## check if item is a file 
     print("Item is a directory:", path.isdir("textfile.txt")) ## check if item is a directory (it is not) ##

item_exists()

 ## Generate the item path ##
def item_path():
     print("Item's path:", path.realpath("textfile.txt")) ## the path of the file
     print("Item's path and name:", path.split(path.realpath("textfile.txt"))) ## the path and name of the file

item_path()

## Generating the modification times
def mod_time():
     t = time.ctime(path.getmtime("textfile.txt")) # get the modification time
     print(t) ## print the modification time
     print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))) # print a more readable modification time

mod_time()

## how long ago was the files modified
def mod_time2():
     td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
     ## current time - last modified time
     print("It has been", td, "since the file was modified") ## time in dd:hh:mm:ss format
     print("Or," , td.total_seconds(), "seconds") ## time in seconds 

mod_time2() # run created function

## Manipulate the filesystem shell methods using the operating system's shell utilities ##
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main_12(): # create new function to make a duplicate of the file
     if path.exists("textfile.txt"): ## if the file exists
          src = path.realpath("textfile.txt") ## get the real path in the directory ##
          dst = src + ".bak" # adds parameter of name of file + bak to denote that it is a backup
          shutil.copy(src, dst) ## this creates the copy

main_12() ## run the function ##

def renamefile(): ## create new function to rename the file ##
     if path.exists("textfile.txt"): # if the file exist 
          os.rename("textfile.txt", "newfile.txt") # rename the file

renamefile() ## run the function

def store_in_zip(): ## create new function
     if path.exists("newfile.txt"): ## if file exist
          src = path.realpath("newfile.txt")
          root_dir, tail = path.split(src) ## assigns the two values of the split the crucial one here being the directory value
          shutil.make_archive("archive", "zip", root_dir) ## function is make archive as a zip usinng the directory from the file

store_in_zip()

def control_in_zip() : ## create new function
     with ZipFile("testzip.zip","w") as newzip: ## create testzip.zip and give write access and then create variable as newzip
          newzip.write("newfile.txt") ## add this file to the zip
          newzip.write("textfile.txt.bak") ## add this file to the zip

control_in_zip() ## run the function

### Finding the size of a type of file in a directory ##
def file_info():
     total_bytes = 0 ## parameter total_bytes is reset to 0
     folder = "deps" ## parameter folder is set as deps
     dirlist  = os.listdir(folder) ## pull the list of files in the folder ##
     for entry in dirlist: ## for every file in the directory ##
          if os.path.isfile(folder + "/" + entry) and entry.endswith(".txt"): ## for every file in the directory that ends in txt and is a text file ##
               filesize = os.path.getsize(folder+ "/" + entry) ## find the size of all files in deps that are a text file ##
               total_bytes += filesize ## add all the filesizes calculated
     return total_bytes

file_info()

### Date, Time and Datetime classes ###
import datetime
from datetime import date, time, datetime

def today_date(): ## create a new function ##
     today = date.today() ## make parameter today equal today's date
     print("Today's date is ", today) ## print "Today's date is" with previously created parameter

today_date() ## run function

def today_information(): # create new function #
     today = date.today() # create parameter today with today's date #
     print("Date Components = Date:", today.day, "Month:" , today.month, "Year:", today.year) 
     # pull out the year, day and month of the date and print them ##

today_information()

def today_weekday(): ## create new function
     today = date.today() # create a parameter called today with information on the current date
     print("Today's weekday number is", today.weekday()) 
     ## Produces a number relevant to the weekday of today 0 =  Monday and 6 = Sunday ##
     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
     ## parameter of days of week in the relevant order of the weekday number ##
     print("Which is a", days[today.weekday()]) ##produce the weekday by searching the parameter with number of the day
today_weekday() 

def today_now(): #create new function
     today = datetime.now() ## create parameter as current date and time
     print("The current date and time is", today) 
     ## print "The current date and time is" and the parameter previously created
today_now()

def time_now(): #create new function
     t = datetime.time(datetime.now()) ## factor of the time component of the current date and time
     print("The current time is",t) ## Prints "The urrent time" and the factor created above]
time_now()