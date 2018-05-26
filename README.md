# Stereo Camera Microservice

Basic camera service that publishes an image once per second

## Input

* One Open-CV2 compatible camera

## Output

Publishes images to any service that accepts "raw_video" as input. Uses HTTP PUT

Field | Description
--- | ---
time | unix epoch
uuid | uuid v4 identifier for sample
type | 'raw_video'
source | 'camera service'
data | binary sample data as string (ndarray as list)

## Requirements

* python3
* cv2

## Sensor Nexus

This service is part of the maragi sensor nexus

![Maragi Sensor Nexus](/sensor_nexus.png "Maragi Sensor Nexus")
