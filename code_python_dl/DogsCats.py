# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/14 8:00
# @File    ：DogsCats.py
# @Function:

# %%
import os

import torch
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms


# 自定义数据集
class DogsVsCats(Dataset):
    def __init__(self, data_dir, split='train', transform=None):
        # 数据集路径列表 计算总数
        imgs = [os.path.join(data_dir, img) for img in os.listdir(data_dir)]
        imgs_num = len(imgs)

        # 数据集划分 train val test
        if split == 'train':
            self.image_paths = imgs[:int(0.8 * imgs_num)]
        elif split == 'val':
            self.image_paths = imgs[int(0.8 * imgs_num):]
        else:
            self.image_paths = imgs
        self.split = split

        # 数据转换
        if transform is None:
            if split == 'train':
                self.transform = transforms.Compose([
                    transforms.RandomHorizontalFlip(),
                    transforms.RandomRotation(10),
                    transforms.Resize((256, 256)),
                    transforms.RandomCrop(224),
                    transforms.ToTensor(),
                    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                ])
            else:
                self.transform = transforms.Compose([
                    transforms.Resize((224, 224)),
                    transforms.ToTensor(),
                    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                ])
        else:
            self.transform = transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        # 加载图像数据 图像数据转换
        image = Image.open(self.image_paths[idx]).convert('RGB')
        image = self.transform(image)

        # 图片路径 提取标签信息 转换为张量
        filename = self.image_paths[idx].split('/')[-1]
        if self.split == 'test':
            label = int(filename.split('.')[0])
        else:
            label = 1 if 'dog' in filename else 0
        label = torch.tensor(label, dtype=torch.long)

        return image, label
