import requests, os, bs4, lxml, re
import pandas as pd
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import sqlite3 as s3

# relevant 'crawlable' information
# ev3page-finish < start_date & end_date
# ev3page < page-items
# ev3page-title < title
# ev3page-week < week day
# ev3page-venue < venue
# ev3page-day < day
# ev3page-month < month
# ev3page-year < year
# ev3page-hour < hours

def functie2():

    # # Read from recipe URL List
    # with open('festivals.json', 'w') as f:
    #     festivals = f.readlines()

    # # Checking if file doesn't exist yet
    # if os.path.exists("festivals.json"):
    #     os.remove("festivals.json")
    # else:
    #     print("File is not present in system, making file")

# Make a file containing recipe information
    # with open('recipe.txt', 'a', encoding='utf-8') as f:

        print("Retrieving data from https://festivalfans.nl/agenda/")

        urls = ['https://festivalfans.nl/agenda/']

        events_list = []
        counter = 0

        for url in urls:
            # request the URL and parse the HTML using BeautifulSoup
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # <div class="ev3page">
            ev3page_amount = r'<div class="[^"]ev3page3[^"]">(.*?)<\/div>'
            matches = re.search(ev3page_amount, str(soup), re.DOTALL)

            if matches:
                div_content = matches.group(1)
                ev3page_number = int(re.sub(r'\D', '', div_content))
                print(ev3page_number)
            else:
                print('No match found')

            # find all the div elements with class 'ev3page'
            events = soup.find_all('div', class_='ev3page')

            # loop through each event and scrape the relevant information
            for event in events:
                # scrape start and end date
                element = event.find('div', class_='ev3page-finish')

                if element is not None:
                    start_date = event.find('div', class_='ev3page-finish').text.strip()
                    end_date = event.find_all('div', class_='ev3page-finish')[-1].text.strip()
                else:
                    continue
                date_range = f"{start_date} - {end_date}"
                counter +=1

                # scrape event name
                link = event.find_all('a', href=re.compile(r'https://festivalfans.nl/event/'))
                if len(link) > 1:
                    event_name = link[1].text.strip()
                else:
                    event_name = link[0].text.strip()

                # scrape venue
                venue = event.find('div', class_='ev3page-venue').text.strip()

                # scrape hours
                hours = event.find('div', class_='ev3page-hour').text.strip()

                # scrape week day
                week = event.find('div', class_='ev3page-week').text.strip()

                events_dict ={
                    'Index': counter,
                    'Name': event_name,
                    'In': venue,
                    'Day': week,
                    'Date': date_range,
                    'Hours': hours,
                }

                events_list.append(events_dict)

        # ! return the scraped information for each event
        events_dict = {'Events': events_list}

        # for k in events_dict['Events'][::]:
        #     print(k)

        df = pd.DataFrame.from_dict(events_dict['Events'][::])
        print(df)

        return df.to_json(orient= 'table', index= False)



        # # Append this festival to the file
        # f.write(f"Name: {event_name}\n In: {venue}\n Day: {week}\n 'Date': {date_range}\n 'Hours': {hours}")
        # print(f"Name: {event_name} has been added")
        # for idx_events, event in enumerate(events):
        #     f.write(f"- {event}\n")
        #     # Make sure that there is an enter at the end of the ingredient list
        #     if idx_events == len(events) - 1:
        #         f.write("\n")







# conn = sqlite3.connect('festivals.db')
# df.to_sql('events', conn, if_exists='replace', index=False)

#     conn.close()

# {"Events":[{"Date":"Date: 31 Mar - 01 Apr","Day":"Vrijdag","Hours":"18:00 - 23:00","In":"GelreDome, Arnhem","Name":"Snollebollekes Live in Concert"},{"Date":"Date: 07 Apr - 09 Apr","Day":"Vrijdag","Hours":"12:00 - 23:00","In":"NDSM-Werf, Amsterdam","Name":"DGTL Amsterdam"}]}