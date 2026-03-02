
class BankAcc:
    def __init__(self,acc,balance):
        self.acc=acc
        self.balance=0
    @property
    def acc(self):
        return self._acc  # phải dùng biến ._ để gán
    @acc.setter
    def acc(self,acc):
        if isinstance(acc,str):
            print("Số tài khoản hợp lệ ")
        else:
            print("Nhập số tài khoản hợp lệ")
            return 0
    @property
    def balance(self):
        return self._balance
    def deposit(self,amount):
           if amount <=0:
            print("Số tiền nạp không hợp lệ")
           else: 
            self.balance=self._balance+amount 
    def withdraw(self):
             
             if amount<=0:
                 print("Số tiền rút không hợp lệ")
             elif amount>self.balance:
                 print("Số dư không đủ") 
             elif amount <self._balance or amount>0:
                 self._balance=self.balance-amount  
                 print("Rút tiền thành công")         
    def inkq(self):
        print("Số dư hiện tại là: ", self.balance)


acc1=input("Nhập stk")
acc=BankAcc(acc1)    
acc.deposit = input("Nhập số tiền muốn nạp")
acc.withdraw=input("Nhập số tiền muốn rút") 
acc.inkq()  
