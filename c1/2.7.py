# kiểm tra số đã cho có phải số đối xứng không
n=int(input("Nhập số: "))
tong=0
dao=n
while dao>0:
    tong=tong*10 +dao%10
    dao=dao//10
if tong==n:
   print(n, "là số đối xứng")
else: 
   print("không có số đối xứng")