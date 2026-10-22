# 17. Dùng input() để nhận bốn giá trị và in type() của chúng ngay sau khi nhập
ma_may = input("Nhập mã máy: ")
cong_suat_w = input("Nhập công suất W: ")
so_phut = input("Nhập số phút: ")
don_gia_kwh = input("Nhập đơn giá điện/kWh: ")

print(ma_may, type(ma_may))
print(cong_suat_w, type(cong_suat_w))
print(so_phut, type(so_phut))
print(don_gia_kwh, type(don_gia_kwh))

# 18. Chuyển công suất sang float, số phút sang int và đơn giá sang float
cong_suat_w = float(cong_suat_w)
so_phut = int(so_phut)
don_gia_kwh = float(don_gia_kwh)

# 19. Tính lại điện năng và chi phí sau khi chuyển kiểu
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Điện năng (kWh):", dien_nang_kwh, type(dien_nang_kwh))
print("Chi phí (VNĐ):", chi_phi, type(chi_phi))