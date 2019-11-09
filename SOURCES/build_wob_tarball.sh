#!/bin/bash

VERSION=$1
DIR=wob-${VERSION}

git clone --recursive git@github.com:francma/wob.git $DIR
pushd $DIR
git checkout tags/$VERSION
popd
tar cvjpf ${DIR}.tar.bz2 $DIR
rm -rf $DIR

