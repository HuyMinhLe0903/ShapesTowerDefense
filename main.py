import pygame
import services
import screenInfo

WIDTH = None
HEIGHT = None
SCREEN = None
SCREEN_NAME = None
BACKGROUND_IMAGE = None
BACKGROUND_SIZE = None
GUI = None
CLICK_ENABLED = True

def DrawGui():
    global GUI
    global SCREEN
    screenData = screenInfo.SCREEN_LIST[screenInfo.screenUsing]
    for key,value in screenData["GUI"].items():           
        if "button" in key:        
            services.DrawButtonOnScreen(
                SCREEN,
                value["Text"],
                value["TextSize"],
                value["TextColor"],
                value["Color"],
                value["SizeX"],
                value["SizeY"],
                value["PosX"],
                value["PosY"],
                value["ShapeRect"]
            )
        elif "text" in key:
            services.DrawTextOnScreen(
                SCREEN,
                value["Text"],
                value["Color"],
                value["TextSize"],
                value["PosX"],
                value["PosY"],
                value["TextRect"],
                value["Bold"]
            )
        elif "netCharacters" in key:
            services.DrawNetOnScreen(
                SCREEN,
                value["Col"],
                value["Row"],
                value["LineColor"],
                value["SquareColor"],
                value["PosX"],
                value["PosY"],
                value["SquareWidth"],
                value["SquareHeight"],
                value["Rect"]
            )
            services.DrawListCharacterTypeNet(
                SCREEN,
                value["PosX"],
                value["PosY"],
                value["SquareHeight"],
                value["SquareWidth"],
                value["Col"],
                value["Row"]
            )
        elif "net" in key:
            services.DrawNetOnScreen(
                SCREEN,
                value["Col"],
                value["Row"],
                value["LineColor"],
                value["SquareColor"],
                value["PosX"],
                value["PosY"],
                value["SquareWidth"],
                value["SquareHeight"],
                value["Rect"]
            )
            
def UpdateScreen():
    global GUI
    global SCREEN
    services.DrawTextOnScreen(
        SCREEN,
        f"FPS:{round(FPS.get_fps())}",
        "White",
        25,
        0,0,
        "topleft",
        True  
    )

    GUI = screenInfo.SCREEN_LIST[screenInfo.screenUsing].get("GUI")

    DrawGui()

def ChangeScreen(targetScreen):
    global BACKGROUND_IMAGE
    global BACKGROUND_SIZE
    global GUI
    screenInfo.screenUsing = targetScreen
    BACKGROUND_IMAGE = pygame.image.load(screenInfo.SCREEN_LIST[targetScreen].get("BackGround"))
    BACKGROUND_SIZE = pygame.transform.scale(
        BACKGROUND_IMAGE,
        (screenInfo.SCREEN_LIST[targetScreen].get("WIDTH"),screenInfo.SCREEN_LIST[targetScreen].get("HEIGHT"))
    )
    GUI = screenInfo.SCREEN_LIST[targetScreen].get("GUI")

def CheckClick(mouseX,mouseY):
    global BACKGROUND_IMAGE
    global BACKGROUND_SIZE
    global CLICK_ENABLED
    global GUI
    global TUTORIAL_ENABLED
    for key,value in GUI.items():
        if "button" in key and services.CheckClickButton(
                SCREEN,value["SizeX"],value["SizeY"],
                value["PosX"],value["PosY"],value["ShapeRect"],
                mouseX,
                mouseY
        ):
            func = value["Function"]
            if func is None:
                return
            if func and screenInfo.buttonActions[func]:
                ChangeScreen(screenInfo.buttonActions[func])

def RUN_MAIN_WINDOW(title,bg):
    pygame.init()
    global RUNNING
    global SCREEN
    global BACKGROUND_IMAGE
    global BACKGROUND_SIZE
    global FPS
    global CLICK_ENABLED
    global GUI
    global WIDTH
    global HEIGHT

    WIDTH = screenInfo.SCREEN_LIST["startScreen"].get("WIDTH")
    HEIGHT = screenInfo.SCREEN_LIST["startScreen"].get("HEIGHT")

    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption(title)
    SCREEN.fill(bg)

    BACKGROUND_IMAGE = pygame.image.load(screenInfo.SCREEN_LIST["startScreen"].get("BackGround"))
    BACKGROUND_SIZE = pygame.transform.scale(
        BACKGROUND_IMAGE,
        (WIDTH,HEIGHT)
    )

    GUI = screenInfo.SCREEN_LIST["startScreen"].get("GUI")

    FPS = pygame.time.Clock()
    RUNNING = True
    
    while RUNNING:
        SCREEN.fill((0,0,0))
        SCREEN.blit(BACKGROUND_SIZE,(0,0))

        UpdateScreen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            if event.type == pygame.MOUSEBUTTONDOWN and CLICK_ENABLED:
                mouseX,mouseY = event.pos
                CheckClick(mouseX,mouseY)
        
        FPS.tick(60)         
        pygame.display.flip() 
        
    pygame.quit()

if __name__ == "__main__":
    RUN_MAIN_WINDOW("Shapes Tower Defense",(0,0,0))