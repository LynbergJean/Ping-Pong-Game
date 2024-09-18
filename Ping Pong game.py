import pygame, sys, random
 
pygame.init()
 
WIDTH, HEIGHT = 1280, 720       
 
FONT = pygame.font.SysFont("Arial", int(WIDTH/20))  # Updated font to a common one
 
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))   # Make Screen this size
pygame.display.set_caption("Pong")
CLOCK = pygame.time.Clock()

# Paddles
player = pygame.Rect(WIDTH-110, HEIGHT/2 -50, 10,100)
opponent = pygame.Rect(110, HEIGHT/2 -50, 10, 100)
opponent_score, player_score = 0, 0

# Ball
ball_radius = 20
ball = pygame.Rect(WIDTH/2 -10, HEIGHT/2 -10, ball_radius,ball_radius)
x_speed, y_speed = 1,1

def drawDotLine():
    for i in range(0, HEIGHT, HEIGHT//20):
        pygame.draw.rect(SCREEN, (255, 255, 255), (WIDTH//2 - 5, i, 10, HEIGHT//40))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle key presses
    keys_pressed = pygame.key.get_pressed()

    # Player movement
    if keys_pressed[pygame.K_UP]:
        if player.top > 0:
            player.top -= 5
    if keys_pressed[pygame.K_DOWN]:
        if player.bottom < HEIGHT:
            player.top += 5

    # Opponent movement
    if keys_pressed[pygame.K_w]:
        if opponent.top > 0:
            opponent.top -= 5
    if keys_pressed[pygame.K_s]:
        if opponent.bottom < HEIGHT:
            opponent.top += 5

    # Ball movement
    ball.x += x_speed * 5
    ball.y += y_speed * 5

    # Check for ball collision with top and bottom walls
    if ball.y + ball_radius >= HEIGHT or ball.y - ball_radius <= 0:
        y_speed *= -1

    # Check for ball going out of bounds (left or right)
    if ball.x <= 0:
        player_score += 1
        ball.center = (WIDTH/2, HEIGHT/2)
        x_speed, y_speed = random.choice([-1, 1]), random.choice([-1, 1])

    if ball.x >= WIDTH:
        opponent_score += 1
        ball.center = (WIDTH/2, HEIGHT/2)
        x_speed, y_speed = random.choice([-1, 1]), random.choice([-1, 1])

    # Collision with paddles
    if player.x - ball.width <= ball.x <= player.x and player.top <= ball.y <= player.bottom:    
        x_speed = -10
        middleplayer = player.y + player.height/2
        differenceY =  ball.y - middleplayer
        y_speed = differenceY / (player.height/2)

    if opponent.x - ball.width <= ball.x <= opponent.x and opponent.top <= ball.y <= opponent.bottom:
        x_speed = 10
        middleopponent = opponent.y + opponent.height/2
        differenceY =  ball.y - middleopponent
        y_speed = differenceY / (opponent.height/2)

    # Clear the screen before drawing
    SCREEN.fill("black")

    # Draw paddles and ball
    pygame.draw.rect(SCREEN, "white", player)
    pygame.draw.rect(SCREEN, "white", opponent)
    pygame.draw.circle(SCREEN, 'white', ball.center, ball_radius)

    # Draw dotted line
    drawDotLine()

    # Render scores
    player_score_text = FONT.render(str(player_score), True, "white")
    opponent_score_text = FONT.render(str(opponent_score), True, "white")
    SCREEN.blit(player_score_text, (WIDTH/2 + 50, 50))
    SCREEN.blit(opponent_score_text, (WIDTH/2 - 100, 50))

    # Update display
    pygame.display.update()

    # Set the frame rate
    CLOCK.tick(60)
