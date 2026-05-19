import cv2
import threading
import queue
import time
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class CameraCapture:
    def __init__(self, device: int = 0, width: int = 1280, height: int = 720):
        self.cap = cv2.VideoCapture(device)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        self.frame_queue: queue.Queue = queue.Queue(maxsize=5)
        self.running = False
        self.thread: Optional[threading.Thread] = None

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._capture_loop, daemon=True)
        self.thread.start()

    def _capture_loop(self):
        while self.running:
            ret, frame = self.cap.read()

            if not ret:
                logger.warning("Camera frame read failed")
                continue

            if not self.frame_queue.full():
                self.frame_queue.put(frame)

            time.sleep(0.001)

    def get_frame(self):
        if self.frame_queue.empty():
            return None
        return self.frame_queue.get()

    def stop(self):
        self.running = False
        self.cap.release()