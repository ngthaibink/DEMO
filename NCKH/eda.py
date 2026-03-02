import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# đọc dữ liệu từ file csv
df= pd.read_csv(r"C:\Users\user\Documents\NCKH\datac2.csv")
print(df.head())
# xem các biến và cột
print(df.shape) 
df.info()
print(list(df.columns))
# từ dữ liệu đọc được,ta thấy có 15 quan sát và 11 biến số phù hợp cho hồi quy tuyến tính 
print("Số quan sát:", df.shape[0])
print("Số biến:", df.shape[1])
print("Tên các biến:", list(df.columns))
dinh_luong=df.select_dtypes(include=["int64","float64"]).columns
print("Biến định lượng: ")
print(list(dinh_luong))
dinh_tinh = df.select_dtypes(include=["object"]).columns
print("Biến định tính:")
print(list(dinh_tinh))
print("Kiểm tra giá trị có bị thiếu hay không: ")
print(df.isnull().sum())
print(df.describe())
# vẽ biểu đồ Histogram của X
df['Tổng diện tích'].hist(bins=20)
plt.xlabel("Tổng diện tích(m2)")
plt.ylabel("Tần suất")
plt.title("Bảng phân phối của tổng diện tích")
plt.show()
# vẽ biểu đồ Histogram của Y
print(df.columns)
df['giá '].hist(bins=20)
plt.xlabel("Gía")
plt.ylabel("Tần suất")
plt.title("Bảng phân phối của giá")
plt.show()
# vẽ biểu đồ kiểm tra mối quan hệ tuyến tính
plt.scatter(df['Tổng diện tích'],df['giá '])
plt.xlabel("Tổng diện tích")
plt.ylabel("Giá")
plt.title("Biểu đồ biểu diễn mối quan hệ giữa giá và diện tích nhà")
plt.show()
# kiểm tra hệ số tương quan
print(df[['Tổng diện tích', 'giá ']].corr())
