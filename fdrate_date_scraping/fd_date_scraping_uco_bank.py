import requests 
from bs4 import BeautifulSoup
import datefinder 
from urllib.request import urlopen 
from datetime import datetime

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
bcode=110
url = "https://www.suryodaybank.com/deposits/fixed-deposit/rate-of-interest"

headers = {
  'Connection': 'keep-alive',
  'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
  'Accept': '*/*',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Origin': 'https://uk.eu-supply.com',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://uk.eu-supply.com/ctm/supplier/publictenders?B=BLUELIGHT',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cookie': 'EUSSESSION=b18ce90d-32b9-429c-8d74-7151a997e8cd'
}
payload="Branding=BLUELIGHT&SearchFilter.BrandingCode=BLUELIGHT&CpvContainer.CpvIds=&CpvContainer.CpvIds=&SearchFilter.PagingInfo.PageNumber=2&SearchFilter.PagingInfo.PageSize=25"

url = "https://www.ucobank.com/en/interest-rates-on-deposit-schemes"

def get_date():

    try:

        res = requests.get(url, headers=headers, data=payload)
        # print(res)
        if res.status_code==200:
            soup = BeautifulSoup(res.content, "html.parser")
            info = soup.find('div', id="mainbody")
            # print(info)
            content = info.find_all("strong")

            # print(content)
            cn = ""
            for i in content[2]:
                cn += i.text 
            # print(cn)
            dates = datefinder.find_dates(cn)

            redate = ""
            cnt = 0
            for date in dates:
                # print(date)
                if cnt==0:
                    cnt +=1
                    continue
                date_val = date.strftime("%d/%m/%y")
                redate += datetime.strptime(date_val, '%m/%d/%y').strftime("%d-%b-%y")

            return redate , bcode
        
        else:
            return "", bcode
        
    except:
        return "", bcode
    
# ans = get_date()
# print(ans)