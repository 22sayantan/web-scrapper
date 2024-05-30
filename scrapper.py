import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def My_Scrapper(url,tag):

    header = { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    response = requests.get(url,headers = header)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

    # main_tag = soup.find_all('h2')
    Questions = soup.find_all(tag)
    # print(Questions)

    Ques_List = list()

    for ques in Questions:
        Ques_List.append(ques.text)

    return Ques_List

def list_to_csv(Q_list,file_name):
    list_len = len(Q_list)
    df = pd.DataFrame(Q_list)
    df.index +=1

    df.columns = ['Questions']
    print(df)
    df.to_csv(f'C:/Users/sayan/Desktop/Sayantan/Python/wEb ScraPper/questions_sheets/{file_name}.csv', encoding="utf-8-sig")
    print(f'your csv file for {file_name} is ready with {list_len} Questions !')

url_1 = 'https://www.javatpoint.com/javascript-interview-questions'
tag_1 = 'h3'
scraped_data_1 = My_Scrapper(url_1,tag_1)
scraped_data_1 = scraped_data_1[:-4]

url_2 = 'https://www.interviewbit.com/javascript-interview-questions/'
tag_2 = 'h3'
scraped_data_2 = My_Scrapper(url_2,tag_2)
scraped_data_2 = scraped_data_2[2:-3]

url_3 = 'https://www.simplilearn.com/tutorials/javascript-tutorial/javascript-interview-questions'
tag_3 = 'h3'
scraped_data_3 = My_Scrapper(url_3,tag_3)
scraped_data_3 = scraped_data_3[1:]

new_list = []
# '''
print(len(scraped_data_3))
for i in scraped_data_3:
    print(i)
    new_list.append(i)

# print(len((set(new_list))))
# '''


# '''
list_of_lists = [[new_list,'Javascript_Q_set']]
for i in list_of_lists:
    list_to_csv(i[0],i[1])
# '''
