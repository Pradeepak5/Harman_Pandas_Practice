import pandas as pd
df=pd.read_csv("Student.csv")
print(df.info())

student=pd.DataFrame([['Pradeep','1'],['deepak','2']],columns=('Name','RollNo'))
student.to_csv("studentdata.csv")
print("csv file created successfully")

