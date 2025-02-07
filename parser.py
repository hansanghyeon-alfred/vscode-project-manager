import json
import sys
import os

# 현재행되고있는 파선파일의 경로를 가져와 
projectDir = os.path.dirname(os.path.realpath(__file__))

# Determine the file path based on the editor argument
# 로그를 남겨줘
if len(sys.argv) > 2 and sys.argv[2].lower() == 'windsurf':
    filePath = os.path.join(os.path.expanduser(
        '~'), 'Library/Application Support/Windsurf/User/globalStorage/alefragnani.project-manager/projects.json')
    iconPath = os.path.join(projectDir, 'Windsurf.icns')
else:
    filePath = os.path.join(os.path.expanduser(
        '~'), 'Library/Application Support/Code/User/globalStorage/alefragnani.project-manager/projects.json')
    iconPath = os.path.join(projectDir, 'icon.png')

# read file
with open(filePath, 'r') as file:
    data = file.read()

# parse file
projects = json.loads(data)

# sort
projects = sorted(projects, key=lambda k: k['name'])
items = []
for project in projects:
    item = {
        "title": project['name'],
        "subtitle": project['rootPath'].split('/')[-1],
        "arg": project['rootPath'],
        "icon": {
            "path": iconPath
        }
    }
    if len(sys.argv) > 1:
        if sys.argv[1].lower() in project['name'].lower():
            items.append(item)
    else:
        items.append(item)

result = {
    "items": items
}

output = json.dumps(result)
print(output)

sys.exit(0)
