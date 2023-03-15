# localhost_api_setup_django
A little API django app to solve issues of continuous downloadings of some models or libraries on the server side through setup-file.


PROBLEM: Servers working with setup.py might download files from deployes links in the setup.py continuosly after each release (for example language models for NLP). This might slow down the server.

SOLUTION to try: This repository consists of two part: 1. py file "testing_web_api" where a parsed data from the localhost api django app is processed (the logic in the script concerns only bound purpose, so you should change it or modify for your purposes).
2. Django app for a localhost api that allows to find a file automatically in the C directory (if Windows) or specify a path to the file that would fasten the server launch. The app produces an API (its reference is in the "testing_web_api") with a path in the localhost to get a needed file.
The app can be launched on the standard django test server "python manage.py runserver 80". If the api does not work, an online (or other) path will be returned, so the download process will start without failure on the server.
Ideally the app might be dockerized with a functionality to launch it in the background restart-allowing modus in the docker container.
