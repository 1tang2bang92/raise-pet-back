import json
import time

FILE_PATH = r'./cache/info.json'


def get_breed_info():
    with open(FILE_PATH, 'r') as f:
        data = json.load(f)

    return data

def save_breed(file):
    if file and file.filename.endswith(('.jpg', '.jpeg', '.png')):
        file.save(FILE_PATH+str(time.time())+file.filename.split('.')[-1].lower())
        return 'File uploaded successfully'
    else:
        return 'Invalid file format. Only JPG, JPEG, and PNG files are allowed.'