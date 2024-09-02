## Go implementation of (POA) Orbit Chain

Official Golang  implementation of the Orbit Chain.

## Building the source
```shell
make geth
```

or, to build the full suite of utilities:

```shell
make all
```


### Hardware Requirements

Minimum:

* CPU with 2+ cores
* 4GB RAM
* 1TB free storage space to sync the Mainnet
* 8 MBit/sec download Internet service

Recommended:

* Fast CPU with 4+ cores
* 16GB+ RAM
* High-performance SSD with at least 1TB of free space
* 25+ MBit/sec download Internet service


## generate new account
`./build/bin/geth account new --datadir ./my-bootnode `
` ./build/bin/geth account new --datadir ./node1 `
` ./build/bin/geth account new --datadir ./node2 `


## Defining the genesis state

First, you'll need to create the genesis state of your networks, which all nodes need to be
aware of and agree upon. This consists of a small JSON file (e.g. call it `genesis.json`)

Note:
extraData: This is normally optional, but mandatory with clique! It configures the network and enables signers. It contains three parts, lets break it down:

32 bytes vanity data. That means you can put into the first 32 bytes whatever you want. In our case its all zeros
0x0000000000000000000000000000000000000000000000000000000000000000
The concatenated addresses from the sealers of the clique network. It's written as hex-string without the "0x" at the beginning. It must be a multiple of 20 bytes
0001fcd01073fe6017920a97cc384bee72c98beb
0002f7067c48ef957b21009685ab69ee768e38bd
The last part is a 65 bytes proposer seal, which is 65 bytes long (or 130 characters), in hex notation without the 0x. It's all zeroes in the genesis block because there are no proposers yet.
0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
You can read more about it in EIP-650
All combined is 0x00000000000000000000000000000000000000000000000000000000000000000001fcd01073fe6017920a97cc384bee72c98beb0002f7067c48ef957b21009685ab69ee768e38bd0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

```json
{
    "config": {
        "chainId": 271997,
        "homesteadBlock": 0,
        "eip150Block": 0,
        "eip155Block": 0,
        "eip158Block": 0,
        "byzantiumBlock": 0,
        "constantinopleBlock": 0,
        "petersburgBlock": 0,
        "istanbulBlock": 0,
        "berlinBlock": 0,
        "clique": {
            "period": 3,
            "epoch": 30000
        }
    },
    
    "timestamp": "0x00",
    "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "extraData": "0x0000000000000000000000000000000000000000000000000000000000000000b420ea2c43acabba17881e49957731b53fc2a5fd0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "difficulty":"0x000000",
    "gasLimit": "0x1c9c380",
    "nonce":"0x0000000000000042",
    "coinbase": "0x0000000000000000000000000000000000000000",
    "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "alloc": {
        "0x6f2be83aa9179e71dada3e94b274e9dbf10e4702": {
            "balance": "0x3635c9adc5dea00000"
        },
        "0xb420ea2c43acabba17881e49957731b53fc2a5fd": {
            "balance": "0x3635c9adc5dea00000"
        }
    },
     "feePerTx":"",
    "proposedFee":"",
    "votes":""
}
```

With the genesis state defined in the above JSON file, you'll need to initialize **every**
`geth` node with it prior to starting it up to ensure all blockchain parameters are correctly
set:



HTTP based JSON-RPC API options:

  * `--http` Enable the HTTP-RPC server
  * `--http.addr` HTTP-RPC server listening interface (default: `localhost`)
  * `--http.port` HTTP-RPC server listening port (default: `8545`)
  * `--http.api` API's offered over the HTTP-RPC interface (default: `eth,net,web3`)
  * `--http.corsdomain` Comma separated list of domains from which to accept cross origin requests (browser enforced)
  * `--ws` Enable the WS-RPC server
  * `--ws.addr` WS-RPC server listening interface (default: `localhost`)
  * `--ws.port` WS-RPC server listening port (default: `8546`)
  * `--ws.api` API's offered over the WS-RPC interface (default: `eth,net,web3`)
  * `--ws.origins` Origins from which to accept WebSocket requests
  * `--ipcdisable` Disable the IPC-RPC server
  * `--ipcapi` API's offered over the IPC-RPC interface (default: `admin,debug,eth,miner,net,personal,txpool,web3`)
  * `--ipcpath` Filename for IPC socket/pipe within the datadir (explicit paths escape it)


## initialize genesis block
` ./build/bin/geth --datadir ./my-bootnode init ./genesis.json   `
` ./build/bin/geth --datadir ./node1 init ./genesis.json   `
` ./build/bin/geth --datadir ./node2 init ./genesis.json   `

## protact key using clef

1. `clef --keystore ./node1/keystore --configdir ./clef-node1 --chainid 271997 --suppress-bootwarn init`

2. `clef --keystore ./node1/keystore --configdir ./clef-node1 --chainid 271997 --suppress-bootwarn setpw 0xB02aDdbbc1fCACd3abB30513A3E552f6469EE7D4   `

3. ``clef --keystore ./node1/keystore --configdir ./clef-node1 --chainid 271997 --suppress-bootwarn  attest  `sha256sum rules.js | cut -f1`
``
4. `clef --keystore ./node1/keystore --configdir ./clef-node1 --chainid 271997 --suppress-bootwarn --rules ./rules.js`




#### Creating the rendezvous point

With all nodes that you want to run initialized to the desired genesis state, you'll need to
start a bootstrap node that others can use to find each other in your network and/or over
the internet. The clean way is to configure and run a dedicated bootnode:

```shell
$ bootnode --genkey=boot.key
$ bootnode --nodekey boot.key -addr :30305 --verbosity=3
```

*Note: You could also use a full-fledged `geth` node as a bootnode, but it's the less
recommended way for development deployments. We recommend using a regular node as bootstrap node for production deployments.*

## run bootnode as regular geth node
`./build/bin/geth --networkid=271997 --datadir ./my-bootnode --port 30305 --authrpc.port 8553`



## start node1 as miner
 `./build/bin/geth --bootnodes enode://0670b8ff1b596a7bddf0e03b1afe6e8d423057591cb58b400c86a77b55e929441d894394269609ad7a1ff8526a7ad53e99b9ef560255b3313c1aaf2631cd7127@192.168.18.16:30305 --http --http.addr 0.0.0.0 --http.port 8545 --http.corsdomain "*" --http.api eth,net,web3,personal --networkid=271997 --datadir ./node1 --signer ./clef/clef.ipc --port 30304  --authrpc.port 8551 --miner.etherbase=0xb420ea2c43acabba17881e49957731b53fc2a5fd --mine --unlock 0xb420ea2c43acabba17881e49957731b53fc2a5fd -allow-insecure-unlock `



## start node2
 `./build/bin/geth --bootnodes enode://672267382b4ae546a471b5cf3984e91e7024b8d46a67788fc3d898bf7528a4b001fa9a5887b32088086d16f74fa4ebc09cb557ac33015efd6a5fed4b2faccc7b@192.168.18.16:30305 --http --http.addr 0.0.0.0 --http.port 8545 --http.corsdomain "*" --http.api eth,net,web3,personal --networkid=271997 --datadir ./node1 --signer ./clef/clef.ipc --port 30306  --authrpc.port 8552 --miner.etherbase=0xeF008F3ECE189110d25cBeAbE3fE7183E767fF80 --mine --unlock 0xeF008F3ECE189110d25cBeAbE3fE7183E767fF80 -allow-insecure-unlock`


## connect to geth JavaScript console
`./build/bin/geth attach ./node1/geth.ipc   `   


## send tx
`eth.sendTransaction({from:eth.accounts[0],to:"0xFD01A2868caACaceB32636fa8A7391f732689Ef9",value:web3.toWei("50000000000")})`
## check balance
`web3.fromWei(eth.getBalance("0xb420eA2C43AcabbA17881E49957731B53fc2a5fd"))`



## rpc url
`http://127.0.0.1:8545`


## check signer in console
`clique.getSigners()`

## check node info in console
`admin.nodeInfo`

`admin.peers`


## References

https://ethereum-blockchain-developer.com/123-geth-clique-blockscout/00-overview/