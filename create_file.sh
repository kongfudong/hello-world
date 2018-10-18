#!/bin/bash
for((j=0;j<2;j++));
do
	echo "create file begin"
	for((i=1;i<10;i++));
	do
		dd if=/dev/zero of=/opt/ENMSimulator/test/sun_$i.txt bs=2k count=1 
	done
	echo "sleep 30"
	sleep 30
	echo "delete file end"
	rm -rf /opt/ENMSimulator/test/sun_*.txt
	echo "delete '$i'" 
done
