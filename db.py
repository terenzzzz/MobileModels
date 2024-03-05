import sqlite3
from device_extractor import apple
from device_extractor import google
from device_extractor import xiaomi
from device_extractor import huawei
from device_extractor import samsung

# 创建或连接到数据库
conn = sqlite3.connect('model.db')
cursor = conn.cursor()

# 创建phone表
cursor.execute('''CREATE TABLE IF NOT EXISTS phone
                (brand TEXT, model TEXT)''')

# 创建pad表
cursor.execute('''CREATE TABLE IF NOT EXISTS tablet
                (brand TEXT, model TEXT)''')

# 创建watch表
cursor.execute('''CREATE TABLE IF NOT EXISTS watch
                (brand TEXT, model TEXT)''')


# APPLE
iphones, ipads, apple_watches, ipods = apple.extract_apple_models("source/apple_all_en.md")

# 插入数据到phone表
for model in iphones:
    cursor.execute("INSERT INTO phone VALUES (?, ?)", ("Apple", model))

# 插入数据到pad表
for model in ipads:
    cursor.execute("INSERT INTO tablet VALUES (?, ?)", ("Apple", model))

# 插入数据到watch表
for model in apple_watches:
    cursor.execute("INSERT INTO watch VALUES (?, ?)", ("Apple", model))

# GOOGLE
phone,pad,watch = google.extract_google_models("source/google.md")
# 插入数据到phone表
for model in phone:
    cursor.execute("INSERT INTO phone VALUES (?, ?)", ("Google", model))

# 插入数据到pad表
for model in pad:
    cursor.execute("INSERT INTO tablet VALUES (?, ?)", ("Google", model))

# 插入数据到watch表
for model in watch:
    cursor.execute("INSERT INTO watch VALUES (?, ?)", ("Google", model))

# Xiaomi
phone,pad,watch = xiaomi.extract_xiaomi_models("source/xiaomi_en.md")
# 插入数据到phone表
for model in phone:
    cursor.execute("INSERT INTO phone VALUES (?, ?)", ("Xiaomi", model))

# 插入数据到pad表
for model in pad:
    cursor.execute("INSERT INTO tablet VALUES (?, ?)", ("Xiaomi", model))

# 插入数据到watch表
for model in watch:
    cursor.execute("INSERT INTO watch VALUES (?, ?)", ("Xiaomi", model))

# Huawei
phone,pad,watch = huawei.extract_huawei_models("source/huawei_global_en.md")
# 插入数据到phone表
for model in phone:
    cursor.execute("INSERT INTO phone VALUES (?, ?)", ("Huawei", model))

# 插入数据到pad表
for model in pad:
    cursor.execute("INSERT INTO tablet VALUES (?, ?)", ("Huawei", model))

# 插入数据到watch表
for model in watch:
    cursor.execute("INSERT INTO watch VALUES (?, ?)", ("Huawei", model))


# Samsung
phone,pad,watch = samsung.extract_samsung_models("source/samsung_cn.md")
# 插入数据到phone表
for model in phone:
    cursor.execute("INSERT INTO phone VALUES (?, ?)", ("Samsung", model))

# 插入数据到pad表
for model in pad:
    cursor.execute("INSERT INTO tablet VALUES (?, ?)", ("Samsung", model))

# 插入数据到watch表
for model in watch:
    cursor.execute("INSERT INTO watch VALUES (?, ?)", ("Samsung", model))


# 提交更改并关闭连接
conn.commit()
conn.close()
