#!/bin/bash

python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
cd /home/ducpham/MLops/BashScript/Script/cronjob
python3 crawl.py