import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st


# Function to scrape weather data
def scrape_weather():
    # url = "https://www.accuweather.com/en/pk/pakistan-weather"	

    html_content = '''<div class="nearby-locations-list">
    <div class="nearby-locations-list">
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=258955&amp;target=">
				<span class="text title no-wrap">Abbottabad</span>
				<svg class="icon" data-src="/images/weathericons/38.svg" viewBox="0 0 288 288" width="128" height="128"><g stroke-width="9.63" fill="none" fill-rule="evenodd"><path d="M235.937 174.607A64.663 64.663 0 0 0 272 146.826c-25.176 5.672-51.244-4.75-65.569-26.217-14.325-21.466-13.945-49.538.954-70.609-28.582 4.311-50.778 27.157-54.263 55.852" stroke="#686763" stroke-linejoin="bevel"></path><path d="M71.993 237.44c-30.58-.066-55.317-24.91-55.25-55.49.066-30.58 24.91-55.316 55.49-55.25h9.293c17.698-20.794 46.193-28.857 72.163-20.418 25.97 8.438 44.283 31.71 46.378 58.937h11.652c19.943 0 36.11 16.167 36.11 36.11 0 19.944-16.167 36.112-36.11 36.112H71.993Z" stroke="#BABABA"></path></g></svg>
				<span class="text temp">11°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=259613&amp;target=">
				<span class="text title no-wrap">Ahmadpur East</span>
				<svg class="icon" data-src="/images/weathericons/33.svg" viewBox="0 0 288 288" width="128" height="128"><path d="M221.96 203.022a106.311 106.311 0 0 1-106.68-106.31 105.34 105.34 0 0 1 19.875-61.661C85.26 42.978 47.299 84.06 43.33 134.424c-3.97 50.363 27.09 96.885 75.125 112.53 48.035 15.645 100.534-3.664 126.986-46.705a106.311 106.311 0 0 1-23.481 2.773Z" stroke="#686763" stroke-width="9.244" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="bevel"></path></svg>
				<span class="text temp">20°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=259636&amp;target=">
				<span class="text title no-wrap">Bahawalpur</span>
				<svg class="icon" data-src="/images/weathericons/33.svg" viewBox="0 0 288 288" width="128" height="128"><path d="M221.96 203.022a106.311 106.311 0 0 1-106.68-106.31 105.34 105.34 0 0 1 19.875-61.661C85.26 42.978 47.299 84.06 43.33 134.424c-3.97 50.363 27.09 96.885 75.125 112.53 48.035 15.645 100.534-3.664 126.986-46.705a106.311 106.311 0 0 1-23.481 2.773Z" stroke="#686763" stroke-width="9.244" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="bevel"></path></svg>
				<span class="text temp">19°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=260626&amp;target=">
				<span class="text title no-wrap">Faisalabad</span>
				<svg class="icon" data-src="/images/weathericons/35.svg" viewBox="0 0 288 288" width="128" height="128"><g stroke-width="8.792" fill="none" fill-rule="evenodd"><path d="M136.323 121.88a100.498 100.498 0 0 1 16.398-80.978 103.839 103.839 0 0 0-86.782 121.731M93.943 216.003a104.718 104.718 0 0 0 163.672-17.98 102.564 102.564 0 0 1-61.943-5.496" stroke="#686763" stroke-linejoin="bevel"></path><path d="M159.095 135.596h-5.407c-12.979-16.162-34.666-22.506-54.309-15.886-19.643 6.62-33.066 24.796-33.615 45.517h-7.87a25.41 25.41 0 1 0 0 50.776h101.114a40.225 40.225 0 1 0 0-80.407h.087Z" stroke="#BABABA"></path></g></svg>
				<span class="text temp">17°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=260623&amp;target=">
				<span class="text title no-wrap">Gujranwala</span>
				<svg class="icon" data-src="/images/weathericons/36.svg" viewBox="0 0 288 288" width="128" height="128"><g stroke-width="10.764" fill="none" fill-rule="evenodd"><path d="M189.565 73.268h4.952a26.91 26.91 0 0 1 48.009-16.147h9.095c11.89 0 21.529 9.64 21.529 21.529 0 11.89-9.639 21.529-21.529 21.529h-62.056c-7.43 0-13.455-6.025-13.455-13.456 0-7.431 6.024-13.455 13.455-13.455Z" stroke="#BABABA"></path><path d="M123.85 261.643c57.675 22.82 123.414 1.058 156.082-51.669-50.074 11.483-102.036-9.155-130.585-51.865-28.549-42.71-27.75-98.614 2.005-140.493A127.072 127.072 0 0 0 50.114 185.379" stroke="#686763" stroke-linejoin="bevel"></path><path d="M39.134 191.675h4.737a43.057 43.057 0 0 1 76.534 25.834h6.889c11.778.582 21.03 10.301 21.03 22.094 0 11.793-9.252 21.512-21.03 22.094h-88.16c-18.568-1.03-33.096-16.388-33.096-34.984 0-18.597 14.528-33.954 33.096-34.984v-.054Z" stroke="#BABABA"></path></g></svg>
				<span class="text temp">18°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=259633&amp;target=">
				<span class="text title no-wrap">Gujrat</span>
				<svg class="icon" data-src="/images/weathericons/36.svg" viewBox="0 0 288 288" width="128" height="128"><g stroke-width="10.764" fill="none" fill-rule="evenodd"><path d="M189.565 73.268h4.952a26.91 26.91 0 0 1 48.009-16.147h9.095c11.89 0 21.529 9.64 21.529 21.529 0 11.89-9.639 21.529-21.529 21.529h-62.056c-7.43 0-13.455-6.025-13.455-13.456 0-7.431 6.024-13.455 13.455-13.455Z" stroke="#BABABA"></path><path d="M123.85 261.643c57.675 22.82 123.414 1.058 156.082-51.669-50.074 11.483-102.036-9.155-130.585-51.865-28.549-42.71-27.75-98.614 2.005-140.493A127.072 127.072 0 0 0 50.114 185.379" stroke="#686763" stroke-linejoin="bevel"></path><path d="M39.134 191.675h4.737a43.057 43.057 0 0 1 76.534 25.834h6.889c11.778.582 21.03 10.301 21.03 22.094 0 11.793-9.252 21.512-21.03 22.094h-88.16c-18.568-1.03-33.096-16.388-33.096-34.984 0-18.597 14.528-33.954 33.096-34.984v-.054Z" stroke="#BABABA"></path></g></svg>
				<span class="text temp">17°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=261159&amp;target=">
				<span class="text title no-wrap">Hyderabad</span>
				<svg class="icon" data-src="/images/weathericons/33.svg" viewBox="0 0 288 288" width="128" height="128"><path d="M221.96 203.022a106.311 106.311 0 0 1-106.68-106.31 105.34 105.34 0 0 1 19.875-61.661C85.26 42.978 47.299 84.06 43.33 134.424c-3.97 50.363 27.09 96.885 75.125 112.53 48.035 15.645 100.534-3.664 126.986-46.705a106.311 106.311 0 0 1-23.481 2.773Z" stroke="#686763" stroke-width="9.244" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="bevel"></path></svg>
				<span class="text temp">24°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=258278&amp;target=">
				<span class="text title no-wrap">Islamabad</span>
				<svg class="icon" data-src="/images/weathericons/38.svg" viewBox="0 0 288 288" width="128" height="128"><g stroke-width="9.63" fill="none" fill-rule="evenodd"><path d="M235.937 174.607A64.663 64.663 0 0 0 272 146.826c-25.176 5.672-51.244-4.75-65.569-26.217-14.325-21.466-13.945-49.538.954-70.609-28.582 4.311-50.778 27.157-54.263 55.852" stroke="#686763" stroke-linejoin="bevel"></path><path d="M71.993 237.44c-30.58-.066-55.317-24.91-55.25-55.49.066-30.58 24.91-55.316 55.49-55.25h9.293c17.698-20.794 46.193-28.857 72.163-20.418 25.97 8.438 44.283 31.71 46.378 58.937h11.652c19.943 0 36.11 16.167 36.11 36.11 0 19.944-16.167 36.112-36.11 36.112H71.993Z" stroke="#BABABA"></path></g></svg>
				<span class="text temp">17°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=259634&amp;target=">
				<span class="text title no-wrap">Jhang</span>
				<svg class="icon" data-src="/images/weathericons/35.svg" viewBox="0 0 288 288" width="128" height="128"><g stroke-width="8.792" fill="none" fill-rule="evenodd"><path d="M136.323 121.88a100.498 100.498 0 0 1 16.398-80.978 103.839 103.839 0 0 0-86.782 121.731M93.943 216.003a104.718 104.718 0 0 0 163.672-17.98 102.564 102.564 0 0 1-61.943-5.496" stroke="#686763" stroke-linejoin="bevel"></path><path d="M159.095 135.596h-5.407c-12.979-16.162-34.666-22.506-54.309-15.886-19.643 6.62-33.066 24.796-33.615 45.517h-7.87a25.41 25.41 0 1 0 0 50.776h101.114a40.225 40.225 0 1 0 0-80.407h.087Z" stroke="#BABABA"></path></g></svg>
				<span class="text temp">18°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=261158&amp;target=">
				<span class="text title no-wrap">Karachi</span>
				<svg class="icon" data-src="/images/weathericons/33.svg" viewBox="0 0 288 288" width="128" height="128"><path d="M221.96 203.022a106.311 106.311 0 0 1-106.68-106.31 105.34 105.34 0 0 1 19.875-61.661C85.26 42.978 47.299 84.06 43.33 134.424c-3.97 50.363 27.09 96.885 75.125 112.53 48.035 15.645 100.534-3.664 126.986-46.705a106.311 106.311 0 0 1-23.481 2.773Z" stroke="#686763" stroke-width="9.244" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="bevel"></path></svg>
				<span class="text temp">21°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=260622&amp;target=">
				<span class="text title no-wrap">Lahore</span>
				<svg class="icon" data-src="/images/weathericons/11.svg" viewBox="0 0 288 288" width="128" height="128"><g stroke="#BABABA" stroke-width="10.214" fill="none" fill-rule="evenodd"><path d="M261.77 160a58.681 58.681 0 0 0-54.033-81.715h-9.857c-18.765-22.093-49.013-30.67-76.583-21.715-27.57 8.954-47.004 33.669-49.206 62.572H59.783a38.304 38.304 0 0 0-38.354 38.304V160H261.77ZM1 195.75h285.949M1 160h285.949M1 231.55h285.949"></path></g></svg>
				<span class="text temp">17°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=260831&amp;target=">
				<span class="text title no-wrap">Larkana</span>
				<svg class="icon" data-src="/images/weathericons/33.svg" viewBox="0 0 288 288" width="128" height="128"><path d="M221.96 203.022a106.311 106.311 0 0 1-106.68-106.31 105.34 105.34 0 0 1 19.875-61.661C85.26 42.978 47.299 84.06 43.33 134.424c-3.97 50.363 27.09 96.885 75.125 112.53 48.035 15.645 100.534-3.664 126.986-46.705a106.311 106.311 0 0 1-23.481 2.773Z" stroke="#686763" stroke-width="9.244" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="bevel"></path></svg>
				<span class="text temp">21°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=260624&amp;target=">
				<span class="text title no-wrap">Multan</span>
				<svg class="icon" data-src="/images/weathericons/11.svg" viewBox="0 0 288 288" width="128" height="128"><g stroke="#BABABA" stroke-width="10.214" fill="none" fill-rule="evenodd"><path d="M261.77 160a58.681 58.681 0 0 0-54.033-81.715h-9.857c-18.765-22.093-49.013-30.67-76.583-21.715-27.57 8.954-47.004 33.669-49.206 62.572H59.783a38.304 38.304 0 0 0-38.354 38.304V160H261.77ZM1 195.75h285.949M1 160h285.949M1 231.55h285.949"></path></g></svg>
				<span class="text temp">19°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=259370&amp;target=">
				<span class="text title no-wrap">Peshawar</span>
				<svg class="icon" data-src="/images/weathericons/35.svg" viewBox="0 0 288 288" width="128" height="128"><g stroke-width="8.792" fill="none" fill-rule="evenodd"><path d="M136.323 121.88a100.498 100.498 0 0 1 16.398-80.978 103.839 103.839 0 0 0-86.782 121.731M93.943 216.003a104.718 104.718 0 0 0 163.672-17.98 102.564 102.564 0 0 1-61.943-5.496" stroke="#686763" stroke-linejoin="bevel"></path><path d="M159.095 135.596h-5.407c-12.979-16.162-34.666-22.506-54.309-15.886-19.643 6.62-33.066 24.796-33.615 45.517h-7.87a25.41 25.41 0 1 0 0 50.776h101.114a40.225 40.225 0 1 0 0-80.407h.087Z" stroke="#BABABA"></path></g></svg>
				<span class="text temp">14°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=257185&amp;target=">
				<span class="text title no-wrap">Quetta</span>
				<svg class="icon" data-src="/images/weathericons/33.svg" viewBox="0 0 288 288" width="128" height="128"><path d="M221.96 203.022a106.311 106.311 0 0 1-106.68-106.31 105.34 105.34 0 0 1 19.875-61.661C85.26 42.978 47.299 84.06 43.33 134.424c-3.97 50.363 27.09 96.885 75.125 112.53 48.035 15.645 100.534-3.664 126.986-46.705a106.311 106.311 0 0 1-23.481 2.773Z" stroke="#686763" stroke-width="9.244" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="bevel"></path></svg>
				<span class="text temp">6°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=260625&amp;target=">
				<span class="text title no-wrap">Rawalpindi</span>
				<svg class="icon" data-src="/images/weathericons/38.svg" viewBox="0 0 288 288" width="128" height="128"><g stroke-width="9.63" fill="none" fill-rule="evenodd"><path d="M235.937 174.607A64.663 64.663 0 0 0 272 146.826c-25.176 5.672-51.244-4.75-65.569-26.217-14.325-21.466-13.945-49.538.954-70.609-28.582 4.311-50.778 27.157-54.263 55.852" stroke="#686763" stroke-linejoin="bevel"></path><path d="M71.993 237.44c-30.58-.066-55.317-24.91-55.25-55.49.066-30.58 24.91-55.316 55.49-55.25h9.293c17.698-20.794 46.193-28.857 72.163-20.418 25.97 8.438 44.283 31.71 46.378 58.937h11.652c19.943 0 36.11 16.167 36.11 36.11 0 19.944-16.167 36.112-36.11 36.112H71.993Z" stroke="#BABABA"></path></g></svg>
				<span class="text temp">15°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=259647&amp;target=">
				<span class="text title no-wrap">Sargodha</span>
				<svg class="icon" data-src="/images/weathericons/36.svg" viewBox="0 0 288 288" width="128" height="128"><g stroke-width="10.764" fill="none" fill-rule="evenodd"><path d="M189.565 73.268h4.952a26.91 26.91 0 0 1 48.009-16.147h9.095c11.89 0 21.529 9.64 21.529 21.529 0 11.89-9.639 21.529-21.529 21.529h-62.056c-7.43 0-13.455-6.025-13.455-13.456 0-7.431 6.024-13.455 13.455-13.455Z" stroke="#BABABA"></path><path d="M123.85 261.643c57.675 22.82 123.414 1.058 156.082-51.669-50.074 11.483-102.036-9.155-130.585-51.865-28.549-42.71-27.75-98.614 2.005-140.493A127.072 127.072 0 0 0 50.114 185.379" stroke="#686763" stroke-linejoin="bevel"></path><path d="M39.134 191.675h4.737a43.057 43.057 0 0 1 76.534 25.834h6.889c11.778.582 21.03 10.301 21.03 22.094 0 11.793-9.252 21.512-21.03 22.094h-88.16c-18.568-1.03-33.096-16.388-33.096-34.984 0-18.597 14.528-33.954 33.096-34.984v-.054Z" stroke="#BABABA"></path></g></svg>
				<span class="text temp">17°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=259648&amp;target=">
				<span class="text title no-wrap">Sheikhupura</span>
				<svg class="icon" data-src="/images/weathericons/36.svg" viewBox="0 0 288 288" width="128" height="128"><g stroke-width="10.764" fill="none" fill-rule="evenodd"><path d="M189.565 73.268h4.952a26.91 26.91 0 0 1 48.009-16.147h9.095c11.89 0 21.529 9.64 21.529 21.529 0 11.89-9.639 21.529-21.529 21.529h-62.056c-7.43 0-13.455-6.025-13.455-13.456 0-7.431 6.024-13.455 13.455-13.455Z" stroke="#BABABA"></path><path d="M123.85 261.643c57.675 22.82 123.414 1.058 156.082-51.669-50.074 11.483-102.036-9.155-130.585-51.865-28.549-42.71-27.75-98.614 2.005-140.493A127.072 127.072 0 0 0 50.114 185.379" stroke="#686763" stroke-linejoin="bevel"></path><path d="M39.134 191.675h4.737a43.057 43.057 0 0 1 76.534 25.834h6.889c11.778.582 21.03 10.301 21.03 22.094 0 11.793-9.252 21.512-21.03 22.094h-88.16c-18.568-1.03-33.096-16.388-33.096-34.984 0-18.597 14.528-33.954 33.096-34.984v-.054Z" stroke="#BABABA"></path></g></svg>
				<span class="text temp">18°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=259649&amp;target=">
				<span class="text title no-wrap">Sialkot</span>
				<svg class="icon" data-src="/images/weathericons/11.svg" viewBox="0 0 288 288" width="128" height="128"><g stroke="#BABABA" stroke-width="10.214" fill="none" fill-rule="evenodd"><path d="M261.77 160a58.681 58.681 0 0 0-54.033-81.715h-9.857c-18.765-22.093-49.013-30.67-76.583-21.715-27.57 8.954-47.004 33.669-49.206 62.572H59.783a38.304 38.304 0 0 0-38.354 38.304V160H261.77ZM1 195.75h285.949M1 160h285.949M1 231.55h285.949"></path></g></svg>
				<span class="text temp">16°</span>
			</a>
			<a class="nearby-location weather-card" href="/web-api/three-day-redirect?key=260835&amp;target=">
				<span class="text title no-wrap">Sukkur</span>
				<svg class="icon" data-src="/images/weathericons/33.svg" viewBox="0 0 288 288" width="128" height="128"><path d="M221.96 203.022a106.311 106.311 0 0 1-106.68-106.31 105.34 105.34 0 0 1 19.875-61.661C85.26 42.978 47.299 84.06 43.33 134.424c-3.97 50.363 27.09 96.885 75.125 112.53 48.035 15.645 100.534-3.664 126.986-46.705a106.311 106.311 0 0 1-23.481 2.773Z" stroke="#686763" stroke-width="9.244" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="bevel"></path></svg>
				<span class="text temp">21°</span>
			</a>
	</div>
    </div>'''

    # response = requests.get(url)
    # print("URL dettails =====> ", response.text)

    soup = BeautifulSoup(html_content, 'html.parser')

    # Containers for weather data
    cities, temperatures, conditions = [], [], []

    # Find all weather cards for cities
    weather_cards = soup.find_all('a', class_='nearby-location weather-card')

    for card in weather_cards:
        # Extract city name
        city_tag = card.find('span', class_='text title no-wrap')
        city = city_tag.text.strip() if city_tag else None
        cities.append(city)

        # Extract temperature
        temp_tag = card.find('span', class_='text temp')
        temp = temp_tag.text.strip() if temp_tag else None
        temperatures.append(temp)

        # Extract weather condition
        # condition_tag = card.find('svg')
        # condition = condition_tag if condition_tag else None
        # conditions.append(condition)

    # Create a DataFrame
    weather_df = pd.DataFrame({
        'City': cities,
        'Temperature (°C)': temperatures,
        # 'Condition': conditions
    })

    return weather_df

# Streamlit App
st.title("Weather Data for Pakistani Cities")

# Fetch and display weather data
weather_df = scrape_weather()

# Search functionality
search_city = st.text_input("Search for a city")
if search_city:
    weather_df = weather_df[weather_df['City'].str.contains(search_city, case=False)]

# Sort by temperature
if not weather_df.empty:
    sort_order = st.radio("Sort by temperature:", ["Ascending", "Descending"], index=0)
    weather_df = weather_df.sort_values(by="Temperature (°C)", ascending=(sort_order == "Ascending"))


# Display weather data
st.dataframe(weather_df)
