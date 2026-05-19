#!/bin/bash

sudo apt update && sudo apt upgrade -y

sudo apt install -y \
    python3-pip \
    python3-venv \
    git \
    build-essential \
    libatlas-base-dev \
    libopencv-dev \
    cmake \
    pkg-config

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt