import os
import re
import pip
import json
import argparse
from json2html import *


def install_package(package):
    try:
        return __import__(package, fromlist=['*'])
    except ImportError:
        print("Installing json2html package")
        pip.main(['install', package])
        print("Installation complete")
        return __import__(package, fromlist=['*'])


def load_json(json_to_load):
    with open(json_to_load, "r") as json_file:
        loaded_json = json.load(json_file)
    return loaded_json

def generate_name(json_name):
    match = re.match(r"(.*).json", json_name)
    html_name = match.group(1) + ".html"
    return html_name


converter = install_package("json2html")

parser = argparse.ArgumentParser(description='Convert provided json into html file')
parser.add_argument(dest='json', action='store', help='Path to json file which you want to convert')

args = parser.parse_args()

json_to_convert = load_json(args.json)
json_name = os.path.basename(args.json)
html_name = generate_name(json_name)
cwd = os.getcwd()

with open(os.path.join(cwd, html_name), "w", encoding="utf-8") as html_file:
    print("Saving tool output to: %s" % cwd + "\\" + html_name)
    html_file.write(json2html.convert(json = json_to_convert))
