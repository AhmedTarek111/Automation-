from datetime import date
def age_calculator():
    user_birthdate=date.fromisoformat(input("your birthday time"))
    now=date.today()
    age = now.year - user_birthdate.year - ((now.month, now.day) < (user_birthdate.month, user_birthdate.day))
    print(age) 
age_calculator()
