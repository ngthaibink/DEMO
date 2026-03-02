# cho 2 số nguyên , viết ctr trả về tích khi số đó nhỏ hơn
# hoặc bằng 1000, nếu ko trả về tổng
a,b=input("Nhập hai số nguyên: ").split()
a=int(a)
b=int(b)
tich=a*b
tong=a+b
if(tich <=1000):
  print(tich)
else:
  print(tong)