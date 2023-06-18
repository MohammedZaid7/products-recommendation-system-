import pandas as pd
import seaborn as sns

sales_data = pd.read_excel(r'C:\Users\expen\OneDrive\Desktop\OnlineRetail (1).xlsx')
sales_data["InvoiceDate"] = pd.to_datetime(sales_data["InvoiceDate"])
sales_data["Month"] = sales_data["InvoiceDate"].dt.month_name()
product_country_pivot = pd.pivot_table(sales_data, index="Description", columns="Country", values="Quantity", aggfunc=sum, fill_value=0)
product_month_pivot = pd.pivot_table(sales_data, index="Description", columns="Month", values="Quantity", aggfunc=sum, fill_value=0)
global_top_products = sales_data.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)
sns.barplot(x=global_top_products.values, y=global_top_products.index, color='blue')
sns.heatmap(product_country_pivot, cmap="Blues", annot=True)
sns.heatmap(product_month_pivot, cmap="Blues", annot=True)
print("========================Globally Popular products:================================")
print(global_top_products.head(10))
print("========================Country Popular products:================================")
print(product_country_pivot.head(10))
print("========================Monthly Popular products:================================")
print(product_month_pivot.head(10))
