import requests

def check_site(url):

    try:
        response = requests.get(url)
        print('response.url: ' + response.url)
        print('response.status_code: ' + str(response.status_code))
        response.raise_for_status()
    except requests.exceptions.HTTPError as res_HTTPError:
        print('res_HTTPError: ' + str(res_HTTPError))
    except requests.exceptions.ConnectionError as res_ConnectionError:
        print('res_ConnectionError: ' + str(res_ConnectionError))
    finally:
        return response.status_code


if __name__ == "__main__":
    url = 'https://python101.online'
    # url = 'https://run.mocky.io/v3/4db5e403-9bd7-40b4-9be2-415506dcf06b'

    print('check {}'.format(url))
    check_site(url)