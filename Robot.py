class Robot():

    def __init__(self, name: str, start_x: int=0, start_y: int=0):

        self._x = start_x
        self._y = start_y
        self._elevator_state = 0

        self.name = name
        self._direction = 0

        self._pos_dict = {0:'bottom', 1:'middle', 2:'top'}
        self._dir_dict = {0:'north', 1:'east', 2:'south', 3:'west'}

        if name.lower() == "marvin":
            print("Life! Don't talk to me about life.\n")

    def get_position(self) -> [int, int]:
        return [self._x, self._y]

    def get_elevator_position(self) -> str:
        return self._pos_dict[self._elevator_state]

    def get_direction(self) -> str:
        return self._dir_dict[self._direction]

    def move(self):
        if self._direction == 0:
            self._y += 1
        elif self._direction == 1:
            self._x += 1
        elif self._direction == 2:
            self._y -= 1
        elif self._direction == 3:
            self._x -= 1

    def turn_left(self):
        self._direction = self._direction-1 if self._direction-1 >= 0 else 3

    def turn_right(self):
        self._direction = self._direction+1 if self._direction+1 <= 3 else 0

    def raise_elevator(self):
        self._elevator_state = 3 if self._elevator_state + 1 > 3 else self._elevator_state + 1

    def lower_elevator(self):
        self._elevator_state = 0 if self._elevator_state -1 < 0 else self._elevator_state - 1

    def open_the_pod_bay_doors(self):
        print("I'm sorry, Dave. I'm afraid I can't do that.\n")

    def print_rules(self):
        msg = (
            'A robot may not injure a human being or, through inaction, allow a human being to come to harm.\n'
            'A robot must obey orders given it by human beings except where such orders would conflict with the First Law.\n'
            'A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.\n'
        )

        print(msg)

    def __str__(self):
        robot_str = (
            f'### ROBOT OBJECT ###\n'
            f'Name:       {self.name} \n'
            f'Direction:  {self.get_direction()} \n'
            f'Position:   {self.get_position()} \n'
            f'Elevator:   {self.get_elevator_position()}\n'
        )

        return robot_str