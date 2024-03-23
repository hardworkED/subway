# subway
This application is built with Django. It shows:
- a list of Subway outlets details provided by https://subway.com.my/find-a-subway with filtered 'kuala lumpur'. 
- map view of the outlets with 5km radius catchment.
- API provided.

 >**Note:** Make sure have **Django** and packages in **requirements.txt** is installed.

## Configuration: Google API Key
Please visit https://developers.google.com/maps/documentation/javascript/adding-a-google-map#key for requesting an API key.

Locate file **mysite2\mysite2\settings.py** and replace `YOUR_API_KEY`.

### Launch server
`python "mysite2\manage.py runserver"`

### Launch web browser
The server will normally be hosted on http://localhost:8000/