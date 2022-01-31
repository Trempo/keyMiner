import random
import blocksmith
import requests
import time

while(True):
    kg = blocksmith.KeyGenerator()
    kg.seed_input('You Cant Teach an Old Dog New Tricks')
    key = kg.generate_key()
    address = blocksmith.EthereumWallet.generate_address(key)
    apirequest = 'https://api.etherscan.io/api?module=account&action=balance&address={}&tag=latest&apikey=FISZWYFX8X26K4XCHYQPC2D7VVT841IY2J'.format(address)
    r = requests.get(apirequest)

    print('Key: {} - {}'.format(key, r.json()['result']!="0"))

    if(r.json()['result']!='0'):
        print('Found a key: {} with {}'.format(key, r.json()['result']))
        f = open('key.txt', 'a')
        f.write("key: {} - Address: {}".format(key, address))
        f.close()
    else:
        time.sleep(0.01)

