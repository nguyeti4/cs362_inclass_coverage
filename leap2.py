#To run: python filename.py

def leap(string):
    #string = input("Enter a pos. int: ")
    if(string.isdigit()==True):
        num = int(string)
        if (num % 400) == 0 :
            return (str(num) + " is a leap year")
        else:
            if (num % 100) == 0:
                return (str(num) + " is not a leap year")
            else:
                if (num % 4) == 0:
                    return (str(num) + " is a leap year")
                else:
                    return (str(num) + " is not a leap year")
    else:
        if(string[0]=='-'):
            return ("error: input needs to be a POSITIVE int")
        else:
            return ("error: input needs to be an INT")
#leap()