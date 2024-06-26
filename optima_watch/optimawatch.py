import npyscreen
import psutil
import threading
import time
import datetime
import logging

# Setup basic logging
logging.basicConfig(filename='system_monitor.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class SystemMonitorApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="System Monitor", color="STANDOUT")

class MainForm(npyscreen.FormWithMenus):
    def create(self):
        max_width = max([len(item) for item in ["CPU Usage:", "Memory Usage:", "Swap Usage:", "Disk Usage:", "System Uptime:", "Load Average:", "Network Traffic:"]]) + 4
        self.cpu = self.add(npyscreen.TitleSlider, out_of=100, name="CPU Usage:".ljust(max_width), relx=2)
        self.memory = self.add(npyscreen.TitleSlider, out_of=100, name="Memory Usage:".ljust(max_width), relx=2)
        self.swap = self.add(npyscreen.TitleSlider, out_of=100, name="Swap Usage:".ljust(max_width), relx=2)
        self.disk = self.add(npyscreen.TitleSlider, out_of=100, name="Disk Usage:".ljust(max_width), relx=2)
        self.uptime = self.add(npyscreen.TitleFixedText, name="System Uptime:".ljust(max_width), relx=2)
        self.load = self.add(npyscreen.TitleFixedText, name="Load Average:".ljust(max_width), relx=2)
        self.network = self.add(npyscreen.TitleFixedText, name="Network Traffic:".ljust(max_width), relx=2)
        self.exit_button = self.add(npyscreen.ButtonPress, name="Exit", when_pressed_function=self.exit_application)

        self.start_data_thread()

    def start_data_thread(self):
        threading.Thread(target=self.update_values, daemon=True).start()

    def update_values(self):
        while True:
            cpu_usage = psutil.cpu_percent(interval=0.1)
            memory_usage = psutil.virtual_memory().percent
            swap_usage = psutil.swap_memory().percent
            disk_usage = psutil.disk_usage('/').percent  # Monitor the root partition
            uptime_seconds = time.time() - psutil.boot_time()
            load_average = ', '.join(map(str, psutil.getloadavg()))
            net_io = psutil.net_io_counters()
            network_usage = f"Sent: {self.human_readable(net_io.bytes_sent)}, Received: {self.human_readable(net_io.bytes_recv)}"

            self.cpu.value = cpu_usage
            self.memory.value = memory_usage
            self.swap.value = swap_usage
            self.disk.value = disk_usage
            self.uptime.value = f"Uptime: {str(datetime.timedelta(seconds=int(uptime_seconds)))}"
            self.load.value = f"Load: {load_average}"
            self.network.value = network_usage

            self.display()
            time.sleep(1)
            logging.info(f"Updated values: CPU {cpu_usage}%, Memory {memory_usage}%, Disk {disk_usage}%")

    def human_readable(self, bytes):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
            if bytes < 1024:
                return f"{bytes:.2f} {unit}"
            bytes /= 1024
        return f"{bytes:.2f} PB"

    def exit_application(self):
        logging.info("Exiting application")
        self.parentApp.setNextForm(None)
        self.editing = False
        self.parentApp.switchFormNow()

if __name__ == '__main__':
    app = SystemMonitorApp()
    app.run()
