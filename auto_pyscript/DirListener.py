import os
import yaml
from MusTool import addMus
from MusTool import delMus
from MusTool import countMus

# 遍历文件夹,并返回所包含文件的内容
def walk_file_list(file):
    # with open('status_code.txt', 'a+', encoding='UTF-8') as f:
    #     for line in f.readlines():
    #         print(line)
    #     updateTime = os.path.getmtime('status_code.txt')
    #     print(updateTime)
    #     updateTime = time.localtime(updateTime)
    #     print(updateTime)
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        # print(type(files))
        # print(str(files))
        file_list = []
        for f in files:
            # print(os.path.join(root, f))
            file_list.append(f + "\n")
        return file_list
        # # 遍历所有的文件夹
        # for d in dirs:
        #     print("d")
        #     # print(os.path.join(root, d))
        #     # print(d)
        # with open('status_code.txt', 'w+', encoding='UTF-8') as f2:
        #     f2.writelines(list)


# 遍历文件夹,并返回所包含文件的内容
def walk_file_set(file):
    # with open('status_code.txt', 'a+', encoding='UTF-8') as f:
    #     for line in f.readlines():
    #         print(line)
    #     updateTime = os.path.getmtime('status_code.txt')
    #     print(updateTime)
    #     updateTime = time.localtime(updateTime)
    #     print(updateTime)
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        # print(type(files))
        # print(str(files))
        file_set = set()
        for f in files:
            # print(os.path.join(root, f))
            file_set.add(f)
        return file_set
        # # 遍历所有的文件夹
        # for d in dirs:
        #     print("d")
        #     # print(os.path.join(root, d))
        #     # print(d)
        # with open('status_code.txt', 'w+', encoding='UTF-8') as f2:
        #     f2.writelines(list)


def create_code_file(file_dir, code_file):
    # 获取文件夹文件列表
    file_list = walk_file_list(file_dir)
    # 获取文件夹最后更新时间
    final_time = os.path.getmtime(file_dir)
    file_list.append("finalTime:"+str(final_time))
    with open(code_file, 'w+', encoding='UTF-8') as f:
        f.writelines(file_list)


def check_is_upd(file_dir, code_file):
    if not os.path.exists(code_file):
        print('未检测到记录文件...')
        print('正在创建记录文件...')
        create_code_file(file_dir, code_file)
        print('创建记录文件完成')
        return False
    final_time = os.path.getmtime(file_dir)
    mark_time = ''
    with open(code_file, 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            if line.find('finalTime') != -1:
                mark_time = line[line.find(':') + 1:]
    if str(final_time) == mark_time.strip():
        return False
    return True


def walk_meta(code_file):
    meta_list = set()
    with open(code_file, 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            if line.find("finalTime") != -1:
                pass
            else:
                meta_list.add(line.strip())
    return meta_list


def main():
    yaml_path = 'config.yaml'
    with open(yaml_path, 'rb') as f:
        # yaml文件通过---分节，多个节组合成一个列表
        date = yaml.safe_load(f)
        # salf_load_all方法得到的是一个迭代器，需要使用list()方法转换为列表

    file_dir = date["path"]["music_dir"]
    code_file = date["path"]["code_file"]
    ejs_file = date["path"]["ejs"]

    if check_is_upd(file_dir, code_file):
        print("更新")
        file_set = walk_file_set("d:\\Cirike\\cdn.static.resource\\music")
        meta_set = walk_meta(code_file)
        add_set = file_set - meta_set
        del_set = meta_set - file_set
        if len(add_set) == 0 and len(del_set) == 0:
            print("没有新增的音频文件")
            create_code_file(file_dir, code_file)
        else:
            if len(add_set) != 0:
                for i in add_set:
                    addMus(i, ejs_file)
                create_code_file(file_dir, code_file)
            if len(del_set) != 0:
                for i in del_set:
                    delMus(i, ejs_file)
                create_code_file(file_dir, code_file)
    else:
        print("没有新增的音频文件")

    print('校验完成')
    countMus(ejs_file)


if __name__ == '__main__':
    main()
