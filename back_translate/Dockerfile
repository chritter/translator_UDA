FROM continuumio/miniconda3:4.7.12

RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

RUN apt-get install -y gcc zip vim

RUN conda create -n env python=3.6
#RUN conda create -n env python=2.7

#RUN conda init bash
RUN echo "source activate env" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH
RUN conda install -n env absl-py nltk tensorflow==1.14
RUN /bin/bash
RUN pip install tensor2tensor uvicorn fastapi

# RUN pip install fastapi uvicorn

#RUN conda activate env

# download the NN checkpoints
#RUN wget https://storage.googleapis.com/uda_model/text/back_trans_checkpoints.zip
#RUN unzip back_trans_checkpoints.zip && rm back_trans_checkpoints.zip
#RUN ./download.sh


#RUN pip install

RUN python -m nltk.downloader punkt


## download the checkpoint files
#RUN download.sh


ENTRYPOINT [ "/usr/bin/tini", "--" ]
#CMD './run.sh'

# hint that port will be used for API
EXPOSE 8000

# copy entire directory where docker file is into docker container at /work
WORKDIR /work
COPY . /work/
#COPY *.py /work/
#COPY *.sh /work/
#COPY checkpoints /work/checkpoints #


# start the API
CMD './start_api.sh'
#CMD '/bin/bash'

# uvicorn api:app --reload
