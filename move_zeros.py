def move_zeros(numbers):
    zeros = []
    no_zeros = []
    for i in numbers:
        if i == 0:
            zeros.append(i)
        else:
            no_zeros.append(i)

    moved_zeros_list = no_zeros + zeros
    return (print(f"The moved zero list is {moved_zeros_list}"))

# Entering list of numbers


numbers = int(input("Enter the length of numbers list: "))
unarranged_numbers = []
for i in range(numbers):
    number = int(input(f"Enter number {i + 1}: "))
    unarranged_numbers.append(number)

print(f"The unarranged list of numbers is= {unarranged_numbers}")
move_zeros(unarranged_numbers)
