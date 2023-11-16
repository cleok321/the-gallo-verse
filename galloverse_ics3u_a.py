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

star_x_christine = 640*5
star_y_christine = 0

switch_christine = "right"

#--------------------------

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
olivia_timer = 0
olivia_circle_counter = 0

olivia_circles_list = []

olivia_text = "Aw sweet! Man-made horrors beyond my comprehension!"

olivia_font = pygame.font.SysFont("Arial",20)

for i in range(20,640,40):
    for j in range(20,480,40):
        if (i + j) % 80 == 0:
            olivia_circles_list.append({"x":i,"y":j})

#HUZZAH I DONT NEED TO WORRY ABOUT VARIABLE NAMES THANK GOD FOR LOCAL VARIABLES
def olivia_draw_circles():
    for circle in olivia_circles_list:
        num = (circle["x"] + circle["y"])/20 + olivia_timer
        r = 255 * abs(math.cos(math.pi*(num/60-1/3)))
        g = 255 * abs(math.cos(math.pi*(num/60-2/3)))
        b = 255 * abs(math.cos(math.pi*(num/60-3/3)))
        
        circle_x = x+circle["x"]
        circle_y = y+circle["y"]+math.sin(math.pi*num/20)*8
        circle_colour = (r,g,b)
        circle_size = 20
        # mouse hover doesn't work in galloverse :(
        '''mouse_x, mouse_y = pygame.mouse.get_pos()       
        x_distance = abs(circle_x - mouse_x)
        y_distance = abs(circle_y - mouse_y)
        
        if x_distance <= 100 and y_distance <= 100:
            circle_size += (200 - x_distance - y_distance)/10'''
        
        pygame.draw.circle(screen,circle_colour,(circle_x,circle_y),circle_size)

def olivia_generate_text():
    letters = "aaaaaaaabbcccddddeeeeeeeeeeeefffgghhhhhhiiiiiiiijkllllmmmnnnnnnnnooooooooppqrrrrrrsssssssstttttttttuuuvwwxyyz"
    symbols = "!?,.:;"
    string = " "
    for i in range(15):
        num = random.randrange(0,25)
        if num == 24 and string[i-1] not in symbols and string[i-1] != " ":
            string += symbols[random.randrange(0,len(symbols))] + " "
        elif num > 15 and string[i-1] != " ":
            string += " "
        else:
            string += letters[random.randrange(0,len(letters))]
    string += symbols[random.randrange(0,3)]
    string = string [1:]
    return(string)
# ------------------

cord_yang1 = 320
cord_yang3 = 440
cord_yang2 = 440
cord_yang4 = 200
cord_yang5 = 200
count_yang = 0
upyang = 0
upyang2 = 0
upyang3 = 0
upyang4 = 0
upyang5 = 0

#-----------------

#position (0, 1440)
#OUTSIDE LOOP:
DARK_GREEN = (24, 87, 13)
EVERGREEN = (35, 130, 4)
bark_x_ocampo = 20
bark_y_ocampo = 1670

leaves_x_ocampo = 75
leaves_y_ocampo = 1575

x = 0 
y = 0 

#Car outer
polygon_ocampo = [
(x, y+300),
(x+10, y+100),
(x+60, y+275),
(x+65, y+80),
(x+150, y+80),
(x+140, y+140),
(x+175, y+155),
(x+200, y+300)
]

#Window
polygon_ocampo2 = [
(x+50, y+270),
(x+50, y+240),
(x+140, y+240),
(x+190, y+290)
]

#Wheels
polygon_ocampo3 = [
(x+30, y+340),
(x+67, y+310),
(x+100, y+340),
(x+67, y+370)
]

polygon_ocampo4 = [
(x+210, y+340),
(x+247, y+310),
(x+280, y+340),
(x+247, y+370)
]
# Lucas -----------------

asteroid_x_p = 0
asteroid_y_p = 0

asteroid_2_x_p = 0 
asteroid_2_y_p = 0

smallhole_1_x_p = 20
smallhole_1_y_p = 10

smallhole_2_x_p = -20
smallhole_2_y_p = -10

smallhole_3_x_p = 20
smallhole_3_y_p = -20

smallhole_4_x_p = -5
smallhole_4_y_p = 30

ufo_body_x_p  = 0
ufo_body_y_p = 0 

line1_x_p = 0 

#Jaden Lam-------------------
#Stars
x_lam = random.randrange(10, 50)
y_lam = random.randrange(10, 50)
size_lam = random.randrange(1, 3)

#Stars' Colour
white_r_lam = 255
white_g_lam = 255
white_b_lam = 255
    
blue_g_lam = 200
blue_b_lam = 255
    
red_r_lam = 255
    
yellow_r_lam = 255
yellow_g_lam = 255

#Space Ship
tri_x_lam = 0
tri_y_lam = 0
tri_r_lam = 255
tri_g_lam = 255
tri_b_lam = 255

#-------------------
car_x_matros = 0
parking_lines = 0
road_lines1 = 0
road_lines2 = 0
sidewalk_lines1 = 0
sidewalk_lines2 = 0

#-------------------

line_x_joanne = 200
plane_x_joanne = 0
frames_joanne = 0
num_dashes_joanne = 0

#-------------------
arm_r_a_rhee = 320
arm_r_b_rhee = 290
hand_r_rhee = 305
hand_r_y_rhee = 270
arm_r_y_a_rhee = 260
arm_r_y_b_rhee = 265
wave_a_rhee = False
wave_b_rhee = False
wave_c_rhee = False
arm_l_a_rhee = 160
arm_l_b_rhee = 190
hand_l_rhee = 175
hand_l_y_rhee = 270
arm_l_y_a_rhee = 260
arm_l_y_b_rhee = 265
arm_far_rhee = False
eye_a_rhee = 150
eye_b_rhee = 25
eye_c_rhee = 163
eye_d_rhee = 8
blink_rhee = False

# -------------------

circle_x_sebast = 200
circle_y_sebast = 100
river_sebast = 250

random_x_sebast = random.randrange(0, 640)
random_y_sebast = random.randrange(0, 480)

plot_width_sebast = 640
duck_behind_x = 200

plot_height_sebast = 480


building_x_sebast = 50
count_sebast = 0

#_-----------------

circle_x_chk = 40
circle_y_chk = 40
circle_a_chk = 40
circle_b_chk = 40

# -----------------

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

    #Christine ----------------------------
    x = 0
    y = 0
    width = 640
    height = 480

    points_christine = [
        (star_x_christine + 0, star_y_christine + 45),
        (star_x_christine + 20, star_y_christine + 45),
        (star_x_christine + 30, star_y_christine +25),
        (star_x_christine + 40, star_y_christine + 45),
        (star_x_christine + 60, star_y_christine + 45),
      
        (star_x_christine + 45, star_y_christine + 60),
        (star_x_christine + 55, star_y_christine + 80),
        (star_x_christine + 30, star_y_christine +65),
        (star_x_christine + 5, star_y_christine + 80),
        (star_x_christine + 15, star_y_christine + 60)
    ]

    roof_points = [
        (x+165, y+170),
        (x+250, y+200),
        (x+485, y+170)
    ]
    
    if star_x_christine > 640:
        switch_christine = "left"
    elif star_x_christine < 0:
        switch_christine = "right"

    if switch_christine == "right":
        star_x_christine += 3
    else:
        star_x_christine -=3

    #Background
    pygame.draw.rect(screen, (152,245,255), (x, y, width, height))

    #Rain?
    for i in range(30):
        pygame.draw.circle(screen, (255,187,255), (x+40, y+50+20*i), 3)
        pygame.draw.circle(screen, (255,187,255), (x+90, y+50+20*i), 3)
        pygame.draw.circle(screen, (221,160,221), (x+570, y+50+20*i), 3)
        pygame.draw.circle(screen, (221,160,221), (x+60, y+50+20*i), 3)
        pygame.draw.circle(screen, (255,187,255), (x+620, y+50+20*i), 3)
        pygame.draw.circle(screen, (255,187,255), (x+530, y+50+20*i), 3)

    #Clouds
    pygame.draw.circle(screen, (255,225,255), (x+160, y+350), 35)
    pygame.draw.circle(screen, (255,225,255), (x+200, y+350), 45)
    pygame.draw.circle(screen, (255,225,255), (x+260, y+350), 65)
    pygame.draw.circle(screen, (255,225,255), (x+300, y+350), 60)
    pygame.draw.circle(screen, (255,225,255), (x+320, y+350), 65)
    pygame.draw.circle(screen, (255,225,255), (x+360, y+350), 50)
    pygame.draw.circle(screen, (255,225,255), (x+400, y+350), 65)
    pygame.draw.circle(screen, (255,225,255), (x+460, y+350), 45)
    pygame.draw.circle(screen, (255,225,255), (x+500, y+350), 35)

    for i in range(5):
        pygame.draw.circle(screen, (216,191,216), (x+0+45*i, y+50), 40)
        pygame.draw.circle(screen, (255,225,255), (x+140+35*i, y+80), 35)

    for i in range(3):
        pygame.draw.circle(screen, (216,191,216), (x+530+45*i, y+80), 40)
    for i in range(2):
        pygame.draw.circle(screen, (255,225,255), (x+0+45*i, y+200), 40)

    #House
    pygame.draw.rect(screen, (255,182,193), (x+165, y+170, 320, 160))

    #Outline
    pygame.draw.line(screen, (171,130,255), (x+250, y+200), (x+250, y+350), width=2)
    pygame.draw.line(screen, (171,130,255), (x+165, y+170), (x+165, y+340), width=2)
    pygame.draw.line(screen, (171,130,255), (x+485, y+170), (x+485, y+350), width=2)
    
    #Windows
    pygame.draw.line(screen, (171,130,255), (x+265, y+235), (x+470, y+210), width=30)    
    pygame.draw.line(screen, (171,130,255), (x+190, y+215), (x+220, y+225), width=30)    
    pygame.draw.line(screen, (171,130,255), (x+190, y+275), (x+220, y+285), width=30) 
    pygame.draw.line(screen, (171,130,255), (x+265, y+290), (x+470, y+270), width=30) 
       
    #Roof
    pygame.draw.polygon(screen, (171,130,255), roof_points)
    
    #Candle
    pygame.draw.rect(screen, (75,0,130), (x+245, y+140, 10, 50))
    pygame.draw.circle(screen, (255,215,0), (x+250, y+140), 10)

    #Clouds
    pygame.draw.circle(screen, (255,225,255), (x+320, y+350), 40)
    pygame.draw.circle(screen, (255,225,255), (x+260, y+345), 30)
    pygame.draw.circle(screen, (255,225,255), (x+200, y+350), 40)
    pygame.draw.circle(screen, (255,225,255), (x+450, y+350), 45)
    
    #Star
    pygame.draw.polygon(screen, (255,215,0), points_christine)

    
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
    #  OLIVIA ------------------
    x = 3840
    y = 1440
    if olivia_timer % 60 == 0:
        olivia_text = olivia_font.render(olivia_generate_text(),True,"black")
    olivia_timer += 1
    pygame.draw.rect(screen,(80,30,70),(x,y,640,480))
    olivia_draw_circles()
    
    olivia_cat_x = 5*(abs(100-olivia_timer/2%200))+x-75
    olivia_cat_y = -50*(abs(math.sin(olivia_timer/10)))+y
    #text
    pygame.draw.ellipse(screen,"black",(olivia_cat_x+50,y+150,180,120))
    pygame.draw.polygon(screen,"black",((olivia_cat_x+125,y+263),(olivia_cat_x+155,y+263),(olivia_cat_x+140,olivia_cat_y*0.5+y*0.5+330)))
    pygame.draw.ellipse(screen,"white",(olivia_cat_x+54,y+154,172,112))
    pygame.draw.polygon(screen,"white",((olivia_cat_x+130,y+260),(olivia_cat_x+150,y+260),(olivia_cat_x+140,olivia_cat_y*0.5+y*0.5+320)))
    screen.blit(olivia_text,(olivia_cat_x+70,y+195))
    
    #body
    pygame.draw.ellipse(screen,"black",(olivia_cat_x+96,olivia_cat_y+351,88,78))
    pygame.draw.polygon(screen,"black",((olivia_cat_x+104,olivia_cat_y+340),(olivia_cat_x+101,olivia_cat_y+377),(olivia_cat_x+131,olivia_cat_y+360)))
    pygame.draw.polygon(screen,"black",((olivia_cat_x+175,olivia_cat_y+340),(olivia_cat_x+178,olivia_cat_y+377),(olivia_cat_x+148,olivia_cat_y+360)))
    pygame.draw.ellipse(screen,"white",(olivia_cat_x+100,olivia_cat_y+355,80,70))
    pygame.draw.polygon(screen,"white",((olivia_cat_x+106,olivia_cat_y+345),(olivia_cat_x+106,olivia_cat_y+370),(olivia_cat_x+126,olivia_cat_y+360)))
    pygame.draw.polygon(screen,"white",((olivia_cat_x+173,olivia_cat_y+345),(olivia_cat_x+173,olivia_cat_y+370),(olivia_cat_x+153,olivia_cat_y+360)))
    #mouth
    if 100-olivia_timer/2%200 > 0:
        olivia_cat_x -= 5
    else:
        olivia_cat_x += 5
    pygame.draw.ellipse(screen,"black",(olivia_cat_x+127,olivia_cat_y+378,26,39))
    pygame.draw.ellipse(screen,"white",(olivia_cat_x+130,olivia_cat_y+381,20,33))
    pygame.draw.ellipse(screen,"black",(olivia_cat_x+122,olivia_cat_y+378,20,20))
    pygame.draw.ellipse(screen,"black",(olivia_cat_x+138,olivia_cat_y+378,20,20))
    pygame.draw.ellipse(screen,"white",(olivia_cat_x+119,olivia_cat_y+376,23,19))
    pygame.draw.ellipse(screen,"white",(olivia_cat_x+138,olivia_cat_y+376,23,19))
    pygame.draw.rect(screen,"white",(olivia_cat_x+120,olivia_cat_y+370,40,20))
    #eyes
    pygame.draw.ellipse(screen,"black",(olivia_cat_x+123,olivia_cat_y+380,6,8))
    pygame.draw.ellipse(screen,"black",(olivia_cat_x+151,olivia_cat_y+380,6,8))

    # Lucas -----------------------------------------------------------

    asteroid_x_p += 1
    asteroid_y_p += 1
    smallhole_1_x_p += 1
    smallhole_1_y_p += 1
    smallhole_2_x_p += 1
    smallhole_2_y_p += 1
    smallhole_3_x_p += 1
    smallhole_3_y_p += 1
    smallhole_4_x_p += 1
    smallhole_4_y_p += 1
    asteroid_2_x_p += 1.5
    asteroid_2_y_p += 1.5
    ufo_body_x_p += 1
    line1_x_p += 1
    
    x = 1280
    y = 960
    width = 640
    height = 480
    circle_list_p = []
    for i in range(40):
        circle_p = {
            'x_p': random.randint(x, x + 640),
            'y_p': random.randint(y, y + 480),
            'radius_p': random.randint(1,4)
        }
        circle_list_p.append(circle_p)
    ufo_body_y_p = int((HEIGHT - 200) / 2 + math.sin(ufo_body_x_p / 100) * 100)
    line1_y_p = int((HEIGHT - 200) / 2 + math.sin(line1_x_p / 100) * 100)
    flame_variation_1_p = random.randint(-5, 5)  
    if asteroid_y_p - 50 >= HEIGHT or asteroid_x_p - 50 >= WIDTH:
      asteroid_x_p = x
      asteroid_y_p = y
      smallhole_1_x_p = x + 20
      smallhole_1_y_p = y + 20
      smallhole_2_x_p = x - 20
      smallhole_2_y_p = y - 10
      smallhole_3_x_p = x + 20
      smallhole_3_y_p = y - 20
      smallhole_4_x_p = x - 5
      smallhole_4_y_p = y + 30
    if asteroid_2_y_p >= HEIGHT or asteroid_2_x_p >= WIDTH:
      asteroid_2_x_p = x
      asteroid_2_y_p = y 
    if ufo_body_y_p >= HEIGHT or ufo_body_x_p >= WIDTH:
      ufo_body_x_p = x 
      ufo_body_y_p = y
      line1_x_p = x
      line1_y_p = y
    pygame.draw.rect(screen, (20, 20, 20), (x, y, width, height))
# STARS
    for circle_p in circle_list_p:  
      pygame.draw.circle(screen, (255, 255, 255), (x + circle_p['x_p'], y + circle_p['y_p']), circle_p['radius_p'])
# PLANET
    pygame.draw.circle(screen, (20, 20, 160), (x + 30, y + 200), 10)
    pygame.draw.polygon(screen, (20, 160, 20), [(x + 31, y + 202), (x + 34, y + 200), (x + 36, y + 202), (x + 30, y + 210), (x + 28, y + 202)])
    pygame.draw.polygon(screen, (20, 160, 20), [(x + 25, y + 195), (x + 28, y + 194), (x + 30, y + 197), (x + 24, y + 199), (x + 22, y + 202)])
# PLANET 2
    pygame.draw.circle(screen, (201, 28, 40), (x + 300, y + 100), 10)
    pygame.draw.polygon(screen, (227, 151, 70), [(x + 301, y + 102), (x + 306, y + 102), (x + 300, y + 110)])
    pygame.draw.polygon(screen, (227, 151, 70), [(x + 295, y + 95), (x + 300, y + 97), (x + 294, y + 99), (x + 292, y + 102)])
# UFO
    pygame.draw.ellipse(screen, (173, 169, 163), (x + ufo_body_x_p, y + ufo_body_y_p + 100, 50, 20), 0)
    pygame.draw.arc(screen, (67, 153, 91), (x + ufo_body_x_p + 8, y + ufo_body_y_p + 90, 33, 40), 0, 3.14, 300)
    pygame.draw.line(screen, (123, 237, 119), (x +  line1_x_p +10, y + line1_y_p + 125), (x + line1_x_p, y + line1_y_p + 140), 3) 
    pygame.draw.line(screen, (123, 237, 119), (x +  line1_x_p + 25, y + line1_y_p + 127), (x + 25 + line1_x_p, y + line1_y_p + 142), 3) 
    pygame.draw.line(screen, (123, 237, 119), (x +  line1_x_p + 40, y + line1_y_p + 125), (x + 50 + line1_x_p, y + line1_y_p + 140), 3) 
# ASTEROID 1 (BIG ONE)
    pygame.draw.polygon(screen, (84, 200, 204), [(x + asteroid_x_p, y + asteroid_y_p - 50), (x + asteroid_x_p - 50, y + asteroid_y_p), (x + asteroid_x_p - 100 + flame_variation_1_p, y + asteroid_y_p - 100)])
    pygame.draw.polygon(screen, (93, 144, 158), [(x + asteroid_x_p, y + asteroid_y_p - 50), (x + asteroid_x_p - 50, y + asteroid_y_p), (x + asteroid_x_p - 75 + flame_variation_1_p, y + asteroid_y_p - 75)])
    pygame.draw.circle(screen, (140, 129, 116), (x + asteroid_x_p, y + asteroid_y_p), 50)
    pygame.draw.circle(screen, (89, 85, 80), (x + smallhole_1_x_p, y + smallhole_1_y_p), 10)
    pygame.draw.circle(screen, (89, 85, 80), (x + smallhole_2_x_p, y + smallhole_2_y_p), 20)
    pygame.draw.circle(screen, (89, 85, 80), (x + smallhole_3_x_p, y + smallhole_3_y_p), 7)
    pygame.draw.circle(screen, (89, 85, 80), (x + smallhole_4_x_p, y + smallhole_4_y_p), 9)    

    # Youlchan --------------------------------------------------------

    x = 0
    y = 480 * 5
    width = 640
    height = 480
    # animation
    count_yang += 1
    if count_yang == 1:
      n_yang = random.randrange(16)
      n_yang2 = random.randrange(16)
      n_yang3 = random.randrange(16)
      n_yang4 = random.randrange(16)
      n_yang5 = random.randrange(16)
      yang1 = random.randrange(6)
      yang2 = random.randrange(6)
      yang3 = random.randrange(6)
      yang4 = random.randrange(6)
      yang5 = random.randrange(6)
    if count_yang == 20:
      cord_yang3 += n_yang
      cord_yang1 -= n_yang2
      cord_yang2 -= n_yang3
      upyang4 -= yang4
      upyang5 += yang5
    if count_yang == 30:
      upyang += yang1
      upyang2 -= yang2
      upyang3 += yang3
      cord_yang4 += n_yang4
      cord_yang5 += n_yang5
    if count_yang == 40:
      cord_yang3 -= n_yang*2
      cord_yang1 += n_yang2*2
      cord_yang2 += n_yang3*2
      upyang -= yang1*2
      upyang2 += yang2*2
      upyang5 -= yang5*2
    if count_yang == 50:
      cord_yang4 += n_yang4
      cord_yang5 += n_yang5
      upyang3 -= yang3*2
      upyang4 += yang4*2
    if count_yang == 60:
      cord_yang1 = 320
      cord_yang4 = 200
      cord_yang5 = 200
      upyang4 = 0
      upyang5 = 0
    if count_yang == 70:
      cord_yang3 = 440
      cord_yang2 = 440
      upyang = 0
      upyang2 = 0
      upyang3 = 0
      count_yang = 0
    # bg
    pygame.draw.rect(screen, (150,20,20), (x, y, width, height))

  
    
    # Sclera 
    pygame.draw.ellipse(screen, (255,255,255),(x + 320 - 60 ,y + 240 - 30, 120, 60))
    pygame.draw.ellipse(screen, (255,255,255),(x + 440 - 30,y + 380 , 120, 60))
    pygame.draw.ellipse(screen, (255,255,255),(x + 440 - 30,y + 100 - 60, 120, 60))
    pygame.draw.ellipse(screen, (255,255,255),(x + 200 - 90,y + 380 , 120, 60))
    pygame.draw.ellipse(screen, (255,255,255),(x + 200 - 90,y + 100- 60, 120, 60))
    #Iris
    pygame.draw.circle(screen, (255,100, 100),(x + cord_yang1 ,y + 240 + upyang), 30)
    pygame.draw.circle(screen, (255,100, 100),(x + cord_yang2+30, y+410 + upyang2),30)
    pygame.draw.circle(screen, (255,100, 100),(x + cord_yang3 + 30,y + 70 + upyang3), 30)
    pygame.draw.circle(screen, (255,100, 100),(x + cord_yang4 -30,y + 410 + upyang4), 30)
    pygame.draw.circle(screen, (255,100, 100),(x + cord_yang5 -30,y + 70 + upyang5), 30)
    #Pupil
    pygame.draw.circle(screen, (25,50,50),(x + cord_yang1 ,y + 240 + upyang), 15)
    pygame.draw.circle(screen, (0,0,0),(x + cord_yang2 + 30 ,y + 410 + upyang2), 15)
    pygame.draw.circle(screen, (0,0,0),(x + cord_yang3 + 30,y + 70 + upyang3), 15)
    pygame.draw.circle(screen, (0,0,0),(x + cord_yang4 -30,y + 410 + upyang4), 15)
    pygame.draw.circle(screen, (0,0,0),(x + cord_yang5 -30,y + 70 + upyang5), 15)

    # JOSH OCAMPO ---------------------------------------------------------------------------------------
    x = 0
    y = 1440
    width = 640
    height = 480
    
    bark_x_ocampo -= 5
    leaves_x_ocampo -= 5

    # Must draw with reference to that coordinate
    #car
    pygame.draw.polygon(screen, (245, 32, 17), ((x, y+340), (x+10, y+280), (x+60, y+280), (x+65, y+250), (x+150, y+250), (x+200, y+290), (x+290, y+300), (x+300, y+340)))
    pygame.draw.polygon(screen, (15, 245, 252), ((x+67, y+280), (x+72, y+255), (x+143, y+255), (x+190, y+290)))
    pygame.draw.rect(screen, (245, 32, 17), (x+110, y+250, 7, 40))
    pygame.draw.polygon(screen, (46, 44, 44), ((x+30, y+340), (x+67, y+310), (x+100, y+340),(x+67, y+370)))
    pygame.draw.polygon(screen, (46, 44, 44), ((x+210, y+340), (x+247, y+310), (x+280, y+340),(x+247, y+370)))

    #tree
    pygame.draw.rect(screen, (105, 71, 13), (bark_x_ocampo + 90, bark_y_ocampo - 100, 35, 250))
    pygame.draw.circle(screen, (EVERGREEN), (leaves_x_ocampo, leaves_y_ocampo), 40)
    pygame.draw.circle(screen, (DARK_GREEN), (leaves_x_ocampo + 25, leaves_y_ocampo - 30), 37)
    pygame.draw.circle(screen, (EVERGREEN), (leaves_x_ocampo + 65, leaves_y_ocampo - 20), 50)
    pygame.draw.circle(screen, (EVERGREEN), (leaves_x_ocampo + 65, leaves_y_ocampo + 20), 40)
    pygame.draw.circle(screen, (DARK_GREEN), (leaves_x_ocampo + 35, leaves_y_ocampo + 40), 40)
    pygame.draw.circle(screen, (DARK_GREEN), (leaves_x_ocampo + 95, leaves_y_ocampo + 30), 40)
    if leaves_x_ocampo == -100: 
        bark_x_ocampo = 640 
        leaves_x_ocampo = 695

    #Jaden Lam-------------------------------------------------------------------------------
    x = 640 * 4
    y = 0
    
    #Star Blinking
    blink_lam = random.randrange(1, 16)
    
    if blink_lam == 1:
        white_r_lam = 0
        white_g_lam = 0
        white_b_lam = 0
    if blink_lam == 2:
        blue_g_lam = 0
        blue_b_lam = 0
    if blink_lam == 3:
        red_r_lam = 0
    if blink_lam == 4:
        yellow_r_lam = 0
        yellow_g_lam = 0

    #Space Ship
    tri_x_lam += 2
    if tri_r_lam != 0:
        tri_r_lam -= 1
        tri_g_lam -= 1
        tri_b_lam -= 1
    
    #White Stars
    pygame.draw.circle(screen, (white_r_lam, white_g_lam, white_b_lam), (x+x_lam+100, y+y_lam+150), size_lam-1)
    pygame.draw.circle(screen, (white_r_lam, white_g_lam, white_b_lam), (x+x_lam+360, y+y_lam+300), size_lam-2)
    pygame.draw.circle(screen, (white_r_lam, white_g_lam, white_b_lam), (x+x_lam+150, y+y_lam+40), size_lam+1)
    #Blue Stars
    pygame.draw.circle(screen, (0, blue_g_lam, blue_b_lam), (x+x_lam+200, y+y_lam+260), size_lam-2)
    pygame.draw.circle(screen, (0, blue_g_lam, blue_b_lam), (x+x_lam, y+y_lam+120), size_lam)
    pygame.draw.circle(screen, (0, blue_g_lam, blue_b_lam), (x+x_lam+450, y+y_lam+220), size_lam+1)
    #Red Stars
    pygame.draw.circle(screen, (red_r_lam, 0, 0), (x+x_lam+400, y+y_lam+120), size_lam+2)
    pygame.draw.circle(screen, (red_r_lam, 0, 0), (x+x_lam+160, y+y_lam+250), size_lam-1)
    pygame.draw.circle(screen, (red_r_lam, 0, 0), (x+x_lam+300, y+y_lam+180), size_lam)
    #Yellow Stars
    pygame.draw.circle(screen, (yellow_r_lam, yellow_g_lam, 0), (x+x_lam+210, y+y_lam+240), size_lam)
    pygame.draw.circle(screen, (yellow_r_lam, yellow_g_lam, 0), (x+x_lam+490, y+y_lam+60), size_lam-2)
    pygame.draw.circle(screen, (yellow_r_lam, yellow_g_lam, 0), (x+x_lam+30, y+y_lam+280), size_lam+1)
    
    #Space Ship
    pygame.draw.polygon(screen, (tri_r_lam, tri_g_lam, tri_b_lam), [(x+tri_x_lam, y+tri_y_lam+150), (x+tri_x_lam, y+tri_y_lam+200), (x+tri_x_lam+100, y+tri_y_lam+175)])

     # -----------------------------------------Joakim start

    # DRAWING
    # Must have these coordinates
    x = 1280
    y = 480
    width = 640
    height = 480


     # sky
    pygame.draw.rect(screen, (70, 200, 225), (x, y, plot_width_sebast, plot_height_sebast))
    #grass
    pygame.draw.rect(screen, (10, 225, 155), (x, y + plot_height_sebast /2 + 50, plot_width_sebast, plot_height_sebast/6)) 

    # Must draw with reference to that coordinate
    #river
    pygame.draw.rect(screen, (0, 155, 255), (x, y + plot_height_sebast - 140, plot_width_sebast, plot_height_sebast/4)) 

    #   Chimney
    pygame.draw.rect(screen, (0, 0, 0), (x + 200, y + 50, 30, 150))
    #building 
    pygame.draw.rect(screen, (60, 60, 90), (x + 150, y + 150, 400, 150))
    # roof
    pygame.draw.polygon(screen, (72, 54, 41), ( (x +  100, y + 150), (x  + 330, y + 70), (x + 600, y + 150) ))

    # duck
    #duck body
    pygame.draw.ellipse(screen, (225, 225, 0), (x + circle_x_sebast, y + circle_y_sebast + river_sebast, 100, 60), 30)
    #river on duck
    pygame.draw.ellipse(screen, (0, 155, 225), (x + circle_x_sebast - 10, y + circle_y_sebast + 35 + river_sebast, 130, 60), 30)

    #duck head
    pygame.draw.circle(screen, (225, 225, 0), (x + circle_x_sebast + 85, y + circle_y_sebast - 5 + river_sebast), 20)

    #duck eye
    pygame.draw.circle(screen, (0, 0, 0), (x + circle_x_sebast + 80, y + circle_y_sebast - 15 + river_sebast ), 3)

    #duck beak
    pygame.draw.rect(screen, (225, 100, 0), (x + circle_x_sebast + 90, y + circle_y_sebast - 5 + river_sebast, 17, 5), 10)  

    #duck body
    pygame.draw.ellipse(screen, (225, 200, 0), (x + circle_x_sebast - duck_behind_x, y + circle_y_sebast + river_sebast, 100, 60), 30)

    #river on duck
    pygame.draw.ellipse(screen, (0, 155, 225), (x + circle_x_sebast - duck_behind_x - 10, y + circle_y_sebast + 35 + river_sebast, 130, 60), 30)

    #duck head
    pygame.draw.circle(screen, (225, 200, 0), (x + circle_x_sebast + 85 - duck_behind_x, y + circle_y_sebast - 5 + river_sebast), 20)

    #duck eye
    pygame.draw.circle(screen, (0, 0, 0), (x + circle_x_sebast + 80 - duck_behind_x, y + circle_y_sebast - 15 + river_sebast ), 3)

    #duck beak
    pygame.draw.rect(screen, (225, 100, 0), (x + circle_x_sebast + 90 - duck_behind_x, y + circle_y_sebast - 5 + river_sebast, 17, 5), 10)  

    if circle_x_sebast < plot_width_sebast - 150:
      circle_x_sebast += 1
    else:
      circle_x_sebast = 100

    while building_x_sebast < 600:
      building_x_sebast += 100


    random_x_sebast = random.randrange(0, 640)
    random_y_sebast = random.randrange(0, 480)


    if count_sebast % 3 == 0:
      pygame.draw.rect(screen, (90, 150, 255), (x + random_x_sebast, y + random_y_sebast, 2, 30)) 

    count_sebast += 1

    #------- Joakim end


    
    # Christian -------------------------------------------------------------------------------------
    x = 3840
    y = 2880
    width = 640
    height = 480
    
    car_x_matros += 3
    
    if car_x_matros > width:
        car_x_matros = 0
    
    # Rather than screen.fill, draw a rectangle
    pygame.draw.rect(screen, (0, 66, 0), (x, y, width, height-200))

    # Parking Lot
    # Background Parking
    pygame.draw.rect(screen, (80, 80, 80), (x, y+200, width-300, height))

    # Parking Lines
    while parking_lines < (width-300):
        pygame.draw.rect(screen, (255, 255, 255), (x+parking_lines, y+350, width-635, height-350))
        parking_lines += 50
    pygame.draw.rect(screen, (255, 255, 255), (x, y+415, width-337, height-475))

    # Road
    # Sidewalk
    pygame.draw.rect(screen, (166, 166, 166), (x, y+90, width, height-300))
    pygame.draw.rect(screen, (166, 166, 166), (x+320, y, width-460, height))
    while sidewalk_lines1 <= width:
        pygame.draw.rect(screen, (150, 150, 150), (x+sidewalk_lines1, y+90, width-638, height-300))
        sidewalk_lines1 += 30
    while sidewalk_lines2 <= height:
        pygame.draw.rect(screen, (150, 150, 150), (x+320, y+sidewalk_lines2, width-460, height-478))
        sidewalk_lines2 += 30
    
    # Road Entrance to Lot
    road_entrance = [
        (x+312, y+270),
        (x+355, y+270),
        (x+355, y+330),
        (x+312, y+330)
    ]
    pygame.draw.polygon(screen, (80, 80, 80), road_entrance)
    
    # Main road
    pygame.draw.rect(screen, (80, 80, 80), (x, y+120, width, height-360))
    pygame.draw.rect(screen, (0, 0, 0), (x, y+130, width, height-380))
    while road_lines1 <= width:
        pygame.draw.rect(screen, (255, 255, 0), (x+road_lines1, y+175, width-610, height-475))   
        road_lines1 += 50
    pygame.draw.rect(screen, (80, 80, 80), (x+350, y, width-520, height))
    pygame.draw.rect(screen, (0, 0, 0), (x+360, y, width-540, height))
    while road_lines2 <= height:
        pygame.draw.rect(screen, (255, 255, 0), (x+405, y+road_lines2, width-635, height-450))
        road_lines2 += 50
    road_center_matros = [
        (x+350, y+130),
        (x+470, y+130),
        (x+470, y+229),
        (x+350, y+229)
    ]
    pygame.draw.polygon(screen, (0, 0, 0), road_center_matros)

    # Car 1
    car_body_matros = [
        (x + car_x_matros, y + 191),
        (x + 80 + car_x_matros, y + 191),
        (x + 80 + car_x_matros, y + 220),
        (x + car_x_matros, y + 220)
    ]

    car_frontlight1 = [
        (x + 75 + car_x_matros, y + 195),
        (x + 75 + car_x_matros, y + 202),
        (x + 80 + car_x_matros, y + 202),
        (x + 80 + car_x_matros, y + 195)
    ]

    car_frontlight2 = [
        (x + 75 + car_x_matros, y+206),
        (x + 75 + car_x_matros, y+213),
        (x + 80 + car_x_matros, y+213),
        (x + 80 + car_x_matros, y+206)
    ]

    car_backlight1 = [
        (x + car_x_matros, y + 191),
        (x + car_x_matros, y + 198),
        (x + 5 + car_x_matros, y + 198),
        (x + 5 + car_x_matros, y + 191)
    ]

    car_backlight2 = [
        (x + car_x_matros, y + 220),
        (x + car_x_matros, y + 213),
        (x + 5 + car_x_matros, y + 213),
        (x + 5 + car_x_matros, y + 220)
    ]

    car_windshield = [
        (x + 68 + car_x_matros, y + 194),
        (x + 54 + car_x_matros, y + 199),
        (x + 54 + car_x_matros, y + 212),
        (x + 68 + car_x_matros, y + 217)
        
    ]
    
    pygame.draw.polygon(screen, (0, 99, 0), car_body_matros)
    pygame.draw.polygon(screen, (255, 255, 0), car_frontlight1)
    pygame.draw.polygon(screen, (255, 255, 0), car_frontlight2)
    pygame.draw.polygon(screen, (255, 0, 0), car_backlight1)
    pygame.draw.polygon(screen, (255, 0, 0), car_backlight2)
    pygame.draw.polygon(screen, (0, 0, 99), car_windshield)

    # Car 2
    b_car_body_matros = [
        (x + 450, y + 357),
        (x + 421, y + 357),
        (x + 421, y + 437),
        (x + 450, y + 437)
    ]

    b_car_frontlight1 = [
        (x + 425, y + 357),
        (x + 432, y + 357),
        (x + 432, y + 361),
        (x + 425, y + 361)
    ]

    b_car_frontlight2 = [
        (x+437, y+357),
        (x+444, y+357),
        (x+444, y+361),
        (x+437, y+361)
    ]

    b_car_backlight1 = [
        (x + 421, y + 437),
        (x + 428, y + 437),
        (x + 428, y + 432),
        (x + 421, y + 432)
    ]

    b_car_backlight2 = [
        (x + 450, y + 437),
        (x + 443, y + 437),
        (x + 443, y + 432),
        (x + 450, y + 432)
    ]

    b_car_windshield = [
        (x + 424, y + 370),
        (x + 447, y + 370),
        (x + 442, y + 385),
        (x + 429, y + 385)
    ]

    pygame.draw.polygon(screen, (204, 102, 0), b_car_body_matros)
    pygame.draw.polygon(screen, (255, 255, 0), b_car_frontlight1)
    pygame.draw.polygon(screen, (255, 255, 0), b_car_frontlight2)
    pygame.draw.polygon(screen, (255, 0, 0), b_car_backlight1)
    pygame.draw.polygon(screen, (255, 0, 0), b_car_backlight2)
    pygame.draw.polygon(screen, (0, 0, 99), b_car_windshield)

    # ----------------------------------------------------------------------------------------

    
    x = 1280
    y = 2400
    width = 640
    height = 480

    plane_x_joanne += 1
    frames_joanne += 1


    pygame.draw.rect(screen, (128, 192, 255), (x, y, width, height))

    pygame.draw.rect(screen, (174, 255, 91), (x, y + 340, width, 140))

    pygame.draw.ellipse(screen, (255, 255, 255), (x + 30, y + 60, 45, 35))
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 65, y + 65, 50, 35))
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 105, y + 60, 45, 35))
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 55, y + 42, 40, 35))
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 85, y + 42, 40, 35))

    pygame.draw.ellipse(screen, (255, 255, 255), (x + 180, y + 60, 45, 35))
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 215, y + 65, 50, 35))
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 255, y + 60, 45, 35))
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 205, y + 42, 40, 35))
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 235, y + 42, 40, 35))

    pygame.draw.ellipse(screen, (255, 255, 255), (x + 330, y + 60, 45, 35))
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 365, y + 65, 50, 35))
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 405, y + 60, 45, 35))
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 355, y + 42, 40, 35))
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 385, y + 42, 40, 35))

    pygame.draw.ellipse(screen, (255, 255, 255), (x + 480, y + 60, 45, 35))
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 510, y + 65, 50, 35))
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 550, y + 60, 45, 35))
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 500, y + 42, 40, 35))
    pygame.draw.ellipse(screen, (255, 255, 255), (x + 530, y + 42, 40, 35))


    spacing_joanne = 7
    line_joanne = 50
    space_joanne = 0
    width_joanne = 6
    count_joanne = 0

    if frames_joanne % 13 == 0:
        num_dashes_joanne += 1

    while count_joanne <= num_dashes_joanne:
        line = pygame.draw.aaline(screen, (250, 250, 250), (x + space_joanne, y + 205), (x + 10 + space_joanne, y + 205))
        space_joanne += width_joanne + spacing_joanne
        count_joanne += 1

    if frames_joanne > 640:
        pygame.draw.rect(screen, (128, 192, 255), (x, y + 200, width, 10))
        space_joanne = 0
        count_joanne = 0
        frames_joanne = 0
        num_dashes_joanne = 0


    pygame.draw.ellipse(screen, (255, 128, 0), (x + plane_x_joanne, y + 200, 30, 20))
    pygame.draw.ellipse(screen, (96, 96, 96), (x + 28 + plane_x_joanne, y + 205, 7, 10))
    pygame.draw.ellipse(screen, (0, 0, 0), (x + 29 + plane_x_joanne, y + 185, 4, 20))
    pygame.draw.ellipse(screen, (0, 0, 0), (x + 29 + plane_x_joanne, y + 215, 4, 20))
    pygame.draw.ellipse(screen, (204, 102, 0), (x - 48 + plane_x_joanne, y + 190, 13, 20))
    pygame.draw.polygon(screen, (255, 128, 0), [(x + 11 + plane_x_joanne, y + 201), (x - 48 + plane_x_joanne, y + 201), (x - 48 + plane_x_joanne, y + 210), (x + 14 + plane_x_joanne, y + 220)])
    pygame.draw.ellipse(screen, (255, 85, 0), (x + -15 + plane_x_joanne, y + 208, 30, 5))
    pygame.draw.circle(screen, (128, 192, 255), (x + 12 + plane_x_joanne, y + 198), 7)

    if plane_x_joanne > 640:
        plane_x_joanne = 0
    
    # ----------------------------------------------------------------------------------------

    if arm_far_rhee is False:
        if arm_l_a_rhee < 145:
            arm_far_rhee = True
        arm_l_a_rhee -= 1
        arm_l_b_rhee -= 1
        arm_l_y_a_rhee -= 1
        arm_l_y_b_rhee -= 1
        hand_l_rhee -= 1
        hand_l_y_rhee -= 1
    elif arm_far_rhee is True:
        if arm_l_a_rhee > 165:
            arm_far_rhee = False
        arm_l_a_rhee += 1
        arm_l_b_rhee += 1
        arm_l_y_a_rhee += 1
        arm_l_y_b_rhee += 1
        hand_l_rhee += 1
        hand_l_y_rhee += 1

    if wave_a_rhee is False:
        if arm_r_y_a_rhee < 149:
            wave_a_rhee = True
        if wave_b_rhee is False:
            arm_r_a_rhee += 1
            arm_r_b_rhee += 1
            hand_r_rhee += 1
            if arm_r_a_rhee > 335:
                wave_b_rhee = True
        arm_r_y_a_rhee -= 1
        arm_r_y_b_rhee -= 1
        hand_r_y_rhee -= 1
    elif wave_a_rhee is True:
        if arm_r_a_rhee < 315:
            wave_a_rhee = False
        if arm_r_y_a_rhee > 245:
            wave_b_rhee = False
        if wave_b_rhee is False:
            arm_r_a_rhee -= 1
            arm_r_b_rhee -= 1
            hand_r_rhee -= 1
        arm_r_y_a_rhee += 1
        arm_r_y_b_rhee += 1
        hand_r_y_rhee += 1

    if blink_rhee is False:
        if eye_b_rhee < 10:
            blink_rhee = True
        eye_a_rhee += 0.5
        eye_b_rhee -= 0.5
        eye_c_rhee += 0.25
        eye_d_rhee -= 0.25
    elif blink_rhee is True:
        if eye_b_rhee > 25:
            blink_rhee = False
        eye_a_rhee -= 0.5
        eye_b_rhee += 0.5
        eye_c_rhee -= 0.25
        eye_d_rhee += 0.25

    x = 2560
    y = 2400
    width = 640
    height = 480

    pygame.draw.rect(screen, (142, 84, 176), (x, y, width, height))
    pygame.draw.rect(screen, (142, 84, 176), (x, y, width, height))
    pygame.draw.polygon(screen, (42, 97, 60), [(x, y + 480), (x, y + 325), (x + 640, y + 325), (x + 640, y + 480)])
    pygame.draw.circle(screen, (245, 250, 182), (x + 400, y + 80), 60)
    pygame.draw.circle(screen, (142, 84, 176), (x + 420, y + 60), 40)
    pygame.draw.polygon(screen, (64, 64, 59), [(x + 200, y + 350), (x + 205, y + 290), (x + 275, y + 290), (x + 280, y + 350), (x + 250, y + 350), (x + 240, y + 280), (x + 230, y + 350)])
    pygame.draw.polygon(screen, (46, 46, 41), [(x + 197, y + 340), (x + 196, y + 355), (x + 191, y + 365), (x + 230, y + 365), (x + 232, y + 340)])
    pygame.draw.polygon(screen, (46, 46, 41), [(x + 283, y + 340), (x + 284, y + 355), (x + 289, y + 365), (x + 250, y + 365), (x + 248, y + 340)])
    pygame.draw.polygon(screen, (79, 79, 70), [(x + 200, y + 300), (x + 205, y + 190), (x + 275, y + 190), (x + 280, y + 300)])
    pygame.draw.circle(screen, (64, 64, 59), (x + hand_l_rhee, y + hand_l_y_rhee), 15)
    pygame.draw.circle(screen, (64, 64, 59), (x + hand_r_rhee, y + hand_r_y_rhee), 15)
    pygame.draw.polygon(screen, (79, 79, 70), [(x + arm_l_a_rhee, y + arm_l_y_a_rhee), (x + 176, y + 206), (x + 202, y + 221), (x + 203, y + 218), (x + arm_l_b_rhee, y + arm_l_y_b_rhee)])
    pygame.draw.polygon(screen, (79, 79, 70), [(x + arm_r_a_rhee, y + arm_r_y_a_rhee), (x + 304, y + 206), (x + 278, y + 221), (x + 277, y + 218), (x + arm_r_b_rhee, y + arm_r_y_b_rhee)])
    pygame.draw.polygon(screen, (112, 112, 95), [(x + 240, y + 265), (x + 215, y + 195), (x + 265, y + 195)])
    pygame.draw.polygon(screen, (99, 99, 90), [(x + 240, y + 265), (x + 225, y + 220), (x + 210, y + 230)])
    pygame.draw.polygon(screen, (99, 99, 90), [(x + 240, y + 265), (x + 255, y + 220), (x + 270, y + 230)])
    pygame.draw.polygon(screen, (46, 46, 41), [(x + 175, y + 195), (x + 210, y + 190), (x + 270, y + 190), (x + 305, y + 195), (x + 306, y + 205), (x + 270, y + 225), (x + 250, y + 225), (x + 240, y + 190), (x + 230, y + 225), (x + 210, y + 225), (x + 174, y + 205)])
    pygame.draw.polygon(screen, (64, 64, 59), [(x+215,y+190), (x+205,y+170), (x+210,y+140), (x+225,y+130), (x+255,y+130), (x+270,y+140), (x+275,y+170), (x+265,y+190)])
    pygame.draw.ellipse(screen, (245, 245, 54), [(x + 217, y + eye_a_rhee), (20, eye_b_rhee)])
    pygame.draw.ellipse(screen, (245, 245, 54), [(x + 243, y + eye_a_rhee), (20, eye_b_rhee)])
    pygame.draw.ellipse(screen, (255, 255, 207), [(x + 222, y + eye_c_rhee), (12, eye_d_rhee)])
    pygame.draw.ellipse(screen, (255, 255, 207), [(x + 244, y + eye_c_rhee), (12, eye_d_rhee)])
    pygame.draw.polygon(screen, (46, 46, 41), [(x + 226, y + 185), (x + 232, y + 170), (x + 240, y + 165), (x + 248, y + 170), (x + 254, y + 185), (x + 240, y + 188)])

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
