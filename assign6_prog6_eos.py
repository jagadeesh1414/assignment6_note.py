list1 = [43,23,14,10,643,11,34,19,32]
 
even_count, odd_count = 0, 0
for num in list1:
#even numbers
 
   if num % 2 == 0:
      even_count += 1
 
 #odd numbers  
   else:    
       odd_count += 1
print("Number of even numbers from a series of numbers: ", even_count)
print("Number of odd numbers from a series of numbers : ", odd_count)