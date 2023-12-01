import shioaji as sj  #引入shioaji套件，命名為sj
api = sj.Shioaji()  #建立shioaji api物件
api.login(   #登入
    u_id="",  #帳號
    passwd="5Msqh9X4D6e7ztJChjac4Py43APt4fUKAizsY5HYvxCk",  #密碼
    contracts_cb=lambda security_type: print(f"{repr(security_type)} fetch done.")
)
contract_2890 = api.Contracts.Stocks["2890"]
print(contract_2890)
contract_2330 = api.Contracts.Stocks['2330']
print(contract_2330)    




#避險部位程式

# import pandas, numpy
# import pandas_datareader as web

# # 從yahoo finance 下載資料
# close_stock = web.DataReader('2330.TW', 'yahoo')['Close']  # 只抽取收盤價，此時為時間序列
# close_index = web.DataReader('^TWII', 'yahoo')['Close'] # 期貨計算用加權指數代替 直接用期貨算更好

# # 合併成df
# df = pandas.DataFrame({'stock': close_stock, 
#                        'index': close_index})

# # 計算報酬率
# ret = (df - df.shift(1)) / df.shift(1)

# # 資料處理
# df = df.dropna() # 去掉遺失值

# # 相關係數
# corr = ret.corr() # 高度正相關，避險要空期貨

# # 變異數矩陣(共變異數)
# cov = ret.cov()

# # 變異數
# var = ret.var()

# # bata係數
# bata = cov / var['index'] # Cov(ra,rm) ／ Var(rm)  
# print(bata.iloc[0,1]) # 1.3597010457753163

# # 避險口數 =  bata * 現貨市值/ (期貨指數*每點價值)
# # 台積電部位500萬，大台指期16000點為例
# sell = bata.iloc[0,1] * 5000000 / (16000*200)
# print(sell) # 2.1245328840239317 約空台指期2口
