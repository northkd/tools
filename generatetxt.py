'''用于划分数据集的train，test，val'''

import os
from tqdm import tqdm
from random import shuffle

base = 'D:/tellhow-ai/workplace/WORK/AImatch/PaddleDetection/dataset/anjian_voc_coco'
img_base = 'JPEGImage'
xml_base = 'Annotation'

images_list = os.listdir(os.path.join(base, img_base))
shuffle(images_list)

split_num_1 = int(0.8 * len(images_list)) 

with open(os.path.join(base, 'train.txt'), 'w') as f:
    for im in tqdm(images_list[:split_num_1]):
        img_id = im[:-4]
        line = '{}/{}.jpg {}/{}.xml\n'.format(img_base, img_id, xml_base, img_id)
        f.write(line)

with open(os.path.join(base, 'test.txt'), 'w') as f:
    for im in tqdm(images_list[split_num_1:]):
        img_id = im[:-4]
        line = '{}/{}.jpg {}/{}.xml\n'.format(img_base, img_id, xml_base, img_id)
        f.write(line)
        
split_num_2 = int(0.2 * (0.8 * len(images_list))) 

with open(os.path.join(base, 'val.txt'), 'w') as f:
    for im in tqdm(images_list[:split_num_2]):
        img_id = im[:-4]
        line = '{}/{}.jpg {}/{}.xml\n'.format(img_base, img_id, xml_base, img_id)
        f.write(line)


# python tools/x2coco.py --dataset_type voc --voc_anno_dir dataset/anjian_voc_coco/ --voc_anno_list dataset/anjian_voc_coco/train.txt --voc_label_list dataset/anjian_voc_coco/label_list.txt  --voc_out_name voc_train.json