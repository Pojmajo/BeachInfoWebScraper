import requests
from bs4 import BeautifulSoup
import Constants


class BeachScraper:
    def __init__(self):
        self.URL = Constants.WEB_URL
        try:
            self.page = requests.get(self.URL)
            self.soup = BeautifulSoup(self.page.content, "html.parser")
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def weather_conditions(self, dictionary):
        results = self.soup.find_all("div", class_='sekcja')
        for div in results:
            beach_name = div.find('div', class_='tytul').text.rstrip()
            air_temperature = div.find('div', class_='temp_pow').text.rstrip()
            water_temperature = div.find('div', class_='temp_wody').text.rstrip()
            flag_color_url = div.find('div', class_='flaga').img['src']
            flag_color = flag_color_url.split("/")[-1:]
            flag_color = flag_color[0].split('_', 1)[-1].rstrip('.png')
            if beach_name in dictionary:
                dictionary[beach_name].extend((air_temperature, water_temperature))
                if flag_color == 'czerwona':
                    dictionary[beach_name].append('red')
                elif flag_color == 'biała':
                    dictionary[beach_name].append('white')
                else:
                    dictionary[beach_name].append('blue')
                    print("We have no data about weather conditions at the %s beach." % beach_name)
            else:
                print('Oh no! There are no such beach in our dictionary!')
