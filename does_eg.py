# (c) 2018, Ellie Sceeles & Charlie Bolton

class Electronic():
    count = 0
    def __init__(self, status):
        self.status = status.upper()
        Electronic.count += 1
    def showStatus(self):
        print(self.status)
    def changeStatus(self):
        if self.status == "ON":
            self.status = "OFF"
        else:
            self.status = "ON"
    @classmethod
    def howmuch(cls):
        print (cls.count)

class HeadLight(Electronic):
    def __init__(self, status):
        super().__init__(status)
    def does(self):
        return 'illuminates'

class SoundSystem(Electronic):
    def __init__(self, status):
        super().__init__(status)
    def does(self):
        return 'rocks'

class DriveTrain():
    def does(self):
        return 'propels'

class Car():
    def __init__ (self, headlight, drivetrain, soundsystem):
        self.headlight = headlight
        self.drivetrain = drivetrain
        self.s = soundsystem
    def does(self):
        print(f'The headlight {self.headlight.does()}\nThe train {self.drivetrain.does()}\nThe soundsytem {self.s.does()}')

blinky = HeadLight("off")
thomas = DriveTrain()
boom = SoundSystem("off")

Herbie = Car(blinky, thomas, boom)
Herbie.does()

Martha = Car(blinky, thomas, boom)
Berta = Car(blinky, thomas, boom)

blinky.showStatus()
blinky.changeStatus()
blinky.showStatus()

blinky1 = HeadLight("off")
thomas1 = DriveTrain()
boom1 = SoundSystem("off")

Todd = Car(blinky1, thomas1, boom1)

Electronic.howmuch()

