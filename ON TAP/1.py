# viết mã python để xóa kỉ tự khỏi một chuỗi từ 0 đến n
a=[1,2,3,4,5]
n=int(input("Nhập số từ 0 đến n cần xóa "))
a=a[n+1:]
print(f'{a}')

# in số theo thứ tự ngược lại
n=int(input("Nhập sô nguyên: "))
while n !=0:
    a=n%10
    print(a,end=" ")
    n=n//10
    

