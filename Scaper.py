import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

base_url = "https://www.transfermarkt.com/transfers/neuestetransfers/statistik?land_id=0&wettbewerb_id=alle&minMarktwert=500000&maxMarktwert=500000000&plus=1&page="

total_pages = 8
data = []

for page in range(1, total_pages + 1):
    url = base_url + str(page)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='items')
    rows = table.find_all('tr', class_=['odd', 'even'])

    for row in rows[3:]:
        player_info = {
            'Player': row.find_all('td')[0].find('img')['alt'],
            'Age': row.find_all('td')[4].text,
            'Nationality': row.find_all('td')[5].find('img')['alt'],
            'Left Team': row.find_all('td')[8].find('a')['title'],
            'Joined Team': row.find_all('td')[12].find('a')['title'],
            'Transfer Date': row.find_all('td')[14].text,
            'Market Value': row.find_all('td')[15].text.replace('€', '').strip(),
            'Fee': row.find_all('td')[16].text.replace('€', '').replace(',', '').strip()
        }
        data.append(player_info)

df = pd.DataFrame(data)




csv_filename = 'transfer_data_final.csv'
df.to_csv(csv_filename, index=False)

print(f"Data saved to {csv_filename}")
