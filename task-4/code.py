# Employee Payroll and Deduction Analysis

emp_id = input("Enter Employee ID: ")
emp_name = input("Enter Employee Name: ")

basic_pay = float(input("Enter Basic Pay: "))
allowances = float(input("Enter Allowances: "))
overtime_pay = float(input("Enter Overtime Pay: "))
incentives = float(input("Enter Incentives: "))

# Validation
if basic_pay < 0 or allowances < 0 or overtime_pay < 0 or incentives < 0:
    print("Error: Salary components cannot be negative.")
else:
    # Gross Salary Calculation
    gross_salary = basic_pay + allowances + overtime_pay + incentives

    # Progressive Deductions
    if gross_salary <= 20000:
        deduction_rate = 0.05
    elif gross_salary <= 50000:
        deduction_rate = 0.10
    else:
        deduction_rate = 0.15

    deduction_amount = gross_salary * deduction_rate

    # Net Salary
    net_salary = gross_salary - deduction_amount

    # Salary Statement
    print("\n")
    print("=" * 40)
    print("      EMPLOYEE SALARY STATEMENT")
    print("=" * 40)
    print("Employee ID      :", emp_id)
    print("Employee Name    :", emp_name)
    print("-" * 40)
    print("Basic Pay        : ₹", basic_pay)
    print("Allowances       : ₹", allowances)
    print("Overtime Pay     : ₹", overtime_pay)
    print("Incentives       : ₹", incentives)
    print("-" * 40)
    print("Gross Salary     : ₹", gross_salary)
    print("Deduction Rate   :", deduction_rate * 100, "%")
    print("Deductions       : ₹", deduction_amount)
    print("-" * 40)
    print("Net Salary       : ₹", net_salary)
    print("=" * 40)
