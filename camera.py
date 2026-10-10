from config import WIDTH, HEIGHT

class PiCamera:
    def __init__(self):
        from picamera2 import Picamera2
        from libcamera import controls
        self.camera = Picamera2()
        try:
            # RGB888 của Picamera2 cho mảng BGR đúng với OpenCV.
            cfg = self.camera.create_video_configuration(
                main={"size": (WIDTH, HEIGHT), "format": "RGB888"},
                controls={"FrameRate": 15})
            self.camera.configure(cfg)
            if "AfMode" in self.camera.camera_controls:
                self.camera.set_controls({"AfMode": controls.AfModeEnum.Continuous})
            self.camera.start()
        except Exception:
            self.camera.close()
            raise

    def read(self):
        return self.camera.capture_array("main")

    def close(self):
        try:
            self.camera.stop()
        finally:
            self.camera.close()
