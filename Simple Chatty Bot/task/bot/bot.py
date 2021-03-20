print("Hello! My name is Aid.")
print("I was created in 2020.")
print("Please, remind me your name.")
name = input()
print("What a great name you have, {}!".format(name))
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
user_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is {}: that's a good time to start programming!".format(user_age))
print("Now I will prove to you that I can count to any number you want.")
number = int(input())
i = 0
while (i <= number):
    print("{}!".format(i))
    i += 1
print("Let's start your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.\n2. to decompose a program into several small subroutines.\n3. to determine the execution time of program.\n4. To interupt the execution of a program.")


while True:
    answer = input()
    correct = "2"
    if answer == correct:
        print("Completed, have a nice day!")
        print("Congratulations, have a nice day!")
        exit()
    else:
        print("Please, try again.")





