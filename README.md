# SG_PyWeatherBot
Python Telegram bot for Weather in Singapore. 
This is a project for NUS ISS PyDot Course. Here's a brief detail:

1. Project Name - SimpleSGWeatherBot

2. A Telegram bot that has the capability to: 
   - provide instant weather forecast for current or specific location at the current time or the whole day 
   - Know if it will rain at that location or when rain is expected for that location.

3. This is DATA Related Project

4. Brief of task:	 	 	 	
   - Create Weather Forecast(WF) writer to retrieve and parse 2Hr and 24hr Weather Data using data.gov weather API and save to MongoDB
   - Create WF reader to read weather forecast from mongodb.
   - Create WF geolocation. Get Lat/Long from address. calculate the proximity of address parameter with the    area label. 
   - Create bot (using botogram) to process request and return response. Call WF reader to summarize and   
     display result. Bot to accept optional address parameter. If available, use WF geolocation to get the 
     nearest area label.
   - Store API Key in text file and read from text file at runtime.      	 	
   - Automate updating of Weather data in mongodb(used cron tab)


5. Usage Details


