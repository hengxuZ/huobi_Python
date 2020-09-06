import os,json

data_path = os.getcwd()+"/quantify/data/data.json"
    

    
def get_json_data():
    tmp_json = {}
    with open (data_path,'r') as f:
        tmp_json = json.load(f)
        f.close()
    return tmp_json    

def modify_json_data(data):
    with open (data_path,"w") as f:
        json.dump(data,f)
    f.close()

####------下面为输出函数--------####

def get_buy_price():
    data_json = get_json_data()
    return data_json["runBet"]["next_buy_price"]

def get_sell_price():
    data_json = get_json_data()
    return data_json["runBet"]["grid_sell_price"]



# 买入后，修改 补仓价格 和 网格平仓价格
def modify_price(deal_price):
    print("买入成功，开始修改补仓价和网格价")
    data_json = get_json_data()
    data_json["runBet"]["next_buy_price"]  = round( deal_price  * (1 - data_json["config"]["double_throw_ratio"]/100),2 )
    data_json["runBet"]["grid_sell_price"]  = round( deal_price * (1 + data_json["config"]["profit_ratio"]/100),2 )

    modify_json_data(data_json)
    print("修改后的补仓价格为:{double}。修改后的网格价格为:{grid}".format(double=data_json["runBet"]["next_buy_price"], grid=data_json["runBet"]["grid_sell_price"] ))
    
    
if __name__ == "__main__":
    modify_price(3)