import logging
import sys
import time

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


class BlockChain(object):

    def __init__(self):
        self.transaction_pool = []
        self.chain = []
        self.create_block(0, 'init hash')
    
    def create_block(self, nonce, previous_hash):
        block = {
            'timestamp': time.time(),
            'transactions': self.transaction_pool,
            'nonce': nonce,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        self.transaction_pool = []
        return block

def pprint(chains):
    for i, chain in enumerate(chains):
        print(f'{"="*25} chain {i} {"="*25}')
        for k, v in chain.items():
            print(f'{k:25}{v}')
    print(f'{"*"*25}')

if __name__ == '__main__':
    blockchain = BlockChain()
    pprint(blockchain.chain)
    blockchain.create_block(5, 'hash 1')
    pprint(blockchain.chain)
    blockchain.create_block(2, 'hash 2')
    pprint(blockchain.chain)
