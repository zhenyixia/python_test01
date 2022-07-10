# -*- coding:utf-8 -*-
# @Author: lyp
# @Desc  : 批量提交与push
# @Time  : 2022/7/10 16:19
import os

ex_repository = ['toBeBetterJavaer', 'python', 'Python-100-Days', 'somebaks', 'yulinfengdian']


re_path1 = "D:\GIT-repo"
first_dir = os.listdir(re_path1)
all_repository = []
for dd in first_dir:
    path = os.path.join(re_path1, dd)
    if os.path.isfile(path):
        continue

    repository = os.listdir(path)
    for name in repository:
        path2 = os.path.join(path, name)
        if os.path.isfile(path2) or name in ex_repository:
            continue
        all_repository.append(path2)
print(all_repository)


def batch_add_commit_push():
    for path in all_repository:
        one = os.path.basename(path)
        cmd = f'cd {path} & git branch'
        print(cmd)
        f = os.popen(cmd)
        result = f.readlines()
        branch = 'master'
        for temp in result:
            if '* main' in temp:
                branch = 'main'
                print(f'git branh --> {result}')
                break

        # 防止出现误报： Your branch is ahead of 'origin/master' by 2 commits.
        #   (use "git push" to publish your local commits)
        cmd = f'cd {path} & git remote -v'
        f = os.popen(cmd)
        result = f.readlines()
        if result:
            cmd = f'cd {path} & git remote remove origin'
            print(cmd)
            os.system(cmd)

        cmd = f'cd {path} & git add .'
        print(cmd)
        os.system(cmd)

        cmd = f'cd {path} & git cm "统一提交"'
        print(cmd)
        os.system(cmd)

        cmd = f'cd {path} & git push git@github.com:zhenyixia/{one}.git {branch}'
        print(cmd)
        os.system(cmd)

        cmd = f'cd {path} & git push git@gitee.com:zhenyixia001/{one}.git {branch}'
        print(cmd)
        os.system(cmd)
        # print(f'{cmd3}{one}.git')
        # print(f'{cmd4}{one}.git')
    os.system('@pause')


def batch_print_branch():
    for one in all_repository:
        path = os.path.join(re_path1, one)
        f = os.popen(f'cd {path} & git branch')
        result = f.readlines()
        # print(f'{one}--{result}')
        if '* main\n' in result:
            print(f'{one}--{result}')


if __name__ == '__main__':
    batch_add_commit_push()
    # batch_print_branch()
