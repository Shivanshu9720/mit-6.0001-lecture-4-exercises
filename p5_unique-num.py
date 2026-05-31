# IF SECRET NUM FIND PRINT FOUND IF NOT PRINT NOT FOUND 
#THIS IS A UNIQUE PROBLEM 
 
found = False
secret = int(input('Enter The Secret number: ')) 
 
 #using for loop to search multiple time in sequence
for i in range (1,11):
    if i == secret :
        found = True         
       # means work happend so true becoz we find the number
    
if not found :# means work not done// on  above in if loop, if we not found the sec num  means 
    print('Not found')              #found = false here below [if not ] make it ture and fns run
                                    # this if condi. always run    
else:
    print("Found")        # ager top me i = sec ho gya to found true ho jayega and neche wla if me found false ho 
                           # jayega and else run                             
                                    