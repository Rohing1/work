import time
from DownloadKit import DownloadKit
from pathlib import Path

# 从文本文件中读取URL链接
def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines() if line.strip()]
    return urls

# 获取脚本所在目录
script_dir = Path(__file__).resolve().parent

urls_file = 'files/fileURLs.txt'
full_path = script_dir / urls_file

print("脚本目录:", script_dir)
print("fileURL.txt完整路径:", full_path)

# 确认文件存在
if full_path.exists():
    print(f"{full_path} 存在")
else:
    print(f"{full_path} 不存在")

# 创建下载器对象
d = DownloadKit(full_path.parent)  # 使用文件所在目录作为下载目录

# 从URL文本文件中读取URL链接
urls = read_urls_from_file(full_path)

# 添加多个任务
start_time = time.time()
for url in urls:
    d.add(url)
end_time = time.time()

# 计算并打印下载所花费的时间（秒）
elapsed_time = end_time - start_time
print(f"程序运行了 {elapsed_time} 秒")
