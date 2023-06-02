#class if_class:
#    def positive_negative(self, num):
#        if num>=0:
 #           return f"{num} is positive"
  #      else:
#            return f"{num} is negative"
#        
#    def check_even_odd(self,num):
#        return "Even" if num % 2 == 0 else "Odd"
# #for loop

#class for_odd_even:
#  def oddeven(self,num):
#    for i in range(num,num+1):
#        if(num%2 == 0):
#            print(num,"even")
#        else:
#           print(num,"odd")    

#obj = for_odd_even()
#print(obj.oddeven(4))

# class for_class:
    
#     def print_range(self,range_num):
#         for i in range(range_num):
#             print(i)
            
#     def reverse_order(self,range_num):
#         for i in range(range_num,0,-1):
#             print(i)
            
#     def multiplication_table(self,num,range_num):
#         for i in range(1,range_num+1):
#             print(f"{i} x {num} = {i * num}")
            
#     def display_factors(self,num):
#         for i in range(num):
#             if n % i == 0:
#                 print(i)
                
#     def prime_numbers(self,num):
#         count = 0
#         for i in range(2, num + 1):
#             if num % i == 0:
#                 count += 1
#         if count == 2:
#             print("It is a prime number")
#         else:
#             print("It is not a prime number")
            
#     def prime_factors(self,num):
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 factor = i
#                 count = 0
#                 for j in range(2, factor + 1):
#                     if factor % j == 0:
#                         count += 1
#                 if count == 2:
#                     print(factor)
                    
        
#     def number_of_digits(self,num):
#         temp = num
#         count = 0
#         for i in str(temp):
#             temp //= 10
#             count += 1
#         print(count)
        
    
# for_obj = for_class()

# while loop
class while_class:
    
    def print_range(self,num):
        i = 1
        while i <= num:
            print(i,end=" ")
            i+=1
            
    def reverse_order(self,num):
        while num > 0:
            print(num,end=" ")
            num = num - 1
            
    def multiplication_table(self,num,target_range):
        i = 1
        while target_range > 0:
            print(f"{num} * {i} = {num * i}")
            i += 1
            times -= 1
            
    def print_factors(self,num):
        while num > 0:
            if num % i == 0:
                print(i)
                i+=1
                num -= 1
    
    def prime_number(self,num):
        count = 0
        i = 1
        while num > 0:
            if num % i == 0:
                count += 1
        
        if count == 2:
            print("Prime")
        else:
            print("not prime")
            
    def prime_factors(self,num):
        i = 1
        while num > 0:
            if num % i == 0:
                factor = i
                count = 0
                j = 2
                while factor > 0:
                    if factor % j == 0:
                        count += 1
                    j+=1
                    factor-=1
                if count == 2:
                    print(factor)
        i+=1
        num-=1
        
    def num_of_digits(self,num):
        count = 0
        while(num > 0):
            count += 1
            num//=10
        print(count)
        
    def armstrong_num(self,num):
        temp = num
        temp2 = num
        digits = 0
        while temp2 != 0:
            temp2 //= 10
            digits += 1

        sum_digits = 0
        while temp != 0:
            sum_digits = sum_digits + (temp % 10) ** digits
            temp //= 10

        if sum_digits == num:
            print(f"{num} is an Armstrong number")
        else:
            print(f"{num} is not an Armstrong number")
            
    
    def palindrome_num(self,num):
        temp = num
        rev = 0
        while temp != 0:
            rev = rev * 10 + (temp % 10)
            temp //= 10

        if num == rev:
            print(f"{num} is a palindrome number")
        else:
            print(f"{num} is not a palindrome number")
    

        


