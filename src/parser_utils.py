import json
import csv
import logging
import yaml
import xml.etree.ElementTree as ET


def parse_json(filepath):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)

        logging.info("PARSE_JSON_SUCCESS")
        return data

    except (FileNotFoundError, json.JSONDecodeError) as error:
        logging.error(f"PARSE_JSON_ERROR: {error}")
        return []


def parse_yaml(filepath):
    try:
        with open(filepath, "r") as file:
            data = yaml.safe_load(file)

        logging.info("PARSE_YAML_SUCCESS")
        return data

    except (FileNotFoundError, yaml.YAMLError) as error:
        logging.error(f"PARSE_YAML_ERROR: {error}")
        return []


def parse_xml(filepath):
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()

        logging.info("PARSE_XML_SUCCESS")
        return root

    except (FileNotFoundError, ET.ParseError) as error:
        logging.error(f"PARSE_XML_ERROR: {error}")
        return []


def parse_csv(filepath):
    try:
        with open(filepath, "r", newline="") as file:
            reader = csv.DictReader(file)
            data = list(reader)

        logging.info("PARSE_CSV_SUCCESS")
        return data

    except (FileNotFoundError, csv.Error) as error:
        logging.error(f"PARSE_CSV_ERROR: {error}")
        return []