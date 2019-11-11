#!/bin/bash
if ! [ -f "./src/a9eed7dbbb875d537a60baf6442c86cb" ];
    then echo "Error: err_auth";
    exit 1;
fi;
mylngt=$(printf "%d" "$1");
tmprtr=$(printf "%d" "$2");
cdir="$3";
if [ "$mylngt" = "0" ]; 
    then mylngt=$((1));
    mylngt=${mylngt#0};
fi;
if [ "$tmprtr" -lt "2000" ] || [ "$tmprtr" -gt "10000" ];
    then tmprtr=$((3400));
    tmprtr=${tmprtr#0};
fi;
if [ "$mylngt" -lt "-179" ] || [ "$mylngt" -gt "180" ]; 
    then echo "Invalid input! Please, give an integer between -179 and 180.";
    exit 1;
fi;
cmdstr="./bin/xflux -l 1.0 -k $tmprtr";
isnf=$(< "./conf/no_fork");
israndr=$(< "./conf/randr_en");
case "$israndr" in
    *"1"*)
        cmdstr="$cmdstr -r 1";
    ;;
    *)
        echo -e "\n";
    ;;
esac;
# case "$isnf" in *"1"*) cmdstr="$cmdstr -nofork"; ;; *) echo -e "\n"; ;; esac;
killall xflux;
while true;
    do allxflux=$(pidof xflux);
    wtsp=" ";
    tmpxflux=${allxflux%%"$wtsp"*};
    allxflux=${allxflux#*"$wtsp"};
    case "$allxflux" in
        *" "*)
            kill -9 "$tmpxflux";
            continue;
        ;;
        *)
            kill -9 "$tmpxflux";
            break;
        ;;
    esac;
done;
hour=$(date '+%H');
mins=$(date '+%M');
hour=${hour#0};
mins=${mins#0};
mylngt=${mylngt#0};
hourtomin=$(($hour*60));
totalmin=$(($hourtomin+$mins));
# night 21:04
nightmin=$((1264));
if [ "$totalmin" -le "$nightmin" ];
    then minsdif=$(($nightmin-$totalmin));
    degdif=$(($minsdif/4));
    lngt=$(($mylngt+$degdif));
    if [ "$lngt" -gt "180" ];
        then lngt=$(($lngt-360));
    fi;
    cmdstr="$cmdstr -g $lngt";
    $cmdstr;
    echo "$?" > "./conf/flux_exit.txt";
else minsdif=$(($totalmin-$nightmin));
    degdif=$(($minsdif/4));
    lngt=$(($mylngt-$degdif));
    if [ "$lngt" -lt "-179" ];
        then lngt=$(($lngt+360));
    fi;
    cmdstr="$cmdstr -g $lngt";
    $cmdstr;
    echo "$?" > "./conf/flux_exit.txt";
fi;
exit 0;
