#!/bin/bash

command -v xterm;
isxterm="$?";
command -v terminator;
isterminator="$?";
command -v rxvt;
isrxvt="$?";
command -v gnome-terminal;
isgnometerm="$?";
command -v konsole;
iskonsole="$?";
command -v lxterminal;
islxterminal="$?";
command -v xfce4-terminal;
isxfceterm="$?";

if [ "$isxterm" -eq "0" ];
    then xterm -e "echo '';";
elif [ "$isterminator" -eq "0" ];
    then terminator -e "echo '';";
elif [ "$isrxvt" -eq "0" ];
    then rxvt -e "echo '';";
elif [ "$isgnometerm" -eq "0" ];
    then gnome-terminal -e "echo '';";
elif [ "$iskonsole" -eq "0" ];
    then konsole -e "echo '';";
elif [ "$islxterminal" -eq "0" ];
    then lxterminal -e "echo '';";
elif [ "$isxfceterm" -eq "0" ];
    then xfce4-terminal -e "echo '';";
else echo "Note: This terminal is not fully compatible with Linux Nightly. Errors may occur.";
fi;

if ! [ -f "./src/a9eed7dbbb875d537a60baf6442c86cb" ];
    then echo "Error: err_auth";
    exit 1;
fi;

cdir=$(pwd);
if [ -f "./conf/lgtd_deg" ] && [ -f "./conf/tmprt_indx" ] && [ -f "./conf/lat_deg" ] && [ -f "./conf/no_fork" ] && [ -f "./conf/randr_en" ] && [ -f "./conf/zip_all" ] && [ -f "./conf/zip_code" ];
    then latf=$(< "./conf/lat_deg");
    zipf=$(< "./conf/zip_code");
    lngtf=$(< "./conf/lgtd_deg");
    tmprtrf=$(< "./conf/tmprt_indx");
    iszip=$(< "./conf/zip_all");
    isnf=$(< "./conf/no_fork");
    israndr=$(< "./conf/randr_en");
    cmdstr="'$cdir/bin/xflux' -k $tmprtrf";
    case "$iszip" in
        *"1"*)
            cmdstr="$cmdstr -z $zipf";
        ;;
        *)
            cmdstr="$cmdstr -l $latf.0 -g $lngtf.0";
        ;;
    esac;
# case "$isnf" in *"1"*) cmdstr="$cmdstr -nofork"; ;; *) echo -e "\n"; ;; esac;
    case "$israndr" in
        *"1"*)
            cmdstr="$cmdstr -r 1";
        ;;
        *)
            echo -e "\n";
        ;;
    esac;
    echo -e "[Desktop Entry]\nName=Day Mode\nName[el]=Λειτουργία ημέρας\nComment[el]=Ρυθμίσεις προβολής\nGenericName=Linux Nightly\nIcon=$cdir/icons/sundark.png\nType=Application\nExec='$cdir/src/daymode.sh'" > "$cdir/daymode.desktop";
    echo -e "[Desktop Entry]\nName=Night Mode\nName[el]=Λειτουργία νύχτας\nComment[el]=Ρυθμίσεις προβολής\nGenericName=Linux Nightly\nIcon=$cdir/icons/moondark.png\nType=Application\nExec='$cdir/conf/start.sh'" > "$cdir/nightmode.desktop";
    echo -ne "#!/bin/bash\n'$cdir/src/nightmode.sh' '$lngtf' '$tmprtrf' '$cdir'" > "$cdir/conf/exec.sh";
    echo -ne " > '$cdir/conf/exec_out.txt';" >> "$cdir/conf/exec.sh";
    chmod +x "./conf/exec.sh";
    echo -ne "#!/bin/bash\nkillall xflux;\nwhile true;\n    do allxflux=\$(pidof xflux);\n    wtsp=\" \";\n    tmpxflux=\${allxflux%%\"\$wtsp\"*};\n    allxflux=\${allxflux#*\"\$wtsp\"};\n	case \"\$allxflux\" in\n		*\" \"*)\n            kill -9 \"\$tmpxflux\";\n			continue;\n		;;\n		*)\n            kill -9 \"\$tmpxflux\";\n			break;\n		;;\n	esac;\ndone;\n$cmdstr" > "$cdir/conf/exec2.sh";
    echo -ne " > '$cdir/conf/exec_out.txt';\necho \"\$?\" > '$cdir/conf/flux_exit.txt';\nexit 0;" >> "$cdir/conf/exec2.sh";
    chmod +x "./conf/exec2.sh";
else exit 1;
fi;

exit 0;