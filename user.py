import pandas as pd
user=pd.DataFrame(columns=['Name','Address','Gender','Mobile Number','Emailid','UserName','Password'])
user.to_csv("user.csv")