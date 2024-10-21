!wget -O cars.jpg https://www.uzdaily.uz/storage/img/cars/cars-road.jpg
import torch
from PIL import Image
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
imgs = ['https://www.uzdaily.uz/storage/img/cars/cars-road.jpg']