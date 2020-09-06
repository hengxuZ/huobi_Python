# encoding: utf-8
from system.huobi_tool import get_market_price, buy_coin, sell_coin
from system.price import get_buy_price, get_sell_price, modify_price
from system.dingding import dingding_warn
import time,traceback

def loop_fun():
        while True:
            if get_buy_price() >= get_market_price("eosusdt"):
                print("满足买价，购买价为：%f" % get_buy_price())
                order_id=buy_coin("eosusdt",get_buy_price())
                modify_price(get_buy_price())
                
            elif get_sell_price() < get_market_price("eosusdt"):
                print("满足卖价，卖价为：%f" % get_sell_price())
                order_id=sell_coin("eosusdt",get_sell_price())
                modify_price(get_sell_price())
            else:
                print("未能交易,继续运行") 
          


if __name__ == "__main__":
    try:
        loop_fun()
    except Exception as e:
        error_info = "报警："+str(e)
        print(error_info)
        dingding_warn(error_info) 
    # order_id=sell_coin("eosusdt",5)
    # modify_price(get_sell_price())
    # get_market_price("eosusdt")