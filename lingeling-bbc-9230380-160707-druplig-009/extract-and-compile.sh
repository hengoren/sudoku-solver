#!/bin/sh
unzip druplig-009.zip
mv druplig-009 druplig
cd druplig
./configure.sh
make
cd ..
tar xf lingeling-bbc-9230380-160707.tar.gz
mv lingeling-bbc-9230380-160707 lingeling
cd lingeling
./configure.sh
make
