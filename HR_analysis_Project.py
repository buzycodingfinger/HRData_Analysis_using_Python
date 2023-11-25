import numpy as np
import pandas as pd
from datetime import date

data=pd.read_csv('HRDataset.csv')
print(data)

print(data.size)
print(data.shape)

#null values
print(data.isnull().any())

#null values sum
print(data.isnull().sum())

#replacing date of termination to 0 values
data['DateofTermination']=data['DateofTermination'].replace(to_replace=np.nan,value=0)
print(data['DateofTermination'].isnull().sum())

manager_data=data.loc[:,["Department","ManagerName","ManagerID"]]
print(manager_data)

print(manager_data.head())
print(manager_data.tail())

n_value=manager_data[manager_data['ManagerID'].isnull()]
print(n_value)

manager_data.loc[manager_data["ManagerName"]== "ManagerID"]

data['ManagerID']=data['ManagerID'].replace(to_replace=np.nan,value=39.0)
print(data.isnull().sum())
print(data.isnull().sum().sum())

#DATA ANALYSIS

#Count of employees in each department
count_Emp=data.groupby('Department')['Department'].count()
print(count_Emp)

#Average salary of employees in each department
Avg_Salary=data.groupby('Department')['Salary'].mean()
print(Avg_Salary.round(4))

#Avg salary of employees based on gender
sex_Salary=data.groupby(['Department','Sex'],as_index=False).Salary.mean()
print(sex_Salary.round(4))

#Most popular RecruitmentSource of the company based on department
Recruitment_Source=data.groupby(['Department','RecruitmentSource']).size().reset_index(name='counts')
print(Recruitment_Source)

##Total number of working days for terminated employee from datetime import date
Employee_Name=input("Enter the name: ")
print(Employee_Name)

Start_Year=int(input("Enter the year: "))
Start_Month=int(input("Enter the month: "))
Start_Day=int(input("Enter the day: "))
Start_Date=date(Start_Year,Start_Month,Start_Day)
print(Start_Date)

T_Year=int(input("Enter the termination year: "))
T_Month=int(input("Enter the termination month: "))
T_Day=int(input("Enter the termination day: "))
T_Date=date(T_Year,T_Month,T_Day)
print(T_Date)

business_days=pd.bdate_range(Start_Date,T_Date)
print(business_days)
print("Employee name: ", Employee_Name, "Working days", len(business_days))

#Fetch the manager name of departments
Manager_Details=data.groupby(['Department','ManagerName','ManagerID']).size().reset_index(name="counts")
print(Manager_Details)

