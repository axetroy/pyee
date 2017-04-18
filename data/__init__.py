class Pyee:
    def __init__(self):
        self.__events = {}

    def on(self, event, handler):
        events = self.__events
        if (event in events) is False:
            events[event] = []

        events[event].append(handler)

    def emit(self, event, *data):
        events = self.__events
        if (event in events) is False:
            return
        handlers = events[event]
        for handler in handlers:
            handler(data)