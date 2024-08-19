# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:15:57 2024

@author: Student
"""
a = int(input("Nhập số nguyên thứ nhất (a): "))
b = int(input("Nhập số nguyên thứ hai (b): "))

tong = a + b
hieu = a - b
tich = a * b
print("Tổng của a và b là:", tong)
print("Hiệu của a và b là:", hieu)
print("Tích của a và b là:", tich)
if b != 0:
    thuong = a / b
    chia_du = a % b
    chia_nguyen = a // b

    thuong_2_chu_so = round(thuong, 2)
    thuong_3_chu_so = round(thuong, 3)
    print("Thương của a và b là:", thuong_2_chu_so) 
    print("Thương của a và b là:", thuong_3_chu_so) 
    print("Chia lấy dư của a và b là:", chia_du)
    print("Chia lấy nguyên của a và b là:", chia_nguyen)
else:
    thuong = "Không thể chia cho 0"
    chia_du = "Không thể chia cho 0"
    chia_nguyen = "Không thể chia cho 0"
    thuong_2_chu_so = thuong
    thuong_3_chu_so = thuong
    print("Thương của a và b là:", thuong)
    print("Chia lấy dư của a và b là:", chia_du)
    print("Chia lấy nguyên của a và b là:", chia_nguyen)
    