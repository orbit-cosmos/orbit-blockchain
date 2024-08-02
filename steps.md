## generate new account
 `./build/bin/geth account new --datadir ./node1` 
 `./build/bin/geth account new --datadir ./node2 `
 
## initialize genesis block
 `./build/bin/geth --datadir ./node1 init ./genesis.json`
 `./build/bin/geth --datadir ./node2 init ./genesis.json`


## generate bootnode privatekey
`bootnode -genkey boot.key`

## run bootnode
`bootnode --nodekey boot.key -addr :30305 --verbosity=3`



## start node1 as miner
 `./build/bin/geth --bootnodes enode://f8a176b9bc1c75759762802db9e9a82e13e2ee631bc833e8b9c728cde00f1dfd284a6c7954909382fd4c9cad42a0274073b74de26e2efd1ceaa5ae6bd9700f44@192.168.18.39:30305 --http --http.addr 0.0.0.0 --http.port 8545 --http.corsdomain "*" --http.api eth,net,web3,personal --networkid=271997 --datadir ./node1 --password ./node1/password.txt --port 30304  --authrpc.port 8551 --miner.etherbase=0x6f2be83aa9179e71dada3e94b274e9dbf10e4702 --mine --unlock 0x6f2be83aa9179e71dada3e94b274e9dbf10e4702 -allow-insecure-unlock `



## start node2
 `./build/bin/geth --bootnodes enode://eb423fe1c2383c01dd7342c4606239b6e15f979f183326c777ccccb12320f184f68df6d7784c153553c4092412b65477b28adc7da575f351acf7affc33016369@192.168.18.39:30305 --http --http.addr 0.0.0.0 --http.port 8545 --http.corsdomain "*" --http.api eth,net,web3,personal --networkid=271997 --datadir ./node1 --password ./node1/password.txt --port 30306  --authrpc.port 8552 --unlock 0xb420ea2c43acabba17881e49957731b53fc2a5fd -allow-insecure-unlock`

## connect to geth JavaScript console
`./build/bin/geth attach ./node1/geth.ipc   `   


## send tx
`eth.sendTransaction({from:eth.accounts[0],to:"0xFD01A2868caACaceB32636fa8A7391f732689Ef9",value:wev3.toWei("50000000000")})`
## check balance
`web3.fromWei(eth.getBalance("0xb420eA2C43AcabbA17881E49957731B53fc2a5fd"))`



## rpc url
`http://127.0.0.1:8545`



## check signer in console
`clique.getSigners()`

## check node info in console
`admin.nodeInfo`

`admin.peers`