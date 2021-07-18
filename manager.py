import lights
import problems

TIME_OUT = 5


class Manager:
    def __init__(self):
        self.score = 100
        self.car_lamps = lights.lamps()
        self.behavior = []
        self.problems_list = problems.init()

    def ispress_left(self):
        if self.car_lamps.system:
            if self.car_lamps.clearance:
                self.car_lamps.closesystem()
            elif self.car_lamps.headlight:
                self.car_lamps.closeheadlight()
                self.car_lamps.openclearance()

    def ispress_right(self):
        if self.car_lamps.headlight is not True:
            if self.car_lamps.clearance:
                self.car_lamps.closeclearance()
                self.car_lamps.openheadlight()
            else:
                self.car_lamps.opensystem()
                self.car_lamps.openclearance()

    def ispress_up(self):
        if self.car_lamps.headlight:
            if self.car_lamps.headlight_dipped:
                self.car_lamps.openheadlight_fullbeam()

    def ispress_down(self):
        if self.car_lamps.headlight:
            if self.car_lamps.headlight_fullBeam:
                self.car_lamps.openheadlight_dipped()

    def check(self, order, index, times):
        if 0 <= index <= 4:  # 近光灯
            if self.car_lamps.headlight and self.car_lamps.headlight_dipped:
                if len(times) == 0:
                    return True
                elif len(times) == 1:
                    if times[0] == "s":
                        return True
                    else:
                        return False
                elif len(times) == 2:
                    if order >= 2:
                        if self.problems_list[order - 1] == 11 and self.problems_list[order - 2] == 10:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False

        elif 5 <= index <= 9:
            if self.car_lamps.headlight and self.car_lamps.headlight_dipped:
                if len(times) == 0 or len(times) == 1:
                    return False
                elif len(times) == 2:
                    if times[0] == times[1] == "s":
                        return True
                    else:
                        return False
                elif len(times) == 3:
                    if times[1] == times[2] == "s":
                        return True
                    else:
                        return False
                elif len(times) == 4:
                    if times[2] == times[3] == "s" and times[0] == 'd' and times[1] == 's':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif index == 10:  # 远光灯
            if self.car_lamps.headlight and self.car_lamps.headlight_fullBeam:
                if len(times) == 0:
                    return False  # 不可能出现两次远光灯
                elif len(times) == 1:
                    if times[0] == "w":  # 前一次是近光灯
                        return True
                    else:
                        return False
                elif len(times) == 2:
                    if times[1] == "w":
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

        elif index == 11:
            if self.car_lamps.clearance and len(times) == 1:
                return True
            else:
                return False

        elif index == -1:   # 请打开前照灯
            if self.car_lamps.system and self.car_lamps.headlight_dipped and len(times) == 2:
                return True
            else:
                return False

        elif index == -2:   # 关闭所有灯光
            if self.car_lamps.system is False:
                return True
            else:
                return False
        else:
            return False

