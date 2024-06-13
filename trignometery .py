# import matplotlib.pyplot as plt
# from math import cos
# #initalize empty lists
# x_new = []
# y_new = []

# #Loop to generate x and y 
# for x in range(-100 , 100):
#     y = 3 -2 *cos(x)
#     x_new.append(x)
#     y_new.append(y)
    
# #create the plot
# plt.plot(x_new, y_new)

# #Add tites and labels
# plt.title('Graph of y = 3 -2*cos(x)')
# plt.xlabel('x')
# plt.ylabel('y')

# #show the table
# plt.show()


import  matplotlib.pyplot as plt
from math import sin

#initalize the empty list
x_new = []
y_new = []

#Loop for the range
for x in range (-100,100):
    y = 3 -2 *sin(x)
    x_new.append(x)
    y_new.append(y)
    
#create the plot
plt.plot(x_new, y_new)

#add titles and labels
plt.title('Graph of y = 3 -2*sin(x)')
plt.xlabel('x')
plt.ylabel('y')

#show the table
plt.show()

# import matplotlib.pyplot as plt
# from math import tan 

# #initlaize the value of empty list
# x_new = []
# y_new = []

# #loop for the range
# for x in range (-100,100):
#     y = 3 - 2*tan(x)
#     x_new.append(x)
#     y_new.append(y)
    
# #create the plot
# plt.plot(x_new, y_new)

# #add titles
# plt.title('Graph of y = 3 -2*tan(x)')
# plt.xlabel('x')
# plt.ylabel('y')

# #show the table
# plt.show()