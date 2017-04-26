#!/bin/bash

fecha=`date +%F`
git status
git add .
git status
echo -n "Esto se subira Enter: "
read var
git commit -am "'$fecha'"
git status
echo -n "quieres subir Enter: "
read var
git push
