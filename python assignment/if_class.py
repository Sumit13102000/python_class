class if_class:
    
    def positive_negative(self,num):
        if num >= 0:
            return f"{num} is positive"
        else:
            return f"{num} is negative"
        
    def check_even_odd(self,num):
        return "Even" if num % 2 == 0 else "Odd"
    
    def check_leap_year(self,year):
        if year % 100 == 0:
            if year % 400 == 0:
                print("It is a leap year")
            else:
                print("It is not a leap year")
        else:
            if year % 4 == 0:
                print("It is a leap year")
            else:
                print("It is not a leap year")