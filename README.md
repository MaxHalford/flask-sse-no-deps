## Flask SSE example

> Look ma, no dependencies!

This repository is an example of how to perform [server-sent events (SSE)](https://www.wikiwand.com/en/Server-sent_events) in Flask with no extra dependencies. Libraries such as [flask-sse](https://github.com/singingwolfboy/flask-sse) are great, but they require having to use Redis or some other sort of [pubsub](https://www.wikiwand.com/en/Publish%E2%80%93subscribe_pattern) backend. While this can be fine, I wanted to show that you can do SSE by only using Flask. The following instructions explain how to run the example. For more information on how this works, please see [the accompanying blog post](https://maxhalford.github.io/blog/flask-sse-no-deps).

You're going to need three terminal sessions to run this example in it's entirety. The first will run the server, the second will listen to events, and the third will trigger events. You may also open an additional terminal if you want to add another listener. In fact, having multiple listeners is a good test to check that a single message is correctly dispatched once to each listener.

In the first terminal, create a virtual environment, activate it, and install the necessary requirements.

```sh
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Next, run the server.

```sh
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

In the second terminal, listen for updates.

```sh
source env/bin/activate
python listen.py
```

Finally, in the third terminal, run the `emit.py` script.

```sh
source env/bin/activate
python emit.py
```

This will run an infinite loop which sends a GET request to the `/ping` route every second. This in turn will trigger an event which will be displayed in the listening terminal. You should see a new `pong` message being displayed every second or so.
