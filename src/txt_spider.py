import os.path                  # 系統功能模組
import numpy                    # 分析模組
import requests                 # 網路模組
from collections import Counter # 次數統計模組

from PIL import Image           # 圖片處理模組
import jieba                    # 分詞模組
import matplotlib.pyplot as plt # 視覺化模組
import wordcloud                # 文字雲模組

with open('spider_zonggui_previous.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    print(data)
    print('------------------')

