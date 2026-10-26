"""
Bài tập 01: Kế thừa cơ bản 🧬
================================
Mục tiêu: Tạo class con kế thừa class cha
"""
import math

# TODO 1: Tạo class cha DongVat(ten, tuoi) với methods: an(), ngu()
# Tạo class con Cho(ten, tuoi, giong) thêm method: sua()
# Tạo class con Meo(ten, tuoi, mau_long) thêm method: keu()
# Tạo object và gọi cả method cha lẫn con
print("=== TODO 1 ===")


class DongVat:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def an(self):
        return f"{self.ten} đang ăn"

    def ngu(self):
        return f"{self.ten} đang ngủ"


class Cho(DongVat):
    def __init__(self, ten, tuoi, giong):
        super().__init__(ten, tuoi)
        self.giong = giong

    def sua(self):
        return f"{self.ten} ({self.giong}): Gâu gâu!"


class Meo(DongVat):
    def __init__(self, ten, tuoi, mau_long):
        super().__init__(ten, tuoi)
        self.mau_long = mau_long

    def keu(self):
        return f"{self.ten} (lông {self.mau_long}): Meo meo!"


cho = Cho("Milu", 3, "Corgi")
meo = Meo("Tom", 2, "xám")
print(cho.an())    # method của class cha
print(cho.sua())   # method của class con
print(meo.ngu())   # method của class cha
print(meo.keu())   # method của class con


# TODO 2: Tạo class cha HinhHoc
# Tạo class con: HinhTron(ban_kinh), HinhChuNhat(dai, rong)
# Mỗi class có: tinh_dien_tich(), tinh_chu_vi(), __str__()
print("\n=== TODO 2 ===")


class HinhHoc:
    def tinh_dien_tich(self):
        raise NotImplementedError("Class con phải cài đặt tinh_dien_tich()")

    def tinh_chu_vi(self):
        raise NotImplementedError("Class con phải cài đặt tinh_chu_vi()")

    def __str__(self):
        return (f"{self.__class__.__name__}: diện tích = {self.tinh_dien_tich():.2f}, "
                f"chu vi = {self.tinh_chu_vi():.2f}")


class HinhTron(HinhHoc):
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh

    def tinh_dien_tich(self):
        return math.pi * self.ban_kinh ** 2

    def tinh_chu_vi(self):
        return 2 * math.pi * self.ban_kinh


class HinhChuNhat(HinhHoc):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def tinh_dien_tich(self):
        return self.dai * self.rong

    def tinh_chu_vi(self):
        return 2 * (self.dai + self.rong)


print(HinhTron(5))
print(HinhChuNhat(4, 6))


# TODO 3: Kiểm tra kế thừa
# Dùng isinstance() và issubclass() kiểm tra quan hệ
# In ra kết quả
print("\n=== TODO 3 ===")
print("isinstance(cho, Cho):", isinstance(cho, Cho))
print("isinstance(cho, DongVat):", isinstance(cho, DongVat))
print("isinstance(cho, Meo):", isinstance(cho, Meo))
print("issubclass(Cho, DongVat):", issubclass(Cho, DongVat))
print("issubclass(Meo, Cho):", issubclass(Meo, Cho))
print("issubclass(HinhTron, HinhHoc):", issubclass(HinhTron, HinhHoc))
print("isinstance(HinhChuNhat(1, 2), HinhHoc):", isinstance(HinhChuNhat(1, 2), HinhHoc))


# TODO 4 (Thử thách): Đa kế thừa
# class Flyer: def fly(self): ...
# class Swimmer: def swim(self): ...
# class Duck(Flyer, Swimmer): ...
print("\n=== TODO 4 ===")


class Flyer:
    def fly(self):
        return "Đang bay trên trời ✈️"


class Swimmer:
    def swim(self):
        return "Đang bơi dưới nước 🏊"


class Duck(Flyer, Swimmer):
    def __init__(self, ten):
        self.ten = ten


duck = Duck("Donald")
print(f"{duck.ten}: {duck.fly()}")
print(f"{duck.ten}: {duck.swim()}")
print("MRO:", [c.__name__ for c in Duck.__mro__])