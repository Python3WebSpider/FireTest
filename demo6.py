import argparse
import requests
import fire


def scrape(url, timeout):
    response = requests.get(url, timeout=timeout)
    print(response.text)


parser = argparse.ArgumentParser(description='Scrape Function')
parser.add_argument('url', type=str,
                    help='an integer for the accumulator')
parser.add_argument('timeout',  type=int,
                    help='sum the integers (default: find the max)')

if __name__ == '__main__':
    args = parser.parse_args()
    scrape(args.url, args.timeout)
