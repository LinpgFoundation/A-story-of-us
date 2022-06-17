from os import path as PATH
from shutil import move as MOVE
from subprocess import check_call

from linpg import Builder  # type: ignore

# 删除dist文件夹
Builder.delete_file_if_exist("dist")

# 打包main文件
check_call(["pyinstaller", "main.spec"])

# 重命名文件
MOVE(PATH.join("dist", "main"), PATH.join("dist", "A_story_of_us"))

# 移除移除的缓存文件
folders_need_remove: tuple[str, ...] = ("build", "logs", "__pycache__", "crash_reports")
for folder_p in folders_need_remove:
    Builder.delete_file_if_exist(folder_p)
