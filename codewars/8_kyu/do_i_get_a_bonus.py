def bonus_time(salary: int, bonus: bool) -> str:
    """
    If bonus is true, the salary should be multiplied 10.
    If bonus is false, one must receive only his stated salary.
    """
    # return "$" + str(salary * 10) if bonus else "$" + str(salary)
    return f"${salary * 10 if bonus else salary}"


print(bonus_time(1000, True))