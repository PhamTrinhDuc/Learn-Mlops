#!/bin/bash

python3 -m venv myenv
source myenv/bin/activate
cd /home/ducpham/MLops/BashScript/Script/cronjob
python3 crawl.py