import os

from flask import g

from . import discover


IR_DATA_DIR = 'baseapp/broadlink/'
IR_DATA_EXT = '.irdump'
rm = None


def connect_to_rm():
    print("Connecting to RM")
    for i in range(5):
        devices = discover(timeout=i*2)
        if devices or len(devices) > 0:
            break
    if not devices:
        return None

    devices[0].auth()
    return devices[0]


def get_rm():
    global rm
    if rm is None or not rm.check_temperature():
        rm = g._rmconnection = connect_to_rm()
    return rm


def get_devices():
    try:
        return [entry.name for entry in os.scandir(IR_DATA_DIR)
                if entry.is_dir() and '__' not in entry.name]
    except FileNotFoundError:
        return None


def get_commands(device):
    path = os.path.join(IR_DATA_DIR, device)
    try:
        return [x[:-len(IR_DATA_EXT)]
                for x in os.listdir(path)
                if IR_DATA_EXT in x]
    except FileNotFoundError:
        return None


def get_device_dict():
    return {d: get_commands(d) for d in get_devices()}


def send_command(device, command, rm=None):
    path = os.path.join(IR_DATA_DIR, device, command + IR_DATA_EXT)
    try:
        with open(path, 'rb') as fh:
            (rm or get_rm()).send_data(fh.read())
            return fh.tell() > 0
    except FileNotFoundError:
        pass
    return False

