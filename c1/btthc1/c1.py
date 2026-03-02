# khởi tạo và input validation
ten_NTB=input("Nhập họ tên: ")
mssv_NTB=input("Nhập MSSV: ")
# tính định mức
n=int(mssv_NTB[-1])
if n==0: 
   n=10
dinh_muc_NTB=50+(n*5)
print("Định mức ta có: ",dinh_muc_NTB)

chi_so_cu=input("Nhập chỉ số cũ: ")
chi_so_moi=input("Nhập chỉ số mới: ")

while  chi_so_cu.isdigit() or  chi_so_moi.isdigit():
   print("Cả 2 chỉ số phải là số")
   if not chi_so_cu.isdigit():
       chi_so_cu=input("Nhập lại chỉ số cũ: ")
   if not chi_so_moi.isdigit():
       chi_so_moi=input("Nhập lại chỉ số mới: ")

chi_so_cu=int(chi_so_cu)
chi_so_moi=int(chi_so_moi)

while chi_so_moi <=0 or chi_so_cu<=0:
   print("Vui lòng nhập chỉ số lớn hơn 0")
   if(chi_so_moi<=0):
      chi_so_moi=int(input("Nhập lại chỉ số mới: "))
   else: 
       chi_so_cu=int(input("Nhập lại chỉ số cũ: "))
while chi_so_moi <= chi_so_cu:
   print("Vui lòng nhập chỉ số mới lơn hơn chỉ số cũ")
   chi_so_moi=int(input("Nhập lại chỉ số mới: "))

# in ra hai chữ số
print("Chỉ số mới là: ", chi_so_moi)
print("Chỉ số cũ là: ",chi_so_cu)

# tính tiền 
so_dien_NTB=ư