#!/bin/python3

import argparse
import re
import urllib.error
import urllib.request

def crawl(url, regex, userAgent, fileName):
    if userAgent != False and fileName != False:
        print("========================")
        print(f"[+] User-Agent: {userAgent}")
        print(f"[+] OutputFile: {fileName}")
        print(f"[+] Crawling...")
        print("========================\n")

        user = {"user-agent": userAgent}

        file = open(fileName, "a")

        if regex == "link":
            try:
                req = urllib.request.urlopen(urllib.request.Request(url, headers=user))
                occurrences = re.findall(br"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-zA-Z][0-9a-zA-Z]))+", req.read())
                
                for link in occurrences:
                    print(f"Link: {link.decode()}")
                    file.write(f"Link: {link.decode()}\n")

                file.close()
                exit(0)

            except urllib.error.HTTPError as error:
                print("can't do the web request in this domain !!!")
                print(f"the web request returns status code: {error.code}")
                exit(0)

            except urllib.error.URLError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

            except ValueError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)
             

        elif regex == "phone":
            try:
                req = urllib.request.urlopen(urllib.request.Request(url, headers=user))
                occurrences = re.findall(br"([0-9]{3}|[0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})", req.read())
                
                for phones in occurrences:
                    print(f"phonephones: {phones.decode()}")
                    file.write(f"Link: {link.decode()}\n")

                file.close()
                exit(0)

            except urllib.error.HTTPError as error:
                print("can't do the web request in this domain !!!")
                print(f"the web request returns status code: {error.code}")
                exit(0)

            except urllib.error.URLError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

            except ValueError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)
             

        elif regex == "email":
            try:
                req = urllib.request.urlopen(urllib.request.Request(url, headers=user))
                occurrences = re.findall(br"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", req.read())
                
                for email in occurrences:
                    print(f"Emails: {email.decode()}")
                    file.write(f"Link: {link.decode()}\n")

                file.close()
                exit(0)

            except urllib.error.HTTPError as error:
                print("can't do the web request in this domain !!!")
                print(f"the web request returns status code: {error.code}")
                exit(0)

            except urllib.error.URLError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

            except ValueError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

        else:
            try:
                req = urllib.request.urlopen(urllib.request.Request(url, headers=user))
                occurrences = re.findall(regex, req.read())
                
                for occu in occurrences:
                    print(f"Occurence: {occu.decode()}")
                    file.write(f"Link: {link.decode()}\n")

                file.close()
                exit(0)

            except urllib.error.HTTPError as error:
                print("can't do the web request in this domain !!!")
                print(f"the web request returns status code: {error.code}")
                exit(0)

            except urllib.error.URLError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

            except ValueError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

    elif fileName != False:
        print("========================")
        print(f"[+] User-Agent: No-userAgent")
        print(f"[+] OutputFile: {fileName}")
        print(f"[+] Crawling...")
        print("========================\n")

        user = {"user-agent": "Crawl2.0 - WebCrawler"}

        file = open(fileName, "a")

        if regex == "link":
            try:
                req = urllib.request.urlopen(urllib.request.Request(url, headers=user))
                occurrences = re.findall(br"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-zA-Z][0-9a-zA-Z]))+", req.read())
                
                for link in occurrences:
                    print(f"Link: {link.decode()}")
                    file.write(f"Link: {link.decode()}\n")

                file.close()
                exit(0)

            except urllib.error.HTTPError as error:
                print("can't do the web request in this domain !!!")
                print(f"the web request returns status code: {error.code}")
                exit(0)

            except urllib.error.URLError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

            except ValueError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)
             

        elif regex == "phone":
            try:
                req = urllib.request.urlopen(urllib.request.Request(url, headers=user))
                occurrences = re.findall(br"([0-9]{3}|[0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})", req.read())
                
                for phones in occurrences:
                    print(f"phonephones: {phones.decode()}")
                    file.write(f"Link: {link.decode()}\n")

                file.close()
                exit(0)

            except urllib.error.HTTPError as error:
                print("can't do the web request in this domain !!!")
                print(f"the web request returns status code: {error.code}")
                exit(0)

            except urllib.error.URLError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

            except ValueError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)
             

        elif regex == "email":
            try:
                req = urllib.request.urlopen(urllib.request.Request(url, headers=user))
                occurrences = re.findall(br"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", req.read())
                
                for email in occurrences:
                    print(f"Emails: {email.decode()}")
                    file.write(f"Link: {link.decode()}\n")

                file.close()
                exit(0)

            except urllib.error.HTTPError as error:
                print("can't do the web request in this domain !!!")
                print(f"the web request returns status code: {error.code}")
                exit(0)

            except urllib.error.URLError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

            except ValueError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

        else:
            try:
                req = urllib.request.urlopen(urllib.request.Request(url, headers=user))
                occurrences = re.findall(regex, req.read())
                
                for occu in occurrences:
                    print(f"Occurence: {occu.decode()}")
                    file.write(f"Link: {link.decode()}\n")

                file.close()
                exit(0)

            except urllib.error.HTTPError as error:
                print("can't do the web request in this domain !!!")
                print(f"the web request returns status code: {error.code}")
                exit(0)

            except urllib.error.URLError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

            except ValueError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

    elif userAgent != False:
        print("========================")
        print(f"[+] User-Agent: {userAgent}")
        print(f"[+] OutputFile: No-outputFile")
        print(f"[+] Crawling...")
        print("========================\n")

        user = {"user-agent": userAgent}

        if regex == "link":
            try:
                req = urllib.request.urlopen(urllib.request.Request(url, headers=user))
                occurrences = re.findall(br"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-zA-Z][0-9a-zA-Z]))+", req.read())
                
                for link in occurrences:
                    print(f"Link: {link.decode()}")

                exit(0)

            except urllib.error.HTTPError as error:
                print("can't do the web request in this domain !!!")
                print(f"the web request returns status code: {error.code}")
                exit(0)

            except urllib.error.URLError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

            except ValueError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)
             

        elif regex == "phone":
            try:
                req = urllib.request.urlopen(urllib.request.Request(url, headers=user))
                occurrences = re.findall(br"([0-9]{3}|[0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})", req.read())
                
                for phones in occurrences:
                    print(f"phonephones: {phones.decode()}")

                exit(0)

            except urllib.error.HTTPError as error:
                print("can't do the web request in this domain !!!")
                print(f"the web request returns status code: {error.code}")
                exit(0)

            except urllib.error.URLError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

            except ValueError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)
             

        elif regex == "email":
            try:
                req = urllib.request.urlopen(urllib.request.Request(url, headers=user))
                occurrences = re.findall(br"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", req.read())
                
                for email in occurrences:
                    print(f"Emails: {email.decode()}")

                exit(0)

            except urllib.error.HTTPError as error:
                print("can't do the web request in this domain !!!")
                print(f"the web request returns status code: {error.code}")
                exit(0)

            except urllib.error.URLError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

            except ValueError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

        else:
            try:
                req = urllib.request.urlopen(urllib.request.Request(url, headers=user))
                occurrences = re.findall(regex, req.read())
                
                for occu in occurrences:
                    print(f"Occurence: {occu.decode()}")

                exit(0)

            except urllib.error.HTTPError as error:
                print("can't do the web request in this domain !!!")
                print(f"the web request returns status code: {error.code}")
                exit(0)

            except urllib.error.URLError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

            except ValueError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

    else:
        print("========================")
        print(f"[+] User-Agent: No-UserAgent")
        print(f"[+] OutputFile: No-outputFile")
        print(f"[+] Crawling...")
        print("========================\n")

        user = {"user-agent": "Crawl2.0 - WebCrawler"}

        if regex == "link":
            try:
                req = urllib.request.urlopen(urllib.request.Request(url, headers=user))
                occurrences = re.findall(br"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-zA-Z][0-9a-zA-Z]))+", req.read())
                
                for link in occurrences:
                    print(f"Link: {link.decode()}")

                exit(0)

            except urllib.error.HTTPError as error:
                print("can't do the web request in this domain !!!")
                print(f"the web request returns status code: {error.code}")
                exit(0)

            except urllib.error.URLError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

            except ValueError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)
             

        elif regex == "phone":
            try:
                req = urllib.request.urlopen(urllib.request.Request(url, headers=user))
                occurrences = re.findall(br"([0-9]{3}|[0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})", req.read())
                
                for phones in occurrences:
                    print(f"phonephones: {phones.decode()}")

                exit(0)

            except urllib.error.HTTPError as error:
                print("can't do the web request in this domain !!!")
                print(f"the web request returns status code: {error.code}")
                exit(0)

            except urllib.error.URLError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

            except ValueError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)
             

        elif regex == "email":
            try:
                req = urllib.request.urlopen(urllib.request.Request(url, headers=user))
                occurrences = re.findall(br"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", req.read())
                
                for email in occurrences:
                    print(f"Emails: {email.decode()}")

                exit(0)

            except urllib.error.HTTPError as error:
                print("can't do the web request in this domain !!!")
                print(f"the web request returns status code: {error.code}")
                exit(0)

            except urllib.error.URLError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

            except ValueError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)

        else:
            try:
                req = urllib.request.urlopen(urllib.request.Request(url, headers=user))
                occurrences = re.findall(regex, req.read())
                
                for occu in occurrences:
                    print(f"Occurence: {occu.decode()}")

                exit(0)

            except urllib.error.HTTPError as error:
                print("can't do the web request in this domain !!!")
                print(f"the web request returns status code: {error.code}")
                exit(0)

            except urllib.error.URLError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)
            
            except ValueError:
                print("Invalid URL, pass like this: https://google.com, http://test.com")
                exit(0)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-u", "--url", help="set the URL: https://google.com, http://test.com", required=True)
    parser.add_argument("-r", "--regex", help="set one personalized regex or use one predefined: link, phone, email", required=True)
    parser.add_argument("-a", "--userAgent", help="set the user-agent")
    parser.add_argument("-O", "--output", help="set the output file name")

    args = parser.parse_args()


    url = str(args.url)

    if args.regex == "link":
        regex = "link"

    elif args.regex == "phone":
        regex = "phone"

    elif args.regex == "email":
        regex = "email"

    else:
        regex = str.encode(open(args.regex, "r").read())
        

    if args.userAgent:
        agent = args.userAgent
    
    else:
        agent = False 

    if args.output:
        fileName = args.output

    else:
        fileName = False

    crawl(url, regex, agent, fileName)

if __name__ == "__main__":
    main()