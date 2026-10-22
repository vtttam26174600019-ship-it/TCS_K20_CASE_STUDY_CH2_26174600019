from datetime import datetime

# Lấy thời điểm hiện tại và định dạng chuỗi
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

# Tính khoảng thời gian giữa hai mốc
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))

# Dự đoán kết quả của phép trừ trước khi chạy:
# - Từ 13:15 đến 15:05 là 1 giờ 50 phút (1:50:00).

# GIẢI THÍCH SỰ KHÁC NHAU GIỮA CÁC KIỂU DỮ LIỆU 
# - datetime: Đại diện cho một thời điểm cụ thể (bao gồm cả ngày, giờ, phút, giây...).
# - str (string): Chuỗi ký tự thuần túy dùng để hiển thị văn bản.
# - timedelta: Đại diện cho khoảng thời gian hoặc hiệu số giữa hai mốc thời gian.