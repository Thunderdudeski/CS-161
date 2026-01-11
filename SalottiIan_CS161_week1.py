import datetime
from calendar import monthrange

PET_NAME = "Roxy"
PET_TYPE = "Dog"
def main():
    #Part 1
    print(f"I have a {PET_TYPE} and her name is {PET_NAME}.\n\n")

    #Part 2
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    yearly_savings = int(input("Please enter your yearly savings: "))
    print(f"Hello {name}, you are currently {age} years old. \n"
          f"In 10 years you will be {age + 10} years old."
          f"If you save ${yearly_savings} for five years, you will have ${yearly_savings * 5}.\n"
          f"Your average monthly savings is ${yearly_savings / 12}.\n\n")

    #Part 3
    seconds_in_month = monthrange(datetime.date.today().year, datetime.date.today().month)[1] * 24 * 60 * 60
    print(f"The number of seconds in the current month is {seconds_in_month}.\n\n")

    #Part 4
    total_eggs = int(input("Please enter your total eggs: "))
    print(f"This amount of eggs makes {total_eggs // 12} dozen with {total_eggs % 12} left over.")

if __name__ == '__main__':
    main()