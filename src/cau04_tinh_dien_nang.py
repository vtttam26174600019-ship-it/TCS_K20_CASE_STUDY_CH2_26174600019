# Cho các giá trị ban đầu
cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

# 13 & 14. Tính điện năng, chi phí và in giá trị kèm kiểu dữ liệu (với 90 phút)
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print(dien_nang_kwh, type(dien_nang_kwh))
print(chi_phi, type(chi_phi))

# 15. Dự đoán kết quả trước khi chạy (cho trường hợp 60 phút):
# - Điện năng dự đoán: 0.375 kWh
# - Chi phí dự đoán: 1125.0 VNĐ

# 16. Thay so_phut bằng 60 rồi chạy lại và so sánh
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print(dien_nang_kwh, type(dien_nang_kwh))
print(chi_phi, type(chi_phi))