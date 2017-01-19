#!/bin/sh
rm -rf yalsat*
unzip ../archives/yalsat*
mv yalsat* yalsat
cd yalsat
./configure.sh
make libyals.a
cd ..
rm -rf lingeling*
tar xf ../archives/lingeling*
mv lingeling* lingeling
cd lingeling
./configure.sh
make treengeling
install -s treengeling ../../bin/
