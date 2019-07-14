

class UssdServiceOp:
    # CODES
    INIT = None
    CONT = None
    PROMPT = None
    DISPLAY = None

    BACK = ''
    HOME = ''

    def __init__(self, INIT=1, CONT=18, PROMPT=2, DISPALY=17, BACK='0', HOME='#'):
        self.INIT = INIT
        self.CONT = CONT
        self.PROMPT = PROMPT
        self.DISPLAY = DISPLAY
        self.BACK =  BACK
        self.HOME = HOME