# import cv2
# import time


# def display_video_frames(url, buffer_size):
#     # Create a video capture object
#     cap = cv2.VideoCapture(url)

#     # Set the buffer size of the video capture object
#     cap.set(cv2.CAP_PROP_BUFFERSIZE, buffer_size)

#     fps = cap.get(cv2.CAP_PROP_FPS)
#     print(f"{fps} frames per second")

#     # Check if the video capture object was successfully opened
#     if not cap.isOpened():
#         print("Failed to open video stream.")
#         return    
    
#     # Calculate the delay between each frame based on the desired fps
#     delay = 1 / fps

#     while True:
#         # Read the next frame from the video stream
#         ret, frame = cap.read()

#         # Check if the frame was successfully read
#         if ret:
#             # Display the frame
#             cv2.imshow('Storebaelt Pylon ', frame)
    
#             # Check for 'q' key press to exit
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#         else:
#             print("Cannot read frame...")
#             # If reading the frame failed, break the loop
#             break

#         # Introduce a delay to achieve the desired frame rate
#         time.sleep(delay)

#     # Release the video capture object and close the window
#     cap.release()
#     cv2.destroyAllWindows()


# if __name__ == '__main__':
#     # URL of the video stream
#     video_url = "https://stream.sob.m-dn.net/live/sb1/index.m3u8"

#     # Buffer size in frames
#     buffer_size = 20000

#     # Display the video frames
#     display_video_frames(video_url, buffer_size)

import argparse 
from vechicle_counter import TrafficCounter

def CLI():
    #Define default values here to make documentation self-updating
    minArea_default       = 0
    direction_default     = ['H','0.85']
    numCount_default      = 20
    videoWidth_default    = 640
    videoParams_default   = ['mjpg','avi']
    startingFrame_default = 10

    parser = argparse.ArgumentParser(description='Finds the contours on a video file')          #creates a parser object
    parser.add_argument('-p','--path', default="https://stream.sob.m-dn.net/live/sb1/index.m3u8", type=str,help="""A video filename or path.
    Works better with .avi files.
    If no path or name is provided, the camera will be used instead.""")        #instead of using metavar='--path', just type '--path'. For some reason the metavar argument was causing problems
    parser.add_argument('-a','--minArea',type=int,help=f'The minimum area (in pixels) to draw a bounding box (default is {minArea_default})',
                        default=minArea_default)
    parser.add_argument('-d','--direction', type=str,default=direction_default,nargs=2,help=f"""A character: H or V
    representing the orientation of the count line. H is horizontal, V is vertical.
    If not provided, the default is {direction_default[0]},{direction_default[1]}. The second parameter
    is a float number from 0 to 1 indicating the place at which the
    line should be drawn.""")
    parser.add_argument('-n','--numCount',type=int,default=numCount_default,help=f"""The number of contours to be detected by the program (default is {numCount_default}).""")
    parser.add_argument('-w','--webcam',type=int,nargs='+',help="""Allows the user to specify which to use as the video source""")
    parser.add_argument('--rgb',action='store_true',help="Boolean flag to use rbg colors.")
    parser.add_argument('-vo','--video_out',type=str,default="",help="Provide a video filename to output")
    parser.add_argument('-vw','--video_width',type=int,default=videoWidth_default,help=f"Videos will be resized to this width (default is {videoWidth_default}). Height will be computed automatically to preserve aspect ratio")
    parser.add_argument('-vp','--video_params',type=str,default=videoParams_default,nargs=2,help=f"Provide video codec and extension (in that order) for the output video. Example: `--video_params mjpg avi`. Default values are {videoParams_default[0]} {videoParams_default[1]}")
    parser.add_argument('-sf','--starting_frame',type=int,default=startingFrame_default,help=f"Select the starting frame for video analysis (default is {startingFrame_default}). All frames before that will still be used for the background average")
    args = parser.parse_args()
    return args

def make_video_params_dict(video_params):
    codec     = video_params[0]
    extension = video_params[1]
    
    params_dict = {
        'codec'    :codec,
        'extension':extension,
    }
    return params_dict

def main(args):
    video_source   = args.path
    line_direction = args.direction[0]
    line_position  = float(args.direction[1])
    video_width    = args.video_width
    min_area       = int(args.minArea)
    video_out      = args.video_out
    numCnts        = int(args.numCount)
    video_params   = make_video_params_dict(args.video_params)
    starting_frame = args.starting_frame
    tc = TrafficCounter(video_source,
                        line_direction,
                        line_position,
                        video_width,
                        min_area,
                        video_out,
                        numCnts,
                        video_params,
                        starting_frame,)

    tc.main_loop()

if __name__ == '__main__':
    args = CLI()
    main(args)