import folium
from Scraper import BeachScraper
import Constants


def main():
    beaches_in_gdansk = Constants.coordinatesDict
    scraper = BeachScraper()
    scraper.weather_conditions(beaches_in_gdansk)
    map_gdansk = folium.Map(location=Constants.GDANSK, zoom_start=12)
    fg = folium.FeatureGroup(name="Gdansk beaches")
    for key, value in beaches_in_gdansk.items():
        fg.add_child(folium.Marker(location=value[:2], popup=key + "\nTemperatura powietrza: " + value[2] + "\nTemperatura wody: " + value[3], icon=folium.Icon(color=value[-1])))
    map_gdansk.add_child(fg)
    map_gdansk.save(Constants.BEACHES_URL)


if __name__ == "__main__":
    main()
