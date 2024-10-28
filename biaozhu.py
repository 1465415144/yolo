import os

# 定义固定边界框（YOLO 格式：class x_center y_center width height）
fixed_bbox_ok = "0 0.466562 0.614583 0.271875 0.175833"  # 0 代表 OK
fixed_bbox_ng = "1 0.466562 0.614583 0.271875 0.175833"  # 1 代表 NG

# 定义类别映射
class_mapping = {'OK': fixed_bbox_ok, 'NG': fixed_bbox_ng}

# 遍历 OK 和 NG 文件夹
for label, bbox in class_mapping.items():
    img_dir = f'E:/ALL1.1/ALL/{label}'
    label_dir = f'E:/ALL1.1/labels/{label}'
    os.makedirs(label_dir, exist_ok=True)

    for img_file in os.listdir(img_dir):
        if img_file.endswith(('.jpg', '.bmp', '.jpeg')):
            txt_file = os.path.splitext(img_file)[0] + '.txt'
            txt_path = os.path.join(label_dir, txt_file)
            with open(txt_path, 'w') as f:
                f.write(bbox + '\n')

print("边界框标签文件生成完成。")