import urllib.request
import urllib.error
import argparse
import re


# Arguments 
# =====================================================================

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--link", help="Use this option to collect information from only one page, Example: -l google.com, -l facebook.com")
parser.add_argument("-L", "--LINK", help="Use this option to collect information from multiple pages, Example: -L google.com, -L facebook.com")
parser.add_argument("-t", "--type", help="use this option to set what you'll want to collect, OBS: use phone(phone), link(links), email(emails). if you haven't even chosen one of the options, put the name of a file that contains a regular expression that you want", required=True)
parser.add_argument("-w", "--wordlist", help="pass the name of the wordlist file")
parser.add_argument("-o", "--output", help="pass the name you want to the output file")
parser.add_argument("-u", "--useragent", help="pass the user agent")

arguments = parser.parse_args()


# Menu
# =====================================================================

def menu():
    print(".......-:......:-.......")
    print("...=..-W-......-W-..=...")
    print("..*=..#@........@#..=*..")
    print(".-W+.:W=..=WW=..=W:.+W-.")
    print(".+W:.+W*.*WWWW+.*W*.:W+.")
    print(".*W-.+W*.:WWWW:.*W+.-W*.")
    print(".*W*..#W**=WW=**W#..*W*.")
    print("..:====#@WWWWWW@#====:..")
    print("-+#WWWW##WWWWWW##WWWW#+-")
    print("WW+.+W+.#WWWWWW#.+W+.+WW")
    print("*W:.:W*.@WWWWWW#.*W:.:W*")
    print(".@#..#@.*WWWWWW*.@#..#@-")
    print(".:W:.-W:-@WWWW@-:W-.:W:.")
    print("..:@..:=..*WW*..=:..@:..")
    print("...-*..--......--..*-...")
    print("|")
    print("|-BY sh4d0wgh0s7.py")
    print("")


# Simple Crawl
# =====================================================================

def simpleCrawl(domain, type):
    try:
        print(f"Crawling in {domain}...")
        print("")

        req = urllib.request.urlopen(urllib.request.Request(f"http://{domain}"))
        crawled = re.findall(type, req.read())

        for crawl in crawled:
            print(f"[+] {crawl}")

    except urllib.error.URLError:
        print("could not make a request in this domain")

    except urllib.error.HTTPError:
        print("the page does not exist")

    except KeyboardInterrupt:
        print("Bye Bye")

    except Exception as erro:
        print("an unknown error has occurred !")
        print(erro)
    
# With Output
# =====================================================================

def simpleCrawlOutput(domain, type, output):
    try:
        print(f"Crawling in {domain}...")
        print("")

        req = urllib.request.urlopen(urllib.request.Request(f"http://{domain}"))
        crawled = re.findall(type, req.read())

        if crawled:
            file = open(output, "a")

            for crawl in crawled:
                print(f"[+] {crawl}")
                file.write(f"[+] {crawl}\n")

        file.close()

    except urllib.error.URLError:
        print("could not make a request in this domain")

    except urllib.error.HTTPError:
        print("the page does not exist")

    except KeyboardInterrupt:
        print("Bye Bye")

    except Exception as erro:
        print("an unknown error has occurred !")
        print(erro)


# With User-agent
# =====================================================================

def simpleCrawlUseragent(domain, type, user):
    try: 
        print(f"Crawling in {domain}...")
        print(f"user-agent: {user}")
        print("")

        useragent = {"user-agent": user}

        req = urllib.request.urlopen(urllib.request.Request(f"http://{domain}", headers=useragent))
        crawled = re.findall(type, req.read())

        for crawl in crawled:
            print(f"[+] {crawl}")

    except urllib.error.URLError:
        print("could not make a request in this domain")

    except urllib.error.HTTPError:
        print("the page does not exist")

    except KeyboardInterrupt:
        print("Bye Bye")

    except Exception as erro:
        print("an unknown error has occurred !")
        print(erro)


# With User-agent and output
# =====================================================================

def simpleCrawlUseragentOutput(domain, type, user, output):
    try: 
        print(f"Crawling in {domain}...")
        print(f"user-agent: {user}")
        print("")

        useragent = {"user-agent": user}
        file = open(output, "a")

        req = urllib.request.urlopen(urllib.request.Request(f"http://{domain}", headers=useragent))
        crawled = re.findall(type, req.read())

        if crawled:
            file = open(output, "a")

            for crawl in crawled:
                print(f"[+] {crawl}")
                file.write(f"[+] {crawl}\n")

        file.close()

    except urllib.error.URLError:
        print("could not make a request in this domain")

    except urllib.error.HTTPError:
        print("the page does not exist")

    except KeyboardInterrupt:
        print("Bye Bye")

    except Exception as erro:
        print("an unknown error has occurred !")
        print(erro)





def crawlDir(domain, type, wordlist):
    try:
        print(f"Crawling in {domain}...")
        print("")

        for word in wordlist:
            req = urllib.request.urlopen(urllib.request.Request(f"http://{domain}/{word}"))
            crawled = re.findall(type, req.read())

            for crawl in crawled:
                print(f"[+] {crawl}")


    except urllib.error.HTTPError:
        pass

    except urllib.error.URLError:
        print("could not make a request in this domain")
        
    except KeyboardInterrupt:
        print("Bye Bye")

    except Exception as erro:
        print("an unknown error has occurred !")
        print(erro)


def crawlDirOutput(domain, type, wordlist, output):
    try:
        print(f"Crawling in {domain}...")
        print("")

        file = open(output, "a")

        for word in wordlist:
            req = urllib.request.urlopen(urllib.request.Request(f"http://{domain}/{word}"))
            crawled = re.findall(type, req.read())

            if crawled:
                file = open(output, "a")

                for crawl in crawled:
                    print(f"[+] {crawl}")
                    file.write(f"[+] {crawl}\n")

        file.close()

    
    except urllib.error.HTTPError:
        pass

    except urllib.error.URLError:
        print("could not make a request in this domain")
        
    except KeyboardInterrupt:
        print("Bye Bye")

    except Exception as erro:
        print("an unknown error has occurred !")
        print(erro)



def crawlDirUseragent(domain, type, wordlist, user):
    try:
        print(f"Crawling in {domain}...")
        print(f"user-agent: {user}")
        print("")

        useragent = {"user-agent": user}
        
        for word in wordlist:
            req = urllib.request.urlopen(urllib.request.Request(f"http://{domain}/{word}", headers=useragent))
            crawled = re.findall(type, req.read())

            for crawl in crawled:
                print(f"[+] {crawl}")

    
    except urllib.error.HTTPError:
        pass

    except urllib.error.URLError:
        print("could not make a request in this domain")
        
    except KeyboardInterrupt:
        print("Bye Bye")

    except Exception as erro:
        print("an unknown error has occurred !")
        print(erro)


def crawlDirUseragentOutput(domain, type, wordlist, user, output):
    try:
        print(f"Crawling in {domain}...")
        print(f"user-agent: {user}")
        print("")

        file = open(output, "a")
        useragent = {"user-agent": user}
        
        for word in wordlist:
            req = urllib.request.urlopen(urllib.request.Request(f"http://{domain}/{word}", headers=useragent))
            crawled = re.findall(type, req.read())

            if crawled:
                file = open(output, "a")

                for crawl in crawled:
                    print(f"[+] {crawl}")
                    file.write(f"[+] {crawl}\n")
            
        file.close()

    except urllib.error.HTTPError:
        pass

    except urllib.error.URLError:
        print("could not make a request in this domain")
        
    except KeyboardInterrupt:
        print("Bye Bye")

    except Exception as erro:
        print("an unknown error has occurred !")
        print(erro)



# The Main program 

type = arguments.type

if arguments.link:
    domain = arguments.link 

    if arguments.useragent:
        useragent = open(arguments.useragent, "r").read()

        if arguments.output:
            # crawler with useragent and output
            # =====================================================================
            file = arguments.output
            
            if type == "phone":
                type = br"([0-9]{3}|[0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
                menu()
                simpleCrawlUseragentOutput(domain, type, useragent, file)

            elif type == "link":
                type = br"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-zA-Z][0-9a-zA-Z]))+"
                menu()
                simpleCrawlUseragentOutput(domain, type, useragent, file)

            elif type == "email":
                type = br"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
                menu()
                simpleCrawlUseragentOutput(domain, type, useragent, file)

            else:
                type = str.encode(open(type, "r").read())
                menu()
                simpleCrawlUseragentOutput(domain,type, useragent, file)

        else:
            # Crawler with useragent
            # =====================================================================
            if type == "phone":
                type = br"([0-9]{3}|[0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})" 
                menu()
                simpleCrawlUseragent(domain, type, useragent)

            elif type == "link":
                type = br"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-zA-Z][0-9a-zA-Z]))+"
                menu()
                simpleCrawlUseragent(domain, type, useragent)

            elif type == "email":
                type = br"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
                menu()
                simpleCrawlUseragent(domain, type, useragent)

            else:
                type = str.encode(open(type, "r").read())
                menu()
                simpleCrawlUseragent(domain, type, useragent)

    else:
        # Simple crawler
        # =====================================================================  
        if type == "phone":
            type = br"([0-9]{3}|[0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
            menu()
            simpleCrawl(domain, type)

        elif type == "link":
            type = br"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-zA-Z][0-9a-zA-Z]))+"
            menu()
            simpleCrawl(domain, type)

        elif type == "email":
            type = br"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
            menu()
            simpleCrawl(domain, type)
        
        else:
            type = str.encode(open(type, "r").read())
            menu()
            simpleCrawl(domain, type)


elif arguments.LINK:
    domain = arguments.LINK
    wordlist = open(arguments.wordlist, "r").read()

    if arguments.useragent:
        useragent = open(arguments.useragent, "r").read()

        if arguments.output:
            file = arguments.output

            if arguments.type == "phone":
                type = br"([0-9]{3}|[0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
                menu()
                crawlDirUseragentOutput(domain, type, wordlist, useragent, file)

            elif arguments.type == "link":
                type = br"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-zA-Z][0-9a-zA-Z]))+"
                menu()
                crawlDirUseragentOutput(domain, type, wordlist, useragent, file)

            elif arguments.type == "email":
                type = br"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
                menu()
                crawlDirUseragentOutput(domain, type, wordlist, useragent, file)

            else:
                type = str.encode(open(type, "r").read())
                menu()
                crawlDirUseragentOutput(domain, type, wordlist, useragent, file)

        else:
            if arguments.type == "phone":
                type = br"([0-9]{3}|[0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
                menu()
                crawlDirUseragent(domain, type, wordlist, useragent)

            elif arguments.type == "link":
                type = br"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-zA-Z][0-9a-zA-Z]))+"
                menu()
                crawlDirUseragent(domain, type, wordlist, useragent)

            elif arguments.type == "email":
                type = br"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
                menu()
                crawlDirUseragent(domain, type, wordlist, useragent)

            else:
                type = str.encode(open(type, "r").read())
                menu()
                crawlDirUseragent(domain, type, wordlist, useragent)
            

    else:
        if arguments.type == "phone":
            type = br"([0-9]{3}|[0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
            menu()
            crawlDir(domain, type, wordlist)
     
        elif arguments.type == "link":
            type = br"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-zA-Z][0-9a-zA-Z]))+"
            menu()
            crawlDir(domain, type, wordlist)

        elif arguments.type == "email":
            type = br"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
            menu()
            crawlDir(domain, type, wordlist)

        else:
            type = str.encode(open(type, "r").read())
            menu()
            crawlDir(domain, type, wordlist)