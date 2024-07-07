import numpy as np
import requests
import base64
import cv2 as cv


def vehicle_detect(img):
    vehicle_access_token = '24.7907b72a3bdf1b0d3944539097ebff9c.2592000.1722498130.282335-89936452'

    # 百度云车辆检测接口地址
    vehicle_detect_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"

    # 使用 OpenCV 将图像编码为 JPEG 格式并转换为 base64 编码
    _, encoded_image = cv.imencode('im*/.jpg', img)
    base64_image = base64.b64encode(encoded_image).decode('utf-8')  # 转换为字符串格式

    # 设置车辆检测接口的请求参数
    vehicle_detect_params = {"image": base64_image}

    # 构建车辆检测接口请求 URL 和请求头
    vehicle_detect_request_url = vehicle_detect_url + "?access_token=" + vehicle_access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    # 发送车辆检测接口的 POST 请求
    response = requests.post(vehicle_detect_request_url, data=vehicle_detect_params, headers=headers)

    num_cars = 0  # 初始化车辆数量为 0

    if response.status_code == 200:
        data = response.json()  # 解析车辆检测接口的响应 JSON 数据
        num_cars = data.get('vehicle_num', {}).get('car', 0)  # 获取识别出的小汽车数量

        # 遍历每个检测到的车辆信息
        for item in data.get('vehicle_info', []):
            location = item.get('location', {})  # 车辆位置信息
            x1 = location.get('left', 0)  # 左上角 x 坐标
            y1 = location.get('top', 0)  # 左上角 y 坐标
            x2 = x1 + location.get('width', 0)  # 右下角 x 坐标
            y2 = y1 + location.get('height', 0)  # 右下角 y 坐标

            # 在图像上绘制检测到的车辆位置
            cv.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # 返回处理后的图像和识别出的车辆数量
    return img, num_cars


def pedestrian_detect(img):
    pedestrian_access_token = '24.7907b72a3bdf1b0d3944539097ebff9c.2592000.1722498130.282335-89936452'

    # 百度云人流量检测接口地址
    pedestrian_detect_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_num"

    # 使用 OpenCV 将图像编码为 JPEG 格式并转换为 base64 编码
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image).decode('utf-8')  # 转换为字符串格式

    # 设置人流量检测接口的请求参数
    pedestrian_detect_params = {"image": base64_image}

    # 构建人流量检测接口请求 URL 和请求头
    pedestrian_detect_request_url = pedestrian_detect_url + "?access_token=" + pedestrian_access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    # 发送人流量检测接口的 POST 请求
    response = requests.post(pedestrian_detect_request_url, data=pedestrian_detect_params, headers=headers)

    num_pedestrians = 0  # 初始化行人数量为 0

    if response.status_code == 200:
        pedestrian_data = response.json()  # 解析人流量检测接口的响应 JSON 数据
        num_pedestrians = pedestrian_data.get('person_num', 0)  # 获取识别出的行人数量

    # 返回处理后的图像和识别出的行人数量
    return img, num_pedestrians


# if __name__ == '__main__':
#
#     img_path = '/Users/baozi/summer_training/project1/data/img3.jpg'
#     read_img = cv.imread(img_path)
#
#     if read_img is None:
#         print(f"无法读取图像文件：{img_path}")
#     else:
#         show_img, num_cars = vehicle_detect(read_img)
#         # show_img, num_pedestrians = pedestrian_detect(read_img)
#
#         # print(f"识别到 {num_cars} 辆车辆。")
#         print(f"识别到 {num_cars} 个行人。")
#
#         # 显示处理后的图像
#         cv.imshow('img', show_img)
#         cv.waitKey(0)
#         cv.destroyAllWindows()
