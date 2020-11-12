import argparse
import time

import logging_srv
import site_requests
import sms

parser = argparse.ArgumentParser(description='Web-server monitoring script')

parser.add_argument('url', action="store", help="url of web server to monitor its status")
args = parser.parse_args()

check_url = args.url

def check_srv(url):
    """
    func check seerver url status and send sms
    """

    server_status = site_requests.check_site(check_url)

    if server_status != 200:
        msg_text = 'status ' + check_url + ' is ' + str(server_status)
        sms.send_sms(msg_text)


def main(srv_url):
    """
    main func
    """
    # run function every 60 seconds
    while True:
        check_srv(srv_url)
        time.sleep(60)


if __name__ == "__main__":
    main(args.url)