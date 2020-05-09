#!/bin/bash

value= default
handler= default

get_handler() {
    echo "You have chose Twitter Module, please input a handler"
    read handler
}

run_fb() {
    echo "You have selected the Facebook module"
    echo "Please give us the person's facebook link that you want to search"
    read handler
    echo $handler > ./modules/facebook/input.txt

}

run_tik() {
    echo "You have selected the Tik Tok Module"
    echo "Please input a username"
    read handler
}

echo "please input one of the following values"
echo "Twitter = t"
echo "Facebook = f"
echo "Tik Tok = k"

read value

case $value in
t)
    get_handler
    python ./modules/twitter/twitter_module.py $handler
    exit 0
    ;;
f)
    run_fb
    #python3.7 ./modules/facebook/scraper.py
    $(cd /home/osint/Desktop/workstation/scrounger/modules/facebook && python3.7 scraper.py)
    exit 0
    ;;
k)
    run_tik
    python3.7 ./modules/tiktok/tiktok_module.py --username $handler --download
    exit 0
    ;;
*)
    echo "Invalid Parameter"
    exit 0
    ;;
esac