import yaml

def addMus(msg, ejs_file):
    data = ''

    with open(ejs_file, 'r+', encoding='UTF-8') as f:
        # str = input("请输入文件名:")
        for line in f.readlines():
            # if(line.find('Server') == 0):
            #     line = 'Server=%s' % ('192.168.1.1',) + '\n'
            if line.find('https://cdn.jsdelivr.net/gh/Cirike/cdn.static.resource@master/music') != -1:
                if line.find(']') != -1:
                    line = line[0:line.find(']')] + '\n\t\t\t\t\t"https://cdn.jsdelivr.net/gh/Cirike/cdn.static' \
                                                    '.resource@master/music/' + msg + '",];\n '
            data += line

    with open(ejs_file, 'r+', encoding='UTF-8') as f:
        f.writelines(data)
        print("添加成功!")


def delMus(msg,ejs_file):
    data = ''

    cache = ''

    with open(ejs_file, 'r+', encoding='UTF-8') as f:
        # str = input("请输入文件名:")
        for line in f.readlines():
            # if(line.find('Server') == 0):
            #     line = 'Server=%s' % ('192.168.1.1',) + '\n'
            if line.find('https://cdn.jsdelivr.net/gh/Cirike/cdn.static.resource@master/music') != -1:
                if line.find(msg) != -1:
                    if line.find('];') != -1:
                        # print(cache)
                        # print(line)
                        # cache = cache[0:len(cache)-2]
                        cache = cache[0:len(cache) - 1] + "];\n"
                        # cache.replace("\\n","];\n")
                        line = ''
                        # print(cache)
                        # print(line)
                    else:
                        line = ''
            data += cache
            cache = line
        data += cache

    with open(ejs_file, 'r+', encoding='UTF-8') as f:
        f.writelines(data)
        print("删除成功")


def countMus(ejs_file):
    count = 0

    with open(ejs_file, 'r+', encoding='UTF-8') as f:
        for line in f.readlines():
            if line.find('https://cdn.jsdelivr.net/gh/Cirike/cdn.static.resource@master/music') != -1:
                count += 1
                print(line[line.find('music'):line.find(',')])
        print("文件总数为: ", end='')
        print(count, end="\n")


if __name__ == '__main__':
    yaml_path = 'config.yaml'
    with open(yaml_path, 'rb') as f:
        date = yaml.safe_load(f)
    ejs_file = date["path"]["ejs"]
    while True :
        switch = input("添加文件输入: 'add' \n删除文件输入: 'del' \n查看音频文件总数输入: 'count' \n退出输入: 'exit' \n")
        if switch.strip() == 'add':
            msg = input("请输入添加文件名:")
            if msg.strip() == 'exit':
                break
            addMus(msg.strip(), ejs_file)
        elif switch.strip() == 'del':
            msg = input("请输入待删除文件名:")
            if msg.strip() == 'exit':
                break
            delMus(msg.strip(), ejs_file)
        elif switch.strip() == 'count':
            countMus(ejs_file)
        elif switch.strip() == 'exit':
            break
        else:
            print("无效指令")
