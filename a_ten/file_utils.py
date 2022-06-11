# -*- coding:utf-8 -*-
# @Author: lyp
# @Desc  : 文件工具类
# @Time  : 2022/1/4 16:49
import os.path
import shutil


def create_file(file_path):
    if not os.path.isfile(file_path):
        file = open(file_path, mode='w+')
        return file


def read_all_file(source_path):
    for root, dirs, files in os.walk(source_path):
        for file in files:
            src_file = os.path.join(root, file)
            # shutil.copy(src_file, target_path)
            print(src_file)


def copy_dir_tree(src, dst, timestamp=None):
    """
    将src包含src中的一切拷贝到dst下，效果如： dst/src(只有最后一级目录)/* 或 dst/src(只有最后一级目录)_时间戳/*
    :param src: 源目录
    :param dst: 目标目录
    :param timestamp: 时间戳
    """
    src1 = os.path.basename(src)
    dst1 = os.path.join(dst, src1)
    if timestamp:
        dst1 = f'{dst1}_{timestamp}'

    if os.path.exists(dst1):
        shutil.rmtree(dst1)

    shutil.copytree(src, dst1)


def createIfNotExists(path):
    if os.path.exists(path):
        print("path already exists!")
    else:
        os.mkdir(path)
        print("dir created")


def create_dir_tree(path, is_remove=False):
    if os.path.isdir(path):
        print(f'{path}非法')
        return
    if is_remove:
        shutil.rmtree(path)

    os.makedirs(path)


def copy_file(src, tg):
    if os.path.exists(tg):
        print("path already exists!")

    else:
        os.system("copy %s %s" % (src, tg))
        print("file created")


def check_dirs(src_dir, tg_dir):
    for root, dirs, files in os.walk(src_dir):
        for d in dirs:
            src_dirname = os.path.join(root, d)
            tg_dirname = src_dirname.replace(src_dir, tg_dir)
            createIfNotExists(tg_dirname)
    return True


def copy_all(src_dir, tg_dir):
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            src_filepath = os.path.join(root, f)
            tg_filepath = src_filepath.replace(src_dir, tg_dir)
            copy_file(src_filepath, tg_filepath)
    return True


def count_file_num(src_path):
    count = 0
    for root, dirs, files in os.walk(src_path):
        count += len(files)
    return count


# 将src中的文件全部移动到dst中，并删除src目录
def move_all(src, dst):
    if not os.path.isdir(src):
        print(f'路径不存在：{src}.')
        return

    os.system(f"robocopy {src} {dst}  /R:3 /W:60 /MOVE /DCOPY:T /e /xf .* /xd .*")


# 清空src目录下的一切
def clear_dir(src):
    shutil.rmtree(src)
    os.mkdirs(src)


# 增量复制所有，原来有的会复制，原来没有的也不会删除
def incre_copy_all(src, dst, restrict_list=None, is_move=None):
    """
    增量复制，将src下的一切，复制到dst下，包含目录也一起复制
    :param src: 源目录
    :param dst: 目标目录
    :param restrict_list:  例如：[*.txt *.doc *.bmp *.tif]
    :param is_move: 是否移动，如果将源目录文件全部移动后，则会删除源目录
    """
    print(f"Begin to incremental replication all, src: {src}, dst:{dst}.")

    restrict_files = ""
    if restrict_list:
        restrict_files = " ".join(restrict_files)

    move_param = "" if not is_move else "/MOVE"
    log_name = os.path.basename(src)
    os.system(
        f"robocopy {src} {dst} {restrict_files} /R:3 /W:60 {move_param} /DCOPY:T /e /xf .* /xd .* /LOG:./log/{log_name}_copy.log")
    print("Incremental replication successfully.")


# 增量复制文件，原来有的会复制，原来没有的也不会删除
def incre_copy_file(src, dst, restrict_list=None, is_move=None):
    """
    增量复制，将src下的一切，复制到dst下。但只限于文件
    :param src: 源目录
    :param dst: 目标目录
    :param restrict_list: 限制文件列表，如*.doc,*.txt等
    :param is_move: 是否移动，如果目标目录中包含源目录中的文件，则不会移动。如果将源目录文件全部移动后，则会删除源目录
    :return: True/False
    """
    print(f"Begin to incremental replication only file, src: {src}, dst:{dst}.")
    restrict_files = ""
    if restrict_list:
        restrict_files = " ".join(restrict_list)
    move_param = "" if not is_move else "/MOVE"
    log_name = os.path.basename(src)
    os.system(
        f"robocopy {src} {dst} {restrict_files} /R:3 /W:60 {move_param} /DCOPY:T /e /xf .* /xd * /LOG:./log/{log_name}_copy.log")
    print("Incremental replication successfully.")
    return True


# 删除指定目录下的所有空目录
def delete_empty_dir(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)

            if not os.listdir(dir_path):
                print(f"Begin to delete dir: {dir_path}.")
                os.rmdir(dir_path)


# 处理目录下的文件名，如果有特殊字符的则要处理掉
def process_file_name(src):
    all_files = os.listdir(src)
    window_name_exclude = ["\\", "\/", ":", "*", "?", "\"", "<", ">", "|"]
    to_keys = "-"
    # for file_name in all_files:


# 删除小图片，默认为小于20k的文件
def delete_small_files(src, size=None):
    files = os.listdir(src)
    canonical = 20 * 1024
    count = 0
    for file in files:
        file_path = os.path.join(src, file)
        if os.path.isdir(file_path):
            continue

        now_size = os.path.getsize(file_path)
        if now_size < canonical:
            os.remove(file_path)
            print(f"Delete small file: {file_path}.")
            count += 1

    print(f"Delete file numbers: {count}.")
    return count


def copy_file_delete_small(src_path, dst_path):
    """
    复制文件，如果目标目录中有重复名的文件，则删除大小比较小的文件
    :param src_path: 源目录
    :param dst_path: 目标目录
    """
    if not os.path.isdir(src_path) or not os.path.isdir(dst_path):
        print(f'{src_path}或{dst_path}目录非法。')
        return

    copy_num = 0
    file_names = os.listdir(src_path)
    for file_name in file_names:
        old_path = os.path.join(src_path, file_name)
        new_path = os.path.join(dst_path, file_name)
        if os.path.isfile(new_path):
            new_size = os.path.getsize(new_path)
            old_size = os.path.getsize(old_path)
            if new_size == old_size:
                continue
            elif new_size > old_size:
                os.remove(old_path)
                print(f'删除源目录文件：{old_path}')
            else:
                os.remove(new_path)
                print(f'删除目标目录文件：{new_path}')
                shutil.copy(old_path, new_path)
            continue
        else:
            shutil.copy(old_path, new_path)
            copy_num += 1
    return copy_num


def move_file_delete_small(src_path, dst_path):
    """
    移动文件，如果目标目录中有重复名的文件，则删除大小比较小的文件
    :param src_path: 源目录
    :param dst_path: 目标目录
    """
    if not os.path.isdir(src_path) or not os.path.isdir(dst_path):
        print(f'{src_path}或{dst_path}目录非法。')
        return

    move_num = 0
    delete_num = 0
    file_names = os.listdir(src_path)
    for file_name in file_names:
        old_path = os.path.join(src_path, file_name)
        new_path = os.path.join(dst_path, file_name)
        if os.path.isfile(new_path):
            new_size = os.path.getsize(new_path)
            old_size = os.path.getsize(old_path)
            if new_size >= old_size:
                os.remove(old_path)
                print(f'删除源目录文件：{old_path}')
                delete_num += 1
                continue
            else:
                os.remove(new_path)
                print(f'删除目标目录文件：{new_path}')
                shutil.move(old_path, new_path)
                move_num += 1
            continue
        else:
            shutil.move(old_path, new_path)
            move_num += 1

    print(f'移动到dst：{move_num}个,删除src：{delete_num} 个')
    return move_num, delete_num


def delete_smaller(src_path, dst_path):
    """
    删除源目录与目标目录中，名称相同，但是大小较小的文件
    :param src_path: 源目录
    :param dst_path: 目标目录
    """
    if not os.path.isdir(src_path) or not os.path.isdir(dst_path):
        print(f'{src_path}或{dst_path}目录非法。')
        return

    total_src, total_dst = 0, 0
    file_names = os.listdir(src_path)
    for file_name in file_names:
        old_path = os.path.join(src_path, file_name)
        new_path = os.path.join(dst_path, file_name)
        if os.path.isfile(new_path):
            new_size = os.path.getsize(new_path)
            old_size = os.path.getsize(old_path)
            if new_size > old_size:
                os.remove(old_path)
                total_src += 1
            else:
                os.remove(new_path)
                total_dst += 1
    print(f'删除源目录和目标目录文件个数分别为：{total_src} ，{total_dst}。')


def delete_duplicate(spec_path):
    """
    删除指定目录下所有重复的文件，删除名称相同，但大小较小的
    :param src_path: 源目录
    :param dst_path: 目标目录
    """
    if not os.path.isdir(spec_path):
        print(f'{spec_path}目录非法。')
        return

    # 结构为： file_name: file_path
    file_name2_path = dict()
    dup_total = 0
    for root, dirs, file_names in os.walk(spec_path):
        for file_name in file_names:
            file_path = os.path.join(root, file_name)
            if file_name not in file_name2_path:
                file_name2_path[file_name] = file_path
            else:
                size = os.path.getsize(file_path)
                old_path = file_name2_path[file_name]
                old_size = os.path.getsize(old_path)
                if size > old_size:
                    os.remove(old_path)
                    file_name2_path[file_name] = file_path
                else:
                    os.remove(file_path)
                dup_total += 1

    print(f'去重个数为：{dup_total}。')


def move_img_to_dst(src_path, dst_path, suffix):
    """    将src_path下的所有图片移动到dst_path   """
    if not os.path.isdir(src_path) or not os.path.isdir(dst_path):
        print(f'{src_path} 或 {dst_path}目录非法。')
        return

    # 结构为： file_name: file_path
    file_name2_path = dict()
    dup_total = 0
    for root, dirs, file_names in os.walk(src_path):
        for file_name in file_names:
            file_path = os.path.join(root, file_name)
            size = os.path.getsize(file_path)
            if file_name.endswith(suffix) and size >= 5 * 1024:
                new_path = os.path.join(dst_path, file_name)
                shutil.move(file_path, new_path)
                dup_total += 1

    print(f'移动个数为：{dup_total}。')


if __name__ == '__main__':
    src_path1 = r'F:'
    dst = r'E:\003-图片\temp'
    # move_img_to_dst(src_path1, dst, '.jpg')
    delete_empty_dir(src_path1)
