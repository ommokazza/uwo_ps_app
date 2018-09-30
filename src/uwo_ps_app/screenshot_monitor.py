import os
from time import sleep

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class DirectoryMonitor():
    def __init__(self, path, callback = None):
        self.observer = Observer()
        self.observer.start()
        self.path = path

        if not os.path.exists(self.path):
            os.makedirs(self.path)
        if callback != None:
            self.__update_observer(callback)

    def set_callback(self, callback):
        self.__update_observer(callback)

    def __update_observer(self, callback):
        if callback == None or self.path == None:
            raise Exception("Wrong callback or path")

        event_handler = MonitoringDirectoryEventHandler(callback)
        self.observer.unschedule_all()
        self.observer.schedule(event_handler, self.path, recursive=False)

class MonitoringDirectoryEventHandler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback

    def on_created(self, event):
        if not event.is_directory:
            sleep(1)    # Need some delay to complete saving the screenshot
            self.callback(event.src_path)