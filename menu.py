# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:18:44 2024

@author: Student
"""

def in_menu():
    print(" MENU ")
    print("1. Hu tieu")
    print("2. Chao long")
    print("3. Banh canh")
    print("4. Bun rieu")
    print("5. Pho bo")
    choice = input("Moi nhap lua chon: ")
    return choice
lua_chon = in_menu()
print(f"Ban da chon: {lua_chon}")