#WRONG CODE❌

# s = 'abca'
# count = 0
# seen = ''
# for i in s:
#     if i !=seen:
#         count+=1
#         seen = i
   
# print(count)        
# print(seen)




# 💡 LESSON LEARNED:
#wrong code we use != for numerical value or like a!=b etc 
#for boolen we can use the opposite of in (not in )
#here we deal with string not numbers 


#  CORRECT CODE ✅:

s = 'abca'
seen = ''#string
count = 0
for char in s: # to iterates the value/ letter of s seq wise
    if char not in seen :
        seen = seen + char # seen = seen + char
        count+= 1
        
        
print(count)
print(seen)
