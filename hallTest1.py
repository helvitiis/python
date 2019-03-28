# Even or Odd Checker
# Ally Hall
print("Even or Odd Checker")

def main():
    number = int(input("Please Enter a Number: "))
    i = number % 2
        
    if(i > 0):  
        print("This is an odd number.")
    
    else:  
        print("This is an even number.")
        
if __name__ == "__main__":
    main()
