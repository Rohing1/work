import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('table.xls')

# 转换日期格式
df['截止时间'] = pd.to_datetime(df['截止时间'], errors='coerce')

# 转换特定日期
for index, row in df.iterrows():
    if row['用户'] == 'E' and row['截止时间'].strftime('%Y/%m/%d') == '2025/9/26':
        df.at[index, '截止时间'] = pd.to_datetime('2025-04-19')

# 格式化日期为 'xxxx.xx.xx'
df['截止时间'] = df['截止时间'].dt.strftime('%Y.%m.%d')

# 打印所有列名
# 打印用户、需求和截止时间
for index, row in df.iterrows():
    user = row['用户']
    demand = row['需求']
    deadline = row['截止时间']

    print(f"用户: {user}, 需求: {demand}, 到期时间: {deadline if not pd.isnull(deadline) else '日期缺失'}")

    if user == 'A':
        print("A 用户的详细信息: ", end="")
        for col, val in row.items():
            print(f"{col}: {val}, ", end="")
        print("")  # 换行
