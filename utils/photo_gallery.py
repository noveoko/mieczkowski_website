from glob import glob
import re
from pathlib import Path

pth_to_photos = r"C:\Users\mrkra\OneDrive\Dokumenty\Mieczkowski\www.mieczkowski.com.pl\old_page\photo\grafa\*.jpg"



photos = glob(pth_to_photos)

for file in photos:
    pth = Path(file)
    relative_path = pth.parts[-1::]
    file_name = pth.name
    split_on = re.search('\d', file_name).span()[0]
    type = file_name[:split_on].strip().replace("_","")
    index = file_name[split_on:]
    print(type, index, relative_path)