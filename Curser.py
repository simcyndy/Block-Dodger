import curses
import random

# initialize screen
screen = curses.initscr()

# turn off cursor blinking
curses.curs_set(0)

# get screen dimensions
screen_height, screen_width = screen.getmaxyx()

# set up player and initial position
player = "@"
player_y, player_x = screen_height // 2, 0

# set up coins and initial positions
coins = ["$", "€", "¥"]
coin_yx = [(random.randint(1, screen_height - 2), random.randint(1, screen_width - 2)) for _ in range(len(coins))]

# set up obstacles and initial positions
obstacles = ["#", "&", "%"]
obstacle_yx = [(random.randint(1, screen_height - 2), random.randint(1, screen_width - 2)) for _ in range(10)]

# draw player and coins
screen.addstr(player_y, player_x, player)
for i, coin in enumerate(coins):
    screen.addstr(*coin_yx[i], coin)

# draw obstacles
for obstacle in obstacle_yx:
    screen.addstr(*obstacle, random.choice(obstacles))

# listen for user input and move player accordingly
while True:
    # listen for user input
    key = screen.getch()

    # move player left or right
    if key == curses.KEY_LEFT and player_x > 0:
        player_x -= 1
    elif key == curses.KEY_RIGHT and player_x < screen_width - 1:
        player_x += 1

    # move player up or down
    if key == curses.KEY_UP and player_y > 0:
        player_y -= 1
    elif key == curses.KEY_DOWN and player_y < screen_height - 1:
        player_y += 1

    # check for collisions with coins and obstacles
    for i, coin in enumerate(coins):
        if (player_y, player_x) == coin_yx[i]:
            coin_yx[i] = (random.randint(1, screen_height - 2), random.randint(1, screen_width - 2))
            screen.addstr(*coin_yx[i], coin)

    for obstacle in obstacle_yx:
        if (player_y, player_x) == obstacle:
            curses.flash()

    # update player position on screen
    screen.clear()
    screen.addstr(player_y, player_x, player)

    # update coins and obstacles positions on screen
    for i, coin in enumerate(coins):
        screen.addstr(*coin_yx[i], coin)

    for obstacle in obstacle_yx:
        screen.addstr(*obstacle, random.choice(obstacles))

    # refresh screen
    screen.refresh()

# clean up screen
curses.endwin()
