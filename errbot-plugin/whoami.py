from errbot import BotPlugin, botcmd

class whoami(BotPlugin):
    @botcmd
    def whoami(self, mess, args):
        """ whoami """
        return mess.getFrom().getStripped()

