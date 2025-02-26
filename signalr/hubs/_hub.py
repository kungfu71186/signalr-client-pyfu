from signalr.events import EventHook


class Hub:
    def __init__(self, name, connection):
        self.name = name
        self.server = HubServer(name, connection, self)
        self.client = HubClient(name, connection)
        self.error = EventHook()


class HubServer:
    def __init__(self, name, connection, hub):
        self.name = name
        self.__connection = connection
        self.__hub = hub

        self.__handler = None
        self.__current_I = -1

        def handle(**kwargs):
            if not 'R' in kwargs:
                return
            response = kwargs['R']
            if int(kwargs['I']) == self.__current_I and self.__handler:
                self.__handler(response)

        connection.received += handle

    def invoke(self, method, *data, handler=None):
        self.__handler = handler
        self.__current_I = self.__connection.increment_send_counter()

        self.__connection.send({
            'H': self.name,
            'M': method,
            'A': data,
            'I': self.__current_I
        })

class HubClient(object):
    def __init__(self, name, connection):
        self.name = name
        self.__handlers = {}

        def handle(**kwargs):
            messages = kwargs['M'] if 'M' in kwargs and len(kwargs['M']) > 0 else {}
            for inner_data in messages:
                hub = inner_data['H'] if 'H' in inner_data else ''
                if hub.lower() == self.name.lower():
                    method = inner_data['M']
                    if method in self.__handlers:
                        arguments = inner_data['A']
                        self.__handlers[method].fire(*arguments)

        connection.received += handle

    def on(self, method, handler):
        if method not in self.__handlers:
            self.__handlers[method] = EventHook()
        self.__handlers[method] += handler

    def off(self, method, handler):
        if method in self.__handlers:
            self.__handlers[method] -= handler


class DictToObj:
    def __init__(self, d):
        self.__dict__ = d
