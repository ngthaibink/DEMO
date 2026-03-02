# tính thuế cho thu nhập 
luong=int(input("Nhập tiền lương: "))
n=luong
if luong<=10000:
   print("Không cần đóng thuế")
elif luong>10000 or luong<=20000:
   luong_sau_thue= (luong-10000)*0.1
   print("Số thuế cần đóng là: ", luong_sau_thue)
elif luong>20000:
    luong_sau_thue_2= 10000*0.1 + (luong-20000)*0.2
    print("Số thuế cần đóng là: ", luong_sau_thue_2)