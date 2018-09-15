FROM ubuntu

RUN apt-get update && apt-get install -y \
  python3 \
  python3-pika \
  python3-numpy \
  python3-opencv

ADD amqp_pub.py /

CMD [ "python3", "./amqp_pub.py" ]
