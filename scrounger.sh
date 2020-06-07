#!/bin/bash

value= default
handler= default

cat ./banner

###-------------------------------------------------------###
### Gets the Handlers for the various social media sights ###
###-------------------------------------------------------###
run_twitter() {
    echo "You have chose Twitter Module, please input a handler"
    read handler
}

run_fb() {
    echo "You have selected the Facebook module"
    echo "Please give us the person's facebook handler that you want to search"
    read handler
    echo "https://www.facebook.com/$handler" > ./modules/facebook/input.txt

}

run_tiktok() {
    echo "You have selected the Tik Tok Module"
    echo "Please input a username"
    read handler
}

echo " "
echo "Please input one of the following values"
echo "Twitter = t"
echo "Facebook = f"
echo "Tik Tok = c" ### tiktok info collecttor 
# tiktok video donwloader


###-------------------------------------------------------###
###    Checks to make sure all the output directories are ###
###       created, if they aren't it will make them       ### 
###-------------------------------------------------------###
mkdir -p "/home/osint/Desktop/OSINT_OUTPUT/"
mkdir -p "/home/osint/Desktop/OSINT_OUTPUT/Twitter"
mkdir -p "/home/osint/Desktop/OSINT_OUTPUT/Facebook"
mkdir -p "/home/osint/Desktop/OSINT_OUTPUT/TikTok"


###-------------------------------------------------------###
###    Decides which social media module will be opened   ###
###-------------------------------------------------------###
read value


case $value in
t)
    run_twitter
    python ./modules/twitter/twitter_module.py $handler
    exit 0
    ;;
f)
    run_fb
    $(cd /home/osint/Desktop/scrounger/modules/facebook && python3.7 scraper.py)
    wait
    $(cd /home/osint/Desktop/scrounger/modules/facebook && cp -R data/. "/home/osint/Desktop/OSINT_OUTPUT/Facebook")
    wait
    $(cd /home/osint/Desktop/scrounger/modules/facebook/data && rm -rf *)
    exit 0
    ;;
c)
    run_tiktok
    python3.7 ./modules/tiktok/run.py
    wait
    cp -R "@$handler" "/home/osint/Desktop/OSINT_OUTPUT/TikTok"
    wait
    rm -rf "@$handler"
    exit 0
    ;;
*)
    echo "Invalid Parameter"
    exit 0
    ;;
esac
