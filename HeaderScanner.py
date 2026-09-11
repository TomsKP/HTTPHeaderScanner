import requests
import argparse

security_headers = {
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "X-XSS-Protection",
    "Permissions-Policy",
    "X-UA-Compliant",
    "Cache-Control",
}

parser = argparse.ArgumentParser()
parser.add_argument("--website", default="https://www.google.com")
parser.add_argument("--allowredirect", "--r", default=False, action="store_true")
args = parser.parse_args()

try:
    if args.allowredirect:
        response = requests.get(args.website, allow_redirects=True, timeout=5)
    else:
        response = requests.get(args.website, timeout=5)

    print(f"Target Site: " + args.website)
    print(f"Status Code: " + str(response.status_code))
    print(f"Server: " + response.headers['Server'] + "\n")

    for header in response.headers:
        if header in security_headers:
            print(header + " is present")
        else:
            print(header + " is absent")

except requests.exceptions.ConnectionError as ce:
    print("Connection Error")
except requests.exceptions.Timeout as te:
    print("Timeout")
except requests.exceptions.TooManyRedirects as tr:
    print("Too Many Redirects")
