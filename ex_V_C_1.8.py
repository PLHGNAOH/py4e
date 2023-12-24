# Hàm kiểm tra năm nhuận
def la_nam_nhuan(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

# Hàm trả về số ngày trong tháng thuộc năm cho trước
def tinh_so_ngay_trong_thang(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        if la_nam_nhuan(nam):
            return 29
        else:
            return 28
    else:
        return 0 # Tháng không hợp lệ

# Hàm kiểm tra ngày có hợp lệ hay không
def la_ngay_hop_le(ngay, thang, nam):
    return 0 < nam and 1 <= thang <= 12 and 1 <= ngay <= tinh_so_ngay_trong_thang(thang, nam)

# Hàm tìm ngày kế tiếp của một ngày hợp lệ
def tim_ngay_ke_tiep(ngay, thang, nam):
    ngay += 1 # Tăng ngày lên 1 đơn vị
    if ngay > tinh_so_ngay_trong_thang(thang, nam): # Nếu ngày vượt quá số ngày tối đa của tháng
        ngay = 1 # Ngày kế tiếp là ngày đầu tiên
        thang += 1 # Tăng tháng lên 1 đơn vị
        if thang > 12: # Nếu tháng vượt quá 12
            thang = 1 # Tháng kế tiếp là tháng đầu tiên
            nam += 1 # Tăng năm lên 1 đơn vị
    return ngay, thang, nam

# Hàm tìm ngày trước đó của một ngày hợp lệ
def tim_ngay_truoc_do(ngay, thang, nam):
    ngay -= 1 # Giảm ngày đi 1 đơn vị
    if ngay < 1: # Nếu ngày nhỏ hơn 1
        thang -= 1 # Giảm tháng đi 1 đơn vị
        if thang < 1: # Nếu tháng nhỏ hơn 1
            thang = 12 # Tháng trước đó là tháng cuối cùng
            nam -= 1 # Giảm năm đi 1 đơn vị
        ngay = tinh_so_ngay_trong_thang(thang, nam) # Ngày trước đó là ngày cuối cùng của tháng
    return ngay, thang, nam

# Hàm chính
def main():
    # Nhập ngày, tháng, năm từ bàn phím
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))

    # Kiểm tra ngày có hợp lệ hay không
    if la_ngay_hop_le(ngay, thang, nam):
        print("Ngày hợp lệ!")
        # Tìm ngày kế tiếp và ngày trước đó
        ngay_kt, thang_kt, nam_kt = tim_ngay_ke_tiep(ngay, thang, nam)
        ngay_td, thang_td, nam_td = tim_ngay_truoc_do(ngay, thang, nam)
        # In kết quả
        print(f"Ngày kế tiếp: {ngay_kt}/{thang_kt}/{nam_kt}")
        print(f"Ngày trước đó: {ngay_td}/{thang_td}/{nam_td}")
    else:
        print("Ngày không hợp lệ!")

# Gọi hàm chính
if __name__ == "__main__":
    main()
