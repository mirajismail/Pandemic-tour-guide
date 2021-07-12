import requests

'''
params:
name of country


returns string with brief descripsion about tourist entry

'''


def getTravelRestrictions(name):

    #string manip
    x = ""

    x = name.strip()
    x = x.lower()
    x = x.replace(" ", "-")

    url = "https://blog.wego.com/{}-travel-restrictions-and-quarantine-requirements/".format(x)

    #print(url)

    
    #make request
    result = requests.get(url)
    src = result.content
    lines = src.splitlines()


    #info is always on line 20 apparently
    allwords = str(lines[20])

    #print(allwords)
    
    ind = allwords.find('Tourist Entry')
    end = allwords.find('Testing')
    
    #parse the content from the html
    allwords = allwords[ind:end]


    return allwords.strip()
    
    
    
    
        
        
    
        

#tester code
if __name__ == "__main__":
    
    print(getTravelRestrictions("sweden"))
