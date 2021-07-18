import keyboard
import problems


class lamps:
    def __init__(self):
        self.system = False  # 所有灯光
        self.clearance = False  # 示廓灯
        self.headlight = False  # 前照灯

        self.headlight_fullBeam = False  # 远光灯
        self.headlight_dipped = False  # 近光灯

    def opensystem(self):
        self.system = True

    def closesystem(self):
        self.system = False
        self.clearance = False  # 示廓灯
        self.headlight = False  # 前照灯

    def openclearance(self):
        self.opensystem()  # 打开示廓灯，所有灯光必定打开
        self.clearance = True

    def closeclearance(self):
        self.clearance = False

    def openheadlight(self):
        self.opensystem()  # 打开大灯，所有灯光必定打开
        self.headlight = True
        if self.headlight_fullBeam is False and self.headlight_dipped is False:
            self.headlight_dipped = True
        elif self.headlight_dipped is False and self.headlight_fullBeam is True:
            self.headlight_dipped = True

    def closeheadlight(self):
        self.headlight = False

    def openheadlight_dipped(self):
        self.headlight_dipped = True
        self.headlight_fullBeam = False

    def openheadlight_fullbeam(self):
        self.headlight_dipped = False
        self.headlight_fullBeam = True


