FROM python:3.6.13
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY gru+cnn_10000.hdf5 ./
RUN pip install pip==20.2
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN pip install ./en_core_web_lg-2.3.1.tar.gz
CMD ["python", "app.py"]
