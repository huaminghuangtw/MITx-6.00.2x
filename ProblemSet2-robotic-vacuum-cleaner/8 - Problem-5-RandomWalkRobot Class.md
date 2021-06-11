### Problem 5: RandomWalkRobot Class 
10.0/10.0 points (graded) 

iRobot is testing out a new robot design. The proposed new robots differ in that they change direction randomly **after every time step**, rather than just when they run into walls. You have been asked to design a simulation to determine what effect, if any, this change has on room cleaning times.

Write a new class `RandomWalkRobot` that inherits from `Robot` (like `StandardRobot`) but implements the new movement strategy.
`RandomWalkRobot` should have the same interface as `StandardRobot`.

Test out your new class. Perform a single trial with the `StandardRobot` implementation and watch the visualization to make sure it is doing the right thing. Once you are satisfied, you can call `runSimulation` again, passing `RandomWalkRobot` instead of `StandardRobot`.

Enter your code for classes `Robot` and `RandomWalkRobot` below.

```python
class Robot(object):

    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """

    def __init__(self, room : RectangularRoom, speed):
        """
        Initializes a Robot with the given speed in the specified room.
        The robot initially has a random direction and a random position in the room.
        The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.position = self.room.getRandomPosition()
        self.direction = int(360 * random.random())
        self.speed = speed

        room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in degrees, 0 <= d < 360.
        """
        return self.direction

    def getRobotSpeed(self):
        """
        Return the speed of the robot.

        returns: an float number s giving the speed of the robot, s > 0.
        """
        return self.speed

    def setRobotPosition(self, position : Position):
        """
        Set the position of the robot to POSITION.

        Assumes that position represents a valid position inside this room.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees (0 <= d < 360)
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having been cleaned.
        """
        raise NotImplementedError # don't change this!

# ----------------------------------------------------------------------------------------------------------------------

class RandomWalkRobot(Robot):

    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy:
    it chooses a new direction at random at the end of each time-step.
    """

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having been cleaned.
        """
        robotDirection = self.getRobotDirection()
        robotSpeed = self.getRobotSpeed()

        newPosition = self.position.getNewPosition(robotDirection, robotSpeed)

        if (self.room.isPositionInRoom(newPosition)):
            self.setRobotPosition(newPosition)
            self.room.cleanTileAtPosition(newPosition)
		
        self.setRobotDirection(int(360 * random.random()))
```
