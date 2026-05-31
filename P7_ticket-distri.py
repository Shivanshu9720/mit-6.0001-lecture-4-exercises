# THREE PEOPLE ALYSSA ,BEN, CINDLY(SEENDLY)
# TOTAL NO OF TICKET X  AND DISTRIBUTE
#BEN SELLS 2 FEWER(SUBTRACT ,MINUS) THAN ALYSA
#CINDLY SELLS TWICE AS MANY AS ALYSSA, HOW MANY DID ALYSSA SELL


# FIST WAY ❌ , SLOW FOR BIG NUMB LIKE 1100 TICKET

# for alyssa in range(11)  : # [ticket = 10]//FIRST WE CHECK ALL POSSIBLE VALUE COMBINATION CAN BE (USE FOR LOOP):
#     for ben in range(11):
#      for cindly in range(11):  # IT CHACK MANY TYPE TOO LONG 
        
#           #THESE ARE EQUATION || CAN TRUE OR FALSE(BOOLEAN):
#         total = (alyssa + ben + cindly == 10)  # uper for loop se hm theno ki different value ko late h or neche satisfy krte h if
#         ben_sell = (ben == alyssa-2)         
#         cindly_sell = (cindly == 2*alyssa)   # yaha hm theno logo ki ese value ka set le rhe h jo theno cond ko satisfy kre
                                            
#           # CONDITIONS         # 🎯BECOZ OF (AND)IF ONE OF THAM IS FLASE CONDITION BECOME FALSE || BECOZ IF RUN WHEN TURE:
#         if total and ben_sell and cindly_sell :
#             print(f'Alyssa sold {alyssa} Tickets')   
#             print(f'ben sold {ben} Tickets')         
#             print(f'cindly sold {cindly} Tickets')  # when we get these three combination value which satisfyed above
#                                                    # three condition than it run ❤️
                                                   
                                                   
# FAST CODE WITH ONE VARIABLE   ✅
# IT IS FAST FOR ALSO BIG NUMBER 


ticket = int(input('TOTAL NUM OF TICKET :'))
a = int(input('BEN SELLS HOW FEWER THAN ALYSA :'))
for alyssa in range(ticket + 1) :
    ben = max(alyssa - a , 0)  
    cindly = alyssa *2
    
    if ben + cindly + alyssa == ticket : # '==' BOLLEN CAN TRUE/FLASE:
        print(f'Alyssa sold {alyssa} Tickets')   
        print(f'ben sold {ben} Tickets')         
        print(f'cindly sold {cindly} Tickets')  
               
                                                 