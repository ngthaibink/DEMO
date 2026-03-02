# in từng chữ số theo thứ tự ngược lại 
n=int(input("Nhập số: "))
so=n
while n>0:
    s=n%10      # lấy chữ số cuối
    print(s, end=" ")
    n=n//10     # bỏ chữ số vừa in