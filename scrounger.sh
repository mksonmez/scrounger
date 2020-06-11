#!/bin/bash

value="default"
handler="default"
DONE="false"
DIR_LOC=$(pwd)

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

set_fb_pass() {
    if test -f "modules/facebook/credentials.yaml"; then
        rm "modules/facebook/credentials.yaml"
    fi
    echo "Enter your Facebook Email"
    read -p "Email: " handler
    echo "email: $handler" >> "modules/facebook/credentials.yaml"
    echo "Enter your Facebook Password"
    read -p "Password: " handler
    echo "password: $handler" >> "modules/facebook/credentials.yaml"
}

read_choices() {
    echo " "
    echo "Please input one of the following values"
    echo "Twitter = t"
    echo "Facebook = f"
    echo "Tik Tok (User Info) = c"
    echo "Tik Tok (Download Video) = cd"
    echo "-----------------------------------------"
    echo "Miscellaneous Settings: "
    echo "Facebook Credentials = fbp"
    echo ""
}

is_done() {
    echo ""
    echo "Would you like to run another OSINT Scan?" 
    DONE2="false"
    while [ $DONE2 == "false" ];
    do
        read -p "Yes or No? [y/n]: " input

        case $input in
        y|Y|yes|Yes)
            read_choices
            DONE2="true"
            ;;
        n|N|no|No)
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
    read -p "Enter Your Choice: " value

    case $value in
    t|Twitter|T|twitter)
        run_twitter
        python ./modules/twitter/twitter_module.py $handler
        is_done
        ;;
    f|F|Facebook|facebook)
        run_fb
        $(cd $DIR_LOC/modules/facebook && python3.7 scraper.py)
        wait
        $(cd $DIR_LOC/modules/facebook && cp -R data/. "/home/osint/Desktop/OSINT_OUTPUT/Facebook")
        wait
        $(cd $DIR_LOC/modules/facebook/data && rm -rf *)
        is_done
        ;;
    fbp|FBP)
        set_fb_pass
        wait
        is_done
        ;;
    c|TikTok|tiktok|C|"Tik ToK"|"tik tok")
        mkdir -p "/home/osint/Desktop/OSINT_OUTPUT/TikTok/UserProfiles"
        run_tiktok
        python3.7 ./modules/tiktok_user_info/tiktok_module.py --username "$handler"
        wait
        cp -R "@$handler" "/home/osint/Desktop/OSINT_OUTPUT/TikTok/UserProfiles"
        wait
        rm -rf "@$handler"
        is_done
        ;;
    cd|CD)
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