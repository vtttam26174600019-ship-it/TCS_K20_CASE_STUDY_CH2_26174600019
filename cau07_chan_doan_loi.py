# Đoạn mã sau khi đã chẩn đoán và sửa lỗi:
ma_may = input("Nhập mã máy: ")
# Sửa Lỗi 1: Chuyển cong_suat_w sang kiểu float để thực hiện phép tính số học
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
# Sửa Lỗi 2: Sửa tên biến trong f-string từ {dien_nang:.3f} thành {dien_nang_kwh:.3f}
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# MÔ TẢ CÁC LỖI ĐÃ PHÁT HIỆN KHI CHẠY NGUYÊN TRẠNG
# 1. Lỗi TypeError:
#    - Tên tệp: src/cau07_chan_doan_loi.py, dòng 6.
#    - Loại lỗi: TypeError (can't multiply sequence by non-int of type 'float').
#    - Thông báo lỗi: TypeError: can't multiply sequence by non-int of type 'float'
#    - Nguyên nhân: cong_suat_w là chuỗi (str) nhưng đem đi nhân chia với số.
# 2. Lỗi NameError:
#    - Tên tệp: src/cau07_chan_doan_loi.py, dòng 8.
#    - Loại lỗi: NameError (name 'dien_nang' is not defined).
#    - Thông báo lỗi: NameError: name 'dien_nang' is not defined
#    - Nguyên nhân: Dùng sai tên biến 'dien_nang' thay vì 'dien_nang_kwh'.