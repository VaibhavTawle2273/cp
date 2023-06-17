#Problem solution : 10035 Primary Arithmetic


def count_carry_operations(num1, num2):
    count = 0  # Initialize the carry count to 0
    carry = 0  # Initialize the carry to 0

    while num1 > 0 or num2 > 0:
        # Get the rightmost digits of both numbers
        digit1 = num1 % 10
        digit2 = num2 % 10

        # Calculate the sum of the digits and the carry
        sum_digits = digit1 + digit2 + carry

        if sum_digits >= 10:
            count += 1
            carry = 1
        else:
            carry = 0

        # Update the numbers by removing the rightmost digit
        num1 //= 10
        num2 //= 10

    return count

# Read input until '0 0' is encountered
while True:
    num1, num2 = map(int, input().split())

    if num1 == 0 and num2 == 0:
        break

    carry_count = count_carry_operations(num1, num2)

    if carry_count == 0:
        print("No carry operation.")
    elif carry_count == 1:
        print("1 carry operation.")
    else:
        print(f"{carry_count} carry operations.")