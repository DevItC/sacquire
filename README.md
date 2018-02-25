# FB-Downloader
App for Downloading Facebook videos and images

## Running the app

1. Start a worker process
    
    ```console
    $ python3 worker.py
    ```

2. Start the `Flask` server
    
    ```console
    $ export FLASK_APP=app.py
    $ flask run
    ```

__NOTE__: This two processes must run concurrently. I suggest that for now run these two in two different consoles.
