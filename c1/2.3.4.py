# nhập chuỗi , in ra các kí tự ở vị trí chẵn
# xóa 1 kí tự trong chuỗi
chuoi=str(input("Nhập chuỗi: "))
n=int(input("Nhập vị trí n muốn xóa: "))
chuoi_moi=chuoi[n+1:]
for i in range(len(chuoi)):   # đổi biến chuỗi thành chiều dài
   if i%2==0:
     print(chuoi[i])

chuoi_moi=chuoi[n+1:]
print("Chuỗi mới: ",chuoi_moi)