from maze import Maze
from point import Point
from a_star import AStar

from browser import document, html, timer


maze_size = 20
start = Point(1, 1)
end = Point(maze_size * 2 - 1, maze_size * 2 - 1)

maze = None

scale = 8
ctx = None
canvas = None


def draw(x, y, col=(255, 255, 255)):
    r, g, b = col
    ctx.fillStyle = "rgb("+str(r)+","+str(g)+","+str(b)+")"
    ctx.fillRect(x * scale, y * scale, 1 * scale, 1 * scale)


def reset():
    global ctx
    global maze
    global canvas

    print('Started')

    document["canvas"].text = ""
    canvas = html.CANVAS(width=(maze_size * 2 + 1) * scale,
                         height=(maze_size * 2 + 1) * scale)
    document["canvas"] <= canvas

    ctx = canvas.getContext("2d")
    ctx.fillStyle = "rgb(0, 0, 0)"
    ctx.fillRect(0, 0, canvas.width, canvas.height)

    maze = Maze(maze_size, maze_size)
    maze.generate(Point.random(maze_size, maze_size), draw)

    path = AStar(maze).solve(start, end, draw)

    document["loading"].text = ""
    path.draw(maze, draw)
    # timer.set_timeout(lambda: path.draw(maze, draw), 1000)
    print('Done')


def click(ev):
    global maze_size
    global end
    maze_size = int(document["size"].value)
    end = Point(maze_size * 2 - 1, maze_size * 2 - 1)
    reset()


def canvasClick(ev):
    global maze
    global start
    global end

    rect = canvas.getBoundingClientRect()
    mouse = Point((ev.x - rect.left) // scale, (ev.y - rect.top) // scale)

    print(mouse)
    if mouse.x < 0 or mouse.x > maze_size * 2 or mouse.y < 0 or mouse.y > maze_size * 2:
        print('out')
        return

    lastStart = Point(start.x, start.y)
    start = mouse

    try:
        path = AStar(maze).solve(start, end, draw)
        document["error"].text = ''
        path.draw(maze, draw)
    except:
        print('error')
        start = lastStart
        document["error"].text = 'Cant create path from here!'


document["canvas"].bind('click', canvasClick)
document["reset"].bind("click", click)

reset()
