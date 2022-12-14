# -*- coding: utf-8 -*-
# VGG模型验证

import torch
import torchvision
from PIL import Image
from torch import nn

# from VGGmodel import VGG

image_path = "/home/tzr/Documents/PycharmSYNC/PythonandMLLearning/PytorchLearning/learn1/dataset/bees/train/ants_image/0013035.jpg"
image = Image.open(image_path)
# print(image)
image = image.convert('RGB')
transform = torchvision.transforms.Compose([torchvision.transforms.Resize((32, 32)),
                                            torchvision.transforms.ToTensor()])
# 转为tensor类
image = transform(image)


# print(image.shape)


class VGG(nn.Module):
    def __init__(self):
        super(VGG, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(64 * 4 * 4, 64),
            nn.Linear(64, 10)
        )

    def forward(self, x):
        x = self.model(x)
        return x


model = torch.load("vggmodel/vgg_19.pth",
                   map_location=torch.device('cpu'))
model.eval()
# model = VGG()
# print(model)
image = torch.reshape(image, (1, 3, 32, 32))
with torch.no_grad():
    output = model(image)

print(output)
print(output.argmax(1))

