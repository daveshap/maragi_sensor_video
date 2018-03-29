# Stereo Camera Microservice

provides out-of-the-box functionality for robotics and ai in the form of a simple and robust rest api

## Input

* One or two cameras

## Output

* JSON serialized numpy ndarray(s) of images

## Requirements

* python3
* flask
* time
* json
* sys
* cv2

## API

Endpoint | Method | Request | Response
--- | --- | --- | ---
/ | GET | Returns default dictionary | `{time: unix epoch, img0: serialized ndarray}`
/stereo | GET | Returns stereo dictionary | `{time: unix epoch, img0: serialized ndarray, img1: serialized ndarray}`

[maragi]: https://github.com/benjaminharper2/cam_svc/blob/master/maragi.png "MARAGI Logo"
[design]: https://github.com/benjaminharper2/cam_svc/blob/master/maragi_design.png "Viable MARAGI organization"

![maragi]

# Microservice Architecture for Robotics and Artificial General Intelligence (MARAGI)

## Philosophy

### Biomimicry

At it's core MARAGI is biomimetic. Human bodies, and more specifically the human brain and various components of the nervous system, are all highly integrated and interconnected. Furthermore, these components specialize in specific functions. For example, the optic chiasm is a neural structure found in all vertebrates that facilitates binocular or stereo vision. The function of the optic chiasm is roughly reproduced through computer vision algorithms which also use stereo camera inputs. 

### Metacognition

Furthermore, MARAGI is guided by human metacognition. This is the conscious awareness of the process of thinking. Taking the time to tease apart the mental processes that go into various tasks, such as problem solving, searching, and being creative can provide insights and inspiration in the design of components, services, and organization. 

### Iterative and Incremental Improvement

There's no need to eat the whole elephant at once. Rome wasn't built in a day. Baby steps. Try, try again.  Fail forward. Learn as you go. Complex and sophisticated behaviors are emergent. Greater than the sum of its parts. 

## Architecture

### Sense, Think, Act

MARAGI is not a departure from conventional robotic design. Rather, it is simply a paradigm by which to organize otherwise conventional robotic and AI software. The only potential difference is that MARAGI is not strictly limited to this three-cycle loop. This is due to the unstructured organization of the microservices. MARAGI should always be sensing and thinking, although maybe not always acting. 

### Inherently Parallel

Any successful automaton must be performing many mental operations simultaneously. This is one of the chief driving factors behind the selection of a microservices architecture. Whether you realize it or not, your brain is constantly performing many separate tasks in order to give you a coherent and graceful interaction and understanding of the world and yourself. Your eyes and optic neurons are detecting edges and deciphering this text without your conscious awareness of this. In the same way, many other functions of the brain occur in the unconscious realm. Your motor cortex can drive a walking behavior with minimal conscious input. Your body's sense of proprioception and balance is always being drawn upon for physical coordination and other tasks without any conscious effort. All of these things happen in parallel and automatically. 

### Mesh Network (Semi Layered)

To visualize the interaction of the microservices consider a mesh network. Many technological systems follow a layered or tiered model. 

![design]

You can roughly consider there to be at least three layers to the MARAGI design. These layers are based upon abstraction from interaction with the physical world. The layer of highest abstraction includes things like executive planning and moral imperatives. The lowest layers of abstraction include things like motor controls and taking sensory input. 

### Extensible 

Infinite extensibility is inherent to a microservices architecture. Because of this, new functionality and capabilities can easily be added to any platform of MARAGI design. 

## Standards

### Microservices

Each service should be:

* strictly REST API based
* simple, generic, robust, and concise
* wholly self-contained in it's own repository
* ready to operate out of the box
* available to any other service at any time
* as platform agnostic as possible
* minimally configurable

### Documentation

All READMEs should include:

* Input
* Output
* Requirements
* API documentation
