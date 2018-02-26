# FB-Downloader
App for Downloading Facebook videos and images

## Running the app

1. Install Google Chrome for Ubuntu:

	```console
	$ sudo apt-get install libxss1 libappindicator1 libindicator7
	$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
	$ sudo dpkg -i google-chrome*.deb
	$ sudo apt-get install -f
	```

2. Install xvfb to run chrome headlessly:

	```console
	$ sudo apt-get install xvfb
	```

3. Install chrome driver and add it to path:

	```console
	$ sudo apt-get install unzip
	$ wget -N http://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip
	$ unzip chromedriver_linux64.zip
	$ chmod +x chromedriver

	$ sudo mv -f chromedriver /usr/local/share/chromedriver
	$ sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
	$ sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

    ```
5. Add/Replace the below code in your 
	`features/support/env.rb`

	```ruby
	Capybara.register_driver :chrome do |app|
	  # optional
	  client = Selenium::WebDriver::Remote::Http::Default.new
	  # optional
	  client.timeout = 120
	  Capybara::Selenium::Driver.new(app, :browser => :chrome, :http_client => client)
	end
	Capybara.javascript_driver = :chrome
	```

4. Start a worker process
    
    ```console
    $ python3 worker.py
    ```

5. Start the `Flask` server
    
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
