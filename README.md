### **GrandPyBot, the GrandPa Robot**

#### **Description**

This is the 6th project which has been developed for Openclassrooms.
Ask GrandPy for a place, and it will give you the location with the
postal address and the corresponding map.
Then, he will start to talk about facts on this place.

#### **How does it works ?**

GrandPy will use Google Maps API to retrieve a place and display its map and
Media Wiki API to get an extract about this place. In order to get the 
corresponding wikipedia page according to the location, it will use the 
coordinates of this location.

#### **How to use ?** 

You have 2 options.

**1 - Heroku**

Just visit this link ! _https://nameless-earth-22211.herokuapp.com/_

**2 - Cloning this repository**

**Prerequisites**  

*1) Python*

Install on Linux : 
1) With command line => `apt install python3`
2) Download compressed file here : https://www.python.org/downloads/source/ 

Install on Windows : Download here => https://www.python.org/downloads/windows/

Install on MacOS : Download here => https://www.python.org/downloads/mac-osx/

*2) Google Cloud configuration*

You have to possess a Google Cloud API Key in order to get this
program running. You have to activate Geocoding API and Maps Javascript API.

**Depencies**
- Install the dependencies with _pip install requirements.txt_
- Insert your API key in the corresponding place

**Launching**
- Run _flask run_ in your terminal
- Launch you web browser and go to the local server, _127.0.0.1:5000_ by default
- Write your question in the form and wait for GrandPy to answer you.

**Testing with Pytest library**

Pytest is the library being used in this program.
In order to run the tests, do like so :
- Go the the project's root in your terminal
- Run _pytest_ (Pytest has to be installed)

If the test is validated, it will be green.

You can test the coverage of the tests like so :
_pytest --cov=app --cov-report html_ 

It will generate a _htmlcov_ directory in the project. Launch
_index.html_ in your browser to see the results.