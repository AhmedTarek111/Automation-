
from datetime import date
def Days_Calculator():
    print(''' 
        Hello ,
                    this is some instructions
                            (-_-) 
        1- please type dates in this format (YYYY-MM-DD)
        2- if there single monthes or days type zero before them like may => 05  
        ''')
    while True:    
    # this is dates inputs from user
        try:    
            date1=input("Date 1 :")
            date2=input("Date 2 :")
            # logic of function 
            d1=date.fromisoformat(date1)
            d2=date.fromisoformat(date2)
            result=(d2-d1).days
            print(f"{result} days between dates")
        except ValueError:
                print("don't forget type zero before singe days and months")

        again=input("do you want to do calculate another difference between other dates (y/n) :")
        if again == "y":
            continue
        else:
            print('''
            I hope I helped you
            Bye
            
            ''')
            break
Days_Calculator()
