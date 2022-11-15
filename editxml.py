'''voc数据集xml文件没有path路径时，可用以下代码修改'''

'''本代码先判断是否存在path，如不存在则添加path，并指定添加path中内容'''

import xml.dom.minidom as ET
import os
from xml.etree.ElementTree import parse, Element
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)


xml_file_path = r"./Annotation/"
lst_dir = os.listdir(xml_file_path)

for file_name in lst_dir:
    file_path = xml_file_path + file_name   # 读入所有的xml文件
    doc = parse(file_path)
    root = doc.getroot()
    root.getchildren().index(root.find('filename'))
    element = root.find('path')
    if element is None:
        e = Element('path')
        e.text = './Annotation/'
        root.insert(2, e)
        newStr = os.path.join(xml_file_path, file_name)
        doc.write(newStr, xml_declaration=True)
    else:
        print('1')
    
print('done')

    # tree = ET.parse(file_path)
    # root = tree.getroot()
    # sub_new = ET.Element('path')
    # sub_new.attrib = {"D:\ceshi\Annotation"}
    # sub_new.text = "new element"
    # root.append(sub_new)

# def xml_combine(xml_dir):
#     # root = ET.Element("root")
#     tree = ET.Element(annotations)
#     data = ET.Element(root, 'path')

