# GUESS - and - CHECK CUBE ROOT:

cube = int(input ('Enter number:'))  # normal in for loop if we take cube = 26 and not take any condition 
for guess in range(abs(cube)+1):     # it check 0 - 26 by seq it take lot of time so we make condition       
    if guess**3 >= abs(cube):         # so that if guess goes to high we exit not check all number:
        break
    
    
if guess **3 != abs(cube): # if our guess cube is not equal to cube we print:
    print( cube, 'is not a perfect cube')    
    
else:
       # this if condition run only if cube -ve 
    if cube<0: # if user give us -ve value than becoz of cube output must be -ve Ex: -216 => -6:
        # output means guss -ve ouput ho 
        guess = -guess
    
    print(f'cube root of {cube} is {guess}')
           