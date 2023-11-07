# pygame template
import math
import random
import pygame

def linear_interpolation(x, x0, x1, y0, y1):
    return y0 + (x - x0) * (y1 - y0) / (x1 - x0)


pygame.init()
pygame.font.init()


WIDTH = 1920
HEIGHT = 1080
SIZE = (WIDTH, HEIGHT)

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

num_students = 33
MAP_SIZE = math.ceil(math.sqrt(num_students))
MAP_SIZE += 1 - MAP_SIZE % 2
MID = MAP_SIZE//2
PLOT_WIDTH = 640
PLOT_HEIGHT = 480
MIN_SCALE = HEIGHT/(MAP_SIZE*PLOT_HEIGHT)
MAX_SCALE = 1
screen = pygame.Surface((PLOT_WIDTH * MAP_SIZE, PLOT_HEIGHT * MAP_SIZE))
camera_x = screen.get_width()//2
camera_y = screen.get_height()//2
zoom_level_gallo = 1 # 1-10
grid_font = pygame.font.SysFont('Arial', 20)


# ---------------------------
# Initialize global variables for animation
# These must have your name in there

font_gallo = pygame.font.SysFont('Arial', 120)
welcome_font_gallo = pygame.font.SysFont('Arial', 40)
bg_color_gallo = "#E15E03"
# fg_color_gallo = "#FF9142"
fg_color_gallo = "#FEC661"
text_gallo = font_gallo.render("The Gallo-verse", True, fg_color_gallo)
welcome_text_gallo = welcome_font_gallo.render("Welcome to", True, fg_color_gallo)
frames_gallo = 0
bg_start = pygame.Color("#E05F02")
bg_end = pygame.Color("#6B2D01")
bg_gallo_large = pygame.Surface((1000, 1000))
bg_gallo_large.fill((0, 0, 0))
for x in range(1000):
    pygame.draw.line(bg_gallo_large, bg_end.lerp(bg_start, x/1000), (x, 0), (x, 1000))
bg_gallo_large = pygame.transform.rotate(bg_gallo_large, -45)
bg_gallo = pygame.Surface((640, 480))
bg_gallo.blit(bg_gallo_large, (-500, -500))
welcome_text_buffer = {}
# ---------------------------

ghost_x_maggie = 0
ghost_y_maggie = 200

switch_maggie = "right"

# ----------------------

duncan_glow_x, duncan_glow_y, duncan_glow_radius = 315, 220, 70
duncan_vignette_x, duncan_vignette_y, duncan_vignette_radius = 320, 240, 250

duncan_rect_x, duncan_rect_y, duncan_rect_sizex, duncan_rect_sizey = 285, 190, 60, 70
duncan_circle_x, duncan_circle_y, duncan_circle_radius = 315, 187, 30

duncan_inside_x, duncan_inside_y, duncan_inside_sizex, duncan_inside_sizey = 288, 193, 55, 65
duncan_inner_circle_x, duncan_inner_circle_y, duncan_inner_circle_radius = 315, 190, 27.5

duncan_eye_leftx, duncan_eye_lefty, duncan_eye_left_radius = 307, 190, 6
duncan_eye_rightx, duncan_eye_righty, duncan_eye_right_radius = 322, 190, 5

duncan_hover_speed = 1
duncan_glow_speed, duncan_glow_color, duncan_glow_growth = 2, 245, 1
duncan_background_color, duncan_background_change_speed = 50, 2
#---------------------

circle_x_ilia = 320
circle_y_ilia = 240
flash_color = (0, 0, 255)
last_flash_time = 0
flash_interval = 500
growrate = 5
sizeilia = 150

# ------------------

circle_x_chk = 40
circle_y_chk = 40
circle_a_chk = 40
circle_b_chk = 40

# ------------------

running = True
while running:
    # GALLO VERSE SPECIFIC ----------------------------------------------------------------
    scale = linear_interpolation(zoom_level_gallo, 10, 1, MIN_SCALE, MAX_SCALE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEWHEEL:
            direction = event.y
            zoom_level_gallo -= direction
            zoom_level_gallo = max(min(zoom_level_gallo, 10), 1)
        elif event.type == pygame.MOUSEMOTION:
            click, _, _ = event.buttons
            if click:
                dx, dy = event.rel
                camera_x += -dx/scale
                camera_y += -dy/scale

    # DRAWING
    screen.fill((255, 255, 255))
    window.fill((100, 100, 100))

    # Draw Plot points
    for x in range(0, MAP_SIZE * PLOT_WIDTH, PLOT_WIDTH):
        for y in range(0, MAP_SIZE * PLOT_HEIGHT, PLOT_HEIGHT):
            pygame.draw.circle(screen, (30, 30, 200), (x, y), 5)
            coord_text = grid_font.render(f"({x}, {y})", False, (0, 0, 0))
            screen.blit(coord_text, (x, y))
    
    # -----------MAGGIE
    x = 1920
    y = 960
    width = 640
    height = 480


    width = 640
    height = 480

    points_maggie = [
        (x+345,y+100),
        (x+285,y+150),
        (x+385,y+150)
    ]

    points_maggie1 = [
        (x+275,y+170),
        (x+225,y+220),
        (x+315,y+220)
    ]

    points_maggie2 = [
        (x+405,y+170),
        (x+355,y+220),
        (x+445,y+220)
    ]

    points_maggie3 = [
        (x+385,y+223),
        (x+385,y+203),
        (x+443,y+190)
    ]


    pygame.draw.rect(screen, (200, 200, 200), (x, y, width, height))

    if ghost_x_maggie > 642:
        switch_maggie = "left"
    elif ghost_x_maggie < 0:
        switch_maggie = "right"


    if switch_maggie == "right":
        ghost_x_maggie += 3
    else:
        ghost_x_maggie -= 3

    # BACKGROUND
    pygame.draw.rect(screen, ("#05133d"), (x, y, width, height))

    #ground
    pygame.draw.rect(screen, ("#013220"), (x, y + 280, width, 200))


    #moon
    pygame.draw.circle(screen, ("gray"), (x + 260, y + 140), 70)

    #smallghost
    pygame.draw.circle(screen, ("white"), (x + 380, y + 183), 20)
    pygame.draw.circle(screen, ("black"), (x + 380, y + 189), 4) #mouth
    pygame.draw.circle(screen, ("black"), (x + 376, y + 180), 2) #eye
    pygame.draw.circle(screen, ("black"), (x + 386, y + 180), 2) #eye
    pygame.draw.polygon(screen, ("white"), points_maggie3)

    # HOUSE    
    pygame.draw.rect(screen, (0, 0, 0), (x + 300, y+150, 70, 150))
    pygame.draw.polygon(screen, (0,0,0), points_maggie)


    pygame.draw.rect(screen, (0, 0, 0), (x + 250, y+210, 47, 90))
    pygame.draw.polygon(screen, (0,0,0), points_maggie1)

    pygame.draw.rect(screen, (0, 0, 0), (x + 373, y+210, 47, 90))
    pygame.draw.polygon(screen, (0,0,0), points_maggie2)

    #TOP
    pygame.draw.rect(screen, (0,0,0), (x + 335, y+87, 20, 5))
    pygame.draw.rect(screen, (0,0,0), (x + 343, y+83, 5, 30))


    #FENCE
    for i in range(40):
        pygame.draw.rect(screen, (0, 0, 0), (x + 150 + 10*i, y+270, 5, 25))
    pygame.draw.rect(screen, (0, 0, 0), (x + 150, y+278,400, 3))

    #WINDOW
    pygame.draw.rect(screen, ("#e0b42c"), (x + 390, y+250, 15, 40)) #right
    pygame.draw.rect(screen, ("#e0b42c"), (x + 260, y+250, 15, 40)) #left
    pygame.draw.rect(screen, ("#e0b42c"), (x + 325, y+170, 25, 40)) #middle

    pygame.draw.circle(screen, ("#e0b42c"), (x + 338, y + 170), 12)


    pygame.draw.rect(screen, (0,0,0), (x + 325, y+190, 28, 3))     #middle lines
    pygame.draw.rect(screen, (0,0,0), (x + 335, y+172, 3, 41))
    pygame.draw.rect(screen, (0,0,0), (x + 325, y+174, 28, 3)) 

    #door
    pygame.draw.rect(screen, ("#3f2a14"), (x + 319, y+257, 30, 40))


    #pumpkin
    pygame.draw.circle(screen, ("orange"), (x + 130, y + 290), 14)
    pygame.draw.rect(screen, ("brown"), (x + 127, y+268, 3, 10))

    pygame.draw.circle(screen, ("orange"), (x + 80, y + 310), 14)
    pygame.draw.rect(screen, ("brown"), (x + 77, y+288, 3, 10))

    pygame.draw.circle(screen, ("orange"), (x + 40, y + 302), 14)
    pygame.draw.rect(screen, ("brown"), (x + 37, y+280, 3, 10))

    #grave
    pygame.draw.rect(screen, ("gray"), (x + 525, y+290, 25, 40)) 
    pygame.draw.circle(screen, ("gray"), (x + 538, y + 290), 12)

    pygame.draw.rect(screen, ("gray"), (x + 575, y+280, 25, 40)) 
    pygame.draw.circle(screen, ("gray"), (x + 588, y + 280), 12)

    #path
    pygame.draw.rect(screen, ("#515151"), (x + 319, y+300, 50, 50))


    # GHOST
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie, y + ghost_y_maggie), 30)
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie, y + ghost_y_maggie + 30), 10)
    pygame.draw.rect(screen, (255, 255, 255), (ghost_x_maggie - 30, ghost_y_maggie, 60, 30))
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie - 20, y + ghost_y_maggie + 30), 10)
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie +20, y + ghost_y_maggie + 30), 10)

    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie - 60, y + ghost_y_maggie + 100), 15)
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie - 60, y + ghost_y_maggie + 115), 5)
    pygame.draw.rect(screen, (255, 255, 255), (ghost_x_maggie - 73, ghost_y_maggie + 100, 27, 15))
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie - 72, y + ghost_y_maggie + 115), 5)
    pygame.draw.circle(screen, (255, 255, 255), (x + ghost_x_maggie - 50, y + ghost_y_maggie + 115), 5)


    # DUNCAN -------------------------------

    x = 3200
    y = 960
    width = 640
    height = 480
    
    duncan_rect_y += duncan_hover_speed
    duncan_circle_y += duncan_hover_speed
    
    duncan_inside_y += duncan_hover_speed
    duncan_inner_circle_y += duncan_hover_speed
    
    duncan_eye_lefty += duncan_hover_speed * 0.54
    duncan_eye_righty += duncan_hover_speed * 0.65
    
    duncan_glow_y += duncan_hover_speed
    duncan_glow_color += duncan_glow_speed
    duncan_glow_radius += duncan_glow_growth
    
    duncan_background_color += duncan_background_change_speed
    
    if duncan_circle_y < 197: duncan_hover_speed *= -1
    if duncan_rect_y > 180: duncan_hover_speed *= -1
    if duncan_glow_color >= 255: duncan_glow_speed *= -1
    if duncan_glow_color <= 235: duncan_glow_speed *= -1
    if duncan_glow_radius > 100 or duncan_glow_radius < 60: duncan_glow_growth *= -1
    if duncan_background_color > 50 or duncan_background_color < 2: duncan_background_change_speed *= -1

    pygame.draw.rect(screen, (duncan_background_color, duncan_background_color, duncan_background_color), (x, y, width, height))

    pygame.draw.circle(screen, (235, 235, 235), (x + duncan_vignette_x, y + duncan_vignette_y), duncan_vignette_radius)
    pygame.draw.circle(screen, (duncan_glow_color, duncan_glow_color, duncan_glow_color), (x + duncan_glow_x, y + duncan_glow_y), duncan_glow_radius)
    
    pygame.draw.rect(screen, "Black", (x + duncan_rect_x, y + duncan_rect_y, duncan_rect_sizex, duncan_rect_sizey))
    pygame.draw.circle(screen, "Black", (x + duncan_circle_x, y + duncan_circle_y), duncan_circle_radius)
    
    pygame.draw.rect(screen, "White", (x + duncan_inside_x, y + duncan_inside_y, duncan_inside_sizex, duncan_inside_sizey))
    pygame.draw.circle(screen, "White", (x + duncan_inner_circle_x, y + duncan_inner_circle_y), duncan_inner_circle_radius)
    
    pygame.draw.circle(screen, "Black", (x + duncan_eye_leftx, y + duncan_eye_lefty), duncan_eye_left_radius)
    pygame.draw.circle(screen, "Black", (x + duncan_eye_rightx, y + duncan_eye_righty), duncan_eye_right_radius)

    # ILIA ------------------
    current_time = pygame.time.get_ticks()
    
    # Change the color of the circle only if the flash_interval has passed
    if current_time - last_flash_time >= flash_interval:
        flash_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        last_flash_time = current_time

    sizeilia += growrate
    if sizeilia < 10 or sizeilia > 150:
        growrate = growrate *- 1
    x = 2560
    y = 1440
    width_ilia = 640
    height_ilia = 480

    pygame.draw.rect(screen, (45, 96, 255), (x, y, width_ilia, height_ilia))

    pygame.draw.circle(screen, flash_color, (x + circle_x_ilia, y + circle_y_ilia), sizeilia)

    # CHLOE ----------------------------------------------------------------------------------

    x = 1920
    y = 2400
    width = 640
    height = 480

    circle_x_chk += 1
    circle_a_chk += 2
    circle_b_chk += 1

    pygame.draw.rect(screen, (7, 26, 102), (x, y, width, height))

    # cloud
    # Must draw with reference to that coordinate

    cloud_ptone = pygame.draw.ellipse(screen, ("WHITE"), (x + 50 + circle_x_chk, y + 37 + circle_y_chk, 110, 30))
    cloud_pttwo = pygame.draw.ellipse(screen, ("WHITE"), (x + 68 + circle_x_chk, y + 25 + circle_y_chk, 35, 35))
    cloud_ptthree = pygame.draw.ellipse(screen, ("WHITE"), (x + 95 + circle_x_chk, y + 18 + circle_y_chk, 50, 50))
    if circle_x_chk > 640:
        circle_x_chk = -40
    # falling snow
    pygame.draw.circle(screen, "WHITE", (x + 122 + circle_x_chk, y + 117 + circle_a_chk), 6)
    pygame.draw.circle(screen, "WHITE", (x + 143 + circle_x_chk, y + 155 + circle_b_chk), 5)
    pygame.draw.circle(screen, "WHITE", (x + 181 + circle_x_chk, y + 206 + circle_a_chk), 5)
    pygame.draw.circle(screen, "WHITE", (x + 140 + circle_x_chk, y + 229 + circle_b_chk), 6)
    pygame.draw.circle(screen, "WHITE", (x + 102 + circle_x_chk, y + 146 + circle_a_chk), 6)
    pygame.draw.circle(screen, "WHITE", (x + 101 + circle_x_chk, y + 175 + circle_b_chk), 5)
    pygame.draw.circle(screen, "WHITE", (x + 122 + circle_x_chk, y + 228 + circle_a_chk), 6)

    if circle_a_chk > 460:
        circle_a_chk = -40
    if circle_b_chk > 480:
        circle_b_chk = -40
    # snow
    pygame.draw.circle(screen, "WHITE", (x + 43, y + 55), 4)
    pygame.draw.circle(screen, "WHITE", (x + 33, y + 167), 5)
    pygame.draw.circle(screen, "WHITE", (x + 117, y + 157), 4)
    pygame.draw.circle(screen, "WHITE", (x + 85, y + 134), 5)
    pygame.draw.circle(screen, "WHITE", (x + 104, y + 104), 5)
    pygame.draw.circle(screen, "WHITE", (x + 311, y + 41), 5)
    pygame.draw.circle(screen, "WHITE", (x + 285, y + 135), 5)
    pygame.draw.circle(screen, "WHITE", (x + 204, y + 201), 5)
    pygame.draw.circle(screen, "WHITE", (x + 145, y + 201), 5)
    pygame.draw.circle(screen, "WHITE", (x + 174, y + 281), 4)
    pygame.draw.circle(screen, "WHITE", (x + 308, y + 209), 5)
    pygame.draw.circle(screen, "WHITE", (x + 389, y + 98), 4)
    pygame.draw.circle(screen, "WHITE", (x + 388, y + 273), 5)
    pygame.draw.circle(screen, "WHITE", (x + 387, y + 188), 4)
    pygame.draw.circle(screen, "WHITE", (x + 355, y + 220), 5)
    pygame.draw.circle(screen, "WHITE", (x + 383, y + 145), 4)
    pygame.draw.circle(screen, "WHITE", (x + 307, y + 72), 5)
    pygame.draw.circle(screen, "WHITE", (x + 492, y + 72), 5)
    pygame.draw.circle(screen, "WHITE", (x + 462, y + 163), 4)
    pygame.draw.circle(screen, "WHITE", (x + 451, y + 128), 5)
    pygame.draw.circle(screen, "WHITE", (x + 455, y + 241), 4)
    pygame.draw.circle(screen, "WHITE", (x + 552, y + 162), 4)
    pygame.draw.circle(screen, "WHITE", (x + 519, y + 299), 4)
    pygame.draw.circle(screen, "WHITE", (x + 374, y + 306), 4)
    pygame.draw.circle(screen, "WHITE", (x + 161, y + 41), 4)
    pygame.draw.circle(screen, "WHITE", (x + 244, y + 47), 4)
    pygame.draw.circle(screen, "WHITE", (x + 181, y + 101), 4)
    pygame.draw.circle(screen, "WHITE", (x + 40, y + 256), 4)
    # snowman
    pygame.draw.ellipse(screen, "WHITE", [70 + x, 210 + y, 40, 40])
    pygame.draw.ellipse(screen, "WHITE", [57 + x, 235 + y, 65, 65])
    pygame.draw.ellipse(screen, "WHITE", [40 + x, 270 + y, 100, 100])
    pygame.draw.circle(screen, "BLACK", (x + 80, y + 225), 1)
    pygame.draw.circle(screen, "BLACK", (x + 95, y + 223), 1)
    pygame.draw.polygon(screen, "ORANGE", [(x + 87, y + 228), (x + 87, y + 231), (x + 96, y + 229)])
    pygame.draw.circle(screen, "GREY", (x + 87, y + 257), 5)
    pygame.draw.circle(screen, "GREY", (x + 88, y + 272), 5)
    pygame.draw.circle(screen, "GREY", (x + 91, y + 296), 5)
    pygame.draw.rect(screen, ("RED"), (x + 65, y + 236, 50, 10))
    pygame.draw.rect(screen, ("RED"), (x + 66, y + 246, 7, 80))

    # ground
    pygame.draw.rect(screen, (242, 250, 253), (x + 0.1, y + 355, width, 125))

    # gingerbread house
    pygame.draw.rect(screen, (182, 129, 98), (x + 360, y + 190, 230, 180))
    pygame.draw.polygon(screen, (134, 75, 42), [(x + 403, y + 105), (x + 547, y + 105), (x + 341, y + 203), (x + 617, y + 203)])
    pygame.draw.polygon(screen, (134, 75, 42), [(x + 403, y + 105), (x + 474, y + 139), (x + 341, y + 203)])
    pygame.draw.polygon(screen, (134, 75, 42), [(x + 403, y + 105), (x + 474, y + 137), (x + 341, y + 203)])
    pygame.draw.polygon(screen, (134, 75, 42), [(x + 547, y + 106), (x + 477, y + 139), (x + 616, y + 203)])
    pygame.draw.rect(screen, (152, 95, 63), (x + 465, y + 271, 45, 100))
    pygame.draw.ellipse(screen, ("WHITE"), [x + 390, y + 280, 50, 7])
    pygame.draw.ellipse(screen, ("WHITE"), [x + 530, y + 280, 50, 7])
    pygame.draw.rect(screen, ("WHITE"), (x + 397.5, y + 241, 35, 40))
    pygame.draw.ellipse(screen, "WHITE", [x + 397.5, y + 233, 35, 40])
    pygame.draw.rect(screen, ("WHITE"), (x + 536, y + 241, 35, 40))
    pygame.draw.ellipse(screen, "WHITE", [x + 536, y + 233, 35, 40])
    pygame.draw.rect(screen, (246, 226, 160), (x + 542.5, y + 244, 25, 30))
    pygame.draw.rect(screen, (246, 226, 160), (x + 402.5, y + 244, 25, 30))
    pygame.draw.line(screen, ("WHITE"), (x + 413, y + 241), (x + 413, y + 279))
    pygame.draw.line(screen, ("WHITE"), (x + 554, y + 240), (x + 554, y + 277))
    pygame.draw.line(screen, ("WHITE"), (x + 398, y + 263), (x + 428, y + 263))
    pygame.draw.line(screen, ("WHITE"), (x + 538, y + 262), (x + 568, y + 262))
    pygame.draw.circle(screen, (182, 129, 98), (x + 477, y + 296), 1)
    pygame.draw.circle(screen, (182, 129, 98), (x + 499, y + 296), 1)
    pygame.draw.circle(screen, (182, 129, 98), (x + 486, y + 323), 1)    
    pygame.draw.circle(screen, (182, 129, 98), (x + 477, y + 354), 1)
    pygame.draw.circle(screen, (182, 129, 98), (x + 500, y + 354), 1)
    pygame.draw.circle(screen, (182, 129, 98), (x + 500, y + 354), 1)
    pygame.draw.arc(screen, ("WHITE"), [x + 361, y + 146, 50, 50], 3.141592, 3.141592 * 2, 3)
    pygame.draw.arc(screen, ("WHITE"), [x + 413, y + 146, 50, 50], 3.141592, 3.141592 * 2, 3)
    pygame.draw.arc(screen, ("WHITE"), [x + 513, y + 146, 50, 50], 3.141592, 3.141592 * 2, 3)
    pygame.draw.arc(screen, ("WHITE"), [x + 461, y + 146, 50, 50], 3.141592, 3.141592 * 2, 3)
    pygame.draw.arc(screen, ("WHITE"), [x + 550, y + 146, 50, 50], 3.141592, 3.141592 * 2, 3)
    pygame.draw.circle(screen, ("RED"), (x + 410, y + 167), 5)
    pygame.draw.circle(screen, ("GREEN"), (x + 462, y + 163), 5)
    pygame.draw.circle(screen, ("RED"), (x + 510, y + 168), 5)
    pygame.draw.circle(screen, ("GREEN"), (x + 363, y + 168), 5)
    pygame.draw.circle(screen, ("RED"), (x + 594, y + 170), 5)
    pygame.draw.arc(screen, ("WHITE"), [x + 390, y + 100, 70, 50], 3.141592, 3.141592 * 2, 5)
    pygame.draw.arc(screen, ("WHITE"), [x + 450, y + 100, 70, 50], 3.141592, 3.141592 * 2, 5)
    pygame.draw.arc(screen, ("WHITE"), [x + 500, y + 100, 70, 50], 3.141592, 3.141592 * 2, 5)
    pygame.draw.arc(screen, ("DARK GREEN"), [x + 474, y + 255, 30, 30], 0, 3.141592 * 2, 7)
    

    # ----------------------------------------------------------------------------------------

    # Must have these coordinates
    x = 1920
    y = 1440
    width = 640
    height = 480

    frames_gallo += 1
    text_scale_gallo = abs((math.sin(frames_gallo / 30) - 3) / 3)
    

    # Rather than screen.fill, draw a rectangle
    screen.blit(bg_gallo, (x, y))

    screen.blit(welcome_text_gallo, (x + width//2 - welcome_text_gallo.get_width()//2, y + height//3 - welcome_text_gallo.get_height()//2))
    scaled_text = pygame.transform.scale(text_gallo, (text_gallo.get_width() * text_scale_gallo, text_gallo.get_height() * text_scale_gallo))
    screen.blit(scaled_text, (x + width//2 - scaled_text.get_width()//2, y + height//2 - scaled_text.get_height()//2))
    


    # LEAVE HERE --------------------------------------------
    screen_width, screen_height = screen.get_size()
    scaled_screen = pygame.transform.scale(screen, (int(screen_width * scale), int(screen_height * scale)))
    window.blit(scaled_screen, (-camera_x*scale+WIDTH//2, -camera_y*scale+HEIGHT//2))

    pygame.display.flip()
    clock.tick(30)
    #---------------------------------------------------------


pygame.quit()
