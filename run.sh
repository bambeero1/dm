#!/bin/bash

#cd /myfolder/crawlers/
PATH=$PATH:/usr/local/bin
export PATH
cd /var/www/vhosts/sqlserver.ga/dm/
source /var/www/vhosts/sqlserver.ga/dm/bin/activate
scrapy crawl haraj --nolog


