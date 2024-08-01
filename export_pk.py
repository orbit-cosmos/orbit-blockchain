from web3.auto import w3 
with open("/home/qulzam/Orbit-Cosmos/orbit-blockchain/node1/keystore/UTC--2024-07-24T11-51-42.706451302Z--6f2be83aa9179e71dada3e94b274e9dbf10e4702") as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(encrypted_key,'1234')


import binascii
print("pk------------------")
print(binascii.b2a_hex(private_key))