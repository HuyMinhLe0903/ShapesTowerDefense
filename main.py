import pygame
import services
import screenInfo
import tkinter as tk

WIDTH = None
HEIGHT = None
SCREEN = None
SCREEN_NAME = None
BACKGROUND_IMAGE = None
BACKGROUND_SIZE = None
GUI = None
CLICK_ENABLED = True
TUTORIAL_ENABLED = False

def DrawGui():
    global GUI
    global SCREEN
    for screenName,screenData in screenInfo.SCREEN_LIST.items():
        if screenName == screenInfo.screenUsing:
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
            break

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
    
    if screenInfo.screenUsing == "startScreen":
        GUI = screenInfo.SCREEN_LIST["startScreen"].get("GUI")
    elif screenInfo.screenUsing == "mainMenuScreen":
        GUI = screenInfo.SCREEN_LIST["mainMenuScreen"].get("GUI")
    elif screenInfo.screenUsing == "setUpTeamScreen":
        GUI = screenInfo.SCREEN_LIST["setUpTeamScreen"].get("GUI")
    elif screenInfo.screenUsing == "tutorialScreen":
        GUI = screenInfo.SCREEN_LIST["tutorialScreen"].get("GUI")

    DrawGui()
                
def CheckClick(mouseX,mouseY):
    global BACKGROUND_IMAGE
    global BACKGROUND_SIZE
    global CLICK_ENABLED
    global GUI
    global TUTORIAL_ENABLED
    if screenInfo.screenUsing == "startScreen":
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
                    BACKGROUND_IMAGE = pygame.image.load(screenInfo.SCREEN_LIST["mainMenuScreen"].get("BackGround"))
                    BACKGROUND_SIZE = pygame.transform.scale(
                        BACKGROUND_IMAGE,
                        (screenInfo.SCREEN_LIST["mainMenuScreen"].get("WIDTH"),screenInfo.SCREEN_LIST["mainMenuScreen"].get("HEIGHT"))
                    )
    elif screenInfo.screenUsing == "mainMenuScreen":
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
                        BACKGROUND_IMAGE = pygame.image.load(screenInfo.SCREEN_LIST["setUpTeamScreen"].get("BackGround"))
                        BACKGROUND_SIZE = pygame.transform.scale(
                            BACKGROUND_IMAGE,
                            (screenInfo.SCREEN_LIST["setUpTeamScreen"].get("WIDTH"),screenInfo.SCREEN_LIST["setUpTeamScreen"].get("HEIGHT"))
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
                    screenInfo.screenUsing = "tutorialScreen"
                    BACKGROUND_IMAGE = pygame.image.load(screenInfo.SCREEN_LIST["tutorialScreen"].get("BackGround"))
                    BACKGROUND_SIZE = pygame.transform.scale(
                        BACKGROUND_IMAGE,
                        (screenInfo.SCREEN_LIST["tutorialScreen"].get("WIDTH"),screenInfo.SCREEN_LIST["tutorialScreen"].get("HEIGHT"))
                    )

def RUN_MAIN_WINDOW(title,bg):
    pygame.init()
    global RUNNING
    global SCREEN
    global BACKGROUND_IMAGE
    global BACKGROUND_SIZE
    global FPS
    global CLICK_ENABLED
    global GUI

    WIDTH = screenInfo.SCREEN_LIST["startScreen"].get("WIDTH")
    HEIGHT = screenInfo.SCREEN_LIST["startScreen"].get("HEIGHT")

    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
    SCREEN_NAME = pygame.display.set_caption(title)
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