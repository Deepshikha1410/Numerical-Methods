#Write a python program to calculate approximation values of cube root of 27.Avoid infinte looping using below all three method
#1 write a code using if-break statement
guess = 0.0
cube = 27
increment = 0.0001
while abs(guess**3 - cube) > increment:
    guess += increment
print(f"The cube root of{cube} is {guess :.4f}\n")



# #2 write a code using iteration counter
cube = 27
epison = 0.00001
guess = cube / 2.0
iteration_counter = 0 
while True:
    iteration_counter+=1
    guess_new = (2*guess + cube / (guess **2)) / 3.0
    if abs(guess_new - guess) < epison:
        break
    guess = guess_new
    
print(f"iteration counter: {iteration_counter}")
print(f"The cube root of 27:{guess_new: .6f}\n")

    
# #3 write a code using for loop on a guess value
guess = 0.0
cube = 27
increment = 0.5
epison = 0.01

for i in range(100):
    guess += increment
    if abs(guess**3 - cube) < epison:
        print(guess, "is close enought to cube root of", cube)
        break

else:
    print(guess, "is not close enought to cube root of", cube)


