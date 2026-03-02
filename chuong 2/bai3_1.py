# xây dựng lớp sách với các thuộc tính
#xây dựng phương thức khởi tạo,nhập hiện thông tin 1 cuốn sách
# in ra màn hình tt về sách có tên tác giả nhập vào từ bàn phím
# in ra màn hình tt về sách có giá thấp nhất
class sach: 
    def __init__(tt):
        tt.ten_sach=str(input("Nhập tên sách: "))
        tt.tac_gia=str(input("Nhập tên tác giả: "))
        tt.gia=int(input("Nhập giá sách: "))
    def in_tt(tt):
        print("Tên sách ",tt.ten_sach)
        print(f"Tên tác giả: {tt.tac_gia}")
        print("Giá ",tt.gia)   

ds_sach=[]
n=int(input("Nhập số lượng sách: "))
for i in range(n):
    print("Nhập thông tin : ")
    s=sach()
    ds_sach.append(s)
for s in ds_sach:
    s.in_tt()

tg=input("Nhập tên tác giả cần tìm: ")
co_sach=False
for s in ds_sach:
    if s.tac_gia==tg:
        print("Cuốn sách có tên tác giả này là ")
        s.in_tt()
        co_sach=True
if not co_sach:
    print("Trong danh sách ko có tác giả này")
    
min_gia=ds_sach[0].gia
for s in ds_sach:
    if s.gia<min_gia:
        min_gia=s.gia
for s in ds_sach:
    if s.gia==min_gia:
        print("Sách có giá thấp nhất ")
        s.in_tt()