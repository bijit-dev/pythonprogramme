def calculate_bonus(salary):
    bonus = int(salary * 0.10)
    return bonus
salary = float(input())
bonus = calculate_bonus(salary)
print(bonus)