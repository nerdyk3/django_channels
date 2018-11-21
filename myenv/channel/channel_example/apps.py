from django.apps import AppConfig


class ChannelExampleConfig(AppConfig):
    name = 'channel_example'

    def ready(self):
    	import channel_example.signals
