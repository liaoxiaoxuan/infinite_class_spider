import os.path                  # 系統功能模組
import numpy                    # 分析模組
import requests                 # 網路模組
from collections import Counter # 次數統計模組

from PIL import Image           # 圖片處理模組
import jieba                    # 分詞模組
import re                       # 正則表達示
import matplotlib.pyplot as plt # 視覺化模組
import wordcloud                # 文字雲模組

with open('spider_zonggui_previous.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    print(data)
    print('------------------')



# 定義繁體中文檔名
WORDS_PATH = 'dict.txt.big.txt' # 繁體中文詞庫檔名
TC_FONT_PATH = 'NotoSansTC-Regular.otf' # 繁體中文字型檔名



# 切換 jieba 繁體中文詞庫

jieba.set_dictionary(WORDS_PATH)



# jieba 斷詞

# 精確模式
# for sentence in data:
seg_list = jieba.lcut(data)
print('/'.join(seg_list))

print('---------------')

# # 全模式
# for sentence in data:
#     seg_list = jieba.cut(sentence, cut_all=True)
#     print('/'.join(seg_list))

# print('---------------')

# # 搜索引擎模式
# for sentence in data:
#     seg_list = jieba.cut_for_search(sentence)
#     print('/'.join(seg_list))



# 使用正則表示式提取資訊（書名）
pattern = r"\《(.*?)\》"
matches = re.findall(pattern, data)

# 輸出提取到的資訊
print("提取到的括號內的資訊：", matches)



# 詞頻

# 總覽
counter = Counter(matches)
print(counter)

# 前幾名
# most_counter = Counter(seg_list).most_common(100)
# print(most_counter)



