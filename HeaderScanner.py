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
args = parser.parse_args()

response = requests.get(args.website)

print(f"Target Site: " + args.website)
print(f"Status Code: " + str(response.status_code))
print(f"Server: " + response.headers['Server'] + "\n")\

for header in security_headers:
    if header in response.headers:
        print(header + " is present")
    else:
        print(header + " is absent")