import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("Salary_Data.csv")
data2 = pd.read_csv("Company_Expense_updated.csv")
data.plot(kind = "line",x="YearsExperience",y="Salary",marker="+",ls='--',color='g',linewidth='7')


data.plot(kind = "hist")
data.plot(kind = "pie")
plt.plot(data["YearsExperience"],data["Salary"],color='g')
plt.plot(data2["Months"],data2["Year"],data2["Budget"],data2["Marketing cost"],data2["Management cost"],data2["Transport cost"],data2["Other expenses"])
plt.xlabel("Years of Experience")
plt.ylabel("Taka in Salary")
plt.title("Experience vs Salary")
plt.grid(axis='y',color='r',ls='--')
plt.show()