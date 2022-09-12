import urllib.request as urllib


def get_url(url):
    url = url
    print("Checking connectivity...")

    response = urllib.urlopen(url)
    print("Connected to", url, "succesfully.")
    print("The response code was:", response.getcode())


print("This is a site connectivity checker program")
input_url = input("Input the url of the site you wanna check: ")

get_url(input_url)
