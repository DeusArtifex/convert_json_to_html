# convert_json_to_html
Very generic json2html converter

## Required to run
To run this, you'll need json2html on your machine.
</br>It can be installed via pip:

	pip install json2html
				
Or from the project website: [json2html](https://pypi.org/project/json2html/ "json2html")

## Usage

	convert_json_to_html.py [path_to_json_file]

### Current default behavior
With no parameters present, script will convert the provided .json into .html file with the same name.
Output file will be stored in the /output/ folder, which will be created in scripts directory. If there will be a file
with the same name as the generated one, new file will be generated with incrementation after its name.

### Additional arguments

####--d directory

    convert_json_to_html.py --d "directory_path" [path_to_json_file]
Use to specify a directory in which the output file should be placed in.

####--f force

    convert_json_to_html.py --f [path_to_json_file]
Use to force overwrite of the output file. With "--f" present, output file will be generated with the default/chosen
name, even if it means it will overwrite another file. 

Have a pleasant day.

### [GitHub page](https://github.com/DeusArtifex/convert_json_to_html "convert_json_to_html")

_Created by Rafał "DeusArfifex" Kurek_
