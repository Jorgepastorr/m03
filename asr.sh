#!/bin/bash
# coding: utf-8
clear

whiptail --backtitle "ASR by Joni"   \
       --menu "Què vol fer?" \
       11 50 4 \
       0 "Sortir"
       1 "Restaurar el sistema operatiu Windows"  \
       \
       \
       2>temp


# OK is pressed
if [ "$?" = "0" ];then
        _return=$(cat temp)

        # Sortir
        if [ "$_return" = "0" ];then
            if (whiptail --title "Sortir" --yesno "Vol reiniciar el pc" 8 50) then
                echo "reinicio"
                init 6
            fi

        # Restaurar el sistema operatiu Windows
       elif [ "$_return" = "1" ];then
         imagen_windows=`ls backups/windows/*.windows.*`
         if  [ -f $imagen_windows ]; then
                if (whiptail --title "Restaurar el sistema operatiu Windows" --yesno  "Esta segur que vol restaurar windows. \nTrigara uns minuts." 8 50) then
                    echo "copio"
                    partclone.ntfs -r -s backups/windows/sda1.windows.ntfs.pci -o /dev/sda1 -N
                fi
         else
           whiptail --title "No s'ha trobat ninguna imatge per restaurar. " --msgbox "Executa imatges.sh per generar les imatges o setup.sh per habilitar les opcións de imatges.sh " 8 70
         fi

       elif [ "$_return" = "2" ];then
         imagen_datos=`ls backups/windows/*.datos.*`
         if  [ -f $imagen_datos ]; then
                 if (whiptail --title "Restaurar partició de dades Windows" --yesno  "Esta segur que vol restaurar partició de dades windows. \nTrigara uns minuts." 8 50) then
                     echo "copio"
                    partclone.ntfs -r -s backups/windows/sda8.win.datos.ntfs.pci -o /dev/sda8 -N
                 fi
         else
           whiptail --title "No s'ha trobat ninguna imatge per restaurar. " --msgbox "Executa imatges.sh per generar les imatges o setup.sh per habilitar les opcións de imatges.sh " 8 70
         fi

       elif [ "$_return" = "3" ];then
         imagen_linux=`ls backups/linux/*.linux.*`
         if  [ -f $imagen_linux ]; then
                if (whiptail --title "Restaurar el sistema operatiu linux" --yesno  "Esta segur que vol restaurar linux. \nTrigara uns minuts." 8 50) then
                    echo "copio"
                    partclone.ext4 -r -s backups/linux/sda9.linux.ext4.pci -o /dev/sda9 -N
                fi
          else
            whiptail --title "No s'ha trobat ninguna imatge per restaurar. " --msgbox "Executa imatges.sh per generar les imatges o setup.sh per habilitar les opcións de imatges.sh " 8 70
          fi
        fi

        if (whiptail --title "Sortir" --yesno "Vol reiniciar el pc" 8 50) then
            echo "reinicio"
            init 6
        fi
# Cancel or ESC
else
        # Reiniciem el PC
        echo "Reiniciem el PC"
        init 6
fi


clear

# remove the temp file
rm -f temp
