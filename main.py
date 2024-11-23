from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def 提取主要颜色(图片路径, 聚类数=5):
    图片 = Image.open(图片路径)
    
    #优化
    图片 = 图片.resize((图片.width // 10, 图片.height // 10))
    
    #换为numpy数组
    数组图片 = np.array(图片)
    
    #重塑数组(pixels, 3)
    数组图片 = 数组图片.reshape((-1, 3))
    
    #算法
    聚类器 = KMeans(n_clusters=聚类数)
    聚类器.fit(数组图片)
    
    颜色组 = 聚类器.cluster_centers_
    
    #计算颜色出现次数
    出现次数 = np.bincount(聚类器.labels_)
    
    #排序
    排序后的颜色 = [颜色组[i] for i in np.argsort(出现次数)[::-1]]
    
    #选择第二多
    第二颜色 = None
    for 颜色 in 排序后的颜色:
        红, 绿, 蓝 = 颜色
        if not (红 >= 240 and 绿 >= 240 and 蓝 >= 240) and not (红 <= 153 and 绿 <= 153 and 蓝 <= 153):
            第二颜色 = tuple(int(分量) for 分量 in 颜色)
            break
    
    if 第二颜色:
        return 第二颜色
    else:
        主要颜色 = 排序后的颜色[0]
        主要颜色 = tuple(int(分量) for 分量 in 主要颜色)
        return 主要颜色

#在此处填写图片文件输入路径
图片路径 = '？'
主要颜色 = 提取主要颜色(图片路径, 聚类数=5)
print("主要颜色:", 主要颜色)
