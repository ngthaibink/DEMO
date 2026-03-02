# tính kế thừa
class Employee:
    co_salary=1.04
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay
    def fullname(self):
       return '{}{}'.format(self.name)
    def salary_offical(self):
       self.pay=float(self.pay*self.co_salary)
       return self.pay
class Dev(Employee):
    co_salary=1.2
    def __init__(self,name,pay,pro_lang):
        super().__init__(name,pay)   # gán super init vô lớp cha -> thuộc tính chính 
        self.pro_lang=pro_lang
    def xuat(self):
        print(f'Tên: {self.name}, Lương: {self.pay}, Ngôn ngữ LT: {self.pro_lang}' )

emp=[]
n=int(input("Nhập số lượng Dev muốn nhập: "))
for i in range (n):
    print("==Nhập==")
    namedev=str(input("Nhập tên: "))
    paydev=float(input("Nhập lương "))
    langdev=input("Nhập ngôn ngữ lập trình ")
    dev=Dev(namedev,paydev,langdev) # gán đối tượng vào lớp  
    dev.salary_offical() 
    emp.append(dev)  # thêm đối tượng dev vào ds emp

print("Danh sách Dev ta có: ")
for dev in (emp):
    dev.xuat()    
        
