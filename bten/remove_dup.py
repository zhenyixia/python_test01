# 去重 根据大小，大小相同即认为重复
import os
import shutil

path = r'E:\待整理文件\gif'
file_names0 = os.listdir(path)
file_path1 = [os.path.join(path, name) for name in file_names0]
#
# path2 = r'E:\待整理文件\mp4'
# file_names2 = os.listdir(path2)
# file_path2 = [os.path.join(path2, name) for name in file_names2]

# file_path2.extend(file_path1)
# file_paths = file_path2
file_paths = file_path1
size_file = {}

same_file = set()

for i in range(len(file_paths) - 1, -1, -1):
    file_path = file_paths[i]
    file_size = os.path.getsize(file_path)
    if file_size in size_file:
        os.remove(file_path)
        # same_file.add(file_name)
        # same_file.add(size_file.get(file_size))
        continue
    size_file[file_size] = file_path
#
# new_path = "G:\灾后数据\易我恢复文件\本地磁盘(D)\其他丢失文件\丢失原始名的文件\jpg-2"
# if not os.path.exists(new_path):
#     os.mkdir(new_path)
# print(same_file)
# same_file = list(same_file)
# for i in range(len(same_file) - 1, -1, -1):
#     same = same_file[i]
#     shutil.move(os.path.join(path, same), os.path.join(new_path, same))
