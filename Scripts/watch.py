#!/usr/bin/python
import shutil
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import argparse
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--projectFolder",
                    default="..\\project", help="Your project folder path")
parser.add_argument("-r", "--rbxl", default=".\\rbxl\\project.rbxl",
                    help="Path to your .rbxl file")
parser.add_argument("-d", "--dest", default="..\\",
                    help="Directory above your project folder")
args = parser.parse_args()


def delete(projectFolder="..\\project"):
    try:
        shutil.rmtree(projectFolder)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))


def extract(rbxl=".\\project.rbxl", dest="..\\"):
    # Extract Scripts and Stuff from .rbxl to the dest
    os.system(f"rbxlx-to-rojo.exe {rbxl} {dest} ")

# -----------------------------Rojo Listener-----------------------------------


def logOutput():
    global rojo
    while True:
        output = rojo.stdout.readline()
        if output == '' and rojo.poll() is not None:
            break
        if output:
            print(output.decode().strip())
        time.sleep(0.5)


def rojoService(projectFolder):
    global rojo
    args = [".\\rojo.exe", "serve", projectFolder]
    rojo = subprocess.Popen(
        args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    print("Started Rojo With PID: ", rojo.pid, "\n")

# ----------------------------------------------------------------------------


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global rojo
        src = str(event.src_path).replace("\\", "/")
        print(src)
        if src == str(args.rbxl).replace("\\\\", "/").replace("\\", "/"):
            print(f'event type: {event.event_type}  path : {src}')
            time.sleep(1.5)
            rojo.terminate()
            rojo.wait()
            print("Killed Rojo")
            delete(args.projectFolder)
            extract(args.rbxl, args.dest)
            os.system("clear")
            print("-----------------  Locally Updated  -----------------")
            time.sleep(0.5)
            rojoService(args.projectFolder)


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='./rbxl', recursive=False)
    observer.start()
    rojo = None
    rojoService(args.projectFolder)

    try:
        while True:
            logOutput()
            print("running..")
    except KeyboardInterrupt:
        rojo.terminate()
        observer.stop()
    observer.join()
