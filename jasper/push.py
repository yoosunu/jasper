import requests
from bs4 import BeautifulSoup
# import login

class pusher:

    def extract_code_max():

        #login_function
        # login.login_jbnu()  

        url = "https://www.jbnu.ac.kr/kor/?menuID=139"
        request = requests.get(url, headers={"User-Agent": "Push"})
        codes = []
        if request.status_code == 200:
            soup = BeautifulSoup(request.text, "html.parser")
            table = soup.find("table", class_="ta_bo")
            tbody = table.find("tbody")
            trs = tbody.find_all("tr")

            for tr in trs:
                anchor = tr.find('a')
                link = anchor['href']
                link_code = link[-5:]
                
                codes.append(link_code)
            code_max = max(codes)
                    
        else:
            print("cannot access to site.")
        
        return code_max
    
    def extract_link_code():

        #login_function
        # login.login_jbnu()  

        url = "https://www.jbnu.ac.kr/kor/?menuID=139"
        request = requests.get(url, headers={"User-Agent": "Push"})
        # result = [] #using when extract informations
        info_extracted = [] 
        if request.status_code == 200:
            soup = BeautifulSoup(request.text, "html.parser")
            table = soup.find("table", class_="ta_bo")
            tbody = table.find("tbody")
            trs = tbody.find_all("tr")
            trs.pop(0)
            trs.pop(0)
            
            for tr in trs:
                anchor = tr.find('a')
                link = anchor['href']
                link_code = link[-5:]
                text_not_modified = anchor['title']
                text = text_not_modified[:-3]
                # link_code = tr.find("th", class_="mnom").string.strip() # use this code at push alarm

                
                # extract informations

                notice_info = {
                    'link': link,
                    'link_code': link_code,
                    'text': text,
                }
                # link_extrated = notice_info['link']
                link_code_extracted = notice_info["link_code"]
                link_code_needToPrint = f"https://www.jbnu.ac.kr/kor/?menuID=139&mode=view&no={link_code_extracted}"
                text_extracted = notice_info['text']
                
                # result.append(notice_info)
                info_extracted.extend([link_code_needToPrint])                    
        else:
            print("cannot access to site.")
        
        return link_code_needToPrint
    
    def extract_text():

        #login_function
        # login.login_jbnu()  

        url = "https://www.jbnu.ac.kr/kor/?menuID=139"
        request = requests.get(url, headers={"User-Agent": "Push"})
        # result = [] #using when extract informations
        info_extracted = [] 
        if request.status_code == 200:
            soup = BeautifulSoup(request.text, "html.parser")
            table = soup.find("table", class_="ta_bo")
            tbody = table.find("tbody")
            trs = tbody.find_all("tr")
            trs.pop(0)
            trs.pop(0)
            
            for tr in trs:
                anchor = tr.find('a')
                link = anchor['href']
                link_code = link[-5:]
                text_not_modified = anchor['title']
                text = text_not_modified[:-3]
                # link_code = tr.find("th", class_="mnom").string.strip() # use this code at push alarm

                
                # extract informations

                notice_info = {
                    'link': link,
                    'link_code': link_code,
                    'text': text,
                }
                # link_extrated = notice_info['link']
                link_code_extracted = notice_info["link_code"]
                link_code_needToPrint = f"https://www.jbnu.ac.kr/kor/?menuID=139&mode=view&no={link_code_extracted}"
                text_extracted = notice_info['text']
                
                # result.append(notice_info)
                info_extracted.extend([text_extracted])                    
        else:
            print("cannot access to site.")
        
        return text_extracted
    
    
     


    