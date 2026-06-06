# Câu 1: Tính lương nhân viên 
name = input("Nhập họ tên nhân viên: ")
hours_worked = float(input("Nhập số giờ làm việc: "))
hourly_rate = float(input("Nhập lương mỗi giờ: "))
monthly_salary = hours_worked * hourly_rate
print(f"Lương tháng của nhân viên {name} là: {monthly_salary:,.0f} VNĐ")

# Câu 2: Xếp loại học lực 
average_score = float(input("Nhập điểm trung bình của học sinh: "))
if average_score >= 8.0:
    grade_status = "Giỏi"
elif average_score >= 6.5:
    grade_status = "Khá"
elif average_score >= 5.0:
    grade_status = "Trung bình"
else:
    grade_status = "Yếu"
print(f"Xếp loại học lực: {grade_status}")

# Câu 3: Tính tiền mua hàng 
unit_price = float(input("Nhập đơn giá sản phẩm: "))
quantity = int(input("Nhập số lượng sản phẩm: "))
total_price = unit_price * quantity
if total_price > 500000:
    total_price *= 0.9 
    print("Bạn được giảm giá 10%")
print(f"Tổng tiền phải thanh toán: {total_price:,.0f} VND")

# Bài 4: Tính tổng từ 1 đến n 
n = int(input("Nhập số nguyên dương n: "))
total_sum = 0
for i in range(1, n + 1):
    total_sum += i
print(f"Tổng các số từ 1 đến {n} là: {total_sum}")

# Bài 5: Các số chia hết cho 3 
n = int(input("Nhập số n: "))
count = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        count += 1
print(f"Số lượng các số từ 1 đến {n} chia hết cho 3 là: {count}")

# Bài 6: Đăng nhập hệ thống 
correct_user = "admin"
correct_pass = "123456"
max_attempts = 3
for i in range(1, max_attempts + 1):
    username = input("Nhập Username: ")
    password = input("Nhập Password: ")
    if username == correct_user and password == correct_pass:
        print("Đăng nhập thành công!")
        break
    else:
        attempts_left = max_attempts - i
        print(f"Sai thông tin! Bạn còn {attempts_left} lần thử.")
else:
    print("Tài khoản đã bị khóa do nhập sai quá 3 lần!")

# Bài 7: Thống kê doanh thu tuần 
total_revenue = 0 
for i in range(1, 8):
    daily_revenue = float(input(f"Nhập doanh thu ngày thứ {i}: "))
    total_revenue += daily_revenue
print(f"Tổng doanh thu của tuần là: {total_revenue:,.0f} VND")

# Bài 8: Mô phỏng ATM 
balance = 10000000
withdraw = int(input("Nhập số tiền muốn rút: "))
if withdraw > balance:
    print("Giao dịch thất bại: Số dư tài khoản không đủ.")
elif withdraw % 50000 != 0:
    print("Giao dịch thất bại: Số tiền rút phải là bội số của 50.000 VND")
else:
    balance -= withdraw 
    print(f"Giao dịch thành công! Bạn đã rút {withdraw:,.0f} VND")
    print(f"Số dư còn lại: {balance:,.0f} VND")

# Bài 9: Quản lý cà phê Mini 
print("----MENU QUÁN CÀ PHÊ --------")
print("1.Cà phê - 25.000Đ")
print("2.Trà sữa - 35.000Đ")
print("3.Nước cam - 30.000Đ")
choice = int(input("Mời nhập lựa chọn món (1-3): "))
quantity = int(input("Nhập số lượng: "))
if choice == 1:
    price = 25000
elif choice == 2:
    price = 35000
elif choice == 3:
    price = 30000
else:
    price = 0
    print("Lựa chọn không hợp lệ!")
if price > 0:
    payment = price * quantity 
    if payment > 100000: 
        payment *= 0.9
        print("Hóa đơn trên 100.000đ, bạn được giảm 10%!")
    print(f"Tổng tiền cần thanh toán: {payment:,.0f} VND")

# Bài 10: Kiểm tra số chẵn hay lẻ 
number = int(input("Nhập một số nguyên: "))
if number % 2 == 0:
    print(f"{number} là số chẵn.")
else:
    print(f"{number} là số lẻ.")

# Bài 11: Tìm số lớn nhất trong 3 số 
a = float(input("Nhập số thứ nhất a: "))
b = float(input("Nhập số thứ hai b: "))
c = float(input("Nhập số thứ ba c: "))
max_number = a
if b > max_number:
    max_number = b
if c > max_number:
    max_number = c
print(f"Số lớn nhất trong 3 số là: {max_number}")

# Bài 12: Tính giai thừa
n = int(input("Nhập số nguyên dương n: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Giai thừa của {n} ({n}!) là: {factorial}")
    
# Bài 13: Đoán số 
secret_number = 7
while True:
    guess = int(input("Hãy đoán số bí mật: "))
    if guess == secret_number:
        print("Chúc mừng! Bạn đã đoán đúng số bí mật.")
        break
    else:
        print("Sai rồi, vui lòng thử lại!")

# Bài 14: Tính cước taxi 
distance_km = float(input("Nhập số km khách đi: "))
total_fare = 0
if distance_km <= 1:
    total_fare = distance_km * 15000
elif distance_km <= 10:
    total_fare = 1 * 15000 + (distance_km - 1) * 12000
else:
    total_fare = 1 * 15000 + 9 * 12000 + (distance_km - 10) * 10000
print(f"Tổng tiền cước taxi phải trả: {total_fare:,.0f} VNĐ")