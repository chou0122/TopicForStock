import shioaji as sj  #引入shioaji套件，命名為sj
api = sj.Shioaji()  #建立shioaji api物件
api.login(   #登入
    person_id="5Msqh9X4D6e7ztJChjac4Py43APt4fUKAizsY5HYvxCk",  #帳號
    passwd="982UoLdhHNLD56Q4H95geXFLopBd4EoXNBrS87eFo93G",  #密碼
    contracts_cb=lambda security_type: print(f"{repr(security_type)} fetch done.")
)
contract_2890 = api.Contracts.Stocks["2890"]
print(contract_2890)