import os
import shutil
from subprocess import check_call
from linpg import Builder  # type: ignore

# 更新所有第三方库
# Builder.update_all_site_packages()

# 删除dist文件夹
Builder.delete_file_if_exist("dist")

# 打包main文件
check_call(["pyinstaller", "--noconsole", "main.spec"])

# 重命名文件
shutil.move(os.path.join("dist", "main"), os.path.join("dist", "A_story_of_us"))

# 删除opencv
shutil.rmtree(os.path.join("dist", "A_story_of_us", "cv2"))

# 移除移除的缓存文件
folders_need_remove: tuple[str, ...] = ("build", "logs", "__pycache__", "crash_reports")
for folder_p in folders_need_remove:
    Builder.delete_file_if_exist(folder_p)
