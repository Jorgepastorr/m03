#!/bin/bash
# coding: utf-8
clear

whiptail --backtitle "ASR by Joni"   \
       --menu "Què vol fer?" \
       13 70 4 \
       0 "Sortir" \
       \
       \
       \
       2>temp


# OK is pressed
if [ "$?" = "0" ];then
        _return=$(cat temp)
        echo "retun es: $_return"
        # Sortir
        if [ "$_return" = "0" ];then
                if (whiptail --title "Sortir" --yesno "Vol reiniciar el pc" 8 50); then
                    echo "reinicio"
                    init 6
                else
                    echo "Surt linea de comandes."
                fi

        # Restaurar el sistema operatiu Windows
        elif [ "$_return" = "1" ];then
                whiptail --title "Crear imatge del sistema operatiu Windows" --msgbox "$(echo '\nEs creara una imatge de la partició sda1 a la carpeta backups/windows/')" 10 50
                partclone.ntfs -c -s /dev/sda1 -o backups/windows/sda1.windows.ntfs.pci -N

        elif [ "$_return" = "2" ];then
                whiptail --title "Crear imatge de dades Windows" --msgbox "$(echo '\nEs creara una imatge de la partició sda8 a la carpeta backups/windows/')" 10 50
                partclone.ntfs -c -s /dev/sda8 -o backups/windows/sda8.win.datos.ntfs.pci -N

        elif [ "$_return" = "3" ];then
                whiptail --title "Crear imatge del sistema operatiu Linux" --msgbox "$(echo '\nEs creara una imatge de la partició sda9 a la carpeta backups/linux/')" 10 50
                partclone.ext4 -c -s /dev/sda9 -o backups/linux/sda9.linux.ext4.pci -N

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
