from mycroft import MycroftSkill, intent_handler
import redis

class ComplimentMeSkill(MycroftSkill):
    def __init__(self):
        super(ComplimentMeSkill, self).__init__("ComplimentMeSkill")
        self.redis_client = redis.Redis(host="192.168.1.11", port=6379, db=0)

    @intent_handler('who.is.the.fairest.of.them.all.intent')
    def get_compliment(self): 
        compliment_list = [
            'well, it is you, who is the fairest by far'
        ]
        self.redis_client.publish('notification', compliment_list[0])


def create_skill():
    return ComplimentMeSkill