import pandas as pd
df=pd.read_csv(r"C:\\Users\user\\Documents\\HK2-N2\\LT PYTHON\\diem_thi_thpt.csv")
print(df)
print(df.shape)
df.info()
print(list(df.columns))