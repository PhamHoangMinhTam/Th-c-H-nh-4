# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:44:57 2024

@author: Student
"""

N = int(input("Nhập một số nguyên dương có 2 chữ số: "))

if 10 <= N <= 99:
    hang_chuc = N // 10
    hang_don_vi = N % 10
    tong = hang_chuc + hang_don_vi

    print("Tổng các chữ số của số", N, "là:", tong)
else:
    print("Số nhập vào không phải là số nguyên dương có 2 chữ số.")
