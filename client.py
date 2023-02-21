import http.client, urllib.parse
import json
import base64


def cv2_to_base64(image):
    return base64.b64encode(image).decode('utf8')


data = {"key": ["image"], "value": []}

with open(input('请输入图片路径: '), 'rb') as file:
    image_data1 = file.read()
    image = cv2_to_base64(image_data1)
    data["value"] = image

data_json = json.dumps(data)
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
# conn = http.client.HTTPConnection('81.68.184.250', 120)
conn = http.client.HTTPConnection('localhost', 8888)
conn.request('POST', '/pmsocr/stuff_info_table/', data_json.encode('utf-8'), headers)#往server端发送数据
response = conn.getresponse()

# 预期的response样式：[{'姓名': '张三', '性别': '男', '出生日期': '1982/5/3'}, {'姓名': '李四', '性别': '女', '出生日期': '1982/5/4'}, {'姓名': '张三1', '性别': '男', '出生日期': '1982/5/3'}, {'姓名': '李四2', '性别': '女', '出生日期': '1982/5/4'}] 
print(response.status, response.headers)
stc1 = response.read().decode('utf-8')#接受server端返回的数据
print(stc1)
stc = json.loads(stc1)

print("-----------------接受server端返回的数据----------------")
print(stc)
print("-----------------接受server端返回的数据----------------")

conn.close()
