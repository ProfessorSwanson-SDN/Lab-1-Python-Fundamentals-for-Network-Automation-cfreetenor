import logging
from pathlib import Path

from src.network_device import NetworkDevice
from src.parser_utils import parse_json, parse_yaml, parse_xml, parse_csv


Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/lab.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w"
)


def main():
    logging.info("LAB1_START")

    devices = parse_json("data/devices.json")
    yaml_data = parse_yaml("data/interfaces.yaml")
    xml_data = parse_xml("data/vlans.xml")
    csv_data = parse_csv("data/inventory.csv")

    for device in devices:
        hostname = device.get("hostname", "unknown")
        ip = device.get("ip", "unknown")
        device_type = device.get("type", device.get("role", "unknown"))

        network_device = NetworkDevice(hostname, ip, device_type)
        network_device.summarize()

        location = device.get("location", "unknown")
        role = device.get("role", device_type)

        msg = f"Device {hostname} is a {location} {role}"
        print(msg)
        logging.info(f"DEVICE_MSG: {msg}")

    if isinstance(yaml_data, dict):
        interfaces = yaml_data.get("interfaces", [])
    elif isinstance(yaml_data, list):
        interfaces = yaml_data
    else:
        interfaces = []

    for interface in interfaces:
        name = interface.get("name", "unknown")
        status = interface.get("status", "unknown")

        msg = f"Interface {name} is {status}"
        print(msg)
        logging.info(f"INTERFACE_MSG: {msg}")

    if xml_data != []:
        for vlan in xml_data.findall(".//vlan"):
            vlan_id = vlan.findtext("id", default="unknown")
            name = vlan.findtext("name", default="unknown")

            msg = f"VLAN {vlan_id} is the {name}"
            print(msg)
            logging.info(f"VLAN_MSG: {msg}")

    for item in csv_data:
        hostname = item.get("hostname", "unknown")
        location = item.get("location", "unknown")
        role = item.get("role", item.get("type", "unknown"))

        msg = f"Device {hostname} is a {location} {role}"
        print(msg)
        logging.info(f"DEVICE_MSG: {msg}")

    logging.info("LAB1_END")


if __name__ == "__main__":
    main()