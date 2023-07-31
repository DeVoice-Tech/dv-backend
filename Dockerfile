FROM nvidia/cuda:11.3.1-base-ubuntu20.04

ENV PYTHON_VERSION=3.8

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get -qq update \
    && apt-get -qq install --no-install-recommends \
    libsndfile1-dev \
    git \
    python${PYTHON_VERSION} \
    python${PYTHON_VERSION}-venv \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s -f /usr/bin/python${PYTHON_VERSION} /usr/bin/python3 && \
    ln -s -f /usr/bin/python${PYTHON_VERSION} /usr/bin/python && \
    ln -s -f /usr/bin/pip3 /usr/bin/pip

RUN pip install --upgrade pip

RUN git clone https://github.com/iinjyI/tortoise-tts.git /tortoise-tts

WORKDIR /tortoise-tts

RUN pip install torch==1.12.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113

RUN pip install -r requirements.txt

RUN python3 setup.py install

# Setup the app
COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt
