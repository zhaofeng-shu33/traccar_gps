import json
import argparse
from datetime import datetime

from requests.auth import HTTPBasicAuth
import requests

def load_config():
    with open('config.json') as f:
        return json.load(f)

def get_data(from_time, to_time):
    config_dic = load_config()
    url = config_dic['root_url'] + '/positions'
    a = HTTPBasicAuth(config_dic['email'], config_dic['password'])
    payload = {
        'deviceId': config_dic['deviceId'],
        'from': datetime.isoformat(from_time) + 'Z',
        'to': datetime.isoformat(to_time) + 'Z'
        }
    headers = {'Accept': 'application/gpx+xml'}
    r = requests.get(url, auth=a, params=payload, headers=headers)
    if r.status_code != 200:
        raise ValueError('')
    with open('build/my-data.xml', 'w') as f:
        f.write(r.text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--from_time', default='2020-07-01')
    parser.add_argument('--to_time', default=datetime.now().strftime('%Y-%m-%d'))
    args = parser.parse_args()
    from_time = datetime.strptime(args.from_time, '%Y-%m-%d')
    to_time = datetime.strptime(args.to_time, '%Y-%m-%d')
    get_data(from_time, to_time)
