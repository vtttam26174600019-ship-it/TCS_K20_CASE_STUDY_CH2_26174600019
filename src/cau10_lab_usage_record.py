from datetime import datetime

# Nhập các thông tin từ bàn phím
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập thời gian sử dụng (phút): "))
don_gia_kwh = float(input("Nhập đơn giá điện: "))

# Tính toán các giá trị
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# Kiểm tra xem có sử dụng trên 60 phút không (trả về True/False)
tren_60_phut = so_phut > 60

# Lấy thời điểm ghi nhận hiện tại và định dạng chuỗi
thoi_diem_hien_tai = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# In kết quả theo đúng định dạng mẫu của đề bài
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat_w:.2f} W")
print(f"Thời lượng: {so_phut} phút")
print(f"Điện năng: {dien_nang_kwh} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
print(f"Trên 60 phút: {tren_60_phut}")
print(f"Ghi nhận lúc: {thoi_diem_hien_tai}")