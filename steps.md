## generate new account
- ./build/bin/geth account new --datadir ./node1 
- ./build/bin/geth account new --datadir ./node2 
## initialize genesis block
- ./build/bin/geth --datadir ./node1 init ./genesis.json   
- ./build/bin/geth --datadir ./node2 init ./genesis.json   


## generate bootnode privatekey
bootnode -genkey boot.key

## run bootnode
bootnode --nodekey boot.key 



## start node1
./build/bin/geth --bootnodes "enode://672267382b4ae546a471b5cf3984e91e7024b8d46a67788fc3d898bf7528a4b001fa9a5887b32088086d16f74fa4ebc09cb557ac33015efd6a5fed4b2faccc7b@127.0.0.1:0?discport=30301"  --networkid=271997 --datadir ./node1  --miner.etherbase=0xb420eA2C43AcabbA17881E49957731B53fc2a5fd --mine --unlock 0xb420eA2C43AcabbA17881E49957731B53fc2a5fd --password ./node1/password.txt --port 30304  --authrpc.port 8551



## start node2
./build/bin/geth --bootnodes "enode://672267382b4ae546a471b5cf3984e91e7024b8d46a67788fc3d898bf7528a4b001fa9a5887b32088086d16f74fa4ebc09cb557ac33015efd6a5fed4b2faccc7b@127.0.0.1:0?discport=30301"  --networkid=271997 --datadir ./node2  --miner.etherbase=0xafdd5d4be7b2c76471127ac6036c27f2fe1dc558 --mine --unlock 0xafdd5d4be7b2c76471127ac6036c27f2fe1dc558 --password ./node2/password.txt --port 30305  --authrpc.port 8552

## connect to geth JavaScript console
./build/bin/geth attach ./node2/geth.ipc      




## protact key using clef
1. clef --keystore ./ddir/keystore --configdir ./clef --chainid 271997 --suppress-bootwarn init

2. clef --keystore ./ddir/keystore --configdir ./clef --chainid 271997 --suppress-bootwarn setpw 0xB02aDdbbc1fCACd3abB30513A3E552f6469EE7D4   

3. clef --keystore ./ddir/keystore --configdir ./clef --chainid 271997 --suppress-bootwarn



## send tx
eth.sendTransaction({from:"0xb420eA2C43AcabbA17881E49957731B53fc2a5fd",to:"0xafdd5d4be7b2c76471127ac6036c27f2fe1dc558",value:0x1b1ae4d6e2ef500000})
## check balance
web3.fromWei(eth.getBalance("0xb420eA2C43AcabbA17881E49957731B53fc2a5fd"))