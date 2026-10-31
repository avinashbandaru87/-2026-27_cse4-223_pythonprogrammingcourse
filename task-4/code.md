Employee Payroll and Deduction Analysis
Problem Statement

Develop a Python program to calculate an employee's salary by considering:

Basic Pay
Allowances
Overtime Pay
Incentives

The program should:

Calculate the Gross Salary.
Apply progressive deductions based on salary slabs.
Calculate the Net Salary.
Generate a formatted salary statement showing earnings, deductions, and final payable salary.
Deduction Policy
Gross Salary	Deduction RateUp to ₹20,000	5%
₹20,001 - ₹50,000	10%
Above ₹50,000	15%
Algorithm

Start.

Input employee ID, name, and basic pay.

Input allowances, overtime pay, and incentives.

Validate that all amounts are non-negative.

Calculate Gross Salary:

Gross Salary = Basic Pay + Allowances + Overtime Pay + Incentives


Determine deduction percentage:

Gross Salary ≤ ₹20,000 → 5%
Gross Salary ≤ ₹50,000 → 10%
Gross Salary > ₹50,000 → 15%

Calculate Deduction Amount.

Calculate Net Salary:

Net Salary = Gross Salary - Deduction


Display formatted salary statement.

Stop.

Flowchart
 ┌──────────┐
 │  Start   │
 └────┬─────┘
      │
      ▼
 ┌───────────────┐
 │ Input Employee│
 │ Details       │
 └────┬──────────┘
      │
      ▼
 ┌────────────────┐
 │ Input Salary   │
 │ Components     │
 └────┬───────────┘
      │
      ▼
 ┌────────────────┐
 │ Validate Input │
 └────┬───────────┘
      │
      ▼
 ┌────────────────┐
 │ Calculate Gross│
 │ Salary         │
 └────┬───────────┘
      │
      ▼
 ┌────────────────┐
 │ Apply Deduction│
 │ Rate           │
 └────┬───────────┘
      │
      ▼
 ┌────────────────┐
 │ Calculate Net  │
 │ Salary         │
 └────┬───────────┘
      │
      ▼
 ┌────────────────┐
 │ Display Salary │
 │ Statement      │
 └────┬───────────┘
      │
      ▼
 ┌──────────┐
 │   End    │
 └──────────┘

Python Source Code
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

Sample Input
Enter Employee ID: EMP101
Enter Employee Name: Ram

Enter Basic Pay: 35000
Enter Allowances: 5000
Enter Overtime Pay: 3000
Enter Incentives: 2000

Sample Output
========================================
      EMPLOYEE SALARY STATEMENT
========================================
Employee ID      : EMP101
Employee Name    : Ram
----------------------------------------
Basic Pay        : ₹ 35000.0
Allowances       : ₹ 5000.0
Overtime Pay     : ₹ 3000.0
Incentives       : ₹ 2000.0
----------------------------------------
Gross Salary     : ₹ 45000.0
Deduction Rate   : 10.0 %
Deductions       : ₹ 4500.0
----------------------------------------
Net Salary       : ₹ 40500.0
========================================

Mermaid Flowchart Code
flowchart TD

A([Start])

B[/Enter Employee ID and Name/]

C[/Enter Basic Pay, Allowances, Overtime Pay, Incentives/]

D{Any Value < 0?}

E[Display Error Message]

F[Calculate Gross Salary]

G{Gross Salary <= 20000?}

H[Apply 5% Deduction]

I{Gross Salary <= 50000?}

J[Apply 10% Deduction]

K[Apply 15% Deduction]

L[Calculate Deduction Amount]

M[Calculate Net Salary]

N[Generate Salary Statement]

O([End])

A --> B
B --> C
C --> D

D -- Yes --> E
E --> O

D -- No --> F

F --> G

G -- Yes --> H
H --> L

G -- No --> I

I -- Yes --> J
J --> L

I -- No --> K
K --> L

L --> M
M --> N
N --> O

Formula Used
Gross Salary = Basic Pay + Allowances + Overtime Pay + Incentives

Deduction Amount = Gross Salary × Deduction Rate

Net Salary = Gross Salary − Deduction Amount


This program demonstrates payroll processing, progressive deductions, salary analysis, input validation, and formatted salary statement generation.
