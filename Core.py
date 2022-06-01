import jieba
import jieba.analyse


import pandas as pd


from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

import pyLDAvis
import pyLDAvis.sklearn
import csv
pyLDAvis.enable_notebook()


# print(Raw_data.head())

#資料庫引入
dicts = "C:/Users/user/OneDrive - 東吳大學/python/projetct_consititution_analysis/text/中文分字字庫.txt"
stops = "C:/Users/user/OneDrive - 東吳大學/python/projetct_consititution_analysis/text/stopword.txt"
#df_csv  = "C:/Users/user/OneDrive - 東吳大學/python/projetct_consititution_analysis/DF_CSV.csv"

#Raw_data = pd.read_csv("C:/Users/user/OneDrive - 東吳大學/python/projetct_consititution_analysis/Judgment_Reasoning.csv",encoding='utf-8-sig')
Raw_data = pd.read_csv("C:/Users/user/OneDrive - 東吳大學/python/projetct_consititution_analysis/JR_text.csv",encoding='utf-8-sig')
print(Raw_data.shape)


#斷詞函數
def chinese_word_cut(mytext):
    return " ".join(jieba.cut(mytext))

#斷詞
Raw_data["content_cutted"] = Raw_data.R.apply(chinese_word_cut)

#向量化
## print(Raw_data.content_cutted.head())
n_features = 1000
tf_vectorizer = CountVectorizer(strip_accents = 'unicode',
max_features=n_features,
stop_words='english',
max_df = 0.5,
min_df = 10)
tf = tf_vectorizer.fit_transform(Raw_data.content_cutted)

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

#主題抽取展示

#顯示個主題前X個詞
n_top_words = 20

tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, n_top_words)

#主題抽取視覺化
pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)

#將圖像輸出到另一視窗(方便在不同環境下觀看)
data = pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)
pyLDAvis.show(data)
