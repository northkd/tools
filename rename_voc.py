'''修改voc数据集中xml文件的filename和path为当前文件夹名称和路径'''

import os
import xml.dom.minidom

file_path = "./Annotation"       
img_path = "./JPEGImage"             
xml_files = os.listdir(file_path)       # xml文件名列表
img_files = os.listdir(img_path)        # 图片文件名列表，由于xml文件以及图片名称（图片均为.jpg)后缀一一对应，因此列表内也一一对应
                                        # 必须承认这样会存在问题，比如图片后缀不一样等等肯定会bug，遇到问题再修改吧
for i, xmlFile in enumerate(xml_files):  
    # print(len(xml_files))   # 遍历xml文件夹
    if not os.path.isdir(xmlFile):          # 不是文件夹,打开xml文件
        print("\n",xmlFile)
        dom = xml.dom.minidom.parse(os.path.join(file_path, xmlFile))   # 读取xml文件，送入dom解析
        root = dom.documentElement                                      # 返回整个xml文档的内容
        original_path = root.getElementsByTagName('path')               # 根据标签名称获取path节点
        p0 = original_path[0]       
        # 上述返回值是一个list，观察xml文件发现path和filename长度均为1
        # print(p0)                 # p0其实是机器编码，不是具体文本
        path0 = p0.firstChild.data  # 使用data是将其具体的文本内容提取出来
        print(path0)
        original_filename = root.getElementsByTagName('filename')  # 根据标签名称获取filename节点
        f0 = original_filename[0]   # 同上
        # print(f0)
        fn0 = f0.firstChild.data   # 同上

        img_name = img_files[i]     # 获取和xml对应的图片名称
        modify_path = img_path + "/" + img_name       # 修改path
        modify_filename = img_name                    # 修改filename
        print(modify_path)
        p0.firstChild.data = modify_path              # 把修改后的path值赋给path的机器码
        f0.firstChild.data = modify_filename         # 把修改后的filename值赋给path的机器码

        with open(os.path.join(file_path, xmlFile), 'w') as fh:
            dom.writexml(fh)
            print('DONE')
