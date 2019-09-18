#coding:utf-8
import requests
import hashlib
import time

BASE_URL='https://api1.zg.com'
formdata_headers={
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
}

headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
}

def get_tickers():
    ''' 获取交易所市场数据'''
    url = BASE_URL + '/tickers'
    response=requests.get(url,headers=headers)
    return response.text

def get_depth(symbol , size):
    '''深度 '''
    url = BASE_URL + '/depth'
    data={
        "symbol":symbol,
        "size":size
    }
    response=requests.get(url , data, headers=headers)
    return response.text

def get_kline(symbol , size , type):
    '''获得k线图'''

    url=BASE_URL+'/kline'
    data={
        'symbol':symbol,
        'size':size,
        'type':type
    }
    print(url)
    response=requests.get(url, data,headers= headers)
    return response.text

def get_trades(symbol , size):
    '''获取最新成交记录'''
    url=BASE_URL+ '/trades'
    data={
        "symbol":symbol,
        "size":size
    }
    response=requests.get(url, data,headers= headers)
    return response.text


def get_exchangeInfo():
    '''获得交易对信息'''
    url=BASE_URL+'/exchangeInfo'
    response=requests.get(url)
    return response.text

def get_private_uesr(api_key , secret_key):
    url=BASE_URL + '/private/user'
    params=dict()
    params['api_key'] = api_key
    params['sign'] = build_zg_sign(params, secret_key)

    response = requests.post(url,data= params,headers= formdata_headers)
    return response.text

def get_trade_limit(api_key , market , side , amount , trade_type , secret_key):
    #限价交易
    url = BASE_URL + '/private/trade/limit'
    params=dict()
    params['api_key'] = api_key
    params['market'] = market
    params['side'] = side
    params['amount'] = amount
    params['price'] = trade_type
    params['sign'] = build_zg_sign(params, secret_key)
    response = requests.post(url, data= params, headers= formdata_headers)
    return response.text

def private_trade_market(api_key , market , side , amount , secret_key):
    #市价交易
    url = BASE_URL + '/private/trade/market'
    params=dict()
    params['api_key'] = api_key
    params['market'] = market
    params['side'] = side
    params['amount'] = amount
    params['sign'] = build_zg_sign(params, secret_key)
    response = requests.post(url, data= params, headers= formdata_headers)
    return response.text

def private_trade_cancel(api_key , market , order_id , secret_key):
    #取消交易
    url = BASE_URL + '/private/trade/cancel'
    params=dict()
    params['api_key'] = api_key
    params['market'] = market
    params['order_id'] = order_id
    params['sign'] = build_zg_sign(params , secret_key)
    response = requests.post(url, data= params, headers= formdata_headers)
    return response.text

def private_order_deals(api_key , market , order_id , offset , limit , secret_key):
    #查询成交明细
    url = BASE_URL + '/private/order/deals '
    params=dict()
    params['api_key'] = api_key
    params['market'] = market
    params['order_id'] = order_id
    params['offset']= offset
    params['limit']= limit
    params['sign'] = build_zg_sign(params, secret_key)
    response = requests.post(url, data= params, headers= formdata_headers)
    return response.text

def private_order_pending(api_key , market , order_id , offset , limit , secret_key):
    #查询未成交订单（包括成交部分）
    url = BASE_URL + '/private/order/pending '
    params=dict()
    params['api_key'] = api_key
    params['market'] = market
    params['order_id'] = order_id
    params['offset']= offset
    params['limit']= limit
    params['sign'] = build_zg_sign(params, secret_key)
    response = requests.post(url, data= params, headers= formdata_headers)
    return response.text

def private_order_finished(amount,ctime,deal_fee,deal_money,deal_stock,id,left,maker_fee,market,ftime,taker_fee,type,user,secret_key):
    #查询已成交订单
    url = BASE_URL + '/private/order/pending'

    params=dict()
    params['amount'] = amount
    params['ctime'] = ctime
    params['deal_fee'] = deal_fee
    params['deal_money']= deal_money
    params['deal_stock']= deal_stock
    params['id'] = id
    params['left'] = left
    params['maker_fee'] = maker_fee
    params['market'] = market
    params['ftime'] = ftime
    params['taker_fee'] = taker_fee
    params['type'] = type
    params['user'] = user
    params['sign'] = build_zg_sign(params , secret_key)
    response = requests.post(url, data= params, headers= formdata_headers)
    return response.text


def build_zg_sign(params , secret_key):
    """
    加签方法
    :param params:
    :param secret_key:
    :return:
    """
    sign = ''
    for key in sorted(params.keys()):
        sign += key + '=' + str(params[key]) +'&'
    s = sign + 'secret_key=' + secret_key
    m = hashlib.md5()
    b = s.encode()
    m.update(b)
    return m.hexdigest().upper()


if __name__ == '__main__':
    #print(get_tickers())
    #print(get_depth("BTC_CNZ",10))
    #print(get_exchangeInfo())
    #print(get_kline('BTC_CNZ',5,'1min'))
    # print(get_trades("BTC_CNZ",5))
