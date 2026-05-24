import json
import yaml
import xml.etree.ElementTree as ET
import csv
import logging

def parse_json(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            logging.info("PARSE_JSON_SUCCESS")
            return data
        
    except FileNotFoundError:
        logging.error("PARSE_JSON_ERROR")
        return None
    
    except json.JSONDecodeError:
        logging.error("PARSE_JSON_ERROR")
        return None
    
def parse_yaml(file_path):
    try:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
            logging.info("PARSE_YAML_SUCCESS")
            return data

    except FileNotFoundError:
        logging.error("PARSE_YAML_ERROR")
        return None

    except yaml.YAMLError:
        logging.error("PARSE_YAML_ERROR")
        return None

def parse_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        logging.info("PARSE_XML_SUCCESS")
        return root

    except FileNotFoundError:
        logging.error("PARSE_XML_ERROR")
        return None

    except ET.ParseError:
        logging.error("PARSE_XML_ERROR")
        return None

def parse_csv(file_path):
    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)
            logging.info("PARSE_CSV_SUCCESS")
            return data

    except FileNotFoundError:
        logging.error("PARSE_CSV_ERROR")
        return None

    except csv.Error:
        logging.error("PARSE_CSV_ERROR")
        return None

