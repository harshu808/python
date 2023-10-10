def switch_case(case):
    switch_dict = {
        'case1': 'This is case 1',
        'case2': 'This is case 2',
        'case3': 'This is case 3',
    }

    return switch_dict.get(case, 'This is the default case')


# Test cases
print(switch_case('case1'))  # Output: This is case 1
print(switch_case('case2'))  # Output: This is case 2
print(switch_case('case4'))  # Output: This is the default case
