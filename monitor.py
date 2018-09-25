from time import sleep

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class DirectoryMonitor():
    def __init__(self, callback):
        self.observer = Observer()
        self.observer.start()
        self.event_handler = MonitoringDirectoryEventHandler(callback)

    def set_path(self, path):
        self.observer.unschedule_all()
        self.observer.schedule(self.event_handler, path, recursive=False)

class MonitoringDirectoryEventHandler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback

    def on_created(self, event):
        if not event.is_directory:
            sleep(1)    # Need some delay to complete saving the screenshot
            self.callback(event.src_path)