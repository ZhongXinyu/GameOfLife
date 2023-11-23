
from matplotlib.mathtext import RasterParse
from MyClass import World, Cell
import pytest 

### Test World class

def test_init_world():
    # init with default values
    world = World()
    assert world.width == 10
    # init with custom values
    world = World(8,8)
    assert world.width == 8

def test_addlocation():
    world = World()
    world.make_alive([(1,1), (1,2), (1,3), (5,0)])
    assert world.board[1][1].status == 1
    assert world.board[1][2].status == 1
    assert world.board[1][3].status == 1
    assert world.board[5][0].status == 1
    assert world.board[0][0].status == 0

def test_invalid_location():
    world = World()
    with pytest.raises(ValueError) as exc_info:
        world.make_alive([(100, 100)])
    # Check the exception message
    expected_message = "Invalid location, note that the board is of size 10 * 10, please pass in a valid location of the form (x,y) where 0 <= x < 10 and 0 <= y < 10"
    assert str(exc_info.value) == expected_message


### Test Cell class
def test_init_cell():
    cell = Cell(1)
    assert cell.status == 1
    assert cell.next_status == 1

def test_init_cell_invalid():
    with pytest.raises(ValueError) as exc_info:
        cell = Cell(100)
    # Check the exception message
    expected_message = "Invalid status, please pass in 0 or 1"
    assert str(exc_info.value) == expected_message



