#!/usr/bin/env bash

while true; do
  grep "Mem" /proc/meminfo
  df -h | grep "/[tmp]*$"
  for monitor_file in "$@"; do
    if [ -f $monitor_file ]; then
      echo "[$(date -r ${monitor_file} "+%Y-%m-%d %H:%M")::${monitor_file}] $(tail -n 1 ${monitor_file})"
    fi
  done
  sleep 60
done
