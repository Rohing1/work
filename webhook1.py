import pandas as pd
from datetime import datetime
import requests
import json
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

# 获取当前日期
current_date = datetime.now().strftime('%Y.%m.%d')

# 初始化结果字符串
result = ""
# 打印所有列名
# 打印用户、需求和截止时间，并判断是否到期
for index, row in df.iterrows():
    user = row['用户']
    demand = row['需求']
    deadline = row['截止时间']

    is_due = "是" if deadline == current_date else "否"

    print(f"用户: {user}, 需求: {demand}, 到期时间: {deadline if not pd.isnull(deadline) else '日期缺失'}, 是否为到期时间: {is_due}")

    if user == 'A':
        print("A 用户的详细信息: ", end="")
        for col, val in row.items():
            print(f"{col}: {val}, ", end="")
        print("")  # 换行
# 发送告警信息到 Webhook
webhook_url = "https://oapi.dingtalk.com/robot/send?access_token=f3b01ded0bc4b2399b11e1a1c484beb6fcfc5d902f9ad1f9d99eaf8f9a7b266e"  # 替换为您的实际 Webhook URL
payload = {
    "content": result
}
headers = {
    "Content-Type": "application/json"
}
response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    print("告警信息已成功发送到 Webhook")
else:
    print(f"告警信息发送失败，状态码: {response.status_code}")