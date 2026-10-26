"""
Bài tập 03: Đa hình (Polymorphism) 🎭
========================================
Mục tiêu: Hiểu và áp dụng đa hình
"""
import math


# (Chuẩn bị) Các class hình học dùng cho TODO 1
class HinhHoc:
    def tinh_dien_tich(self):
        raise NotImplementedError


class HinhTron(HinhHoc):
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh

    def tinh_dien_tich(self):
        return math.pi * self.ban_kinh ** 2


class HinhChuNhat(HinhHoc):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def tinh_dien_tich(self):
        return self.dai * self.rong


class HinhTamGiac(HinhHoc):
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Ba cạnh không tạo thành tam giác")
        self.a, self.b, self.c = a, b, c

    def tinh_dien_tich(self):               # công thức Heron
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


# TODO 1: Đa hình qua method chung
# Tạo list: [HinhTron(5), HinhChuNhat(4, 6), HinhTamGiac(3, 4, 5)]
# Dùng for loop gọi tinh_dien_tich() trên mỗi hình
# → Cùng method name, kết quả khác nhau = đa hình!
print("=== TODO 1 ===")
ds_hinh = [HinhTron(5), HinhChuNhat(4, 6), HinhTamGiac(3, 4, 5)]
for h in ds_hinh:
    print(f"{h.__class__.__name__:<12} -> diện tích = {h.tinh_dien_tich():.2f}")


# TODO 2: Đa hình với "hợp đồng"
# Class ThanhToan (cha): phuong_thuc(), xu_ly(so_tien)
# Class TienMat: xu_ly() → "Nhận tiền mặt..."
# Class TheNganHang: xu_ly() → "Trừ thẻ..."
# Class ViDienTu: xu_ly() → "Chuyển qua ví..."
# Viết hàm thanh_toan(don_hang, phuong_thuc) hoạt động với bất kỳ loại nào
print("\n=== TODO 2 ===")


class ThanhToan:
    def phuong_thuc(self):
        return "Chưa xác định"

    def xu_ly(self, so_tien):
        raise NotImplementedError("Class con phải cài đặt xu_ly()")


class TienMat(ThanhToan):
    def phuong_thuc(self):
        return "Tiền mặt"

    def xu_ly(self, so_tien):
        return f"Nhận tiền mặt {so_tien:,.0f}đ"


class TheNganHang(ThanhToan):
    def phuong_thuc(self):
        return "Thẻ ngân hàng"

    def xu_ly(self, so_tien):
        return f"Trừ thẻ {so_tien:,.0f}đ"


class ViDienTu(ThanhToan):
    def phuong_thuc(self):
        return "Ví điện tử"

    def xu_ly(self, so_tien):
        return f"Chuyển qua ví {so_tien:,.0f}đ"


def thanh_toan(don_hang, phuong_thuc):
    print(f"Đơn hàng '{don_hang['ten']}' - phương thức: {phuong_thuc.phuong_thuc()}")
    print("  ->", phuong_thuc.xu_ly(don_hang["gia"]))


don = {"ten": "Laptop", "gia": 15_000_000}
for pt in (TienMat(), TheNganHang(), ViDienTu()):
    thanh_toan(don, pt)


# TODO 3: Duck typing
# Bất cứ object nào có method .speak() đều gọi được
# Không cần kế thừa chung — chỉ cần "có method giống nhau"
print("\n=== TODO 3 ===")


class Vit:
    def speak(self):
        return "Quạc quạc!"


class Nguoi:
    def speak(self):
        return "Xin chào!"


class Robot:
    def speak(self):
        return "Bíp bíp, tôi là robot."


class Da:                                   # KHÔNG có speak()
    pass


def cho_noi(obj):
    if hasattr(obj, "speak"):
        print(f"{obj.__class__.__name__:<6}: {obj.speak()}")
    else:
        print(f"{obj.__class__.__name__:<6}: (không có method speak)")


for o in (Vit(), Nguoi(), Robot(), Da()):
    cho_noi(o)


# TODO 4 (Thử thách): Hệ thống nhân viên
# NhanVien → FullTime, PartTime, Intern
# Mỗi loại tính lương khác nhau
# Viết hàm tong_luong(danh_sach_nhan_vien) dùng đa hình
print("\n=== TODO 4 ===")


class NhanVien:
    def __init__(self, ten):
        self.ten = ten

    def tinh_luong(self):
        raise NotImplementedError


class FullTime(NhanVien):
    def __init__(self, ten, luong_thang, thuong=0):
        super().__init__(ten)
        self.luong_thang = luong_thang
        self.thuong = thuong

    def tinh_luong(self):
        return self.luong_thang + self.thuong


class PartTime(NhanVien):
    def __init__(self, ten, gio_lam, luong_gio):
        super().__init__(ten)
        self.gio_lam = gio_lam
        self.luong_gio = luong_gio

    def tinh_luong(self):
        return self.gio_lam * self.luong_gio


class Intern(NhanVien):
    def __init__(self, ten, tro_cap):
        super().__init__(ten)
        self.tro_cap = tro_cap

    def tinh_luong(self):
        return self.tro_cap


def tong_luong(danh_sach_nhan_vien):
    return sum(nv.tinh_luong() for nv in danh_sach_nhan_vien)


ds = [FullTime("An", 15_000_000, thuong=2_000_000),
      PartTime("Bình", 80, 50_000),
      Intern("Chi", 3_000_000)]
for nv in ds:
    print(f"{nv.__class__.__name__:<9} {nv.ten:<5} -> {nv.tinh_luong():>12,.0f}đ")
print(f"Tổng lương: {tong_luong(ds):,.0f}đ")