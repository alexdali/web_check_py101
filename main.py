import argparse
import time

import logging
import site_requests
import sms

parser = argparse.ArgumentParser(description='Web-server monitoring script')

parser.add_argument('url', action="store", help="url of web server to monitor its status")
args = parser.parse_args()

check_url = args.url

def main(check_url):
    """
    main func
    """

    server_status = site_requests.check_site(check_url)

    if server_status != 200:
        msg_text = 'status ' + check_url + 'is ' + server_status
        sms(msg_text)

if __name__ == "__main__":
    main()