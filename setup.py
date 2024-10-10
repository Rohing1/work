from distutils.core import setup
import py2exe
import os
import shutil

# 指定需要包含的额外文件夹
extra_files = [('files', [os.path.join('D:\\priject\\webhook', 'files')])]

# 在构建前将额外文件夹复制到 dist 目录
def copy_extra_files():
    for folder, files in extra_files:
        target_folder = os.path.join('dist', folder)
        os.makedirs(target_folder, exist_ok=True)
        for file in files:
            if os.path.isfile(file):
                shutil.copy(file, target_folder)

# 配置 py2exe 的 options
setup(
    console=['download1.py'],  # 替换为您的 Python 脚本文件名
    options={
        'py2exe': {
            'includes': [],  # 需要包含的模块名称
            'bundle_files': 2,  # 打包方式，1：一个文件，2：一个文件夹
            'compressed': True,  # 是否压缩
            'optimize': 2,  # 优化级别
            'excludes': [],  # 需要排除的模块名称
            'dll_excludes': [],  # 需要排除的 DLL 文件
            'dist_dir': 'dist',  # 输出目录
            'includes': [],  # 额外包含的模块名称
            'packages': [],  # 额外的包
            'skip_archive': False,  # 是否跳过归档
            'unbuffered': False,  # 是否无缓冲
            'xref': False,  # 是否生成交叉引用
        }
    }
)

copy_extra_files()  # 在构建前复制额外文件夹到 dist 目录