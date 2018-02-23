#!/bin/bash
# coding: utf-8
if  (whiptail --title "bienvenidos al asistende de asr" \
  --yesno "En los siguientes pasos se creara el script para generar las imagenes \n\nDesea continuar?" 10 60) then

    echo "si", $?
    lineas_lsblk=`lsblk | wc -l`
    # introduces partición windows
    windows=$(whiptail --title "Elige partición de sistema windows" \
              --inputbox "\n\n`lsblk`" $(( 9 + $lineas_lsblk )) 78 \
               3>&1 1>&2 2>&3)

    # si la salida es correcta y a introducido algo en el input entra
    if ! [ $? = 0 ] || [ $windows -n ]; then
        echo "usuario a cancelado partición windows"
    else

        echo "El usuario a introducido partición: " $windows

        # opción particion datos
        if ! (whiptail --title "Tienes partición separa de datos windows?" \
          --yesno "\nDeseas crear también imagen de partición datos? " 10 60) then

            echo "no imagen datos", $?
        else
            echo "si imagen datos", $?
            windows_datos=$(whiptail --title "Elige partición de datos windows" \
                      --inputbox "\n\n`lsblk`" $(( 9 + $lineas_lsblk )) 78 \
                       3>&1 1>&2 2>&3)

            # si la salida es correcta y a introducido algo en el input entra
            if ! [ $? = 0 ] || [ $windows_datos -n ]; then
                echo "usuario a cancelado partición datos windows"
            else
                echo "El usuario a introducido partición datos: " $windows_datos

            fi
        fi
        # pregunta por partición linux
        if ! (whiptail --title "Tienes partición de linux?" \
          --yesno "\nDeseas crear también imagen de sistema linux? " 10 60) then

            echo "no imagen linux", $?
        else
            echo "si imagen linux", $?
            linux_particion=$(whiptail --title "Elige partición donde se encuentra linux" \
                      --inputbox "\n\n`lsblk`" $(( 9 + $lineas_lsblk )) 78 \
                       3>&1 1>&2 2>&3)

            # si la salida es correcta y a introducido algo en el input entra
            if ! [ $? = 0 ] || [ $linux_particion -n ]; then
                echo "usuario a cancelado partición linux"
            else
                echo "El usuario a introducido partición linux: " $linux_particion

            fi
        fi

        win="Partición de windows: $windows"
        datos_win=""
        sys_lin=""
        # muestro opiones elejidas y responde si son correctas
        if  ! [ $windows_datos -n ]; then
          datos_win="Particion de datos windows: $windows_datos"
        fi
        if ! [ $linux_particion -n ]; then
          sys_lin="Particion de linux: $linux_particion"
        fi
        if  (whiptail --title "Se asignarán los siguientes valores" \
          --yesno "$win \n$datos_win \n$sys_lin \n\nDesea continuar?" 12 60) then

# modifica archivos parte windows
            echo "entra"
            # borra linea de menu anterior comentada
            sed -i '9d' imatges3.sh
            # añade la nueva sin comentar
            sed -i '9i \       1 "Crear imatge del sistema operatiu Windows"  \\' imatges3.sh
            # identifica que extension tiene la partición windows seleccionda
            ext_win=`lsblk -f | egrep -w $windows |  awk '{ print $2 }'`
            # modifica titulo crear imagen añadiendo extensionseleccionada
            sed -i "30 s/partició .* a/partició $windows a/" imatges3.sh
            # borra linea 31
            sed -i '31d' imatges3.sh
            # crea tarea de partcrone con si extensión y partición adecuada
            sed -i "31i \                partclone.$ext_win -c -s /dev/$windows -o backups/windows/$windows.windows.$ext_win.pci -N" imatges3.sh

            # archivo recuperación asr.sh
            sed -i '9d' asr.sh
            # activa menu de restaurar windows
            sed -i '9i \       1 "Restaurar el sistema operatiu Windows"  \\' asr.sh
            # añade linea para restaurar windows con suis particion y extension correcta
            sed -i '32d' asr.sh
            sed -i "32i \                    partclone.$ext_win -r -s backups/windows/$windows.windows.$ext_win.pci -o /dev/$windows -N" asr.sh

             # edita el archivo images 3 segun las opciones anteriores elegidas
# modifica archivos parte datos
             if  ! [ $windows_datos -n ]; then
               # borra linea de menu anterior comentada
               sed -i '10d' imatges3.sh
               # añade la nueva sin comentar
               sed -i '10i \       2 "Crear imatge de la partició de dades Windows"  \\' imatges3.sh
               # modifica titulo crear imagen añadiendo extensionseleccionada
               sed -i "34 s/partició .* a/partició $windows_datos a/" imatges3.sh
               # identifica que extension tiene la partición windows seleccionda
               ext_win_datos=`lsblk -f | egrep -w $windows_datos |  awk '{ print $2 }'`
               sed -i '35d' imatges3.sh
               # crea tarea de partcrone con si extensión y partición adecuada
               sed -i "35i \                partclone.$ext_win_datos -c -s /dev/$windows_datos -o backups/windows/$windows_datos.win.datos.$ext_win_datos.pci -N" imatges3.sh

               # activa menu y añade linea de recuperación en asr.sh
               sed -i '10d' asr.sh
               sed -i '10i \       2 "Restaurar partició de dades Windows"  \\' asr.sh
               sed -i '43d' asr.sh
               sed -i "43i \                    partclone.$ext_win_datos -r -s backups/windows/$windows_datos.win.datos.$ext_win_datos.pci -o /dev/$windows_datos -N" asr.sh

             else
               sed -i '10d' imatges3.sh
               # añade la nueva  comentada
               sed -i '10i \       \\' imatges3.sh
               sed -i '10d' asr.sh
               sed -i '10i \       \\' asr.sh
             fi
# modifica archivos parte linux
             if ! [ $linux_particion -n ]; then
               # borra linea de menu anterior comentada
               sed -i '11d' imatges3.sh
               # añade la nueva sin comentar
               sed -i '11i \       3 "Crear imatge del sistema operatiu Linux"  \\' imatges3.sh
               # modifica titulo crear imagen añadiendo extensionseleccionada
               sed -i "38 s/partició .* a/partició $linux_particion a/" imatges3.sh
               # identifica que extension tiene la partición windows seleccionda
               ext_linux=`lsblk -f | egrep -w $linux_particion |  awk '{ print $2 }'`
               sed -i '39d' imatges3.sh
               # crea tarea de partcrone con si extensión y partición adecuada
               sed -i "39i \                partclone.$ext_linux -c -s /dev/$linux_particion -o backups/linux/$linux_particion.linux.$ext_linux.pci -N" imatges3.sh

               sed -i '11d' asr.sh
               sed -i '11i \       3 "Restaurar el sistema operatiu linux"  \\' asr.sh
               sed -i '54d' asr.sh
               sed -i "54i \                    partclone.$ext_linux -r -s backups/linux/$linux_particion.linux.$ext_linux.pci -o /dev/$linux_particion -N" asr.sh

             else
               sed -i '11d' imatges3.sh
               # añade la nueva comentada
               sed -i '11i \       \\' imatges3.sh

               sed -i '11d' asr.sh
               sed -i '11i \       \\' asr.sh
             fi

# crea carpetas donde guardar imagenes
             if ! [ -d "backups" ]; then
               echo "no esta backups"
               mkdir -p backups/windows
               mkdir -p backups/linux
             fi
# cambia el script de inicio setup al de recuperación
             sed -i 's,sudo bash /home/centos/setup-asr.sh,sudo bash /home/centos/asr.sh,' /home/centos/.bashrc
# inicia el script de crear imagenes
             bash imatges3.sh


        fi
    fi
fi

clear
