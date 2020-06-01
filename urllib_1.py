from urllib import request
from urllib import response



def main():
    url = "http://ea4b5b22.ngrok.io/hello_get?name=Allen"
    resp = request.urlopen(url)  # type: response
    print(resp.read().decode('utf-8'))


if __name__ == "__main__":
    main()
