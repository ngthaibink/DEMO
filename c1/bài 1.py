# dùng for để nhập số tiền của 7 ngày, dùng for để tính số tiền đã nhập 
def tinh_tong(n):
    tong=0
    for i in range(n):
        x=int(input(f"Nhập số tiền ngày {i+1}: "))
        tong=tong+x
    return tong

a=7
ket_q=tinh_tong(a)

print("Tổng số tiền của 7 ngày là: ", ket_q)



