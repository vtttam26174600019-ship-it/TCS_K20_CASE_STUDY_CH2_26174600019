# Khai báo các biến ban đầu
tong_phut = 135
cong_suat_w = 250

# 9. Dùng // và % để tính số giờ trọn vẹn và số phút còn lại
so_gio = tong_phut // 60
so_phut_du = tong_phut % 60
print("Số giờ trọn vẹn:", so_gio)
print("Số phút còn lại:", so_phut_du)

# 10. Tạo biến su_dung_lau nhận True khi tong_phut > 60
su_dung_lau = tong_phut > 60
print("Sử dụng lâu:", su_dung_lau)

# 11. Tạo biến du_lieu_hop_le nhận True khi cong_suat_w > 0 và tong_phut > 0
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Dữ liệu hợp lệ:", du_lieu_hop_le)

# 12. Dự đoán rồi kiểm chứng hai biểu thức
# Dự đoán: 100 + 20 * 3 = 160 ; (100 + 20) * 3 = 360
bieu_thuc_1 = 100 + 20 * 3
bieu_thuc_2 = (100 + 20) * 3
print("Kết quả biểu thức 1:", bieu_thuc_1)
print("Kết quả biểu thức 2:", bieu_thuc_2)