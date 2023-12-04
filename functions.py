import random

def generate_random_number(level: str) -> None:
    if level == "level_one":
        random_number = random.randint(0, 25)
    elif level == "level_two":
        random_number = random.randint(0, 50)
    elif level == "level_three":
        random_number = random.randint(0, 75)
    elif level == "level_four":
        random_number = random.randint(0, 100)
    else:
        return 0
    return random_number

# for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             input_active = True
#             text = ""
#         elif event.type == pygame.KEYDOWN and input_active:
#             if event.key == pygame.K_RETURN:
#                 input_active = False
#             elif event.key == pygame.K_BACKSPACE:
#                 text =  text[:-1]
#             else:
#                 text += event.unicode