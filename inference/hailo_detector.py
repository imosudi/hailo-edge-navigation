import numpy as np
import cv2
import logging
from hailo_platform import HEF, VDevice
from typing import List, Dict

logger = logging.getLogger(__name__)


class HailoDetector:
    def __init__(self, hef_path: str):
        self.hef = HEF(hef_path)
        self.device = VDevice()

    def infer(self, frame: np.ndarray) -> List[Dict]:
        resized = cv2.resize(frame, (640, 640))

        input_tensor = np.expand_dims(resized, axis=0)

        results = self.device.infer(self.hef, input_tensor)

        detections = []

        for det in results:
            detections.append({
                "class": det["class_name"],
                "confidence": float(det["confidence"]),
                "bbox": det["bbox"]
            })

        return detections