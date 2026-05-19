import psutil

cpu = psutil.cpu_percent()
memory = psutil.virtual_memory().percent
temp = psutil.sensors_temperatures()