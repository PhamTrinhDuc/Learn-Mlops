#!/bin/bash

python3 -m env myenv
source myenv/bin/activate
cd /home/ducpham/MLops/BashScript/Bash script/cronjob
python3 crawl.py