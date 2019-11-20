from Robot import Robot
my_robot=Robot("Fred")
print(my_robot.name)
print(my_robot)

other_robot=Robot("marvin")
other_robot.name="kevin"
print(other_robot.name)
print(other_robot)

class BetterRobot(Robot):
    def __init__(self, name: str, start_x: int=0, start_y: int=0):
        super().__init__(name, start_x, start_y)
    def move(self,distance):

        for _ in range(distance):
            super().move()
my_betterrobot=BetterRobot("Bob")
my_betterrobot.move(int(input("Enter number of spaces to move Bob:")))
print(my_betterrobot)