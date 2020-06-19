# /usr/bin/python3
import subprocess
from py3nvml.py3nvml import *
import time

import datetime

nvmlInit()


def current_temp_():
    while True:
        time.sleep(1)
        handle = nvmlDeviceGetHandleByIndex(0)
        print(f"GPU", nvmlDeviceGetIndex(handle),
              f"| Temp: {nvmlDeviceGetTemperature(handle, NVML_TEMPERATURE_GPU)}",
              f"| Consump : {int(nvmlDeviceGetPowerUsage(handle) / 1000)}"
              f"| PL: {int(nvmlDeviceGetEnforcedPowerLimit(handle) / 1000)}",
              f"| Proc ID: {os.getpid()}",
              nvmlDeviceGetName(handle),
              "|",
              str(datetime.datetime.now().strftime("%Y-%m-%d ""%H:%M:%S")))
        if nvmlDeviceGetTemperature(handle, NVML_TEMPERATURE_GPU) <= 72 and nvmlDeviceGetEnforcedPowerLimit(
                handle) == 135000:
            print("Temp and PL is GOOD!")
            continue
        else:

            if nvmlDeviceGetTemperature(handle, NVML_TEMPERATURE_GPU) >= 73 and nvmlDeviceGetEnforcedPowerLimit(
                    handle) == 135000:
                subprocess.call(["nvidia-smi", "-i", "0", "-pl", "127"])
                print("Change to 127")

    nvmlShutdown()


if __name__ == "__main__":
    current_temp_()
