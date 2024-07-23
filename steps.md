./build/bin/geth account new --datadir ./ddir 

./build/bin/geth --datadir ./ddir/ init ./genesis.json     

clef --keystore ./ddir/keystore --configdir ./clef --chainid 271997 --suppress-bootwarn init

clef --keystore ./ddir/keystore --configdir ./clef --chainid 271997 --suppress-bootwarn setpw 0xB02aDdbbc1fCACd3abB30513A3E552f6469EE7D4   

clef --keystore ./ddir/keystore --configdir ./clef --chainid 271997 --suppress-bootwarn


./build/bin/geth --datadir ./ddir --port 30306 --bootnodes "enode://5eebef2f74d1f780de6dab711d34af8631a5ff464392f677adb29e7c8ad7aae20ab34afd842b4f9125b692ba815f73e9389ae11dc5ada205212d4a1527ea7e98@127.0.0.1:0?discport=30305" --networkid 271997 --unlock 0xB02aDdbbc1fCACd3abB30513A3E552f6469EE7D4 --password password.txt --authrpc.port 8551 --mine --miner.etherbase 0xB02aDdbbc1fCACd3abB30513A3E552f6469EE7D4