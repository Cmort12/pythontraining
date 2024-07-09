# Chapter 1 and Chapter 2 #
print("Hello World!")
print("Goodbye World!")
4*4
10/2 +3
name = "Craig"
print("Hello" , name)
# Chapter 3 #
age = 36
print(age)
print(type(age))
email = "john.doe@example.com" 
print(email)
print(type(email))
cookies = "Sugar"
print(cookies)
cookies = 1 
print(cookies)
print(type(cookies))
2+3
2*3
2**3 #### power ###
3/2 #### division###
3//2 #### division without remainders ####
5%3 #### remainders from division ####
45000/5
0.2+0.5
0.2/0.3
# Chapter 4 #
4==2*2
name = "Annyce"
name== "Frank"
5==4 #does 5 equal 4?#
5!=4 #does 5 not equal 4?#
5>4 #is 5 greater than 4#
5<4 #is 5 less than 4#
age=15
age_to_drive = 15
age == age_to_drive
# An if else statement #
if 5>6:
    print("Yes, 5 is greater than 6.")
else: 
    print("No, 5 is not greater than 6") 
    print("Everyone knows that")

answer = input("Hi, What is your favourite food?")
if answer == "pizza":
    print("Yep! So amazing!")
else: print("Yuck! That's not it!")
print("Thanks for Playing!")
### Chapter 5 ###
print("~~ The Shimmy ~~")

print("Take one step to the right and stomp")
print("Take one step to the left and stamp")
print("Shake those hips")

print("Take one step to the right and stomp")
print("Take one step to the left and stamp")
print("Shake those hips")

print("Take one step to the right and stomp")
print("Take one step to the left and stamp")
print("Shake those hips")

def shimmy():
    print("Take one step to the right and stomp")
    print("Take one step to the left and stomp")
    print("Shake those hips")

shimmy()
shimmy()

## Parameters which change the function ##
def car_wash(amount_paid):
    if(amount_paid==12):
        print("Wash with tri-colour foam")
        print("Rinse twice")
        print("Dry with large blow dryer")
    if(amount_paid==6):
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry")

car_wash(6)   
car_wash(12)
## Returning values from functions ##
def withdraw_money(current_balance, amount) :
    if(current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance

balance = withdraw_money(100,80)

if (balance <= 50):
    print("We need to make a deposit")
else:
    print("Nothing to see here")

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
