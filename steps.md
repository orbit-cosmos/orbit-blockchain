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
 ./build/bin/geth --bootnodes enode://eb423fe1c2383c01dd7342c4606239b6e15f979f183326c777ccccb12320f184f68df6d7784c153553c4092412b65477b28adc7da575f351acf7affc33016369@127.0.0.1:30305 --http --http.addr 0.0.0.0 --http.port 8545 --http.corsdomain "*" --http.api eth,net,web3,personal --networkid=271997 --datadir ./node1 --password ./node1/password.txt --port 30304  --authrpc.port 8551 --miner.etherbase=0x6f2be83aa9179e71dada3e94b274e9dbf10e4702 --mine --unlock 0x6f2be83aa9179e71dada3e94b274e9dbf10e4702 -allow-insecure-unlock 



## start node2
./build/bin/geth --bootnodes enode://eb423fe1c2383c01dd7342c4606239b6e15f979f183326c777ccccb12320f184f68df6d7784c153553c4092412b65477b28adc7da575f351acf7affc33016369@192.168.18.39:30305  --networkid=271997 --datadir ./node2 --unlock 0x848a7752A170da237126D53dC16454B29F505aaF --password ./node2/password.txt --port 30307  --authrpc.port 8552

## connect to geth JavaScript console
./build/bin/geth attach ./node1/geth.ipc      




## protact key using clef
1. clef --keystore ./ddir/keystore --configdir ./clef --chainid 271997 --suppress-bootwarn init

2. clef --keystore ./ddir/keystore --configdir ./clef --chainid 271997 --suppress-bootwarn setpw 0xB02aDdbbc1fCACd3abB30513A3E552f6469EE7D4   

3. clef --keystore ./ddir/keystore --configdir ./clef --chainid 271997 --suppress-bootwarn



## send tx
eth.sendTransaction({from:"0x6f2be83aa9179e71dada3e94b274e9dbf10e4702",to:"0xFD01A2868caACaceB32636fa8A7391f732689Ef9",value:50000000000})
## check balance
web3.fromWei(eth.getBalance("0xb420eA2C43AcabbA17881E49957731B53fc2a5fd"))