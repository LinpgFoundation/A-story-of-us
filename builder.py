import os
import shutil

# 检测pyinstaller是否需要升级
os.system("python -m pip install --upgrade pyinstaller")

# 删除dist文件夹
if os.path.exists("dist"):
    shutil.rmtree("dist")

# 打包main文件
os.system("pyinstaller --noconsole main.spec")

# 移除移除的缓存文件
folders_need_remove: tuple[str] = ("build", "logs", "__pycache__", "crash_reports")
for folder_p in folders_need_remove:
    if os.path.exists(folder_p):
        shutil.rmtree(folder_p)