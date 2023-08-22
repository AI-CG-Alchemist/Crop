import os
import threading

for i in os.listdir('./data'):
    os.system(f'python crop-video.py --inp ./data/{i}')