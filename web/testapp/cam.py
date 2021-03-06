import cv2

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        # self.video = cv2.VideoCapture(0)
        # self.video = cv2.VideoCapture('http://192.168.0.62:8080/video')
        self.video = cv2.VideoCapture('rtmp://218.150.183.58:1935/app/test')
        # self.video = cv2.VideoCapture('http://172.30.1.51:8080/video')
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('test.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        if success:
            ret, jpeg = cv2.imencode('.jpg', image)
            return jpeg.tobytes()
        else:
            return None