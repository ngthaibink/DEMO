import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# đọc dữ liệu từ file csv
df= pd.read_csv(r"C:\Users\user\Documents\NCKH\Advertising.csv")
print(df.head())
# Đọc file csv được tải lên từ dữ liệu, ta tiếp tục phân tích các thông tin chi tiết
print(df.shape) 
df.info()
# Các dữ liệu ở đây đều không có dữ liệu thiếu (missing values).
##Dữ liệu này thể hiện cho ta thấy nó phù hợp với mô hình hồi quy tuyến tính.