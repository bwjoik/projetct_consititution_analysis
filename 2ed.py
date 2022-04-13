import pandas as pd
import numpy as np
import jieba
import jieba.analyse
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer, TfidfVectorizer
import pyLDAvis
import pyLDAvis.sklearn
dicts = "C:/Users/user/OneDrive - 東吳大學/python/projetct_consititution_analysis/text/中文分字字庫.txt"
stops = "C:/Users/user/OneDrive - 東吳大學/python/projetct_consititution_analysis/text/stopword.txt"

jieba.load_userdict(dicts)
jieba.analyse.set_stop_words(stops)

df = pd.read_csv('C:/Users/user/OneDrive - 東吳大學/python/projetct_consititution_analysis/Judgment_Reasoning.csv',encoding = 'utf-8-sig',names=['txt'])

df_words_list=[]
for i in range(0,2):
    df_words= jieba.lcut(df.txt[i],cut_all=False)
    df_words_list=df_words_list+df_words
    



tfidf_vectorizer = TfidfVectorizer(min_df=5)
tfidf_mat = tfidf_vectorizer.fit_transform(df_words_list)
tfidf_mat.todense()
# print(tfidf_mat)
# c_vectorizer = CountVectorizer()
# words_count_mat = c_vectorizer.fit_transform(df_words_list)      
# print(words_count_mat.todense())

# tfidf_vectorizer = TfidfTransformer()
# tfidf_mat = tfidf_vectorizer.fit_transform(words_count_mat) 

# print("字典長度",len(tfidf_vectorizer.vocabulary_))
# print(tfidf_vectorizer.vocabulary_)

n_conponents = 10
lda = LatentDirichletAllocation( n_components=n_conponents, max_iter=50,
learning_method='online',
learning_offset=50.,
random_state=0)
lda.fit(tfidf_mat.todense())

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
        for i in topic.argsort()[:-n_top_words - 1:-1]]))
print()

# pyLDAvis.sklearn.prepare(lda, tf_vectorizer)
# data = pyLDAvis.sklearn.prepare(lda, tfidf_vectorizer)
# pyLDAvis.display(data)

# words_count_mat.todense()
# print(words_count_mat)
# # def is_chap_head(tmpstr):
#     import re
#     pattern = re.compile('第.{1,7}條')
#     return len(pattern.findall(tmpstr))

# df['is_chap_head'] = df.txt.apply(is_chap_head)
# chap_num = 0
# for i in range(len(df)):
#     if df['is_chap_head'][i] == 1:
#         chap_num += 1
#     df.loc[i,'chap'] = chap_num
# del df['is_chap_head']