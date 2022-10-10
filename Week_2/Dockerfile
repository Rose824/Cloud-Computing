FROM python:3.10.7

USER root

###
COPY requirements.txt /tmp/
RUN pip3 install --no--cache-dir -r /tmp/requirements.txt

ENV JUPYTER_USER jovian

RUN useradd -ms /bin/bash ${JUPYTER_USER}
###

RUN pip3 install jupyter

#two ways to create user: 
#1. hard code
# RUN useradd -ms /bin/bash our_user
#not recommanded
#2. 
# ENV JUPYTER_USER our_user
# RUN useradd -ms /bin/bash ${JUPYTER_USER}

EXPOSE 8888
#make sure the order of EXPOSE&PORT is right

USER ${JUPYTER_USER}

CMD jupyter notebook --ip=0.0.0.0 --port 8888 --notebook-dir=/home/$JUPYTER_USER/notebooks
#--ip: this thing should run on local host
#--port: set a specific port
#--allow-root to allow the root user

#Create a directory in the home directory of your user for the notebooks
WORKDIR /home/
RUN mkdir -p /home/new_dir
# Copy the necessary files
COPY home/requirements.txt requirements.txt

# Install the necessary packages
RUN pip install -r /home/new_dir/requirements.txt
#Download your favorite notebooks into this folder
