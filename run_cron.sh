#!/bin/bash
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
cd /root/YT_AlexCarterTrading || exit 1
echo "=== CRON EXECUTION START: $(date -u) ==="
/usr/bin/python3 /root/YT_AlexCarterTrading/batch_runner.py
echo "=== CRON EXECUTION END: $(date -u) ==="