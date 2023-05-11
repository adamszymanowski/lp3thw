# nosetest DO NOT work with python 3.10 and higher
FROM python:3.9

# set directory for the code
WORKDIR /usr/src/lp3thw

# Install dependencies for projects (in projects/ directory of source code)
RUN pip install --no-cache-dir -v nose==1.3.7 flask==2.0.1