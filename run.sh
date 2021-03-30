#!/bin/bash

running=2

while [ $running -gt 1 ]
do
  http 'https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.MA.json?vaccineinfo' Referer:https://www.cvs.com/immunizations/covid-19-vaccine | python3 ./parse.py
  running=$?
done
