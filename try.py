#!/usr/bin/python3
import subprocess
from py3nvml.py3nvml import *
import time

nvmlInit()
starttime = time.time()
handle = nvmlDeviceGetHandleByIndex(0)
current_pwr_limit = (nvmlDeviceGetEnforcedPowerLimit(handle))
current_gpu_temp = current_temp = nvmlDeviceGetTemperature(handle, NVML_TEMPERATURE_GPU)
print(current_gpu_temp)
while current_gpu_temp != 72:
    time.sleep(5 - ((time.time() - starttime) % 5))
else:

    if current_gpu_temp >= 72 and current_pwr_limit >= 135000:
        subprocess.call(["nvidia-smi", "-i", "0", "-pl", "126"])
        print("126")

    if current_gpu_temp >= 72 and current_pwr_limit >= 126000:
        subprocess.call(["nvidia-smi", "-i", "0", "-pl", "117"])
        print("117")

    if current_gpu_temp >= 72 and current_pwr_limit >= 117000:
        subprocess.call(["nvidia-smi", "-i", "0", "-pl", "108"])
        print("108")

nvmlShutdown()

print("tick")
