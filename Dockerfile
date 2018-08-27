FROM ubuntu:latest

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update
RUN apt-get install google-chrome-stable
RUN apt-get install xvfb
RUN apt-get install unzip
RUN wget -N http://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN chmod +x chromedriver
RUN mv -f chromedriver /usr/local/share/chromedriver
RUN ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
RUN ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install redis-server

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]

CMD ["app.py"]