# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/23 20:06
# @File    ：demo2.py
# @Function:

import pprint

import torch
from torchvision import models
from torchvision import transforms  # 图片的预处理
from PIL import Image  # 图片
import matplotlib.pyplot as plt

# pprint.pprint(dir(models))
alexnet = models.AlexNet()
resnet = models.resnet101(pretrained=True)
# print(resnet)

# 图片
img = Image.open(r'data/p1ch2/bobby.jpg')
plt.imshow(img)
plt.axis('off')
plt.show()

# 图片的预处理
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])
img_t = preprocess(img)
print(img_t)  # 处理后 tensor
print(img_t.shape)  # 维度信息 torch.Size([3, 224, 224])

# 给张量加一个维度(批次维度、通道维度、高度维度、宽度维度)
batch_t = torch.unsqueeze(img_t, 0)  # 加在第零维之前
print(batch_t.shape)  # torch.Size([1, 3, 224, 224])

# 使用网络
resnet.eval()  # 评估模式 相对于测试模式
outputs = resnet(batch_t)
print(outputs)  # 输出张量
print(outputs.shape)  # torch.Size([1, 1000])  1个图片 1000个类别

with open(r'data/p1ch2/imagenet_classes.txt') as f:
    labels = [line.strip() for line in f.readlines()]
# print(labels)  # 1000个种类

print(outputs.argmax())  # tensor(207)
print(labels[207])  # golden retriever

_, index = torch.max(outputs, 1)  # 在output第二个维度中找到最大的 输出最大值_和所在索引
print(index)  # tensor([207])

# softmax
print(outputs.sum())  # 1000个的和不是1
percentage = torch.nn.functional.softmax(outputs, dim=1)[0] * 100
print(percentage.shape)  # 1000维度
print(percentage.sum())  # 100

print(labels[index[0]], percentage[index[0]].item())  # golden retriever 96.29334259033203

# 预测前五的可能性
_, indices = torch.sort(outputs, descending=True)
pprint.pprint([[labels[idx], percentage[idx].item()] for idx in indices[0][:5]])
