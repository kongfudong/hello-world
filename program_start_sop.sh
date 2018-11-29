#!/bin/bash
function program(){
p_status=`service rhq-agent status`
status=${p_status#*is}
if [$status = 'running' ];then
        service rhq-agent stop
        else
                service rhq-agent start
fi
}

for ((i=1;i<21;i++));
        do
                echo $i
                program
                sleep 30
        done
