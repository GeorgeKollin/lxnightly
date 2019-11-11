#!/bin/bash
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
exit 0;