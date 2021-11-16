import os
import re
import pip
import json
import argparse
from json2html import *

''' I know it shouldn't be done, but I just wanna
def install_package(package):
    try:
        return __import__(package, fromlist=['*'])
    except ImportError:
        print("Installing json2html package")
        pip.main(['install', package])
        print("Installation complete")
        return __import__(package, fromlist=['*'])
'''


def prepare_directory(dir_name = ""):
    cwd = dir_name
    if os.path.isdir(cwd):
        return cwd
    else:
        os.mkdir(cwd)
        return cwd


def load_json(json_to_load):
    with open(json_to_load, "r") as json_file:
        loaded_json = json.load(json_file)
    return loaded_json


def generate_name(json_name, output_dir, force):
    match = re.match(r"(.*).json", json_name)
    count = 1
    html_name = match.group(1) + ".html"
    while(True):
        if html_name in os.listdir(output_dir) and force == False:
            html_name = match.group(1) + str(count) + ".html"
            count +=1
        else:
            return html_name


def parse_args():
    parser = argparse.ArgumentParser(description='Convert provided json into html file')
    parser.add_argument(dest='json', action='store', help='Path to json file which you want to convert')
    parser.add_argument('--d', dest='dir', action='store', default='output',
                        help='Directory where html file should be generated')
    parser.add_argument('--f', dest='force', action='store_true', help='Forces overwrite of the generated file')

    args = parser.parse_args()

    return args

#converter = install_package("json2html")


args = parse_args()

cwd = prepare_directory(args.dir)
json_to_convert = load_json(args.json)
json_name = os.path.basename(args.json)
html_name = generate_name(json_name, cwd, args.force)


with open(os.path.join(cwd, html_name), "w", encoding="utf-8") as html_file:
    print("Saving tool output to: %s" % cwd + "\\" + html_name)
    html_file.write(json2html.convert(json = json_to_convert))
