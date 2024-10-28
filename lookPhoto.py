import cv2
import os


def draw_bounding_box(image_path, bbox):
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        return

    height, width, _ = image.shape

    # 解析边界框信息
    class_id, x_center, y_center, width_bbox, height_bbox = map(float, bbox.split())

    # 将比例转换为像素值
    x_center *= width
    y_center *= height
    width_bbox *= width
    height_bbox *= height

    # 获取边界框的左上角和右下角坐标
    x1 = int(x_center - width_bbox / 2)
    y1 = int(y_center - height_bbox / 2)
    x2 = int(x_center + width_bbox / 2)
    y2 = int(y_center + height_bbox / 2)

    # 绘制边界框
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 显示图像
    cv2.imshow('Image with Bounding Box', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 示例：为OK类别的图像绘制边界框
ok_bbox = "0 0.466562 0.614583 0.271875 0.175833"
draw_bounding_box('E:/ALL1.1/ALL/OK/240305_194807_0000000794_4_&Cam3ImgRotate.bmp', ok_bbox)