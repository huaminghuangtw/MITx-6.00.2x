### Problem 2: Robot Class 
10.0/10.0 points (graded) 

In *ps2.py* we provided you with the `Robot` class, which stores the position and direction of a robot. For this class, decide what fields you will use and decide how the following operations are to be performed:


- Initializing the object 
- Accessing the robot's position 
- Accessing the robot's direction 
- Setting the robot's position 
- Setting the robot's direction 

Complete the `Robot` class by implementing its methods in _ps2.py_.

**Note**: When a `Robot` is initialized, it should clean the first tile it is initialized on. Generally the model these Robots will follow is that after a robot lands on a given tile, we will mark the entire tile as clean. This might not make sense if you're thinking about really large tiles, but as we make the size of the tiles smaller and smaller, this does actually become a pretty good approximation.

Although this problem has many parts, it should not take long once you have chosen how you wish to represent your data. For reasonable representations, *a majority of the methods will require only a couple of lines of code.*

**Note**: The `Robot` class is an *abstract* class, which means that we will never make an instance of it. Read up on the Python docs on abstract classes at [this link](http://docs.python.org/3/library/abc.html) and if you want more examples on abstract classes, follow [this link](http://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods).

In the final implementation of `Robot`, not all methods will be implemented. Not to worry -- its subclass(es) will implement the method `updatePositionAndClean()`

Enter your code for classes `RectangularRoom` (from the previous problem) and `Robot` below.

```python
class RectangularRoom(object):

    """
    A RectangularRoom represents a rectangular region containing clean or dirty tiles.

    A room has a width and a height and contains (width * height) tiles.
    At any particular time, each of these tiles is either clean or dirty.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        
        #self.tiles = {}
        #for i in range(self.width):
        #    for j in range(self.height):
        #        self.tiles[(i,j)] = False
        self.tiles = { (i,j) : False for i in range(self.width) for j in range(self.height) }        

    def cleanTileAtPosition(self, pos : Position):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        self.tiles[ (math.floor(pos.getX()), math.floor(pos.getY())) ] = True

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer

        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.tiles[(m,n)]
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        cleaned_tiles = [ status for status in self.tiles.values() if status is True ]
        return len(cleaned_tiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        return Position( random.uniform(0, self.width), random.uniform(0, self.height) )

    def isPositionInRoom(self, pos : Position):
        """
        Return True if pos is inside the room.

        pos: a Position object.

        returns: True if pos is in the room, False otherwise.
        """
        # if ( (0 <= pos.getX() < self.width) and (0 <= pos.getY() < self.height) ):
        #     return True
        # else:
        #     return False
        return True if (0 <= pos.getX() < self.width) and (0 <= pos.getY() < self.height) else False

# ----------------------------------------------------------------------------------------------------------------------

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
```
