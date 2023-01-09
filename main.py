import datetime
import json
import requests
import sys
from urllib.request import urlopen


def download_bing(destination):
    url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&mkt=en-US"
    response = urlopen(url)
    data_json = json.loads(response.read())
    for image in data_json['images']:
        image_date = datetime.datetime.strptime(image['startdate'], '%Y%m%d').date().strftime("%Y-%m-%d")
        image_url = 'https://www.bing.com' + image['url']
        img_data = requests.get(image_url).content
        file_name = destination + image_date + '.jpg'
        print(file_name)
        with open(file_name, 'wb') as handler:
            handler.write(img_data)


if __name__ == '__main__':
    download_bing(sys.argv[1])
