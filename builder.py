import shutil
from os import path as PATH
from subprocess import check_call

# 检测pyinstaller是否需要升级
check_call(["python", "-m", "pip", "install", "--upgrade", "pyinstaller"])

# 删除dist文件夹
if PATH.exists("dist"):
    shutil.rmtree("dist")

# 打包main文件
check_call(["pyinstaller", "--noconsole", "main.spec"])

# 重命名文件
shutil.move(PATH.join("dist", "main"), PATH.join("dist", "A_story_of_us"))

# 删除opencv
# shutil.rmtree(PATH.join("dist", "A_story_of_us", "cv2"))

# 移除移除的缓存文件
folders_need_remove: tuple[str, ...] = ("build", "logs", "__pycache__", "crash_reports")
for folder_p in folders_need_remove:
    if PATH.exists(folder_p):
        shutil.rmtree(folder_p)
