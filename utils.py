from web3 import Web3, HTTPProvider
from solc import compile_source
import requests
import json
import io
from google.cloud import vision
from google.cloud.vision import types
from eth_utils import keccak

contract_source = 'publicregister/contracts/contracts/PublicRegister.sol'
web3 = Web3(HTTPProvider('http://localhost:8545'))
cs = compile_source(open(contract_source).read())['<stdin>:PublicRegister']

PublicRegister = web3.eth.contract(abi=cs['abi'],
                                   bytecode=cs['bin'],
                                   bytecode_runtime=cs['bin-runtime'])

testrpc = 'http://localhost:8545'

def deploy_contract():
    tx_hash = PublicRegister.deploy(transaction={
        'from':web3.eth.accounts[0], 'gas': 4000000})
    tx_receipt = web3.eth.getTransactionReceipt(tx_hash)
    address = tx_receipt['contractAddress'] 
    with open('address', 'w') as fout:
        fout.write(address)
    return address


def add_entry(entry):
    hash_ = keccak(entry.encode('utf-8'))
    key = hash_ # for now
    with open('address') as fin:
        address = fin.read()
        register = PublicRegister(address)
        return register.transact(transaction={
            'from': web3.eth.accounts[0], 'gas': 2 * 10 ** 5}).add(
                key, hash_)

def verify_entry(entry):
    hash_ = keccak(entry.encode('utf-8'))
    key = hash_ # for now
    with open('address') as fin:
        address = fin.read()
        register = PublicRegister(address)
        value = register.call().get(key)
        return hash_.decode('iso-8859-1') == value

def get_register():
    with open('address') as fin:
        address = fin.read()
        return PublicRegister(address)

def mine_block():
    requests.post(testrpc,
        data=json.dumps({'jsonrpc': "2.0", 'method': "evm_mine", 
                        'params': [], 'id': 0}))


def detect_text(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    s = '\n'.join([text.description for text in texts])
    return s
