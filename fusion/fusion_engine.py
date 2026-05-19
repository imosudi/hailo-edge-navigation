import math
from typing import List, Dict


class SensorFusionEngine:

    def fuse(
        self,
        detections: List[Dict],
        lidar_points: List
    ) -> List[Dict]:

        fused = []

        for det in detections:
            x1, y1, x2, y2 = det["bbox"]

            center_x = (x1 + x2) / 2

            angle = (center_x / 640.0) * 180.0 - 90.0

            nearest_distance = None

            for lidar_angle, distance in lidar_points:
                deg = math.degrees(lidar_angle)

                if abs(deg - angle) < 5:
                    if nearest_distance is None or distance < nearest_distance:
                        nearest_distance = distance

            fused.append({
                "label": det["class"],
                "confidence": det["confidence"],
                "distance_mm": nearest_distance,
                "direction_deg": angle,
                "threat_level": self._threat(nearest_distance)
            })

        return fused

    @staticmethod
    def _threat(distance):
        if distance is None:
            return "unknown"

        if distance < 500:
            return "critical"

        if distance < 1500:
            return "warning"

        return "safe"