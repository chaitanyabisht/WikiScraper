import urllib.parse as parse
import requests as r
from bs4 import BeautifulSoup

def wikiurl(serach_term):
    return f"https://en.wikipedia.org/wiki/{parse.quote(serach_term)}"

def clean_para(text): # Removes the references in paragraphs e.g. somerandomtext[30] -> somerandomtext
    i = 0  
    result = ''
    while (i < len(text)):
        if (text[i] == '['):
            while (text[i] != ']'):
                i += 1
            i += 1
            continue
        result += text[i]
        i += 1

    return result   

def article(url):
    page=r.get(url)
    soup = BeautifulSoup(page.content,'html.parser')

    content = soup.find('div',id="mw-content-text",class_="mw-body-content mw-content-ltr",lang = 'en',dir = 'ltr').div
    para_headings = content.find_all(['p','h2','h3','h4','h5'])

    ############
    heading = soup.find('h1',id = 'firstHeading').text
    heading_para = ''
    index = 1
    try:
        while (para_headings[index].name != 'h2'):
            heading_para += (para_headings[index].text) + '\n'
            index += 1
    except:
        pass
    #############

    i = 1
    result = {heading:heading_para}
    try:
        while para_headings[i] != None:
            obj = para_headings[i]
            
            if (obj.name == 'h2' and obj.text not in ['Contents','See also[edit]','See also','Notes[edit]','Notes','References[edit]','References','Further reading[edit]','Further reading','External links[edit]','External links']):
                key = (obj.text.split('['))[0]
                i += 1
                value = ''
                while (para_headings[i].name != 'h2'):
                    
                    value += (para_headings[i].text) + '\n'
                    i += 1

                i -= 1
                result[key] = value
                continue
            i+=1
            
    except:
        pass

    for key in result: #Cleaning Paragraphs
        result[key] = clean_para(result[key])

    return result

searchterm = str(input("Enter search term: "))
result = article(wikiurl(searchterm))


for key in result:
    print('*'*60)
    print(key,end = '\n\n')
    print(result[key])