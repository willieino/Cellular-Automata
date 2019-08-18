import pygame, random


# Define some colors and other constants
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
WIN_SIZE = 500

# # NUM_SQUARES = ??
#WIN_SIZE = NUM_SQUARES * 20 + (NUM_SQUARES+1)* 5


 # 1. Create a set of initial states with simple pattern (Ex. blinker)
cur_states = [0] * 400
cur_states[10] = 1
cur_states[30] = 1
cur_states[50] = 1

generation = 0
is_paused = False

cur_states = [0] * 400
for i in range( 0, len(cur_states) ):
    cur_states[i] = random.randint(0,1)

pygame.init()

size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)



done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    generation += 1
    pygame.display.set_caption("Conway's Game of Life, Generation: " + str(generation))

    if not is_paused:
        new_states = [0] * 400

        for index in range(len(cur_states)):
            width = 20
            e = index + width
            w = index - width
            n = index - 1
            s = index + 1
            ne = n + width
            nw = n - width
            se = s + width
            sw = s - width

            live_neighbors = 0
            if e < len(cur_states) and cur_states[e] == 1:
                live_neighbors += 1            
            if w > 0 and cur_states[w] == 1:                
                live_neighbors += 1            
            if n % width != width - 1 and cur_states[n] == 1:                
                live_neighbors += 1            
            if s % width != 0 and cur_states[s] == 1:
                live_neighbors += 1
            if ne < len(cur_states) and ne % width != width - 1 and cur_states[ne] == 1:
                live_neighbors += 1
            if se < len(cur_states) and se % width != 0 and cur_states[se] == 1:
                live_neighbors += 1
            if nw > 0 and nw % width != width - 1 and cur_states[nw] == 1:
                live_neighbors += 1
            if sw > 0 and sw % width != 0 and cur_states[sw] == 1:
                live_neighbors += 1
            if cur_states[index] == 1:
                if live_neighbors < 2:
                    new_states[index] = 0
                elif live_neighbors > 3:
                    new_states[index] = 0
                else:
                    new_states[index] = 1
            else:
                if live_neighbors == 3:
                    new_states[index] = 1
                else:
                    new_states[index] = 0
        cur_states = new_states

    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)
 
    # --- Drawing code should go here
    cur_index = 0
    x = 5
    while x < 500:
        y = 5
        while y < 500:
            state = cur_states[cur_index]
            if state == 0:
                pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, 20, 20))
            else:
                pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, 20, 20)) 
            cur_index += 1
            y += 25
        x += 25


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 5 frames per second
    clock.tick(5)
 
# Close the window and quit.
pygame.quit()


