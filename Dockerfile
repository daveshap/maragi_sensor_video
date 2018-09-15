FROM maragi_cam

ADD amqp_pub.py /

CMD [ "python3", "./amqp_pub.py" ]
