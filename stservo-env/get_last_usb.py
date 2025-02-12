import os
import glob

def get_last_inserted_usb():

    # Directory containing symlinks to USB devices
    disk_by_id_path = '/dev/disk/by-id'

    # Find all USB device symlinks
    usb_devices = glob.glob(os.path.join(disk_by_id_path, 'usb-*'))

    if not usb_devices:
        return None

    # Create a list to hold device details
    devices = []

    for usb_device in usb_devices:
        # Resolve the symlink to the actual device node path
        device_node = os.path.realpath(usb_device)

        # Get the symlink creation time
        dev_stat = os.stat(usb_device)
        dev_time = dev_stat.st_ctime

        devices.append((device_node, dev_time))

    # Sort devices by time (most recent first)
    devices.sort(key=lambda x: x[1], reverse=True)

    # Return the most recently added device node path
    if devices:
        return devices[0][0]
    else:
        return None


if __name__ == "__main__":
    last_usb_device = get_last_inserted_usb()
    if last_usb_device:
        print(f"Device node path of the last inserted USB drive: {last_usb_device}")
    else:
        print("No USB devices found.")