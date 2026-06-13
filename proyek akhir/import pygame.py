import pygame
pygame.init()

# ===== TILE & MAZE =====
TILE = 50
maze_map = [
    "1111111111",
    "1P000000D1",
    "1011111101",
    "1000000101",
    "1110110101",
    "1K00100101",
    "1011011101",
    "1000000001",
    "1111111111"
]

ROWS = len(maze_map)
COLS = len(maze_map[0])
WIDTH = COLS * TILE
HEIGHT = ROWS * TILE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Escape")
clock = pygame.time.Clock()

# ===== COLORS =====
PINK = (255, 182, 193)

# ===== LOAD IMAGES =====
wall_img = pygame.transform.scale(
    pygame.image.load("wall.png"), (TILE, TILE)
)
player_img = pygame.transform.scale(
    pygame.image.load("sofia.png"), (TILE, TILE)
)
key_img = pygame.transform.scale(
    pygame.image.load("kunci.png"), (TILE, TILE)
)
door_img = pygame.transform.scale(
    pygame.image.load("door.png"), (TILE, TILE)
)

# ===== FIND POSITIONS =====
for y, row in enumerate(maze_map):
    for x, cell in enumerate(row):
        if cell == "P":
            player_x, player_y = x, y
        if cell == "K":
            key_x, key_y = x, y
        if cell == "D":
            door_x, door_y = x, y

# ===== GAME STATE =====
has_key = False
game_over = False

# ===== MOVE FUNCTION =====
def move(dx, dy):
    global player_x, player_y, has_key, game_over

    nx = player_x + dx
    ny = player_y + dy

    if maze_map[ny][nx] == "1":
        return

    player_x, player_y = nx, ny

    if (player_x, player_y) == (key_x, key_y):
        has_key = True

    if (player_x, player_y) == (door_x, door_y) and has_key:
        game_over = True

# ===== GAME LOOP =====
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_LEFT:
                move(-1, 0)
            if event.key == pygame.K_RIGHT:
                move(1, 0)
            if event.key == pygame.K_UP:
                move(0, -1)
            if event.key == pygame.K_DOWN:
                move(0, 1)

    # ===== DRAW =====
    screen.fill(PINK)

    for y, row in enumerate(maze_map):
        for x, cell in enumerate(row):
            if cell == "1":
                screen.blit(wall_img, (x*TILE, y*TILE))

    if not has_key:
        screen.blit(key_img, (key_x*TILE, key_y*TILE))

    screen.blit(door_img, (door_x*TILE, door_y*TILE))
    screen.blit(player_img, (player_x*TILE, player_y*TILE))

    if game_over:
        font = pygame.font.SysFont("arial", 48)
        text = font.render("YOU ESCAPED!", True, (0, 150, 0))
        screen.blit(
            text,
            (WIDTH // 2 - text.get_width() // 2,
             HEIGHT // 2 - text.get_height() // 2)
        )

    pygame.display.update()
    clock.tick(10)

pygame.quit()