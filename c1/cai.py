import numpy as np
from sklearn.linear_model import LinearRegression

# dữ liệu đơn giản
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, y)

print("Hệ số:", model.coef_)
print("Intercept:", model.intercept_)
print("Dự đoán x=6:", model.predict([[6]]))
