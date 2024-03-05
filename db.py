import sqlite3
from device_extractor import apple

# 创建或连接到数据库
conn = sqlite3.connect('model.db')
cursor = conn.cursor()

# 创建phone表
cursor.execute('''CREATE TABLE IF NOT EXISTS phone
                (brand TEXT, model TEXT)''')

# 创建pad表
cursor.execute('''CREATE TABLE IF NOT EXISTS pad
                (brand TEXT, model TEXT)''')

# 创建watch表
cursor.execute('''CREATE TABLE IF NOT EXISTS watch
                (brand TEXT, model TEXT)''')

iphones, ipads, apple_watches, ipods = apple.extract_apple_models("source/apple_all_en.md")

# 插入数据到phone表
for model in iphones:
    cursor.execute("INSERT INTO phone VALUES (?, ?)", ("Apple", model))

# 插入数据到pad表
for model in ipads:
    cursor.execute("INSERT INTO pad VALUES (?, ?)", ("Apple", model))

# 插入数据到watch表
for model in apple_watches:
    cursor.execute("INSERT INTO watch VALUES (?, ?)", ("Apple", model))

# 提交更改并关闭连接
conn.commit()
conn.close()
