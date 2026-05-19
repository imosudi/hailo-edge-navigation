import serial
import math
import logging
from typing import List, Tuple

logger = logging.getLogger(__name__)


class HokuyoLiDAR:
    def __init__(
        self,
        port: str = "/dev/ttyACM0",
        baudrate: int = 115200
    ):
        self.serial = serial.Serial(
            port=port,
            baudrate=baudrate,
            timeout=1
        )

    def read_scan(self) -> List[Tuple[float, float]]:
        points = []

        try:
            raw = self.serial.readline().decode("utf-8", errors="ignore")

            for i, value in enumerate(raw.split(",")):
                try:
                    distance = float(value)
                    angle = math.radians(i)

                    if 20 < distance < 4000:
                        points.append((angle, distance))

                except ValueError:
                    continue

        except Exception as e:
            logger.exception(f"LiDAR read error: {e}")

        return points