import requests
import time
import argparse
def loopStatus(url,t,inter):
    for i in range(int(t)):
        try:
            start = time.time()
            response = requests.get(url,timeout=5)
            end = time.time()
            print(f"Reply from {url} in {round((end-start)*1000,2)}ms")
        except requests.exceptions.Timeout:
            print("Request timed out")
        except requests.exceptions.HTTPError:
            print("HTTP Error")
        except requests.exceptions.ConnectionError:
            print("Connection Error : check if the url is correct")
        except requests.exceptions.RequestException:
            print("Some unknown error")
        print("--- Checking Site ---")
        time.sleep(int(inter))

def currentStatus(url):
    try:
        start = time.time()
        response = requests.get(url,timeout=5)
        end = time.time()
        print(f"url : {url}")
        print(f"Status : Online")
        print(f"Status code : {response.status_code}")
        print(f"Ping : {round((end-start)*1000,2)}ms")
    except requests.exceptions.Timeout:
        print(f"url : {url}")
        print(f"Status : Offline")
        print(f"Error : Request Timed out")
    except requests.exceptions.HTTPError:
        print(f"url : {url}")
        print(f"Status : Offline")
        print(f"HTTP Error")
    except requests.exceptions.ConnectionError:
        print(f"url : {url}")
        print(f"Status : Offline")
        print(f"Connection Error : {url} not found")
    except requests.exceptions.RequestException:
        print(f"url : {url}")
        print(f"Status : Offline")
        print(f"Some unknown Error")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Check if a website is online or offline python web_ping.py <url> ")
    parser.add_argument("u",help = "Enter the domain (without https://), e.g. google.com")
    parser.add_argument("-t",help = "Specify the seconds to keep pinging the website")
    parser.add_argument("-i",default=1,help="Enter the interval for timed ping check (default is 1 s)")
    args = parser.parse_args()
    if not args.u:
        parser.error("You must specify a URL using -u")
    url = f"https://{args.u}"
    if args.t:
        loopStatus(url,args.t,args.i)
    else:
        currentStatus(url)
    