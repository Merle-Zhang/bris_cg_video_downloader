# Extract all the links from the HTML file and update the readme.
# 
# Requirement: the HTML file saved from `https://web.microsoftstream.com/studio/videos`
# Output: The updated readme file

import argparse
import re

# Pass in the filename for the HTML file as a command line argument
parser = argparse.ArgumentParser(description='extract links from HTML file')
parser.add_argument('filename', help='the filename of the html file')
args = parser.parse_args()

# Read in the HTML
with open(args.filename, "r") as file:
    txt = file.read()

# Regular expression for file name and stream link
name = r'week[0-9]{2}\-task[0-9]{2}\-([^\s]+)\-[0-9]'
link = r'https://web.microsoftstream.com/video/[^"]+'

# Find all the links and then remove the duplicates
expression = f'aria-label="{name}[^"]+" href="{link}"'
p = re.compile(expression)
namelinks = sorted(list(set([x.group() for x in re.finditer(expression, txt)])))

# Build the map {filename -> streamlink}
links = {re.search(name, namelink).group(): re.search(link, namelink).group() for namelink in namelinks}

# Build the markdown table for the links
table = "\n\n| Name | Link |\n| --- | --- |\n"
for name, link in links.items():
    table += f"| {name} | {link} |\n"
table += "\n"

# Update the table in readme
with open('readme.md', 'r') as file :
  filedata = file.read()

filedata = filedata.replace('ram', 'abcd')

start_comment = "[//]: <> (start-of-links)"
end_comment = "[//]: <> (end-of-links)"

start_index, end_index = filedata.index(start_comment) + len(start_comment), filedata.index(end_comment)

filedata = filedata[:start_index] + table + filedata[end_index:]

with open('readme.md', 'w') as file:
  file.write(filedata)
