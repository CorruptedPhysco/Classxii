def add_emp():
  with open('emp.csv', 'a', newline='') as f:
    W=csv.writer(f)
    W.writerow(['employee number','employee name','salary'])
    name = input("Enter Employee Name:")
    empno = int(input("Enter Employee Number:"))
