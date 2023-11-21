import shioaji as sj  #引入shioaji套件，命名為sj
api = sj.Shioaji()  #建立shioaji api物件
api.login(   #登入
    person_id="1",  #帳號
    passwd="1",  #密碼
    contracts_cb=lambda security_type: print(f"{repr(security_type)} fetch done.")
)
contract_2890 = api.Contracts.Stocks["2330"]
print(contract_2330)