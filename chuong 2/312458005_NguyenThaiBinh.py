# câu 1: xây dựng lớp account để quản lý tk ng dùng
#mmsv =3124580005 -> x=14
#y=5
class Account:
    def __init__(self):
        self.ten=input("Nhập tên người dùng: ")
        so_du=int(input("Nhập số dư: "))
        if so_du<14*1000:
            self.__balance=14*1000
        else:
            self.__balance=so_du

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, new_balance):
        if new_balance<self.__balance:
            print("Số dư không hợp lệ")
        else:
            self.set_balance=new_balance
            print("Số dư mới là: ",self.set_balance)
    def in_tt(self):
        print(f"User {self.ten}, Balance {self.balance}")

acc=Account()
acc.in_tt()
acc.balance=int(input("Số dư mới: "))
acc.in_tt()

# câu 2
class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def travel_time(self,distance):
        return distance/self.speed
class Motorbike(Vehicle):
    def travel_time(self,distance):
        return super().travel_time(distance)*0.9
class Truck(Vehicle):
    def travel_time(self,distance):
        return super().travel_time(distance)*1.2
    
D=(14+5)*10
brandm=input("Nhập tên xe máy:")
speedm=float(input("Nhập vận tốc xe máy:"))
motorbike=Motorbike(brandm,speedm)

brandt=input("Nhập tên xe tải:")
speedt=float(input("Nhập tốc độ xe tải:"))
truck=Truck(brandt,speedt)

tg_motorbike=motorbike.travel_time(D)
tg_truck=truck.travel_time(D)
print(f"Thời gian xe máy chạy: {tg_motorbike:.2f} giờ")
print(f"Thời gian xe tải chạy: {tg_truck:.2f} giờ")

## câu 3 sử dụng thư viện abc,thiết lập lớp trừu tượng service có phương thức trừu tượng
## get_vat()
# lớp foodservice kế thừa service trả về vat là y%
# lớp techservice kế thừa service trả về vat là (y+5)%
# viết ctr khởi tạo dịch vụ và in lớp thuế tương ứng

from abc import ABC,abstractmethod
class Service(ABC):
    @abstractmethod
    def get_vat(self):
        pass
class FoodService(Service):
    def get_vat(self):
        return 5
class TeachService(Service):
    def get_vat(self):
        return (5+5)
food=FoodService()
teach=TeachService()
print(f"VAT Food Service:{food.get_vat()}%")
print(f"VAT Teach Service:{teach.get_vat()}%")
