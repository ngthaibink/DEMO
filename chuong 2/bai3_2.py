# thông tin nhân viên
# xây dựng lớp nhân viên: phương thức khởi tạo, phương thức Nhập/Xuất
#thông tin nhân viên
#Xây dựng lớp Quản lý nhân viên gồm các phương thức: Nhập/xuất một danh sách
##nhân viên
# in ra tt nv có quê ở thái nguyên

class Nhan_vien:
    def __init__(tt):
        tt.ten=str(input("Nhập tên nhân viên: "))
        tt.ma_nv=int(input("Nhập mã số sinh viên: "))
        tt.nam_sinh=int(input("Nhập năm sinh: "))
        tt.que_quan=str(input("Nhập quê quán"))
    def in_tt(tt):
        print("Tên nhân viên:",tt.ten)
        print("Mã nhân viên:", tt.ma_nv)
        print("Năm sinh:",tt.nam_sinh)

class Quan_ly:
    def __init__(tt):
      tt.ds_nv=[]
    def nhap_ds(tt):
        n=int(input("Nhập số lượng nhân viên cần nhập: "))
        for i in range(n):
           nv=Nhan_vien()
           tt.ds_nv.append(nv)
    def xuat_ds(tt):
       print("==Danh sách nhân viên==")
       for nv in tt.ds_nv:
           nv.in_tt()
    def que_quan(tt):
        for nv in tt.ds_nv:
            if nv.que_quan.lower()=="thái nguyên":
                print("Nhân viên có quê ở thái nguyên là")
                nv.in_tt()
            if not co_nv:
                print("Không có nhân viên ở Thái Nguyên")


ql=Quan_ly()
ql.nhap_ds()
ql.xuat_ds()
