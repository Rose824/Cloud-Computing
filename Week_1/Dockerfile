#bonus: how to access a docker container(write a command line)
FROM python:3.7.14

RUN apt-get update && apt-get install wget

RUN wget https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv -O company.csv

RUN grep -o -m1 "\(\\w*\) INC" company.csv | head -1 > company_name.txt && rm company.csv

# | means whatever outcome we have throw it to the right hand side

#entry point is for buiding server; command line is for ...?
