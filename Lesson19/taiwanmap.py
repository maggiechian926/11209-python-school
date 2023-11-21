import matplotlib.pyplot as plt

# 設定圖表大小
plt.figure(figsize=(10, 10))

# 設定背景色
plt.set_facecolor('white')

# 繪製台灣地圖
plt.imshow(plt.imread('taiwan_map.png'))

# 標記人口稠密地區
for label, x, y in zip(labels, x_coords, y_coords):
    plt.annotate(
        label,
        xy=(x, y),
        fontsize=12,
        color='red',
    )

# 顯示圖表
plt.show()
