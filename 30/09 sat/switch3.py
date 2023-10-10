def case1():
    return "This is case 1"


def case2():
    return "This is case 2"


def case3():
    return "This is case 3"


def default_case():
    return "This is the default case"


def switch_case(case):
    switch_dict = {
        'case1': case1,
        'case2': case2,
        'case3': case3,
    }

    selected_case = switch_dict.get(case, default_case)
    return selected_case()


# Test cases
print(switch_case('case1'))  # Output: This is case 1
print(switch_case('case2'))  # Output: This is case 2
print(switch_case('case4'))  # Output: This is the default case
