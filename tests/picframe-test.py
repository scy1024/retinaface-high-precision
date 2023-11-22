'''
Author: sucy suchunyu1998@gmail.com
Date: 2023-11-22 10:21:12
LastEditors: sucy suchunyu1998@gmail.com
LastEditTime: 2023-11-22 10:21:13
FilePath: /retinaface-high-precision/tests/picframe-test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from retinaface import RetinaFace
import cv2
import matplotlib.pyplot as plt
import os

# 更改为你的图片路径
img_path = "/mnt/e/GithubGoodProject/Thesis/Topic_1_Improve_Face_Detection/Video2Frames/DataSet/Chines_Class/pic/frame_8400.jpg"
img = cv2.imread(img_path)

# 进行人脸检测
resp = RetinaFace.detect_faces(img_path, threshold = 0.1)

def int_tuple(t):
    return tuple(int(x) for x in t)

# 创建用于保存人脸的目录
output_dir = "outputs/faces/test"
os.makedirs(output_dir, exist_ok=True)

# 设置统一的人脸图像大小
target_size = (256, 256)

# 遍历检测到的每一个人脸
for i, key in enumerate(resp):
    identity = resp[key]
    landmarks = identity["landmarks"]
    facial_area = identity["facial_area"]

    # 以鼻子为中心，确定截取范围
    nose_center = int_tuple(landmarks["nose"])
    face_height = facial_area[3] - facial_area[1]
    crop_size = int(face_height * 2.5)  # 增大截取范围

    # 确定截取的图像范围
    x1 = max(nose_center[0] - crop_size // 2, 0)
    y1 = max(nose_center[1] - crop_size // 2, 0)
    x2 = min(nose_center[0] + crop_size // 2, img.shape[1])
    y2 = min(nose_center[1] + crop_size // 2, img.shape[0])

    # 截取图像
    cropped_face = img[y1:y2, x1:x2]

    # 调整图像大小
    resized_face = cv2.resize(cropped_face, target_size)

    # 保存调整大小后的图像
    cv2.imwrite(os.path.join(output_dir, f'face_{i}.png'), resized_face)

# 显示处理后的图像
plt.imshow(img[:, :, ::-1])
plt.axis('off')
plt.show()

# 保存处理后的图像
cv2.imwrite('outputs/result.png', img)
