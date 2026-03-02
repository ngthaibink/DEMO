import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# đọc dữ liệu từ file csv
df= pd.read_csv(r"C:\\Users\\user\\Downloads\\clean_movies.csv")
print(df.head())
# xem các biến và cột
print(df.shape) 
df.info()
print(list(df.columns))
print(df.isnull().sum())
print(df.describe())
plt.figure(figsize=(6,4))
sns.boxplot(x=df['gross'])
plt.title("Boxplot of Gross")
plt.show()