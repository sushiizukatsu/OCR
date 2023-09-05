# 既成のdocker imageであるpythonの3.8.0をベースにする
FROM python:3.8.0

# linuxの環境設定
RUN apt-get update \
    && apt-get upgrade -y \
    # 4.3.0.38以降のopencvはlibgl1-mesa-devが必要
    && apt-get install -y libgl1-mesa-dev tesseract-ocr tesseract-ocr-jpn \
    # imageのサイズを小さくするためにキャッシュ削除
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    # pipのアップデート
    && pip install --upgrade pip 

# dataディレクトリを作って，そこにローカルからdataをコピーする
WORKDIR /home/data/
COPY ./data ${PWD}

# pythonのパッケージをインストール
WORKDIR /home/
COPY requirements.txt ocr.py ${PWD}
RUN pip install -r ./requirements.txt