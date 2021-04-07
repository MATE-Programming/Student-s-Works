user_input = input("Enter number: ")
if user_input.isdigit(): # isdigit() возврвщает True если значение input является положительным числом!
    print(user_input, "is number")
else: # а в остальом случае возвращает False
    print(user_input, "is not number")