# Instructions

1. CLONE this repo with `git clone https://github.com/daveshap/cam_svc.git`
2. BUILD the Docker image with `docker build --tag maragi_cam --file Dockerfile .`
3. LAUNCH the image with `./launch.sh` or `docker run -d --privileged --network maragi_net maragi_cam`
