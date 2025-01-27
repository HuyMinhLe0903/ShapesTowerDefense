import pygame
pygame.init()

BASIC_COLOR_LIST = {
    "Red": (255,0,0),
    "Black": (0,0,0),
    "White": (255,255,255),
    "Green": (0,255,0),
    "Blue": (0,0,255),
    "Yellow": (255,255,0),
    "Orange": (255,100,0),
    "Cyan": (0,255,255)
}

def DrawTextOnScreen(SCREEN,TEXT,COLOR,SIZE,X,Y,TEXT_RECT):
    font = pygame.font.Font(None,SIZE)
    
    if type(COLOR) == str:
        COLOR = BASIC_COLOR_LIST[COLOR]
        
    text = font.render(TEXT,True,COLOR)
    textRect = None
    
    if TEXT_RECT != "topleft":
        textRect = text.get_rect(center = (X,Y))
    else:
        textRect = text.get_rect(topleft = (X,Y))
        
    SCREEN.blit(text,textRect)
    
def DrawButtonOnScreen(SCREEN,TEXT,TEXT_SIZE,TEXT_COLOR,COLOR,SIZE_X,SIZE_Y,POS_X,POS_Y,SHAPE_RECT):
    if type(COLOR) == str:
        COLOR = BASIC_COLOR_LIST[COLOR]
        
    rect = pygame.Rect(0,0,SIZE_X,SIZE_Y)
    
    if SHAPE_RECT == "topleft":
        rect.topleft = (POS_X,POS_Y)
    elif SHAPE_RECT == "center":
        rect.center = (POS_X,POS_Y)
        
    pygame.draw.rect(SCREEN,COLOR,rect)
    font = pygame.font.Font(None,TEXT_SIZE)
    text = font.render(TEXT,True,TEXT_COLOR)
    textRect = text.get_rect(center = (POS_X,POS_Y))
    textRect.center = rect.center
    SCREEN.blit(text,textRect)

def CheckClickButton(SCREEN,BUTTON_SIZE_X,BUTTON_SIZE_Y,BUTTON_POS_X,BUTTON_POS_Y,BUTTON_RECT,MOUSE_POS_X,MOUSE_POS_Y):
    rect = pygame.Rect(0,0,BUTTON_SIZE_X,BUTTON_SIZE_Y)

    if BUTTON_RECT == "topleft":
        rect.topleft = (BUTTON_POS_X,BUTTON_POS_Y)
    elif BUTTON_RECT == "center":
        rect.center = (BUTTON_POS_X,BUTTON_POS_Y)

    return rect.collidepoint(MOUSE_POS_X, MOUSE_POS_Y) 