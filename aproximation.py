#Find approximation value of the cube root of 27 using guess=0.0 and cube = 27 
guess = 0.0
cube = 27
epilson = 0.01
increment = 0.1
while abs(guess**3 - cube) >= epilson:
        guess += increment
if abs(guess**3 -cube) >= epilson:
        print("Failed on the cube root of",cube)
else:
        print(guess,"is close enough to the cube root of",cube)
        