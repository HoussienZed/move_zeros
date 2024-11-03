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
