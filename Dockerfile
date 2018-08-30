FROM ubuntu:latest

# Install Google-Chrome for Selenium
RUN curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /chrome.deb
RUN dpkg -i /chrome.deb || apt-get install -yf
RUN rm /chrome.deb

# For smooth running of Selenium
RUN apt-get install xvfb

# Installing chromedriver for usage by Selenium
RUN curl https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip -o /usr/local/bin/chromedriver
RUN chmod +x /usr/local/bin/chromedriver


# Installing redis
RUN apt-get install redis-server

# Install all the module requirements
RUN pip3 install -r requirements.txt

# Working directory
COPY . /app
WORKDIR /app

ENTRYPOINT ["python3"]

# Default command
CMD ["app.py"]

# Expose ports
EXPOSE 5901