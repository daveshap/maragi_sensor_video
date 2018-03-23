# camera microservice

provides out-of-the-box functionality for robotics and ai in the form of a simple and robust rest api

## requirements

* python3
* flask
* time
* json
* sys
* cv2

## usage

`python app.py <port (optional), default 6000>`

Endpoint | Function | Description | Example
--- | --- | --- | ---
/ | GET | Returns default dictionary | `{time: unix epoch, img0: serialized ndarray}`
/stereo | GET | Returns stereo dictionary | `{time: unix epoch, img0: serialized ndarray, img1: serialized ndarray}`

# Microservice Architecture for Robotics and Artificial General Intelligence (MARAGI)

## Philosophy

### Biomimicry

At it's core MARAGI is biomimetic. Human bodies, and more specifically the human brain and various components of the nervous system, are all highly integrated and interconnected. Furthermore, these components specialize in specific functions. For example, the optic chiasm is a neural structure found in all vertebrates that facilitates binocular or stereo vision. The function of the optic chiasm is roughly reproduced through computer vision algorithms which also use stereo camera inputs. 

### Metacognition

Furthermore, MARAGI is guided by human metacognition. This is the conscious awareness of the process of thinking. Taking the time to tease apart the mental processes that go into various tasks, such as problem solving, searching, and being creative can provide insights and inspiration in the design of components, services, and organization. 

## Architecture

### Sense, Think, Act

MARAGI is not a departure from conventional robotic design. Rather, it is simply a paradigm by which to organize otherwise conventional robotic and AI software. The only potential difference is that MARAGI is not strictly limited to this three-cycle loop. This is due to the unstructured organization of the microservices.

### Inherently Parallel

Any successful automaton must be performing many mental operations simultaneously. This is one of the chief driving factors behind the selection of a microservices architecture. Whether you realize it or not, your brain is constantly performing many separate tasks in order to give you a coherent and graceful interaction and understanding of the world and yourself. Your eyes and optic neurons are detecting edges and deciphering this text without your conscious awareness of this. In the same way, many other functions of the brain occur in the unconscious realm. Your motor cortex can drive a walking behavior with minimal conscious input. Your body's sense of proprioception and balance is always being drawn upon for physical coordination and other tasks without any conscious effort. All of these things happen in parallel and automatically. 

## Standards

### Microservices

Each service should be:

* strictly REST API based
* as simple and concise as possible
* as robust as possible
* wholly self-contained
* ready to operate out of the box
* available to any other service at any time
