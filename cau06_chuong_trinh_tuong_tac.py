# Nhập các thông tin từ bàn phím
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút sử dụng: "))
don_gia_kwh = float(input("Nhập đơn giá: "))

# Tính toán điện năng và chi phí
dien_nang = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang * don_gia_kwh

# In kết quả theo đúng định dạng yêu cầu
print("Mã phiên:", ma_phien)
print("Máy:", ma_may)
print("Điện năng:", dien_nang)
print("Chi phí:", chi_phi)