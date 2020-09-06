# encoding: utf-8
from huobi import RequestClient
from huobi.model import *
import json,os,time,xlrd
from huobi.base.printobject import PrintMix
from data.author import my_api_key,my_secret_key,my_url


request_client = RequestClient(api_key=my_api_key, secret_key=my_secret_key,url=my_url)

####------下面为输出函数--------####

# 获取市价
def get_market_price(coin_type):
    request_client = RequestClient()
    trades = request_client.get_market_trade(symbol=coin_type)
    now_price = trades[0].price
    print('市价为：%f' % now_price )
    return now_price
    
# 买单
def buy_coin(coin_type,buy_price):
    order_id = request_client.create_order(coin_type, AccountType.SPOT, OrderType.BUY_LIMIT, amount=50, price=buy_price)
    print("买单为：%d" %order_id)
    insert_transaction_log(order_id)

# 卖单
def sell_coin(coin_type,sell_price):
    order_id = request_client.create_order(coin_type, AccountType.SPOT, OrderType.SELL_LIMIT, amount=50, price=sell_price)
    print("卖单id为:%d" % order_id) 
    insert_transaction_log(order_id)

# 查看订单是否成交
def select_order_deal(order_id):
    order_obj = request_client.get_order(symbol="eosusdt", order_id=order_id)


def insert_transaction_log(order_id):
    json_data = {}
    json_data["order_id"] = order_id
    with open(os.getcwd()+"/quantify/transaction_log/record.json",'a') as f:
        json.dump(json_data,f)
        f.close()
 
if __name__ == "__main__":
    insert_transaction_log(94113157875531)
    # sell_coin("eosusdt",4)
    pass