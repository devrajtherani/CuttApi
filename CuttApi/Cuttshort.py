import requests
import urllib.parse as urlparse
from urllib.parse import urlencode
import urllib
import pyperclip


#ak = stdiomask.getpass("Enter your Cuttly api key: ")

class Cuttshort:
    def __init__(self, ak):
        while True:
            try:
                api_key = ak
                #api_key = input("Enter your Cuttly api key: ")
                api_url = 'http://cutt.ly/api/api.php?key={}'.format(api_key)
                data = requests.get(api_url).json()
                print(data["auth"])
                if data["auth"]==True:
                    while True:
                        try:
                            link = input("Enter the link to be shortened: ")
                            params = {'utm_source':'apidevthe'}
                            #url = urllib.parse.quote(url1)putwhererequired
                            #print(url)same
                    

                            if link.startswith("http"):
                                response = requests.get(link)
                                status = response.status_code
                                print(status)
                                url_parts = list(urlparse.urlparse(link))
                                query = dict(urlparse.parse_qsl(url_parts[4]))
                                query.update(params)
     
                                url_parts[4] = urlencode(query)
                                url1 = urlparse.urlunparse(url_parts)
                                url = urllib.parse.quote(url1)

                                if status==200:
                                    while True:
                                        name = input("Would you like to give a name? : ")
                                        if name=="Yes" or name=="yes":
                                            while True:
                                                name1 = input("Enter name:")
                                                api_url1 = 'http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(api_key, url, name1)
                                                data1 = requests.get(api_url1).json()["url"]
                                                #print(data1)
                                                if data1["status"] == 7:
                                                    shortened_url1 = data1["shortLink"]
                                                    print("Shortened URL:", shortened_url1)
                                                    pyperclip.copy(shortened_url1)
                                                    break
                                                else:
                                                    print("Please re-enter the name as name already exists!")
                                                    continue
                                        elif name=="No" or name=="no":
                                            api_url2 = 'http://cutt.ly/api/api.php?key={}&short={}'.format(api_key, url)
                                            data2 = requests.get(api_url2).json()["url"]
                                            #print(data2)
                                            if data2["status"] == 7:
                                                # OK, get shortened URL
                                                shortened_url2 = data2["shortLink"]
                                                print("Shortened URL:", shortened_url2)
                                                pyperclip.copy(shortened_url2)
                                        else:
                                            print("Please enter either Yes/No!")
                                else:
                                    print("URL does not exist on the Internet")
                            else:
                                link1 = "http://" + link
                                response1 = requests.get(link1)
                                status1 = response1.status_code
                                print(status1)
                                url_parts1 = list(urlparse.urlparse(link1))
                                query1 = dict(urlparse.parse_qsl(url_parts1[4]))
                                query1.update(params)
     
                                url_parts1[4] = urlencode(query1)
                                url2 = urlparse.urlunparse(url_parts1)
                                url3 = urllib.parse.quote(url2)
                                if status1 == 200:
                                    while True:
                                        name3 = input("Would you like to give a name? : ")
                                        if name3=="Yes" or name3=="yes":
                                            while True:
                                                name2 = input("Enter name:")
                                                api_url3 = 'http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(api_key, url3, name2)
                                                data3 = requests.get(api_url3).json()["url"]
                                                if data3["status"] == 7:
                                                    shortened_url3 = data3["shortLink"]
                                                    print("Shortened URL:", shortened_url3)
                                                    pyperclip.copy(shortened_url3)
                                                    break
                                                else:
                                                    print("Please re-enter the name as name already exists!")
                                                    continue
                                        elif name3=="No" or name3=="no":
                                            api_url4 = 'http://cutt.ly/api/api.php?key={}&short={}'.format(api_key, url3)
                                            data4 = requests.get(api_url4).json()["url"]
                                            if data4["status"] == 7:
                                                # OK, get shortened URL
                                                shortened_url4 = data4["shortLink"]
                                                print("Shortened URL:", shortened_url4)
                                                pyperclip.copy(shortened_url4)
                                        else:
                                            print("Please enter either Yes/No!")
                                else:
                                    print("URL does not exist on the Internet")

                        except requests.ConnectionError as exception:
                            
                            print("URL does not exist on the Internet")
                            break
                else:
                    print("The entered API key does not exist. Please retry!")
                    break
            except requests.JSONDecodeError as exception:
                print("There is an issue with the API. Please try after a few seconds")
                break

if __name__ == "__main__":
    import stdiomask
    api_key200 = stdiomask.getpass("Enter your Cuttly api key: ")
    short1 = Cuttshort(api_key200)