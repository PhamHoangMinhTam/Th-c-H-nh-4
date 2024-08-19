# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:52:38 2024

@author: Student
"""
from datetime import datetime
nam_sinh = int(input("Nhập năm sinh của bạn: "))

nam_hien_tai = datetime.now().year

tuoi = nam_hien_tai - nam_sinh

print("Tuổi của bạn là:", tuoi)