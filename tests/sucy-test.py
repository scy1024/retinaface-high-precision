'''
Author: sucy suchunyu1998@gmail.com
Date: 2023-11-21 15:00:00
LastEditors: sucy suchunyu1998@gmail.com
LastEditTime: 2023-11-21 15:00:01
FilePath: /retinaface-high-precision/tests/sucy-test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from retinaface import RetinaFace
import cv2
import matplotlib.pyplot as plt

# 更改为你的图片路径
img_path = "./dataset/demo.png"
img = cv2.imread(img_path)

# 进行人脸检测
resp = RetinaFace.detect_faces(img_path, threshold = 0.1)

def int_tuple(t):
    return tuple(int(x) for x in t)

# 遍历检测到的每一个人脸
for key in resp:
    identity = resp[key]

    landmarks = identity["landmarks"]
    diameter = 1
    cv2.circle(img, int_tuple(landmarks["left_eye"]), diameter, (0, 0, 255), -1)
    cv2.circle(img, int_tuple(landmarks["right_eye"]), diameter, (0, 0, 255), -1)
    cv2.circle(img, int_tuple(landmarks["nose"]), diameter, (0, 0, 255), -1)
    cv2.circle(img, int_tuple(landmarks["mouth_left"]), diameter, (0, 0, 255), -1)
    cv2.circle(img, int_tuple(landmarks["mouth_right"]), diameter, (0, 0, 255), -1)

    facial_area = identity["facial_area"]
    rectangle_color = (0, 0, 255)
    cv2.rectangle(img, (facial_area[2], facial_area[3]), (facial_area[0], facial_area[1]), rectangle_color, 3)

# 显示处理后的图像
plt.imshow(img[:, :, ::-1])
plt.axis('off')
plt.show()

# 保存处理后的图像
cv2.imwrite('outputs/result.png', img)
