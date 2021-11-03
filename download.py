# Download all the videos from the CG workbooks.
# 
# Requirement: internet connection, and curl or wget
# Output: `videos` folder containing all the videos

import os

# Link to the CG repo
repo = "https://github.com/drslock/CG2021/archive/refs/heads/main.zip"

# TODO: Add auto detection for choosing curl or wget,
#       and exit if both of them are not available

# Download with curl or wget
# os.system(f"curl -LJO {repo}")
os.system(f"wget --no-check-certificate --content-disposition {repo}")

# Unzip the file
zip = "CG2021-main.zip"
os.system(f"unzip {zip}")

# Collect the path for all the videos
videos = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".mp4"):
            videos.append(f"{root}/{file}")

# Move the videos into a separate folder
os.system("mkdir videos")
for video in videos:
    tokens = video.split("/")
    week = f"week{tokens[3].split()[0]}"
    task = f"task{tokens[4].split()[0]}"
    category = tokens[5]
    index = tokens[6][tokens[6].index("-")+1:tokens[6].index(".")]
    filename = f"{week}-{task}-{category}-{index}"
    os.system(f'mv "{video}" ./videos/{filename}.mp4')

# Remove the zip and unzipped folder
os.system("rm -r CG2021-main CG2021-main.zip")
