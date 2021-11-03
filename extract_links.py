import re
import argparse

parser = argparse.ArgumentParser(description='extract links from HTML file')
parser.add_argument('filename', help='the filename of the html file')
args = parser.parse_args()

with open(args.filename, "r") as file:
    txt = file.read()

name = r'week[0-9]{2}\-task[0-9]{2}\-([^\s]+)\-[0-9]'
link = r'https://web.microsoftstream.com/video/[^"]+'

expression = f'aria-label="{name}[^"]+" href="{link}"'
p = re.compile(expression)
namelinks = [x.group() for x in re.finditer(expression, txt)]

links = {re.search(name, namelink).group(): re.search(link, namelink).group() for namelink in namelinks}

table = "\n\n| Name | Link |\n| --- | --- |\n"

for name, link in links.items():
    table += f"| {name} | {link} |\n"
table += "\n"

with open('readme.md', 'r') as file :
  filedata = file.read()

filedata = filedata.replace('ram', 'abcd')

start_comment = "[//]: <> (start-of-links)"
end_comment = "[//]: <> (end-of-links)"

start_index, end_index = filedata.index(start_comment) + len(start_comment), filedata.index(end_comment)

filedata = filedata[:start_index] + table + filedata[end_index:]

with open('readme.md', 'w') as file:
  file.write(filedata)
