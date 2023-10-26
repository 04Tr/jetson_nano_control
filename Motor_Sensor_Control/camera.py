import cv2
import keras
import numpy as np
from keras.models import load_model
from astra import Astra

# 加载已经训练好的模型
loaded_model = load_model("red_ball_detection_model.h5")

# 配置Astra相机
camera = Astra(config_path="./config/")
try:
    camera.init_video_stream(video_mode="color_depth", image_registration=True)
except Exception as e:
    print("[错误] 没有发现Astra设备, 请检查接线或驱动")
    print(e)
    exit(-1)

while True:
    # 采集彩色图像
    color_img = camera.read_color_img()

    # 预处理图像，例如调整大小和归一化
    test_image = cv2.resize(color_img, (224, 224))
    test_image = test_image / 255.0

    # 进行红球中心坐标的检测
    predicted_coords = loaded_model.predict(np.array([test_image]))

    # 提取预测的坐标
    rx, ry = predicted_coords[0]

    # 打印预测坐标
    print(f"红球坐标：({rx}, {ry})")

    # 在图像上标记红球中心以便可视化
    cv2.circle(color_img, (int(rx), int(ry)), 10, (0, 0, 255), -1)

    # 显示彩色图像
    cv2.imshow('color', color_img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        # 如果按键为q，退出程序
        break

# 释放相机
camera.release()
# 销毁窗口
cv2.destroyAllWindows()