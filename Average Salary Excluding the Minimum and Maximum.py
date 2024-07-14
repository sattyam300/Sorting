def averageSalary(salary):
    salary.sort()
    return sum(salary[1:-1]) / (len(salary) - 2)
