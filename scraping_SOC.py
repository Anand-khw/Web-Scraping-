                                                                 # For Project Name , Link
import pandas as pd
from bs4 import BeautifulSoup
import requests
data=[]
url="https://shiveshcodes.github.io/wncc-soc.github.io/soc/"
page1=requests.get(url).text
soup=BeautifulSoup(page1,'lxml')
project = soup.find_all('div',class_='rounded hover-wrapper pr-3 pl-3 pt-3 pb-3 bg-white')
x=1
for links in project:
    link={}
    info = links.a['href']
    link['SNo.']=x
    link['Project']=links.find('p',class_='lead text-center font-weight-bold text-dark').text
    link['Link']="https://shiveshcodes.github.io"+info
    x+=1
    data.append(link)
df=pd.DataFrame(data)
df.to_csv('soc1.csv',index=False)
df


                                                          #For Project Name, Mentors, No. of Mentees, Link
import pandas as pd
from bs4 import BeautifulSoup
import requests

data={"S.No.":[],"Project Name":[],"Mentors":[],"No. of Mentees" : [],"Link":[]}
url="https://shiveshcodes.github.io/wncc-soc.github.io/soc/"
page1=requests.get(url).text
soup=BeautifulSoup(page1,'lxml')
project = soup.find_all('div',class_='rounded hover-wrapper pr-3 pl-3 pt-3 pb-3 bg-white')
p=1
for links in project:
    info = links.a['href']
    detail="https://shiveshcodes.github.io"+info
    data['S.No.'].append(p)
    data['Link'].append(detail)
    page2 = requests.get(detail).text
    soup2 = BeautifulSoup(page2,'lxml')
    project_info = soup2.find('div',class_='col-sm-10 col-md-8')
    table={"list_names" : []}
    data["Project Name"].append(project_info.h2.text)
    first_tag = project_info.find_all('p',class_='lead')
    for name in first_tag:
        names = name.text
        table['list_names'].append(names)
    number=table['list_names'].pop()
    data['Mentors'].append(table['list_names'])
    data['No. of Mentees'].append(number)
    p+=1
df = pd.DataFrame.from_dict(data)
df.to_csv('soc_assignment1.csv',index=False)
df
