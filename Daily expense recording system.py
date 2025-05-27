# -*- coding: utf-8 -*-
"""
Created on Tue May 27 23:05:25 2025

@author: andyb
"""

import csv
from collections import defaultdict
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 顯示中文
plt.rcParams['axes.unicode_minus'] = False                # 顯示負號

# 初始化資料結構
daily_total = defaultdict(int)
category_total = defaultdict(int)

# 開啟CSV檔案
with open('expenses.csv', newline='', encoding='big5') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        date = row['日期']
        category = row['類別']
        amount = int(row['金額'])  # 轉成整數
        
        # 累加
        daily_total[date] += amount  # daily_total[date] = daily_total[date] + amount
        category_total[category] += amount  # category_total[category] = category_total[category] + amount

# 顯示結果
print("📅 每日總支出：")
for date, total in daily_total.items():   #根據日期來加  #用,item把key與value組成一個(資料對)
    print(f"{date}: {total} 元")

print("\n📂 各類別總支出：")
for category, total in category_total.items():   #根據類別來加
    print(f"{category}: {total} 元")

#=====================================================================

# 🎨 畫出每日支出折線圖
dates = list(daily_total.keys())
amounts = list(daily_total.values())

plt.figure(figsize=(10, 5))
plt.plot(dates, amounts, marker='o', linestyle='-', color='blue')
plt.title('每日總支出')
plt.xlabel('日期')
plt.ylabel('金額 (元)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

# 🎨 畫出各類別支出圓餅圖
labels = list(category_total.keys())
sizes = list(category_total.values())

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('各類別支出比例')
plt.axis('equal')  # 讓圓餅圖是圓的
plt.show()
    