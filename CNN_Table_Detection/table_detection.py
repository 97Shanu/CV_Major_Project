# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dwmW-vWLecZDYpapw7aiOz-F2uP4_xsQ
"""


from __future__ import print_function
import os
import random
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim as optim
import torch.utils.data
import torchvision
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import torchvision.datasets as td
from IPython.display import HTML
import torch.nn.init as init
import torch.nn.functional as F
# os.environ['CUDA_LAUNCH_BLOCKING'] = '1'
import torchvision.transforms as transforms
import torchvision.utils as vutils
import numpy as np
from torch.utils.data import DataLoader
from torchvision.io import read_image
import torchvision.models as models

# !unzip /content/drive/MyDrive/CV_Project2/table_data.zip



device = torch.device("cuda" if torch.cuda.is_available() else "cpu")



import os
import csv

directory = 'table_data/train_data/labels/train/'  # Replace with the path to your directory
output_csv = 'table_data/train_data/labels/train/0_annotations.csv'  # Replace with the desired path for the output CSV file

# Create a list to store the data from the text files
data = []

# Iterate through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):  # Only process text files
        file_path = os.path.join(directory, filename)
        
        # Read the contents of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
        # Split the content into five columns: label, center_x, center_y, width, height
        for line in lines:
            label, center_x, center_y, width, height = line.strip().split()
            jpg_filename = filename.replace('.txt', '.jpg')
            data.append((jpg_filename, label, center_x, center_y, width, height))

# Write the data to a CSV file
with open(output_csv, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Filename', 'Label', 'Center_X', 'Center_Y', 'Width', 'Height'])  # Write the header row
    
    for item in data:
        writer.writerow(item)


directory = 'table_data/train_data/labels/val/'  # Replace with the path to your directory
output_csv = 'table_data/train_data/labels/val/0_annotations.csv'  # Replace with the desired path for the output CSV file

# Create a list to store the data from the text files
data = []

# Iterate through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):  # Only process text files
        file_path = os.path.join(directory, filename)
        
        # Read the contents of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
        # Split the content into five columns: label, center_x, center_y, width, height
        for line in lines:
            label, center_x, center_y, width, height = line.strip().split()
            jpg_filename = filename.replace('.txt', '.jpg')
            data.append((jpg_filename, label, center_x, center_y, width, height))

# Write the data to a CSV file
with open(output_csv, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Filename', 'Label', 'Center_X', 'Center_Y', 'Width', 'Height'])  # Write the header row
    
    for item in data:
        writer.writerow(item)




import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader
import os
from PIL import Image
import pandas as pd



# class TableDetectorCNN(nn.Module):
#     def __init__(self):
#         super(TableDetectorCNN, self).__init__()
        
#         # Convolutional layers
#         self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
#         self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        
#         # Fully connected layers
#         self.fc1 = nn.Linear(32 * 32 * 32, 128)
#         self.fc2 = nn.Linear(128, 2)

#     def forward(self, x):
#         x = nn.functional.relu(self.conv1(x))
#         x = nn.functional.max_pool2d(x, 2)
#         x = nn.functional.relu(self.conv2(x))
#         x = nn.functional.max_pool2d(x, 2)
#         x = x.view(-1, 32 * 32 * 32)
#         x = nn.functional.relu(self.fc1(x))
#         x = self.fc2(x)
#         return nn.functional.log_softmax(x, dim=1)

class TableDetectorCNN(nn.Module):
    def __init__(self):
        super(TableDetectorCNN, self).__init__()
        
        # Convolutional layers
        self.conv1 = nn.Conv2d(3, 5, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(5, 3, kernel_size=3, stride=1, padding=1)
        
        # Fully connected layers
        self.fc1 = nn.Linear(78732, 39366)  # Adjusted size
        self.fc2 = nn.Linear(39366, 128)  # Adjusted size
        self.fc3 = nn.Linear(128, 2)

    def forward(self, x):
        x = nn.functional.relu(self.conv1(x))
        print(x.shape)
        x = nn.functional.max_pool2d(x, 2)
        print(x.shape)
        x = nn.functional.relu(self.conv2(x))
        print(x.shape)
        x = nn.functional.max_pool2d(x, 2)
        print(x.shape)
        x = x.view(x.size(0), -1)
        print(x.shape)
        x = nn.functional.relu(self.fc1(x))
        print(x.shape)
        x = nn.functional.relu(self.fc2(x))
        print(x.shape)
        x = self.fc3(x)
        print(x.shape)
        return nn.functional.log_softmax(x, dim=1)





class TableDataset(Dataset):
    def __init__(self, annotation_file, image_dir, transform=None):
        self.annotations = pd.read_csv(annotation_file)
        self.image_dir = image_dir
        self.transform = transform
        self.min_width, self.min_height = self.find_min_dimensions()

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, idx):
        image_path = os.path.join(self.image_dir, self.annotations.iloc[idx, 0])
        image = Image.open(image_path).convert("RGB")
        image = image.resize((self.min_width, self.min_height), Image.ANTIALIAS)
        
        label = self.annotations.iloc[idx, 1]
        center_x = self.annotations.iloc[idx, 2]
        center_y = self.annotations.iloc[idx, 3]
        width = self.annotations.iloc[idx, 4]
        height = self.annotations.iloc[idx, 5]
        
        # Normalize coordinates and size to range [0, 1]
        center_x /= self.min_width
        center_y /= self.min_height
        width /= self.min_width
        height /= self.min_height

        if self.transform:
            image = self.transform(image)

        # Create target tensor
        target = torch.tensor([label, center_x, center_y, width, height], dtype=torch.float32)
        # print(image.shape)
        # print(target)
        return image, target

    def find_min_dimensions(self):
        min_width = float("inf")
        min_height = float("inf")

        for idx in range(len(self.annotations)):
            image_path = os.path.join(self.image_dir, self.annotations.iloc[idx, 0])
            image = Image.open(image_path)
            width, height = image.size
            min_width = min(min_width, width)
            min_height = min(min_height, height)

        return min_width, min_height



# class TableDataset(Dataset):
#     def __init__(self, annotation_file, image_dir, transform=None):
#         self.annotations = pd.read_csv(annotation_file)
#         self.image_dir = image_dir
#         self.transform = transform

#     def __len__(self):
#         return len(self.annotations)

#     def __getitem__(self, idx):
#         image_path = os.path.join(self.image_dir, self.annotations.iloc[idx, 0])
#         image = Image.open(image_path).convert("RGB")
        
#         label = self.annotations.iloc[idx, 1]
#         center_x = self.annotations.iloc[idx, 2]
#         center_y = self.annotations.iloc[idx, 3]
#         width = self.annotations.iloc[idx, 4]
#         height = self.annotations.iloc[idx, 5]
        
#         # Normalize coordinates and size to range [0, 1]
#         center_x /= image.width
#         center_y /= image.height
#         width /= image.width
#         height /= image.height

#         if self.transform:
#             image = self.transform(image)

#         # Create target tensor
#         target = torch.tensor([label, center_x, center_y, width, height], dtype=torch.float32)
#         # image_size = image.size
#         # width, height = image.size
#         print(image.shape)
#         print(target)
#         return image, target




# Define hyperparameters
batch_size = 32
num_epochs = 10
learning_rate = 0.001

# Create an instance of the CNN model
model = TableDetectorCNN().to(device)

# Define the loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Create a custom dataset
train_dataset = TableDataset(annotation_file="table_data/train_data/labels/train/0_annotations.csv", image_dir="table_data/train_data/images/train", transform=transforms.ToTensor())

# Create a data loader
train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

dataiter = iter(train_dataloader)
images, labels = next(dataiter)
images_cpu = images.cpu()
print(labels)
def imshow(img):
    npimg = img.numpy()
    plt.imshow(np.transpose(vutils.make_grid(images[0].to(device)[:10], padding=2, normalize=True).cpu(),(1,2,0)))
    plt.show()
imshow(torchvision.utils.make_grid(images_cpu))


# Training loop
total_steps = len(train_dataloader)
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_dataloader):
        images = images.to(device)
        labels = labels.to(device)

        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)

        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (i+1) % 10 == 0:
            print(f"Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{total_steps}], Loss: {loss.item():.4f}")

# Display results
# Add code to display the results of table detection (e.g., visualize predicted tables on images)


def test(model, test_dataloader):
    model.eval()
    total_correct = 0
    total_samples = 0
    
    with torch.no_grad():
        for data in test_dataloader:
            inputs, labels = data
            
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            
            total_samples += labels.size(0)
            # total_correct += (predicted == labels).sum().item()
            diff = torch.abs(predicted.float() - labels.float())
            correct_mask = diff <= 0.05
            total_correct += correct_mask.sum().item()
    accuracy = total_correct / total_samples
    print(f"Test Accuracy: {accuracy:.4f}")


# Create a custom dataset
test_dataset = TableDataset(annotation_file="table_data/train_data/labels/val/0_annotations.csv", image_dir="table_data/train_data/images/val", transform=transforms.ToTensor())

# Create a data loader
test_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

test(model, test_dataloader)



