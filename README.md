# Storebaelt Vechicle Counter - The Great Belt Bridge using OpenCV
![show case](/gifs/showcase.gif)

This is my take on object detection using openCV. The code base builds heavily on top of [Andres Berejnoi](https://github.com/andresberejnoi/OpenCV_Traffic_Counter) repository, so please give him the credit. However, as I am doing most of my work in small object detection, this is my take for extending the mechanism for small obejcts - here detection objects/vechicles on a bridge. 

This little project was mainly for challenging myself in a detection challenge without the use of deep learning. However I would argue that this exact use case showcases the drawbacks and limitations of these techniques, that deep learning offer. 

## Andres Berejnoi's Blog Post
In addition to the video, Andres Berejnoi wrote a [short blog post](https://andresberejnoi.com/computer-vision-with-opencv-car-counting-system/) describing this project. It is supposed to be complementary to the video and not a replacement. 

## How to Set Up
The `requirements.txt` file contains the required libraries to run the script. It also contains other libraries like Jupyter notebook which is not really necessary. The main libraries and configurations needed are the following:

```
Python version: 3.7.8

OpenCV  4.4.0
Numpy   1.19.1
imutils 0.5.3
```

Installing OpenCV might be tricky depending on the system. Create a conda environment and install it in there. Maybe try running the command

```sh
conda install -c menpo opencv
```

## How to Use
There are several command line arguments that can be given to the script. The information here might be outdated, so the safest way to check the available commands is by running:

```sh
python main.py --help
```

Which will return something like:

```
usage: main.py [-h] [-p PATH] [-a MINAREA] [-d DIRECTION DIRECTION]
               [-n NUMCOUNT] [-w WEBCAM [WEBCAM ...]] [--rgb] [-vo VIDEO_OUT]
               [-vw VIDEO_WIDTH] [-vp VIDEO_PARAMS VIDEO_PARAMS]
               [-sf STARTING_FRAME]

Finds the contours on a video file

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  A video filename or path. Works better with .avi
                        files. If no path or name is provided, the camera will
                        be used instead.
  -a MINAREA, --minArea MINAREA
                        The minimum area (in pixels) to draw a bounding box
                        (default is 200)
  -d DIRECTION DIRECTION, --direction DIRECTION DIRECTION
                        A character: H or V representing the orientation of
                        the count line. H is horizontal, V is vertical. If not
                        provided, the default is H,0.5. The second parameter
                        is a float number from 0 to 1 indicating the place at
                        which the line should be drawn.
  -n NUMCOUNT, --numCount NUMCOUNT
                        The number of contours to be detected by the program
                        (default is 10).
  -w WEBCAM [WEBCAM ...], --webcam WEBCAM [WEBCAM ...]
                        Allows the user to specify which one to use as the video
                        source
  --rgb                 Boolean flag to use rbg colors.
  -vo VIDEO_OUT, --video_out VIDEO_OUT
                        Provide a video filename to output
  -vw VIDEO_WIDTH, --video_width VIDEO_WIDTH
                        Videos will be resized to this width (default is 640).
                        Height will be computed automatically to preserve
                        aspect ratio
  -vp VIDEO_PARAMS VIDEO_PARAMS, --video_params VIDEO_PARAMS VIDEO_PARAMS
                        Provide video codec and extension (in that order) for
                        the output video. Example: `--video_params mjpg avi`.
                        Default values are mjpg avi
  -sf STARTING_FRAME, --starting_frame STARTING_FRAME
                        Select the starting frame for video analysis (default
                        is 10). All frames before that will still be used for
                        the background average

```

The most important argument is `-p` which gives the script the name of the file to analyze (use of live camera video is not working yet). The flag `-d` is used to indicate the direction and position of the counting line. Like:

```sh
python main.py -p <path_to_your_video> -d v 0.5
```

The desired video width can also be provided with the flag `-vw`. This will also affect the size of the output video. 

```sh
python main.py -p <path_to_your_video> -vw 640
```

To get videos saved, use the flag `-vo` and some text that will be included in the output file's filename. For example:

```sh
python main.py -p <path_to_your_video> -vo my_video_without_extensions
```

Keep in mind that the default values for the file extension and video codec might not work for your system. Use tag `-vp` to change the default codec and extension combination. The codec is a 4-letter code (i.e. `MJPG`, `XDIV`, `DIVX`,etc). The extension can be something like `avi`, `mp4`, etc. For example:

```sh
python main.py -p <path_to_your_video> -vo some_video_name -vp MJPG avi
```

While the video windows are open, you can press `s` to save a screenshot at that particular frame. Pressing spacebar will pause the video (press spacebar again to resume).

## Interface
I have updated the project and moved away from the original script. In the new one, the computer vision parts are handled in a class TrafficCoutner in traffic_counter.py. To run the script, you must run main.py with a combination of parameters. For example:

```sh
python main.py -p <path_to_your_video> -d V 0.5 
```
