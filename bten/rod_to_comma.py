import os
import re

# 横杠转逗号

# ss = '名词 农田.		farmland . farmland . 	[f-a-r-m-l-a-n-d]. 	farmland .'
# 匹配 f-a-r-m-l-a-n-d
replace_reg = re.compile('\[([\w\s\-]+)\]')


def replace2Comma(sentence):
    s1 = replace_reg.search(sentence)
    if not s1:
        return False
    else:
        s2 = s1.group(1)
    s3 = s2.replace("-", ",")
    sentence = sentence.replace(s2, s3)
    return sentence


def replaceFileContent(dir_path):
    file_names = os.listdir(dir_path)
    file_paths = [os.path.abspath(os.path.join(dir_path, file_name)) for file_name in file_names]

    file_paths.append(os.path.abspath('02-汉到英单词录音库.txt'))
    for file_path in file_paths:
        lines = []
        with open(file_path, 'r', encoding='utf8') as f:
            lines = f.readlines()
        f.close()

        new_lines = []
        count = 0
        need_write = True
        for line in lines:
            result = replace2Comma(line)
            if not result:
                count += 1
                if count >= 3:
                    need_write = False
                    break
            else:
                new_lines.append(result)

        if not need_write:
            continue

        with open(file_path, 'w+', encoding='utf8') as f:
            for line in new_lines:
                f.write(line + '\n')

    print("转换完成！")
    os.system("@pause")


if __name__ == '__main__':
    # path = r'F:\lyp-documents\英语学习2\result-汉到英单词待录音'
    print("开始转换。。。")
    path = r'result-汉到英单词待录音'
    replaceFileContent(path)

    # pyinstaller -F -w -n 横杠转逗号 bten\rod_to_comma.py
