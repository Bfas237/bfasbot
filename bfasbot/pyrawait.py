
from concurrent.futures import Future
import asyncio
from pyrogram import Client, Filters, MessageHandler
import logging, threading, signal 
class AwaitableFuture(Future):
    def __await__(self):
        return (yield from asyncio.wrap_future(self))

class Conversation:
    def __init__(self, client: Client, peer):
        self.peer = peer
        self.client = client
        self.handlers = []
        self.msgs = []
        self.message_handler = MessageHandler(self.handle_message,Filters.chat(self.peer))
        self.last_sent_id = 0
    def handle_message(self, _, message):
        if not self.check(message):
            self.msgs.append(message)
        message.stop_propagation()
    def add_awaiter(self, filters):
        fut = AwaitableFuture()
        self.handlers.append((filters,fut))
        return fut
    def check(self,message):
        for filters,fut in self.handlers:
            if fut.cancelled():
                self.handlers.remove((filters,fut))
            elif filters(message):
                self.handlers.remove((filters,fut))
                fut.set_result(message)
                return True
        return False
    def send_message(self,*args, **kwargs):
        msg = self.client.send_message(self.peer, *args, **kwargs)
        self.last_sent_id = msg.message_id
        return msg
    def get_response(self,filters=Filters.create('empty',lambda *_:True)):
        for msg in self.msgs:
            if msg.message_id < self.last_sent_id:
                self.msgs.remove(msg)
            elif filters(msg):
                fut = AwaitableFuture()
                fut.set_result(msg)
                self.messages.remove()
                return fut
        return self.add_awaiter(filters)
    async def __aenter__(self):
        return self.__enter__()
    def __enter__(self):
        self.client.add_handler(self.message_handler, -1)
        return self
    async def __aexit__(self):
        self.__exit__()
    def __exit__(self, *args):
        self.client.remove_handler(self.message_handler, -1)
        

class AwaitableClient(Client):
    def conversation(self, peer):
        return Conversation(self, peer)
class ProgramKilled(Exception):
    pass
def signal_handler(signum, frame):
    raise ProgramKilled
    
class Job(threading.Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        threading.Thread.__init__(self)
        self.daemon = False
        self.stopped = threading.Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs
        
    def stop(self):
                self.stopped.set()
                self.join()
    def run(self):
            while not self.stopped.wait(self.interval.total_seconds()):
                self.execute(*self.args, **self.kwargs)
            