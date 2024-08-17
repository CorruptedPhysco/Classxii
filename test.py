
import csv
def add_emp():
  with open('emp.csv', 'a', newline='') as f:
    W=csv.writer(f)
    name = input("Enter Employee Name:")
    empno = int(input("Enter Employee Number:"))
    salary = int(input("Enter Employee Salary:"))
    L=[empno, name, salary]
    W.writerow(L)

