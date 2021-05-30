import requests
from bs4 import BeautifulSoup

root_url = 'https://disp.cc/b/'
r = requests.get('https://disp.cc/b/pttHot')
# html.parser->對html內容的解析
soup = BeautifulSoup(r.text, 'html.parser')
# soup有比較常用的3功能 find|find_all|select 裡面參數的運用 1.是放tag 2.是條件
# for span in soup.find_all('span', class_='L34 nowrap listTitle'):
# 另一個寫法使用select(css用法去找)
for span in soup.select('#list span.listTitle'):  # 裡面的#是表示id
    # 取得tag裡面的屬性EX href, id, onclick等類型可用get或是dit[]的方式取得
    url_href = span.find('a').get('href')
    if url_href == '796-59l9':
        break
    url = root_url + url_href
    title = span.text
    print(f'{title}\n{url}')
