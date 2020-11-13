import sys
import argparse
import time

import log_srv
import site_requests
import sms


def check_srv(url):
    """
    func check seerver url status and send sms
    """

    server_status = site_requests.check_site(url)


    if server_status != 200:
        msg_text = 'status ' + url + ' is ' + str(server_status)
        if sms.send_sms(msg_text):
            logger.warning('sms sent with message: ' + msg_text)
        else:
            logger.warning('sms message failed to send')


def main(args):
    """
    main func
    """

    logger.info("App run")

    # all time values are converted into seconds
    sec = 0 if (args.hour > 0 or args.min > 0) else args.sec
    repeat_time = (args.hour * 3600) + (args.min * 60) + sec
    logger.info('repeat_time: ' + str(repeat_time))

    # run function every 60 seconds
    while True:
        check_srv(args.url)
        time.sleep(repeat_time)


logger = log_srv.get_logger(__name__)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Web-server monitoring script. If you specify only the url argument, the server check by default will repeat every 60 seconds')

    parser.add_argument('url', action="store", help="url of web server to monitor its status")
    parser.add_argument('-hh', metavar='hours', action="store", dest='hour', default=0, type=int, help="period in hours to repeat the script run, default=0")
    parser.add_argument('-mm', metavar='minutes', action="store", dest='min', default=0, type=int, help="period in minutes to repeat the script run, default=0")
    parser.add_argument('-ss', metavar='seconds', action="store", dest='sec', default=60, type=int, help="period in seconds to repeat the script run, default is 60")


    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    else:
        args = parser.parse_args()
        main(args)