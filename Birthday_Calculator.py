from datetime import date
def  birthday_Calculator():
    
    user_birthdate=date.fromisoformat(input("your birthday date  : "))
    now=date.today()
    if (user_birthdate.month, user_birthdate.day) < (now.month, now.day):
        next_birthday = date(now.year + 1, user_birthdate.month, user_birthdate.day)
    else:
        next_birthday = date(now.year, user_birthdate.month, user_birthdate.day)
    remaining = next_birthday - now
    remaining_days = remaining.days

    return f"{remaining_days} days Left for your birthdate"
print(birthday_Calculator())