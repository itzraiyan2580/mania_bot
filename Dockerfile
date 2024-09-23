RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN cd /
RUN git clone https://github.com/itzraiyan2580/mania_bot
RUN cd mania_bot
WORKDIR /mania_bot
RUN pip3 install -U -r requirements.txt
CMD python3 main.py
