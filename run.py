import os

for i in os.listdir('./data'):
    os.system(f'python crop-video.py --inp ./data/{i}')