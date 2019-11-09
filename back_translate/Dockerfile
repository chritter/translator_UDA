#FROM continuumio/miniconda
FROM continuumio/miniconda3
#FROM busybox

RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

RUN apt-get install -y gcc zip

#RUN conda create -n env python=3.6
RUN conda create -n env python=2.7

#RUN conda init bash
RUN echo "source activate env" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH
RUN conda install -n env absl-py nltk tensorflow==1.14
RUN /bin/bash
RUN pip install tensor2tensor

# RUN pip install fastapi uvicorn

#RUN conda activate env

#RUN pip install

# copy entire directory where docker file is into docker container at /work
WORKDIR /work
COPY . /work/



RUN python -m nltk.downloader punkt

RUN ./download.sh

## download the checkpoint files
#RUN download.sh


ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD './run.sh'
#CMD '/bin/bash'

# uvicorn api:app --reload
