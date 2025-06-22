import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("SampleSuperstore.csv", encoding='latin1')

print("First five rows of data")
print(df.head())

print("\nTotal Sales:", df['Sales'].sum())
print("\nTotal Profit:", df['Profit'].sum())

top_states=df.groupby("State")["Profit"].sum().sort_values(ascending=False).head(5)
print("\n Top 5 states by Profit:")
print(top_states)


top_cats=df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(10)
top_cats.plot(kind='bar', title='Top 10 Sub Categories by Sales', figsize=(10,5))
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


