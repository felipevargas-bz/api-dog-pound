FROM ubuntu:20.04

RUN apt update && apt upgrade -y && apt install -y \
                            python3 \
                            python3-dev \
                            python3-distutils \
                            python3-pip \
                            mysql-server \
                            libmysqlclient-dev \
                            libffi-dev \
                            libssl-dev \
                            build-essential \
                            libpython3-dev \
                            zlib1g-dev
RUN pip install \
        --upgrade pip \
        "fastapi[all]"\
        uvicorn[standard] \
        SQLAlchemy \
        pycodestyle \
        mysqlclient \
		python-multipart \
		requests
