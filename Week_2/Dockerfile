FROM python:3.10.7

USER root

###
COPY requirements.txt /tmp/
RUN pip3 install --no--cache-dir -r /tmp/requirements.txt

ENV JUPYTER_USER jovian

RUN useradd -ms /bin/bash ${JUPYTER_USER}
###

RUN pip3 install jupyter

RUN mkdir -p /home/$JUPYTER_USER/notebooks
RUN wget https://raw.githubusercontent.com/mschermann/forensic_accounting/master/Introduction.ipynb -P /home/$JUPYTER_USER/notebooks/
RUN chown -R $JUPYTER_USER /home/$JUPYTER_USER/


EXPOSE 8888

USER ${JUPYTER_USER}

CMD jupyter notebook --ip=0.0.0.0 --port 8888 --notebook-dir=/home/$JUPYTER_USER/notebooks

#two ways to create user: 
#1. hard code
# RUN useradd -ms /bin/bash our_user
#not recommanded
#2. 
# ENV JUPYTER_USER our_user
# RUN useradd -ms /bin/bash ${JUPYTER_USER}

#--ip: this thing should run on local host
#--port: set a specific port
#--allow-root to allow the root user
