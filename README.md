# Mono Camera Microservice

This is a simple camera handling microservice that publishes images into the AMQP exchange for video input of MARAGI. Output has the following qualities:

* numpy array
* formatted as json 

# AMQP

* Publish to `maragi-rabbit`
* This is the instance of RabbitMQ for MARAGI

# Docker

* code is intended to run in a docker container
* maragi-rabbit is also a docker container