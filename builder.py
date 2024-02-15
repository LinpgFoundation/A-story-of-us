import shutil
from os import path as PATH
from shutil import move as MOVE
from subprocess import check_call

from linpgtoolbox.builder import Builder  # type: ignore

# 删除dist文件夹
Builder.remove("dist")

# 打包main文件
check_call(["pyinstaller", "main.spec"])

# move assets
_ADDITIONAL_ASSETS: tuple[str, ...] = ("Assets", "Data")
for additional_dir in _ADDITIONAL_ASSETS:
    shutil.copytree(
        PATH.join(".", additional_dir), PATH.join("dist", "main", additional_dir)
    )

# 重命名文件
MOVE(PATH.join("dist", "main"), PATH.join("dist", "A_story_of_us"))

# 移除移除的缓存文件
folders_need_remove: tuple[str, ...] = ("build", "logs", "__pycache__", "crash_reports")
for folder_p in folders_need_remove:
    Builder.remove(folder_p)
