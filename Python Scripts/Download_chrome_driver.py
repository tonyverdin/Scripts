from ChromeVersion import *
from Json_Website import *
import requests
from tqdm import tqdm
from pathlib import Path
from zipfile import ZipFile

get_chrome_version()

File_Path = 'C:\Tests\chromedriver.zip'
Zip_File_Path = 'C:\Tests\chromedriver'
list_of_selium_downloads = get_json_response("https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json")
download_links =  list_of_selium_downloads['channels']['Stable']['downloads']['chrome']

for links in download_links:
    if links['platform']=='win64':link = links['url']

driver = Path(File_Path)
if driver.is_file() == False:
    response  = requests.get(link)
    print(link)
    if response.status_code == 200:
        # Sizes in bytes.
        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024
        open(File_Path,'wb').write(response.content)
        print('File downloaded successfully')
    else:
        print("Download failed")
else:
    print('Skipping download')
    with ZipFile(File_Path,'r') as zObject:
        zObject.extractall(path=Zip_File_Path)
    print(f'Files written to {Zip_File_Path}')