import pygame
from functions import generate_random_number

# initializing pygame
pygame.init()
# setting window and clock
window = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

# setting font text and input variables
font = pygame.font.SysFont(None, 100)
text = ""
input_active = True

# variable to track level
level=0

# all the screens to display
level_one_screen=False
level_two_screen=False
level_three_screen=False
level_four_screen=False
start_screen=True
end_screen=False
game_end_screen=False
instructions_screen=False
low_guess_screen=False
high_guess_screen=False
good_guess_screen=False
pre_screen=False

# guess number for each level (predicting in the start)
level_one_guess= generate_random_number("level_one")
level_two_guess= generate_random_number("level_two")
level_three_guess= generate_random_number("level_three")
level_four_guess= generate_random_number("level_four")
print(level_one_guess)
print(level_two_guess)
print(level_three_guess)
print(level_four_guess)

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
isGameover = False

# function to load pre level screen
def show_level_pre_screen():
    global level, level_one_screen, end_screen, level_two_screen, level_three_screen, level_four_screen,pre_screen
    level_one_pre_image= pygame.image.load("assets/LEVEL 1 SCREEN.png")
    level_two_pre_image= pygame.image.load("assets/LEVEL 2 SCREEN.png")
    level_three_pre_image= pygame.image.load("assets/LEVEL 3 SCREEN.png")
    level_four_pre_image= pygame.image.load("assets/LEVEL 4 SCREEN.png")
    # loading the screen on the base of level
    if level==0:
         window.blit(level_one_pre_image, (0,0))
         for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pre_screen=False
                        level_one_screen=True
    elif level==1:
         window.blit(level_two_pre_image, (0,0))
         for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pre_screen=False
                        level_two_screen=True
    elif level==2:
         window.blit(level_three_pre_image, (0,0))
         for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pre_screen=False
                        level_three_screen=True
    elif level==3:
         window.blit(level_four_pre_image, (0,0))
         for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pre_screen=False
                        level_four_screen=True

# function to load the good guess screen
def show_good_guess():
    correct_guess_image= pygame.image.load("assets/Correct Guess.png")
    window.blit(correct_guess_image, (0,0))
    global level_one_screen,end_screen,level_two_screen,level_three_screen,level_four_screen,level,good_guess_screen,pre_screen
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if level==1:
                         good_guess_screen=False
                         level_one_screen=False
                        #  level_two_screen=True
                         pre_screen=True
                    elif level==2:
                        good_guess_screen=False
                        level_two_screen=False
                        # level_three_screen=True
                        pre_screen=True

                    elif level==3:
                        good_guess_screen=False
                        level_three_screen=False
                        level_four_screen=True
                        pre_screen=True

                    elif level==4:
                        good_guess_screen=False
                        level_four_screen=False
                        end_screen=True
                        level=0

# function to load the low guess screen
def show_low_guess():
    low_guess_image= pygame.image.load("assets/Low guess.png")
    window.blit(low_guess_image, (0,0))
    global level_one_screen,start_screen,level_two_screen,level_three_screen,level_four_screen,level,low_guess_screen
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if level == 0:
                         low_guess_screen=False
                         level_one_screen=True
                    elif level==1:
                        low_guess_screen=False
                        level_two_screen=True
                    elif level==2:
                        low_guess_screen=False
                        level_three_screen=True
                    elif level==3:
                        low_guess_screen=False
                        level_four_screen=True
                         
# function to load the high guess screen
def show_high_guess():
    high_guess_image= pygame.image.load("assets/Guess High.png")
    window.blit(high_guess_image, (0,0))
    global level_one_screen,start_screen,level_two_screen,level_three_screen,level_four_screen,level,high_guess_screen
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if level==0:
                         high_guess_screen=False
                         level_one_screen=True
                    elif level==1:
                        high_guess_screen=False
                        level_two_screen=True
                    elif level==2:
                        high_guess_screen=False
                        level_three_screen=True
                    elif level==3:
                        high_guess_screen=False
                        level_four_screen=True

# function to load level one screen
def show_level_one_screen():
    level_one_range= pygame.image.load("assets/RANGE (0-25).png")
    window.blit(level_one_range, (0,0))

    global input_active, text, level_one_screen, level_one_guess, good_guess_screen, low_guess_screen, high_guess_screen,level

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            text = ""
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                input_active = False
                # Compare the entered number with the guessed number
                entered_number = int(text) if text else 0  # Convert text to an integer, default to 0 if empty
                if entered_number < level_one_guess:
                    print("Too low")
                    level_one_screen=False
                    low_guess_screen=True
                elif entered_number > level_one_guess:
                    print("Too high")
                    level_one_screen=False
                    high_guess_screen=True
                else:
                    print("Good guess!")
                    level+=1
                    level_one_screen=False
                    good_guess_screen=True
                    text=""

            elif event.key == pygame.K_BACKSPACE:
                text =  text[:-1]
            elif event.unicode.isdigit():
                # Check if the entered character is a digit
                new_text = text + event.unicode
                if 0 <= int(new_text) <= 100:
                    text = new_text
    
    global font
    font = pygame.font.SysFont(None, 100)
    text_surface = font.render(text, True, black)
    window.blit(text_surface, (350,430))

# function to load level two screen
def show_level_two_screen():
    level_two_range= pygame.image.load("assets/RANGE (0-50).png")
    window.blit(level_two_range, (0,0))

    global input_active, text, level_two_screen, level_two_guess, good_guess_screen, low_guess_screen, high_guess_screen,level

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            text = ""
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                input_active = False
                # Compare the entered number with the guessed number
                entered_number = int(text) if text else 0  # Convert text to an integer, default to 0 if empty
                if entered_number < level_two_guess:
                    print("Too low")
                    level_two_screen=False
                    low_guess_screen=True
                elif entered_number > level_two_guess:
                    print("Too high")
                    level_two_screen=False
                    high_guess_screen=True
                else:
                    print("Good guess!")
                    level+=1
                    level_two_screen=False
                    good_guess_screen=True
                    text=""
            elif event.key == pygame.K_BACKSPACE:
                text =  text[:-1]
            elif event.unicode.isdigit():
                # Check if the entered character is a digit
                new_text = text + event.unicode
                if 0 <= int(new_text) <= 100:
                    text = new_text   
        
        
    global font
    font = pygame.font.SysFont(None, 100)
    text_surface = font.render(text, True, black)
    window.blit(text_surface, (350,430))

# function to load level three screen
def show_level_three_screen():
    level_two_range= pygame.image.load("assets/RANGE (0-75).png")
    window.blit(level_two_range, (0,0))

    global input_active, text, level_three_screen, level_three_guess, good_guess_screen, low_guess_screen, high_guess_screen,level

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            text = ""
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                input_active = False
                # Compare the entered number with the guessed number
                entered_number = int(text) if text else 0  # Convert text to an integer, default to 0 if empty
                if entered_number < level_three_guess:
                    print("Too low")
                    level_three_screen=False
                    low_guess_screen=True
                elif entered_number > level_three_guess:
                    print("Too high")
                    level_three_screen=False
                    high_guess_screen=True
                else:
                    print("Good guess!")
                    level+=1
                    level_three_screen=False
                    good_guess_screen=True
                    text=""

            elif event.key == pygame.K_BACKSPACE:
                text =  text[:-1]
            elif event.unicode.isdigit():
                # Check if the entered character is a digit
                new_text = text + event.unicode
                if 0 <= int(new_text) <= 100:
                    text = new_text   
        
        
    global font
    font = pygame.font.SysFont(None, 100)
    text_surface = font.render(text, True, black)
    window.blit(text_surface, (350,430))

# function to load level four screen
def show_level_four_screen():
    level_two_range= pygame.image.load("assets/RANGE (0-100).png")
    window.blit(level_two_range, (0,0))

    global input_active, text, level_four_screen, level_four_guess, good_guess_screen, low_guess_screen, high_guess_screen,level

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            text = ""
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                input_active = False
                # Compare the entered number with the guessed number
                entered_number = int(text) if text else 0  # Convert text to an integer, default to 0 if empty
                if entered_number < level_four_guess:
                    print("Too low")
                    level_four_screen=False
                    low_guess_screen=True
                elif entered_number > level_four_guess:
                    print("Too high")
                    level_four_screen=False
                    high_guess_screen=True
                else:
                    print("Good guess!")
                    level+=1
                    level_four_screen=False
                    good_guess_screen=True
                    text=""

            elif event.key == pygame.K_BACKSPACE:
                text =  text[:-1]
            elif event.unicode.isdigit():
                # Check if the entered character is a digit
                new_text = text + event.unicode
                if 0 <= int(new_text) <= 100:
                    text = new_text   
        
        
    global font
    font = pygame.font.SysFont(None, 100)
    text_surface = font.render(text, True, black)
    window.blit(text_surface, (350,430))

# function to load the instruction screen
def show_instructions_screen():
    instructions_image = pygame.image.load("assets/INSTRUCTIONS.png")
    window.blit(instructions_image, (0,0))
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    global pre_screen
                    pre_screen=True
                    global instructions_screen
                    instructions_screen=False
# function to load the end screen
def show_end_screen():
    the_end_screen_image = pygame.image.load("assets/THE END.png")
    window.blit(the_end_screen_image, (0,0))
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("game end")
                    global isGameover
                    isGameover=True

# function to load the start screen
def show_start_screen():
    # Load images
    button_image = pygame.image.load("assets/start_button.png")
    start_image = pygame.image.load("assets/c.GuessMyNumber.png")
    window.blit(start_image, (0,0))
    window.blit(button_image, (250, 400))
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is over the button
                button_rect = button_image.get_rect(topleft=(250, 400))
                if button_rect.collidepoint(event.pos):
                    global instructions_screen
                    instructions_screen=True
                    global start_screen
                    start_screen=False
# main game loop
while not isGameover:
    window.fill(0)
    # getting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameover = True
    # on the base screen variables deciding which screen to load
    if start_screen:
        show_start_screen()

    elif instructions_screen:
        show_instructions_screen()

    elif pre_screen:
        show_level_pre_screen()

    elif level_one_screen:
        show_level_one_screen()

    elif level_two_screen:
        show_level_two_screen()

    elif level_three_screen:
        show_level_three_screen()

    elif level_four_screen:
        show_level_four_screen()
    
    elif high_guess_screen:
         show_high_guess()
    
    elif good_guess_screen:
         show_good_guess()
    
    elif low_guess_screen:
         show_low_guess()

    elif end_screen:
         show_end_screen()

    pygame.display.flip()
    clock.tick(60)

# exiting
pygame.quit()
exit()