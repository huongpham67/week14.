"""
Bài tập 02: Override & super() 🔄
===================================
Mục tiêu: Ghi đè phương thức, gọi class cha
"""

# TODO 1: Override __str__
# Class cha NhanVien: ten, luong, __str__()
# Class con QuanLy: thêm phong_ban, override __str__() thêm phòng ban
# Dùng super().__str__() + thông tin thêm
print("=== TODO 1 ===")


class NhanVien:
    def __init__(self, ten, luong):
        self.ten = ten
        self.luong = luong

    def __str__(self):
        return f"Nhân viên: {self.ten}, lương cơ bản: {self.luong:,.0f}"


class QuanLy(NhanVien):
    def __init__(self, ten, luong, phong_ban):
        super().__init__(ten, luong)
        self.phong_ban = phong_ban

    def __str__(self):
        return super().__str__() + f", phòng ban: {self.phong_ban}"


print(NhanVien("An", 10_000_000))
print(QuanLy("Bình", 10_000_000, "Kỹ thuật"))


# TODO 2: Override method tính lương
# NhanVien.tinh_luong() → lương cơ bản
# QuanLy.tinh_luong() → lương + phụ cấp quản lý (20%)
# TapSu.tinh_luong() → lương × 0.7 (70%)
print("\n=== TODO 2 ===")


class NhanVien(NhanVien):          # mở rộng class ở TODO 1, thêm tinh_luong()
    def tinh_luong(self):
        return self.luong


class QuanLy(QuanLy, NhanVien):
    def tinh_luong(self):
        return super().tinh_luong() * 1.2      # lương + phụ cấp 20%


class TapSu(NhanVien):
    def tinh_luong(self):
        return super().tinh_luong() * 0.7      # 70% lương


for p in (NhanVien("An", 10_000_000),
          QuanLy("Bình", 10_000_000, "Kỹ thuật"),
          TapSu("Cường", 10_000_000)):
    print(f"{p.__class__.__name__:<9} {p.ten:<6} -> {p.tinh_luong():>12,.0f}")


# TODO 3: super().__init__()
# Class cha: Vehicle(name, speed)
# Class con: ElectricCar(name, speed, battery)
# Dùng super().__init__(name, speed) trong __init__ của ElectricCar
print("\n=== TODO 3 ===")


class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __str__(self):
        return f"{self.name} - tốc độ tối đa {self.speed} km/h"


class ElectricCar(Vehicle):
    def __init__(self, name, speed, battery):
        super().__init__(name, speed)
        self.battery = battery

    def __str__(self):
        return super().__str__() + f", pin {self.battery} kWh"


car = ElectricCar("VinFast VF8", 200, 87.7)
print(car)
print("name:", car.name, "| speed:", car.speed, "| battery:", car.battery)


# TODO 4 (Thử thách): Template method pattern
# Class cha Report: generate() gọi header(), body(), footer()
# Class con HTMLReport: override body() tạo HTML
# Class con TextReport: override body() tạo plain text
print("\n=== TODO 4 ===")


class Report:
    def __init__(self, title, data):
        self.title = title
        self.data = data

    def header(self):
        return f"=== {self.title} ==="

    def body(self):
        return "\n".join(str(d) for d in self.data)

    def footer(self):
        return "--- Hết báo cáo ---"

    def generate(self):                     # template method
        return "\n".join([self.header(), self.body(), self.footer()])


class HTMLReport(Report):
    def header(self):
        return f"<html><body><h1>{self.title}</h1>"

    def body(self):
        return "<ul>" + "".join(f"<li>{d}</li>" for d in self.data) + "</ul>"

    def footer(self):
        return "</body></html>"


class TextReport(Report):
    def body(self):
        return "\n".join(f"- {d}" for d in self.data)


data = ["Doanh thu: 100", "Chi phí: 60", "Lợi nhuận: 40"]
print(HTMLReport("Báo cáo tháng", data).generate())
print()
print(TextReport("Báo cáo tháng", data).generate())