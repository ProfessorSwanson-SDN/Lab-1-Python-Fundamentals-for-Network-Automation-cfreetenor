import logging 
logging.basicConfig(
    filename="logs/lab.log",
    level=logging.INFO
)

from src.network_device import NetworkDevice

from src.parser_utils import (
    parse_json,
    parse_yaml,
    parse_xml,
    parse_csv
)



def main():
    devices = parse_json("data/devices.json")
    for device in devices:
        network_device = NetworkDevice(
            device["hostname"],
            device["ip"],
            device["type"]
        )

        network_device.summarize()
    
    interfaces = parse_yaml("data/interfaces.yaml")
    inventory = parse_csv("data/inventory.csv")
    vlans = parse_xml("data/vlans.xml")
    for interface in interfaces["interfaces"]:
        msg = f"Interface {interface['name']} is {interface['status']}"
        print(msg)
        logging.info(f"INTERFACE_MSG: {msg}")

    for device in inventory:
        msg = f"Device {device['hostname']} is a {device['location']} {device['role']}"
        print(msg)
        logging.info(f"DEVICE_MSG: {msg}")

    for vlan in vlans:
        msg = f"VLAN {vlan.find('id').text} is the {vlan.find('name').text}"
        print(msg)
        logging.info(f"VLAN_MSG: {msg}")

if __name__ == "__main__":
    logging.info("LAB1_START")
    main()
    logging.info("LAB1_END")
