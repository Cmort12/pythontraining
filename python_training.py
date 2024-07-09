# Chapter 1 and Chapter 2 #
print("Hello World!")
print("Goodbye World!")
4*4
10/2 +3
name = "Craig"
print("Hello" , name)
# Chapter 3 #
age = 36 ## Declaring the variable ##
print(age) ## Printing the variable ##
print(type(age)) ## Printing the type of data ##
email = "john.doe@example.com"  ## Declaring the variable ##
print(email) ## Printing the variable ##
print(type(email)) ## Printing the type of data ##
cookies = "Sugar" ## declare variable ##
print(cookies) ## print variable ##
cookies = 1  ## redeclare variable ##
print(cookies) ## print new result for variable ##
print(type(cookies)) ## print data type of new result for variable ##
2+3 ## addition ##
5-3 ## subtraction ##
2*3 ## multiplication ##
2**3 #### power ###
3/2 #### division###
3//2 #### division without remainders ####
5%3 #### remainders from division ####
45000/5
0.2+0.5
0.2/0.3
# Chapter 4 #
4==2*2 ## Does 4 equal 2 * 2 ##
name = "Annyce" ## declare variable name as Annyce ##
name== "Frank" ## does variables name equal Frank ##
5==4 #does 5 equal 4?#
5!=4 #does 5 not equal 4?#
5>4 #is 5 greater than 4#
5<4 #is 5 less than 4#
age=15 ## declare age variable ##
age_to_drive = 15 ## declare variable age_to_drive ##
age == age_to_drive ## does age equal age to drive ##
# An if else statement #
if 5>6: ## condition ##
    print("Yes, 5 is greater than 6.") ## result if true ##
else: 
    print("No, 5 is not greater than 6") ## result if false ##
    print("Everyone knows that") ## result if false ##
answer = input("Hi, What is your favourite food?") ## question ##
if answer == "pizza": ## condition ##
    print("Yep! So amazing!") ## result if true ##
else: print("Yuck! That's not it!") ## result if false ##

print("Thanks for Playing!") ## Seperate text not included in if statement ##
### Chapter 5 ###
print("~~ The Shimmy ~~")

# This is the code without the use of the function ##
print("Take one step to the right and stomp")
print("Take one step to the left and stamp")
print("Shake those hips")

print("Take one step to the right and stomp")
print("Take one step to the left and stamp")
print("Shake those hips")

print("Take one step to the right and stomp")
print("Take one step to the left and stamp")
print("Shake those hips")
## This is a way to produce the same output with a function ##
def shimmy():
    print("Take one step to the right and stomp")
    print("Take one step to the left and stomp")
    print("Shake those hips")

shimmy()
shimmy()
shimmy()

## Parameters which change the function ##
def car_wash(amount_paid): ### function called car_wash and parameter called amount_paid ##
    if(amount_paid==12): ## condition if amount_paid = 12 ##
        print("Wash with tri-colour foam") ## present below text if amount_paid = 12 ##
        print("Rinse twice")
        print("Dry with large blow dryer")
    if(amount_paid==6): ## condition if amount_paid = 6 ##
        print("Wash with white foam") ## present below text if amount_paid = 12 ##
        print("Rinse once")
        print("Air dry")

car_wash(6)    ## presents text when amount_paid = 6 ##
car_wash(12) ## presents text when amount_paid = 12 ##
## Returning values from functions ##
def withdraw_money(current_balance, amount) : ## creating function with two parameters##
    if(current_balance >= amount): ## rule to return value ##
        current_balance = current_balance - amount ## rule of returned value ##
        return current_balance ## forces presentation of returned value

balance = withdraw_money(100,80) ## rule to create variable balance ##

withdraw_money(100,50) ## function to return value ##

if (balance <= 50): ## rule to test what text to present ##
    print("We need to make a deposit") ## present text when true ##
else:
    print("Nothing to see here") ## present text when false ##

### Favourite city challange ###
# Function called favourite_city #
# favourite_city should have one parameter: name #
# you should call favourite_city at least three times #
# The output should include : "One of my favourite cities is"#

def favourite_city(name):
    print("One of my favourite cities is", name)

favourite_city("Melbourne")
favourite_city("Canberra")
favourite_city("New York")

### Example of strip ##
txt = "    Ferrari   " ## Variable ##
x = txt.strip() ## variable to strip above
print("I am a buying a", txt, "tomorrow.") ## Example of no strip ##
print("I am a buying a", x, "tomorrow.") ## Example of strip ##

craig = "zzz   Craig zzz" ## Variable that needs strip ##
print(craig.strip(" z")) ## Example of strip with character that needs to be stripped ##
