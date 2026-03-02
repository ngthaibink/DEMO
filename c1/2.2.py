# viết mã lặp qua 10 số đầu tiên, mỗi lần lần lặp in ra tổng số hiện tại
# và số trước đó

tong=0
for i in range(10):
    tong=tong+i
    print(f"Tổng của tổng số hiện tại là: {tong}") #f để viết chuỗi có chèn biến trực tiếp
    print(f"Số hiện tại là: {i}")
