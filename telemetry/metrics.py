from prometheus_client import Gauge

fps_gauge = Gauge("edge_ai_fps", "Current FPS")
cpu_usage = Gauge("cpu_usage_percent", "CPU usage")
memory_usage = Gauge("memory_usage_percent", "Memory usage")
temperature = Gauge("cpu_temperature_c", "CPU temperature")