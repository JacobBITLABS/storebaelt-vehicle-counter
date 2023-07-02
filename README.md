# Storebaelt Vechicle Counter - The Great Belt Bridge using OpenCV
![show case](/gifs/showcase.gif)

This is my take on object detection using openCV. The code base builds heavily on top of [Andres Berejnoi](https://github.com/andresberejnoi/OpenCV_Traffic_Counter) repository, so please give him the credit. However, as I am doing most of my work in small object detection, this is my take for extending the mechanism for small obejcts - here detection objects/vechicles on a bridge. 

This project was primarily a personal challenge aimed at testing my skills in the field of object detection without relying on deep learning techniques. By exploring alternative methods, I wanted to highlight the drawbacks and limitations inherent in such techniques, which are effectively addressed by the capabilities offered by deep learning

## Main Changes
Below, I provide a brief overview of the key modifications and significant mechanisms employed in the technique. It is worth noting that I have made several alterations to the filters used.

### Gaussian Blur removed
The Gaussian Blue filter is commonly employed to reduce noise in images. However, during my experimentation, I observed that the smoothing effect of the filter also blurred the pixel-prints of numerous vehicles, rendering it ineffective in achieving the desired outcome.

### Dilation 
The original implementation included dilation, but I have made some code refinements. We utilize dilation to enhance the visibility of detections, allowing us to track contours more effectively.

### Binding Objects from frame $C_i$ to $C_{i+1}$
The object tracking process relies on the distance between detected contours from one frame to the next. However, this approach can be sensitive, particularly when dealing with small objects. In scenarios where vehicles are positioned closely to each other, their contours may appear closer than the previous position of an individual object. To address this challenge, I have incorporated the L1 distance calculation on either the 'x' or 'y' coordinates, depending on the `-d` argument. This modification has significantly enhanced the reliability of object tracking.

### A few GUI improvement and integrations.
I added the UI to add the dots utilizing the original codes integration of RoI for analysis.

### Parameter finetuning. 
Since older techniques lack the ability to learn invariants or generalize well, we are compelled to finetune parameters for each specific scenario. I invested  effort into conducting testing across various settings, meticulously adjusting parameters. However, it's important to note that this technique remains sensitive to variations in lighting conditions, weather such as rain, and other environmental factors. Even the showcased GIF could benefit from further finetuning tailored to that specific setting.

## Why do small/ tiny object detection work (okay) in this setting?
In general, I initially believed that conducting object detection on such small objects would be extremely challenging due to environmental noise. However, the success in this particular setting can be attributed to the consistent background of the four-laned highway, with the only moving objects being the vehicles on it. By examining the subtracted image (top left), valuable insights can be gained regarding whether a vehicle is a truck or a car, making it somewhat frustrating that the actual detection task is more difficult. The utilization of Region of Interest (RoI) analysis significantly enhances the stability and reliability of the analysis, although it is not yet perfect. Nevertheless, I have already identified some ideas for potential improvements.

### Limitations and drawbacks
This solution is highly parameter-dependent, optimized for the current setting, and sensitive to environmental variations like sunlight, sky conditions, and other factors. During extensive testing, I even evaluated its performance under challenging scenarios, such as heavy rain, where the presence of raindrops on the camera lens introduced significant noise, making it nearly impossible to achieve accurate results. Additionally, testing in low-light conditions posed its own set of challenges. In such situations, both the cars and their front lights were detected as separate entities, necessitating the development of a mechanism to differentiate between them.


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

The most important argument is `-p` which gives the script the name of the file to analyze (default is Great Belt Bridge live camera feed). The flag `-d` is used to indicate the direction and position of the counting line. Like:

```sh
python3 main.py -d H 0.85
```
or
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

# Interface
### 1) Pick RoI
When executing the script the user will first be meet with an interface to big the RoI (region of interest). This is simply done by a mouse click to place white dots on the screen. You can use as many as you want making the RoI arbitrarily jagged. However I recommend that you use to acutally filter noisy areas out of the analysis (as you can see I did not do, with the ship in the gif above). When you are done press `q`-key. 

### 2) Analysis is running on the live feed
A second screen is prompted with the four analyzing feeds.  
- Top Left: Subtracted Image (running avg background (reference background) and current frame).
- Bottom Left: Dialted image (10 iterations).
- Top Right: Background average.
- Bottom Right: Current Frame.