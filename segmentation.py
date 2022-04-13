import jieba
import jieba.analyse


import pandas as pd


from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

import pyLDAvis
import pyLDAvis.sklearn
import csv
pyLDAvis.enable_notebook()

dicts = "C:/Users/user/OneDrive - 東吳大學/python/projetct_consititution_analysis/text/中文分字字庫.txt"
stops = "C:/Users/user/OneDrive - 東吳大學/python/projetct_consititution_analysis/text/stopword.txt"
df_csv  = "C:/Users/user/OneDrive - 東吳大學/python/projetct_consititution_analysis/DF_CSV.csv"

jieba.load_userdict(dicts) 
jieba.analyse.set_idf_path(dicts)
jieba.analyse.set_stop_words(stops)

JR_path = "C:/Users/user/OneDrive - 東吳大學/python/projetct_consititution_analysis/Judgment_Reasoning.csv"

Reader = open(JR_path,"r",encoding = 'UTF-8-sig')
Raw_data = Reader.read() 
 
# print("Read end")
# col = []
# for i in range(1,101):
#     col.append("T"+str(i))
# print(col)

# df = pd.read_csv(JR_path,encoding='utf-8-sig')
# df.rename(columns = {"1":"term"}, inplace = True)

# for i in range(0,806):
    # df.iat[i,0] = list(jieba.analyse.extract_tags(df.iat[i,0], topK=1000, withWeight=False, allowPOS=()))
# print(df.iat[0, 0])

Seged = jieba.analyse.extract_tags(Raw_data, topK=100, withWeight=False, allowPOS=())
# df=pd.DataFrame({'term':Seged})
# dff = pd.DataFrame(df.term.values.reshape(1,-1),index=['term'])
# corpus = [str(item) for item in dff]
# dff.to_csv(df_csv,encoding='utf-8-sig')
# DF_CSV = pd.read_csv(df_csv,encoding='utf-8-sig')
# print(df.content)
# def chinese_word_cut(mytext):
#     return " ".join(jieba.cut(mytext))
# # df["content_cutted"] = df.apply(chinese_word_cut)
# dfp = chinese_word_cut(df)
# n_features = 1000

# tf_vectorizer = CountVectorizer(strip_accents = 'unicode',
# max_features=n_features,
# stop_words='english',
# max_df = 1,
# min_df = 1.0,
# encoding = False)
# tf = tf_vectorizer.fit_transform(df)

# n_conponents = 10
# lda = LatentDirichletAllocation( n_components=n_conponents, max_iter=50,
# learning_method='online',
# learning_offset=50.,
# random_state=0)

# dt_matrix = lda.fit_transform(tf)
# features =  pd.DataFrame(dt_matrix)

# dt_matrix = lda.fit_transform(tf)

# features = pd.DataFrame(dt_matrix,columns = ['T0','T1','T2','T3','T4','T5','T6','T7','T8','T9'])

# # print(features)

# def print_top_words(model, feature_names, n_top_words):
#     for topic_idx, topic in enumerate(model.components_):
#         print("Topic #%d:" % topic_idx)
#         print(" ".join([feature_names[i]
#     for i in topic.argsort()[:-n_top_words - 1:-1]]))
#     print()
    
# n_top_words = 20

# tf_feature_names = tf_vectorizer.get_feature_names()
# print_top_words(lda, tf_feature_names, n_top_words)



# pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)

# data = pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)
# pyLDAvis.display(data)




# TextRank
# TR = jieba.analyse.textrank(Raw_data, topK=10, withWeight=True, allowPOS=())
# print(TR)
# TR_S = pd.Series(TR)
# print(TR_S)
# TR_S.to_csv('C:/Users/user/OneDrive - 東吳大學/python/projetct_consititution_analysis/TR_S.csv')


# print(jieba.analyse.textrank(line2, topK=10, withWeight=True, allowPOS=('n','v')))
# words = pseg.cut(line1)
# for word, flag in words:
#     print('%s %s' %(word,flag))
# J_regex = re.compile(r'第(\S\S\S)號')

# J_regexx = J_regex.findall(line2)
# print(J_regexx)
# for i in range(0,3):
#     print("第" + J_regexx[i] + "號釋字")

 