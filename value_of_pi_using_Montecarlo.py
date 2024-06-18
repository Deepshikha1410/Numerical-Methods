import random

N = 1000                         #initialize the value of N    

circle_point = 0                 #initialize the value of circle_point
square_point = 0                 #initalize the value of square_point

for i in range(N**2):
    #Range of x and y values is -1 to 1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    
# Distance between (x, y)
    original_dist = x**2 + y**2

#check if (x,y) lies isnide the circle
    if original_dist <= 1:
        circle_point +=1
        
    square_point += 1

#calculate the value of pi
pi = 4* circle_point/square_point

print(f"estimated value of pi is : {pi}") 