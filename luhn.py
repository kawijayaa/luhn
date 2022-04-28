def check(input):
    input = "".join(input.split())
    try:
        input_test = int(input)
    except:
        raise ValueError
    even_placed_num = input[-2::-2]
    even_digit_sum = 0
    for x in even_placed_num:
        num = int(x)
        str_multiplied = str(num*2)
        if num*2 >= 10:
            even_digit_sum += int(str_multiplied[0]) + int(str_multiplied[1])
        else:
            even_digit_sum += num*2
    odd_placed_num = input[::-2]
    odd_digit_sum = 0
    for x in odd_placed_num:
        num = int(x)
        odd_digit_sum += num
    verify_num = odd_digit_sum + even_digit_sum
    if verify_num % 10 == 0:
        return True
    else:
        return False
    
def create_check_digit(input):
    input = "".join(input.split())
    try:
        input_test = int(input)
    except:
        print("Not a number")
    input += "0"
    even_placed_num = input[-2::-2]
    even_digit_sum = 0
    for x in even_placed_num:
        num = int(x)
        str_multiplied = str(num*2)
        if num*2 >= 10:
            even_digit_sum += int(str_multiplied[0]) + int(str_multiplied[1])
        else:
            even_digit_sum += num*2
    odd_placed_num = input[::-2]
    odd_digit_sum = 0
    for x in odd_placed_num:
        num = int(x)
        odd_digit_sum += num
    verify_num = odd_digit_sum + even_digit_sum
    if verify_num % 10 == 0:
        input = input[:-1]
        return int(input[-1])
    else:
        return (10 - (verify_num % 10))

def main():
    while True:    
        todo = input("Create check digit or check for error? ")
        if todo.lower() == "check":
            inputted_number = input("Enter Number: ")
            inputted_number = "".join(inputted_number.split())
            try:
                inputted_number_test = int(inputted_number)
            except:
                print("Not a number")

            if check(inputted_number):
                print(f"{inputted_number} is a valid number.")
            else:
                print(f"{inputted_number} is not a valid number.")
        elif todo.lower() == "create":
            inputted_number = input("Enter Number: ")
            inputted_number = "".join(inputted_number.split())
            try:
                inputted_number_test = int(inputted_number)
            except:
                print("Not a number")

            if check(inputted_number):
                print(f"{inputted_number} already has a check digit.")
            else:
                inputted_number += str(create_check_digit(inputted_number))
                print(f"New number with check digit: {inputted_number}")
            
if __name__ == "__main__":
    main()
