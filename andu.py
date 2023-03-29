def functie2():

    print("Retrieving data from https://festivalfans.nl/agenda/")

    import requests, os, bs4, lxml,re
    import pandas as pd
    from datetime import datetime, timedelta
    from bs4 import BeautifulSoup

    # relevant 'crawlable' information
    # ev3page-finish < start_date & end_date
    # ev3page < page-items
    # ev3page-title < name
    # ev3page-week < week day
    # ev3page-venue < venue
    # ev3page-day < day
    # ev3page-month < month
    # ev3page-year < year
    # ev3page-hour < hours
    url = "https://festivalfans.nl/event/"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    events = []

    for event in soup.find_all("div", class_="ev3page"):

     # <div class="ev3page">
        ev3page_amount = r'<div>+class*=*["]ev3page*["]'
        matches = re.search(ev3page_amount, str(soup), re.DOTALL)

      # scrape event name
        link = event.find_all('a', href=re.compile(r'https://festivalfans.nl/event/'))
        if len(link) > 1:
            event_name = link[1].text.strip()
        else:
            event_name = link[0].text.strip()
            event_name = f"Name: {event_name}"

        date = event.find("div", class_="ev3page-finish ").text.strip()



        location = event.find("div", class_="ev3page-location").text.strip()

        event_item = {
            "name": event_name,
            "date": date,
            "location": location
        }

        events.append(event_item)
        event_item = {"events":events}
        # df = pd.DataFrame.from_dict(events)


        return(event_item['event'][0]["name"])


    # urls = ['https://festivalfans.nl/agenda/']

    # for url in urls:
    #     # request the URL and parse the HTML using BeautifulSoup
    #     response = requests.get(url)
    #     soup = BeautifulSoup(response.content, 'html.parser')

    #     # find all the div elements with class 'ev3page'
    #     events = soup.find_all('div', class_='ev3page')



        # # loop through each event and scrape the relevant information
        # for event in events:
        #     # scrape start and end date
        #     element = event.find('div', class_='ev3page-finish')

        #     if element is not None:
        #         start_date = event.find('div', class_='ev3page-finish').text.strip()
        #         end_date = event.find_all('div', class_='ev3page-finish')[-1].text.strip()
        #     else:
        #         continue
        #     date_range = f"Date: {start_date} - {end_date}"

            # # scrape event name
            # link = event.find_all('a', href=re.compile(r'https://festivalfans.nl/event/'))
            # if len(link) > 1:
            #     event_name = link[1].text.strip()
            # else:
            #     event_name = link[0].text.strip()
            # event_name = f"Name: {event_name}"

            # # scrape venue
            # venue = event.find('div', class_='ev3page-venue').text.strip()
            # venue = f"In: {venue}"

            # # scrape hours
            # hours = event.find('div', class_='ev3page-hour').text.strip()
            # hours = f"Hours: {hours}"

            # # scrape week day
            # week = event.find('div', class_='ev3page-week').text.strip()
            # week = f"Day: {week}"

            # # print 10 lines
            # line = '-'*10

            # # ! return the scraped information for each event
            # return(f"{event_name}<br/>{venue}<br/>{week}<br/>{date_range}<br/>{hours}<br/>{line}<br/>")
