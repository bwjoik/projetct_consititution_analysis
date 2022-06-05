import jieba
import jieba.analyse


import pandas as pd


from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

import pyLDAvis
import pyLDAvis.sklearn
import csv
# pyLDAvis.enable_notebook()


# print(Raw_data.head())

#詞庫引入
dicts = "C:/Users/user/OneDrive - 東吳大學/python/projetct_consititution_analysis/text/中文分字字庫.txt"
stopwords_path = "C:/Users/user/OneDrive - 東吳大學/python/projetct_consititution_analysis/text/stopword.txt"
Raw_data = pd.read_csv("C:/Users/user/OneDrive - 東吳大學/python/projetct_consititution_analysis/JR_text.csv",encoding='utf-8-sig')
print(Raw_data.shape)
jieba.load_userdict(dicts)

#斷詞函數          
def chinese_word_cut(mytext):
    return jieba.lcut(mytext)

#斷詞
Raw_data["content_cutted"] = Raw_data.R.apply(chinese_word_cut)
cleared = pd.Series(index = range(0,819))
# print(Raw_data["content_cutted"])
# print(Raw_data.shape)


# #停用詞讀取
with open(stopwords_path,'r',encoding='utf-8-sig') as f:
    stop_words = f.readlines()
    stop_words = [stop_word.rstrip() for stop_word in stop_words] #讀取後不知道為什麼詞後面回有一個空格，移除掉



# print(stop_words)
# print(type(stop_words))

# 停用詞過濾

def stopword_filter(words):
    new_list = []
    for seg in (words):
        for seg in seg:
            if seg not in stop_words:
                new_list.append(seg)
    return new_list

Filted = []
for j in range(0,818):
    Filted.append(stopword_filter(Raw_data.loc[j:j,"content_cutted"]))
    
Target_Data = pd.DataFrame({"Filted":Filted})
# Processed_Data = pd.concat([Raw_data,Filted3],axis=1,sort=False)


#向量化
n_features = 10006
tf_vectorizer = CountVectorizer(strip_accents = 'unicode',
max_features=n_features,
stop_words='english',
max_df = 1,
min_df = 1)
tf = tf_vectorizer.fit_transform(Target_Data)

#主題抽取
lda = LatentDirichletAllocation(n_components=20, max_iter=50,
learning_method='online',
learning_offset=50.,
random_state=0)

lda.fit(tf)

#主題抽取結果展示方法
def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("主題 #%d:" % topic_idx)
        print(" ".join([feature_names[i]
    for i in topic.argsort()[:-n_top_words - 1:-1]]))
print()

#顯示個主題前X個詞
n_top_words = 20

tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, n_top_words)

#主題抽取視覺化
pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)

#將圖像輸出到另一視窗(方便在不同環境下觀看)
data = pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)
pyLDAvis.show(data)