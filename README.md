# OptimaWatch

OptimaWatch is a real-time system performance tracking application designed to monitor key metrics such as CPU usage, memory usage, disk usage, system uptime, load average, and network traffic. It is built using Python with `npyscreen` for a graphical user interface in the terminal and `psutil` for gathering system metrics.

## Features

- **CPU Usage**: Monitor the percentage of CPU utilization.
- **Memory Usage**: Track the percentage of used memory.
- **Swap Usage**: View the swap memory usage.
- **Disk Usage**: Monitor the disk usage for the root partition.
- **System Uptime**: Display the system uptime in hours, minutes, and seconds.
- **Load Average**: Show the average system load over the last 1, 5, and 15 minutes.
- **Network Traffic**: Monitor the amount of data sent and received.

## Installation

To run OptimaWatch, you need Python 3 and the following packages:
- `npyscreen`
- `psutil`

Install the required packages using pip:

```bash
pip install npyscreen psutil
```

## Usage

To start the application, run the script from the terminal:

```bash
python optimawatch.py
```

## Screenshot

Below is a screenshot demonstrating the application in use:

![data9](https://github.com/alilotfi23/OptimaWatch/assets/91953142/bff7adc7-bda8-44fa-8af5-576d54b41b6c)


## Exiting the Application

To exit the application, navigate to the "Exit" button using the arrow keys and press Enter, or simply close the terminal window.
