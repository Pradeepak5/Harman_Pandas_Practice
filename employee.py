import pandas as pd
employee=pd.DataFrame(columns=['Employee_Name','Employee_Code','Company','Designation','Salary'])
employee.to_csv("employee.csv")