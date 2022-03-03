from mycroft import MycroftSkill, intent_file_handler


class Testtwo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('testtwo.intent')
    def handle_testtwo(self, message):
        self.speak_dialog('testtwo')


def create_skill():
    return Testtwo()

