# evaluate / guess :square root of x 
guess  = 0
neg_value = False
x = int(input("Enter Your Interger :"))
if x<0:
    neg_value = True
 # if user put negative value 
# square root is not define for negative value




while guess**2 < x :
    guess+=1
if guess**2 == x:
    print(guess,'Is square root of',x)
    
else:
    print(x,'is not a perfect square')  
    if neg_value:      
     print('Just checking .... did you mean',-x )
