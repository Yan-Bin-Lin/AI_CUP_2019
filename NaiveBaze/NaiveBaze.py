'''
Created on 2019年5月25日

@author: danny
'''
import pickle

class NaiveBaze():
    '''
    load data
    @allnews    is a dict for news where key = news_index and value is a string with space split each word
    @tag        is a list of TD.csv. tag[0] is query. tag[1] is news_index. tag[2] is target
    @query      is a list of 20 query    
    @model      is a dict where key = query and value will return a list where list[0] is the trained model of query and list[1] is Vectorizer of doucument
    '''
    def __init__(self):
        # notice of path here
        with open('savefile', 'rb') as file:
            load = pickle.load(file)
            self.allnews = load['allnews']
            self.tag = load['tag']
            self.query = load['query']
            self.model = load['model'] 
    
    '''
    @input:
        query: string. 20 query
        docs: list. list of string with space to split word
    @output: int. target of predict. 0 means Opposite position. 1 means Same position 
    '''
    def predict(self, query, docs):
        model = self.model[query]
        return model[0].predict(model[1].transform(docs))
    
        
#example
if __name__ == '__main__':      

    query = '核四應該啟用'
    docs = ['蘋果僅 提供 專業 分析 不 保證 獲利 提醒您 小賭 怡情',
            '巨人 國家 聯盟費 城人 比分 手機 直撥 每秒 元市 分元']
    
    
    NB = NaiveBaze()
    print(NB.predict('核四應該啟用', docs))
    

