#!/bin/bash

VERSION=0.0.0
# VERSION=$1
DIR=havoc-${VERSION}

git clone git@github.com:ii8/havoc.git  $DIR
# pushd $DIR
# git checkout tags/$VERSION
# popd
tar -cJvf ${DIR}.tar.xz $DIR
rm -rf $DIR

