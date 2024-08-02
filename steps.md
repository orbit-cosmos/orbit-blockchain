## generate new account
- ./build/bin/geth account new --datadir ./node1 
- ./build/bin/geth account new --datadir ./node2 
## initialize genesis block
- ./build/bin/geth --datadir ./node1 init ./genesis.json   
- ./build/bin/geth --datadir ./node2 init ./genesis.json   


## generate bootnode privatekey
bootnode -genkey boot.key

## run bootnode
bootnode --nodekey boot.key -addr :30305 --verbosity=3



## start node1
 ./build/bin/geth --bootnodes enode://f8a176b9bc1c75759762802db9e9a82e13e2ee631bc833e8b9c728cde00f1dfd284a6c7954909382fd4c9cad42a0274073b74de26e2efd1ceaa5ae6bd9700f44@192.168.18.39:30305 --http --http.addr 0.0.0.0 --http.port 8545 --http.corsdomain "*" --http.api eth,net,web3,personal --networkid=271997 --datadir ./node1 --password ./node1/password.txt --port 30304  --authrpc.port 8551 --miner.etherbase=0x6f2be83aa9179e71dada3e94b274e9dbf10e4702 --mine --unlock 0x6f2be83aa9179e71dada3e94b274e9dbf10e4702 -allow-insecure-unlock 



## start node2
 ./build/bin/geth --bootnodes enode://672267382b4ae546a471b5cf3984e91e7024b8d46a67788fc3d898bf7528a4b001fa9a5887b32088086d16f74fa4ebc09cb557ac33015efd6a5fed4b2faccc7b@192.168.18.16:30305 --http --http.addr 0.0.0.0 --http.port 8545 --http.corsdomain "*" --http.api eth,net,web3,personal --networkid=271997 --datadir ./node1 --signer ./clef/clef.ipc --port 30306  --authrpc.port 8552 --unlock 0xb420ea2c43acabba17881e49957731b53fc2a5fd -allow-insecure-unlock

## connect to geth JavaScript console
./build/bin/geth attach ./node1/geth.ipc      




## protact key using clef

1. clef --keystore ./ddir/keystore --configdir ./clef --chainid 271997 --suppress-bootwarn init

2. clef --keystore ./ddir/keystore --configdir ./clef --chainid 271997 --suppress-bootwarn setpw 0xB02aDdbbc1fCACd3abB30513A3E552f6469EE7D4   

3. clef --keystore ./ddir/keystore --configdir ./clef --chainid 271997 --suppress-bootwarn
4. clef --keystore ./node1/keystore --configdir ./clef --chainid 271997 --suppress-bootwarn --rules ./rules.js
5.  clef --keystore ./node1/keystore --configdir ./clef --chainid 271997 --suppress-bootwarn  attest  `sha256sum rules.js | cut -f1`



## send tx
eth.sendTransaction({from:"0x6f2be83aa9179e71dada3e94b274e9dbf10e4702",to:"0xFD01A2868caACaceB32636fa8A7391f732689Ef9",value:50000000000})
## check balance
web3.fromWei(eth.getBalance("0xb420eA2C43AcabbA17881E49957731B53fc2a5fd"))




## check signer in console
clique.getSigners()

## check node info in console
admin.nodeInfo

admin.peers