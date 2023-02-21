import os
import cv2
from paddleocr import PPStructure
from copy import deepcopy
import base64
import numpy as np
import json
from pandas import read_html

def perdict_stuff_info(image_base64_code):
    table_engine = PPStructure(show_log=False, image_orientation=True)
    img = base64_to_cv2(image_base64_code)
    res = table_engine(img)
    return save_structure_res(res)

def predict_stuff_info_path(image_path):
    table_engine = PPStructure(show_log=False, image_orientation=True)
    img = cv2.imread(image_path)
    res = table_engine(img)
    return save_structure_res(res)

def save_structure_res(res):
    res_cp = deepcopy(res)
    # save res
    result = list()
    res = list()
    for region in res_cp:
        if region['type'].lower() == 'table' and len(region['res']) > 0 and 'html' in region['res']:
            res = read_html(region['res']['html'])
    table = res[0].values.tolist()
    header_line = table[0]
    for line in table:
        type = line[0]

        if type != '姓名' and str(type) != 'nan' and type != '必填' and type != '':
            curr_res = dict()
            for i in range(0, len(line)):
                if str(line[i]) != 'nan':
                    curr_res[header_line[i]] = line[i]
            result.append(curr_res)
    print(result)
    return result
 
def cv2_to_base64(image):
    return base64.b64encode(image).decode('utf8')

def base64_to_cv2(base64_code):
    img_data = base64.b64decode(base64_code)
    img_array = np.fromstring(img_data, np.uint8)
    img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)
    return img

if __name__ == "__main__":
    with open('1.jpg', 'rb') as file:
        image_data1 = file.read()
        image = cv2_to_base64(image_data1)
        perdict_stuff_info(image)