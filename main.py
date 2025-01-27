import pygame
pygame.init()
import services
import screenInfo
import tutorial
import threading

WIDTH = None
HEIGHT = None
SCREEN = None
SCREEN_NAME = None
BACKGROUND_IMAGE = None
BACKGROUND_SIZE = None
GUI = None

WIDTH = screenInfo.startScreen["WIDTH"]
HEIGHT = screenInfo.startScreen["HEIGHT"]

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
SCREEN_NAME = pygame.display.set_caption("SHAPES TOWER DEFENSE")
SCREEN.fill((0,0,0))

BACKGROUND_IMAGE = pygame.image.load(screenInfo.startScreen["BackGround"])
BACKGROUND_SIZE = pygame.transform.scale(
    BACKGROUND_IMAGE,
    (screenInfo.startScreen["WIDTH"],screenInfo.startScreen["HEIGHT"])
)

GUI = screenInfo.startScreen["GUI"]

FPS = pygame.time.Clock()
RUNNING = True

def DrawGui():
    global GUI
    services.DrawTextOnScreen(
        SCREEN,
        f"FPS:{round(FPS.get_fps())}",
        "White",
        25,
        0,0,
        "topleft"   
    )
    
    if screenInfo.screenUsing == "startScreen":
        GUI = screenInfo.startScreen["GUI"]
        for key,value in GUI.items():           
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
    elif screenInfo.screenUsing == "mainMenuScreen":
        GUI = screenInfo.mainMenuScreen["GUI"]
        for key,value in GUI.items():
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
                
def CheckClick(mouseX,mouseY):
    global BACKGROUND_IMAGE
    global BACKGROUND_SIZE
    if screenInfo.screenUsing == "startScreen":
        GUI = screenInfo.startScreen["GUI"]
        for key,value in GUI.items():
            if "button" in key:
                if services.CheckClickButton(
                    SCREEN,
                    value["SizeX"],
                    value["SizeY"],
                    value["PosX"],
                    value["PosY"],
                    value["ShapeRect"],
                    mouseX,
                    mouseY
                ) and value["Function"] == "play game":
                    screenInfo.screenUsing = "mainMenuScreen"
                    GUI = screenInfo.mainMenuScreen["GUI"]
                    BACKGROUND_IMAGE = pygame.image.load(screenInfo.mainMenuScreen["BackGround"])
                    BACKGROUND_SIZE = pygame.transform.scale(
                        BACKGROUND_IMAGE,
                        (screenInfo.mainMenuScreen["WIDTH"],screenInfo.mainMenuScreen["HEIGHT"])
                    )

                elif services.CheckClickButton(
                    SCREEN,
                    value["SizeX"],
                    value["SizeY"],
                    value["PosX"],
                    value["PosY"],
                    value["ShapeRect"],
                    mouseX,
                    mouseY
                ):
                    None
    elif screenInfo.screenUsing == "mainMenuScreen":
        GUI = screenInfo.mainMenuScreen["GUI"]
        for key,value in GUI.items():
            if "button" in key:
                if services.CheckClickButton(
                    SCREEN,
                    value["SizeX"],
                    value["SizeY"],
                    value["PosX"],
                    value["PosY"],
                    value["ShapeRect"],
                    mouseX,
                    mouseY
                ) and value["Function"] == "play mode":
                    print("Hello world")
                elif services.CheckClickButton(
                        SCREEN,
                        value["SizeX"],
                        value["SizeY"],
                        value["PosX"],
                        value["PosY"],
                        value["ShapeRect"],
                        mouseX,
                        mouseY
                    ) and value["Function"] == "set up team":
                        screenInfo.screenUsing = "setUpTeamScreen"
                        GUI = screenInfo.setUpTeamScreen["GUI"]
                        BACKGROUND_IMAGE = pygame.image.load(screenInfo.setUpTeamScreen["BackGround"])
                        BACKGROUND_SIZE = pygame.transform.scale(
                            BACKGROUND_IMAGE,
                            (screenInfo.setUpTeamScreen["WIDTH"],screenInfo.setUpTeamScreen["HEIGHT"])
                        )
                elif services.CheckClickButton(
                    SCREEN,
                    value["SizeX"],
                    value["SizeY"],
                    value["PosX"],
                    value["PosY"],
                    value["ShapeRect"],
                    mouseX,
                    mouseY
                ) and value["Function"] == "gacha":
                    print("hfsdjkf")
                elif services.CheckClickButton(
                    SCREEN,
                    value["SizeX"],
                    value["SizeY"],
                    value["PosX"],
                    value["PosY"],
                    value["ShapeRect"],
                    mouseX,
                    mouseY
                ) and value["Function"] == "tutorial":
                    if tutorial.canRun:
                        tkinterThreading = threading.Thread(target = tutorial.run)
                        tkinterThreading.start()
                        tutorial.canRun = False

def RUN():
    global RUNNING
    global SCREEN
    global BACKGROUND_IMAGE
    global BACKGROUND_SIZE
    global FPS
    while RUNNING:
        SCREEN.fill((0,0,0))
        SCREEN.blit(BACKGROUND_SIZE,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX,mouseY = event.pos
                CheckClick(mouseX,mouseY)
        
        DrawGui()
        
        FPS.tick(60)         
        pygame.display.flip() 
        
    pygame.quit()