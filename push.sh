#!/bin/bash

fecha=`date +%F`
git status
git add .
git commit -am "'$fecha'"
git status
echo -n "quieres subir Enter: "
read var
git push
