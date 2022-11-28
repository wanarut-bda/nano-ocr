#!/bin/bash
echo 'countdown to autostart in... (cancel by Ctrl+C)'
for i in 5 4 3 2 1
do
   echo "$i"
   sleep 1
done

echo 'Started'
gnome-terminal -e "bash -c \"sudo python3 start_webIO.py; exec bash\""
gnome-terminal -e "bash -c \"sudo python3 start_OCR.py; exec bash\""
gnome-terminal -e "bash -c \"sudo python start_capture.py; exec bash\""