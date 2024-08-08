## generate new account
`./build/bin/geth account new --datadir ./my-bootnode `
` ./build/bin/geth account new --datadir ./node1 `
` ./build/bin/geth account new --datadir ./node2 `

## initialize genesis block
` ./build/bin/geth --datadir ./my-bootnode init ./genesis.json   `
` ./build/bin/geth --datadir ./node1 init ./genesis.json   `
` ./build/bin/geth --datadir ./node2 init ./genesis.json   `

## protact key using clef

1. `clef --keystore ./node1/keystore --configdir ./clef --chainid 271997 --suppress-bootwarn init`

2. `clef --keystore ./node1/keystore --configdir ./clef --chainid 271997 --suppress-bootwarn setpw 0xB02aDdbbc1fCACd3abB30513A3E552f6469EE7D4   `

3. ``clef --keystore ./node1/keystore --configdir ./clef --chainid 271997 --suppress-bootwarn  attest  `sha256sum rules.js | cut -f1`
``
4. `clef --keystore ./node1/keystore --configdir ./clef --chainid 271997 --suppress-bootwarn --rules ./rules.js`



## run bootnode
`./build/bin/geth --networkid=271997 --datadir ./my-bootnode --port 30305 --authrpc.port 8553`



## start node1 as miner
 `./build/bin/geth --bootnodes enode://0670b8ff1b596a7bddf0e03b1afe6e8d423057591cb58b400c86a77b55e929441d894394269609ad7a1ff8526a7ad53e99b9ef560255b3313c1aaf2631cd7127@192.168.18.16:30305 --http --http.addr 0.0.0.0 --http.port 8545 --http.corsdomain "*" --http.api eth,net,web3,personal --networkid=271997 --datadir ./node1 --signer ./clef/clef.ipc --port 30304  --authrpc.port 8551 --miner.etherbase=0xb420ea2c43acabba17881e49957731b53fc2a5fd --mine --unlock 0xb420ea2c43acabba17881e49957731b53fc2a5fd -allow-insecure-unlock `



## start node2
 `./build/bin/geth --bootnodes enode://672267382b4ae546a471b5cf3984e91e7024b8d46a67788fc3d898bf7528a4b001fa9a5887b32088086d16f74fa4ebc09cb557ac33015efd6a5fed4b2faccc7b@192.168.18.16:30305 --http --http.addr 0.0.0.0 --http.port 8545 --http.corsdomain "*" --http.api eth,net,web3,personal --networkid=271997 --datadir ./node1 --signer ./clef/clef.ipc --port 30306  --authrpc.port 8552 --unlock 0x6f2be83aa9179e71dada3e94b274e9dbf10e4702 -allow-insecure-unlock`


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