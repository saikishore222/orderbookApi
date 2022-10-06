import json
from flask import Flask,request
from pyserum.connection import conn
from pyserum.market import Market
from pyserum.connection import get_live_markets, get_token_mints
app = Flask(__name__)
@app.route('/order', methods=['GET'])
def search():
    args = request.args
    add = args.get('add')
    orderType=args.get('type')
    cc = conn("https://api.mainnet-beta.solana.com/")
    l=[]
    market_address = add # Address for BTC/USDC
    # Load the given market
    market = Market.load(cc, market_address)
    if(type=='ask'):
        asks = market.load_asks()
        # Show all current ask order
        for ask in asks:
            ask1={"order_id":ask.order_id,"price":ask.info.price,"size":ask.info.size}
            l.append(ask1)
    else:
        # Show all current bid order
        bids = market.load_bids()
        for bid in bids:
            bid1={"order_id":bid.order_id,"price":bid.info.price,"size":bid.info.size}
            l.append(bid1)
    return l 
app.run()
