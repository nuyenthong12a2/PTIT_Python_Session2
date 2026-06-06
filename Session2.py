# Câu 1: Tính lương nhân viên 
name = input("Nhập họ tên nhân viên :")
number_hours = float(input("Nhập số giờ làm việc : "))
salary_hours = float(input("Nhập lương mỗi giờ : "))

salary_month = number_hours * salary_hours

print(f"Lương tháng của nhân viên {name} là: {salary_month:,.0f} VNĐ")

# Câu 2 :Xếp loại học lực 
dtb = float(input("Nhập điểm trung bình của học sinh : "))

if dtb >=8.0:
    xep_loai = "Giỏi"
elif dtb >=6.5:
    xep_loai = "Khá"
elif dtb >=5.0:
    xep_loai = "Trung bình"
else:
    xep_loat ="Yếu"

print (f"Xếp loại học lực :{xep_loai}")

# Câu 3 : Tính tiền mua hàng 
bill = float(input("Nhập đơn giá sản phẩm : "))
salary = int(input("Nhập số lượng sản phẩm : "))

total = bill * salary

if total > 500000:
    total = total * 0.9 
    print ("Bạn được giảm giá 10%")
print (f"Tổng tiền phải thanh toán :{total:,.0f} VND")

# Bài 4 : Tính tổng từ 1 đến n 
n =int(input("Nhập số nguyên  dương n : "))

total = 0

for i in range(1,n+1):
    total +=i
    print (f"Tổng  các số từ 1 đến {n} là : {total}")

# Bài 5 : Các số chia hết cho 3 

n = int(input("Nhập số n : "))
dem = 0
for i in range(1,n+1):
    if i % 3 ==0:
        dem+=1
        print (f"Số lượng các số từ 1 đến {n} chia hết cho 3 là :{dem}")

# Bài 6 : Đăng nhập hệ thống 
user_dung = "admin"
pass_dung = "123456"
so_lan_thu = 3

for i in range(1, so_lan_thu + 1):
    username = input("Nhập Username: ")
    password = input("Nhập Password: ")
    
    if username == user_dung and password == pass_dung:
        print("Đăng nhập thành công!")
        break
    else:
        con_lai = so_lan_thu - i
        print(f"Sai thông tin! Bạn còn {con_lai} lần thử.")
else:
    print("Tài khoản đã bị khóa do nhập sai quá 3 lần!")

# Bài 7 : Thống kê doanh thu tuần 

tong_doanh_thu =0 
for i in range(1,8):
    doanh_thu_ngay = float(input(f"Nhập doanh thu ngày thứ {i} :"))
    tong_doanh_thu += doanh_thu_ngay
print (f"Tổng doanh thu của tuần là : {tong_doanh_thu:,.0f} VND")

# Bài 8 : Mô phỏng ATM 
so_du = 10000000
rut = int(input("Nhập số tiền muốn rút : "))

if rut > so_du :
    print ("Giao dịch thất bại : Số dư tài khoản không đủ .")
elif rut % 50000 != 0:
    print ("Giao dịch thất bại : Số tiền rút phải là bội số của 50.000 VND ")
else:
    so_du -= rut 
    print (f" Giao dịch thành công ! Bạn đã rút {rut :,0f} VND")
    print (f"Số dư còn lại :{so_du:,.0f} VND")

# Bài 9 : Quản lý cà phê Mini 

print ("----MENU QUÁN CÀ PHÊ --------")
print ("1.Cà phê -25.000Đ")
print ("2.Trà sữa -35.000Đ")
print ("3.Nước cam -30.000Đ")

choice = int(input("Mời nhập lựa chọn món (1-3) :"))
so_luong = int(input("Nhập số lượng : "))

if choice ==1:
    gia =25000
elif choice ==2:
    gia = 35000
elif choice ==3:
    gia = 30000
else:
    gia = 0
    print ("Lựa chọn không hợp lệ!")

if gia > 0 :
    payment = gia * so_luong 
    if payment >  100000: 
        total *= 0.9
        print ("Hóa đơn trên 100.000đ , bạn được giảm 10%!")
    print (f"Tổng tiền càn thanh toán : {payment:,.0f} VND")

# Bài 10 : Kiểm tra số chẵn hay lẻ 
n = int(input("Nhập một số nguyên: "))

if n % 2 == 0:
    print(f"{n} là số chẵn.")
else:
    print(f"{n} là số lẻ.")

# Bài 11 : Tìm số lớn nhất trong 3 số 

a = float(input("Nhập số thứ nhất a: "))
b = float(input("Nhập số thứ hai b: "))
c = float(input("Nhập số thứ ba c: "))

max_so = a
if b > max_so:
    max_so = b
if c > max_so:
    max_so = c

print(f"Số lớn nhất trong 3 số là: {max_so}")

# Bài 12:  Tính giai thùa
n = int(input("Nhập số nguyên dương n: "))
giai_thua = 1

for i in range(1, n + 1):
    giai_thua *= i

print(f"Giai thừa của {n} ({n}!) là: {giai_thua}")
    
# Bài 13 : Đoán số 
so_bi_mat = 7

while True:
    doan = int(input("Hãy đoán số bí mật: "))
    if doan == so_bi_mat:
        print("Chúc mừng! Bạn đã đoán đúng số bí mật.")
        break
    else:
        print("Sai rồi, vui lòng thử lại!")

# Bài 14 : Tính cước taxi 
km = float(input("Nhập số km khách đi: "))
tong_tien = 0

if km <= 1:
    tong_tien = km * 15000
elif km <= 10:
    tong_tien = 1 * 15000 + (km - 1) * 12000
else:
    tong_tien = 1 * 15000 + 9 * 12000 + (km - 10) * 10000

print(f"Tổng tiền cước taxi phải trả: {tong_tien:,.0f} VNĐ")