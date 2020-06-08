#!/bin/bash

value="default"
handler="default"
DONE="false"

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

read_choices() {
    echo " "
    echo "Please input one of the following values"
    echo "Twitter = t"
    echo "Facebook = f"
    echo "Tik Tok (User Info) = c"
    echo "Tik Tok (Download Video) = cd" 
}

is_done() {
    echo ""
    echo "Would you like to run another OSINT Scan? (y/n)" 
    DONE2="false"
    while [ $DONE2 == "false" ];
    do
        read input

        case $input in
        y)
            read_choices
            DONE2="true"
            ;;
        n)
            DONE="true"
            DONE2="true"
            ;;
        *)
            echo "Invalid Parameter, Please Input y or n"
    esac
    done
}
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
read_choices

while [ "$DONE" == "false" ];
do
    read value

    case $value in
    t)
        run_twitter
        python ./modules/twitter/twitter_module.py $handler
        is_done
        ;;
    f)
        run_fb
        $(cd /home/osint/Desktop/scrounger/modules/facebook && python3.7 scraper.py)
        wait
        $(cd /home/osint/Desktop/scrounger/modules/facebook && cp -R data/. "/home/osint/Desktop/OSINT_OUTPUT/Facebook")
        wait
        $(cd /home/osint/Desktop/scrounger/modules/facebook/data && rm -rf *)
        is_done
        ;;
    c)
        mkdir -p "/home/osint/Desktop/OSINT_OUTPUT/TikTok/UserProfiles"
        run_tiktok
        python3.7 ./modules/tiktok_user_info/tiktok_module.py --username "$handler"
        wait
        cp -R "@$handler" "/home/osint/Desktop/OSINT_OUTPUT/TikTok/UserProfiles"
        wait
        rm -rf "@$handler"
        is_done
        ;;
    cd)
        python3.7 ./modules/tiktok/run.py
        wait
        cp -R "videos/" "/home/osint/Desktop/OSINT_OUTPUT/TikTok"
        wait
        rm -rf "videos/"
        is_done
        ;;
    *)
        echo "Invalid Parameter"
        is_done
        ;;
    esac
done

./generate_report.sh

exit 0