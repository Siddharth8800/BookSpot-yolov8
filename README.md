# BookSpot-yolov8

BookSpot-yolov8 is a cutting-edge book detection system that utilizes the YOLOv8 algorithm for real-time book detection in video streams. 
This project is designed to identify books in various environments, making it an invaluable tool for libraries, bookstores, and personal book collections.

## Features

- Real-time book detection using YOLOv8
- High accuracy and speed
- Customizable detection settings
- Easy integration with video streams

## Installation

To get started with BookSpot-yolov8, clone this repository to your local machine:

```sh
git clone https://github.com/yourusername/BookSpot-yolov8.git


pip install -r requirements.txt
```


### Usage
To start detecting books in real-time, run the following command:

This will activate the book detection system using your default camera. To use a different camera, modify the capture_index parameter in `bookDetection.py`.

### Customization
You can customize the detection settings by modifying the `pcconfig.py` file. This includes adjusting the confidence threshold, detection speed, and more.