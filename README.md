# FB-Downloader
App for Downloading Facebook videos and images

## Running the app

1. Install Google Chrome for Ubuntu

	```console
	$ wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
	$ echo "deb http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
	$ sudo apt-get update
	$ sudo apt-get install google-chrome-stable
	```

2. Install xvfb to run Chrome headlessly

	```console
	$ sudo apt-get install xvfb
	```

3. Download chromedriver and add it to path

	```console
	$ sudo apt-get install unzip
	$ wget -N http://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip
	$ unzip chromedriver_linux64.zip
	$ chmod +x chromedriver
	$ sudo mv -f chromedriver /usr/local/share/chromedriver
	$ sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
	$ sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
    ```

4. Install Redis server

```console
$ sudo apt-get install redis-server
```

5. Start a worker process
    
    ```console
    $ python3 worker.py
    ```

6. Start the `Flask` server
    
    ```console
    $ export FLASK_APP=app.py
    $ flask run
    ```

__NOTE__: This two processes must run concurrently. I suggest that for now run these two in two different consoles.


## Deploying on Heroku

```console
$ heroku create
$ heroku config:add GOOGLE_CHROME_CHANNEL=stable
$ heroku buildpacks:set heroku/python
$ heroku buildpacks:add https://github.com/heroku/heroku-buildpack-google-chrome.git
$ heroku buildpacks:add https://github.com/heroku/heroku-buildpack-chromedriver.git
$ git push heroku master
$ heroku addons:create redistogo:nano
$ heroku ps:scale worker=1
```
