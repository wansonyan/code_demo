import matplotlib
import cv2
import os
from matplotlib import pyplot as plt
import numpy as np

# 原图片、标签文件、裁剪图片路径
img_path = r'F:\\GraFile\data_hsv(1)\\data_hsv\\H_ORANGE'


# 字典排序，type： 0->按key值排序（升序），1->按value值排序（降序）
def set_rank(a_dict, sort_type=1):
    a_sort_list = sorted(a_dict.items(), key=lambda x: int(x[sort_type]), reverse=sort_type == 1)
    a_sort_dict = {}
    for key, value in a_sort_list:
        a_sort_dict[key] = value
    return a_sort_dict


# 去除字典中频次小于阈值的键值对
def remove_under_threshold(a_dict, th):
    new_map = {}
    for kk in a_dict:
        vv = a_dict[kk]
        if vv >= th:
            new_map[kk] = vv
    return new_map


# 双折线图绘制
def two_line(map1, map2, yy):
    # x坐标相同
    x = map1.keys()
    y1 = map1.values()
    y2 = map2.values()

    matplotlib.use('TkAgg')
    fontsize = 12
    plt.plot(x, y1, 'o-', color="#91CC75", label="H")
    for a, b in zip(x, y1):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=8)
    plt.plot(x, y2, 's-', color="#5470C6", label="HSV-H")
    for a, b in zip(x, y2):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=8)
    plt.xlabel("H VALUES OF BLUE SAFETY HELMET")
    plt.ylabel("FREQUENCY")
    plt.axhline(y=yy)
    plt.legend(loc="best", fontsize=fontsize)
    plt.tight_layout()
    plt.show()


# 三折线图绘制
def three_line(map1, map2, map3):
    # x坐标相同
    x = map1.keys()
    y1 = map1.values()
    y2 = map2.values()
    y3 = map3.values()

    # 将H-HSV-H为0的数据从x、y1、y2、y3中删除
    x_filtered = []
    y1_filtered = []
    y2_filtered = []
    y3_filtered = []
    for i, val in enumerate(y3):
        if val != 0:
            x_filtered.append(list(x)[i])
            y1_filtered.append(list(y1)[i])
            y2_filtered.append(list(y2)[i])
            y3_filtered.append(val)

    plt.plot(x_filtered, y1_filtered, 'o-', color="#91CC75", linewidth=3, markersize=8, label="H")
    plt.plot(x_filtered, y2_filtered, 's-', color="#5470C6", linewidth=3, markersize=8, label="HSV-H")
    plt.plot(x_filtered, y3_filtered, '^-', color="#D190F0", linewidth=3, markersize=8, label="H-HSV-H")
    plt.xlabel("H VALUES OF ORANGE HELMETS")
    plt.ylabel("FREQUENCY")
    plt.legend(loc="best", fontsize=12)
    plt.tight_layout()
    plt.savefig("./png/ORANGE.png", dpi=300)  # 保存图像为文件，设置dpi参数为300
    plt.show()

# 折线图 + 柱状图绘制
def line_bar(map1, map2, yy):
    # x坐标相同
    x = map1.keys()
    y1 = map1.values()
    y2 = map2.values()

    matplotlib.use('TkAgg')
    fontsize = 12
    plt.plot(x, y1, 'o-', color="#91CC75", label="H")
    for a, b in zip(x, y1):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=8)
    plt.bar(x, y2, color="#5470C6", label="HSV-H")
    for a, b in zip(x, y2):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=8)
    plt.xlabel("H VALUES OF ORANGE SAFETY HELMET")
    plt.ylabel("FREQUENCY")
    plt.legend(loc="best", fontsize=fontsize)
    plt.tight_layout()
    plt.show()


# 双柱状图
def two_bar(map1, map2, yy):
    # x坐标相同
    x = map1.keys()
    y1 = map1.values()
    y2 = map2.values()

    matplotlib.use('TkAgg')
    fontsize = 12
    width = 0.3
    x_width1 = [ii for ii in range(len(x))]
    x_width2 = [ww + width for ww in x_width1]
    plt.bar(x_width1, y1, lw=0.5, color="#91CC75", label="H", width=width)
    for a, b in zip(x_width1, y1):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=8)
    plt.bar(x_width2, y2, lw=0.5, color="#5470C6", label="HSV-H", width=width)
    for a, b in zip(x_width2, y2):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=8)
    plt.xlabel("H VALUES OF ORANGE SAFETY HELMET")
    print(x_width1)
    plt.xticks(x_width1, labels=list(x))
    plt.ylabel("FREQUENCY")
    plt.legend(loc="best", fontsize=fontsize)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    pixel_total = 0
    h_map = {}
    hsv_map = {}

    # 声明一个空字典用于储存裁剪图片的类别及其数量
    # 把原图片裁剪后，按类别新建文件夹保存，并在该类别下按顺序编号
    for img_file in os.listdir(img_path):
        if img_file[-4:] in ['.png', '.jpg']:  # 判断文件是否为图片格式
            img_filename = os.path.join(img_path, img_file)  # 将图片路径与图片名进行拼接
            # print("img_filename: " + img_filename)
            img = cv2.imread(img_filename)  # 读取图片
            img_name = (os.path.splitext(img_file)[0])  # 分割出图片名，如“000.png” 图片名为“000”
            HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            h = img.shape[0]
            w = img.shape[1]
            pixel_total += w * h

            for i in range(0, h):
                for j in range(0, w):
                    # pixel_total += 1
                    pixel = HSV[i, j]
                    h = str(HSV[i, j, 0])
                    s = str(HSV[i, j, 1])
                    v = str(HSV[i, j, 2])
                    if h in h_map:
                        h_map[h] += 1
                    else:
                        h_map[h] = 1
                    hsv_key = '(' + h + ', ' + s + ', ' + v + ')'
                    if hsv_key in hsv_map:
                        hsv_map[hsv_key] += 1
                    else:
                        hsv_map[hsv_key] = 1
    print(h_map)
    print(hsv_map)

    # 按出现频次从大到小排序，取前80%
    h_map = set_rank(h_map)
    h_threshold = pixel_total * 0.81
    h_count = 0
    hsv_count = 0

    h_final_map = {}
    for key in h_map:
        h_count += h_map[key]
        h_final_map[key] = h_map[key]
        if h_count >= h_threshold:
            break

    # 按出现频次从大到小排序，取前90%
    hsv_map = set_rank(hsv_map)
    hsv_threshold = pixel_total * 0.9
    hsv_final_map = {}
    for key in hsv_map:
        hsv_count += hsv_map[key]
        hsv_final_map[key] = hsv_map[key]
        if hsv_count >= h_threshold:
            break

    # HSV中取出H
    hsv_h_map = {}
    hsv_h_total = 0
    for key in hsv_final_map:
        hsv_count = hsv_final_map[key]
        hsv_h_total += hsv_count
        end = key.find(',')
        h_key = key[1:end]
        if h_key in hsv_h_map:
            hsv_h_map[h_key] += hsv_count
        else:
            hsv_h_map[h_key] = hsv_count

    # HSV-H按频次从大到小排序，并取前90%
    hsv_h_map = set_rank(hsv_h_map)
    hsv_h_threshold = hsv_h_total * 0.9
    hsv_h_final_count = 0
    hsv_h_final_map = {}
    for key in hsv_h_map:
        hsv_h_final_count += hsv_h_map[key]
        hsv_h_final_map[key] = hsv_h_map[key]
        if hsv_h_final_count >= hsv_h_threshold:
            break

    print("pixel_total = " + str(pixel_total))
    print("threshold = " + str(h_threshold))
    print("H初始数据")
    print(set_rank(h_map))
    print("H取80%数据")
    print(set_rank(h_final_map))
    print("HSV初始数据")
    print(set_rank(hsv_map))
    print("HSV取90%数据")
    print(set_rank(hsv_final_map))
    print("HSV-H")
    print(set_rank(hsv_h_map))
    print("HSV-H取90%")
    print(set_rank(hsv_h_final_map))

    # 获取H的MAX和MIN
    h_final_pixel_total = 0
    hsv_h_final_pixel_total = 0
    for key in h_final_map:
        if key not in hsv_h_final_map:
            hsv_h_final_map[key] = 0
        else:
            h_final_pixel_total += h_final_map[key]

    for key in hsv_h_final_map:
        if key not in h_final_map:
            h_final_map[key] = 0
        else:
            hsv_h_final_pixel_total += hsv_h_final_map[key]

    # 按键值H排序
    h_final_map = set_rank(h_final_map, 0)
    hsv_h_final_map = set_rank(hsv_h_final_map, 0)
    print("零填充-键值排序")
    print(h_final_map)
    print(hsv_h_final_map)

    print(h_final_pixel_total)
    print(hsv_h_final_pixel_total)
    hsv_rate = h_final_pixel_total/hsv_h_final_pixel_total
    rate_map = {}
    for key in h_final_map:
        value1 = h_final_map[key]
        value2 = hsv_h_final_map[key]
        if value1 == 0 or value2 == 0:
            rate_map[key] = 0
        else:
            rate_map[key] = (value1 + hsv_rate * value2)

    # two_line(h_final_map, hsv_h_final_map, pixel_total * 0.05)
    three_line(h_final_map, hsv_h_final_map, rate_map)
