screenUsing = "startScreen"

SCREEN_LIST = {
    "startScreen": {
        "WIDTH": 600,
        "HEIGHT": 400,
        "BackGround": "Image/BackGround.png",
        "GUI": {
            "button1": {
                "Function": "play game",
                "Text": "PLAY",
                "TextSize": 35,
                "TextColor": "Black",
                "SizeX": 120,
                "SizeY": 50,
                "PosX": 300,
                "PosY": 300,
                "Color": "Green",
                "ShapeRect": "center"
            }
        }
    },
    "mainMenuScreen": {
        "WIDTH": 600,
        "HEIGHT": 400,
        "BackGround": "Image/MainMenuBackGround.png",
        "GUI": {
            "button1": {
                "Function": "play mode",
                "Text": "MODE",
                "TextSize": 70,
                "TextColor": "Black",
                "SizeX": 300,
                "SizeY": 180,
                "PosX": 300,
                "PosY": 130,
                "Color": "Cyan",
                "ShapeRect": "center"
            },
            "button2": {
                "Function": "set up team",
                "Text": "SET UP TEAM",
                "TextSize": 25,
                "TextColor": "Black",
                "SizeX": 145,
                "SizeY": 60,
                "PosX": 150,
                "PosY": 240,
                "Color": "Red",
                "ShapeRect": "topleft"
            },
            "button3": {
                "Function": "gacha",
                "Text": "GACHA",
                "TextSize": 25,
                "TextColor": "Black",
                "SizeX": 145,
                "SizeY": 60,
                "PosX": 305,
                "PosY": 240,
                "Color": "Yellow",
                "ShapeRect": "topleft"
            },
            "button4": {
                "Function": "tutorial",
                "Text": "!",
                "TextSize": 35,
                "TextColor": "Red",
                "SizeX": 40,
                "SizeY": 40,
                "PosX": 550,
                "PosY": 10,
                "Color": "Black",
                "ShapeRect": "topleft"
            }
        }
    },
    "setUpTeamScreen": {
        "WIDTH": 600,
        "HEIGHT": 400,
        "BackGround": "Image/SetUpTeamBackGround.png",
        "GUI": {
            "button": {
                "Function": "Leave",
                "Text": "X",
                "TextSize": 35,
                "TextColor": "White",
                "SizeX": 40,
                "SizeY": 40,
                "PosX": 550,
                "PosY": 10,
                "Color": "Red",
                "ShapeRect": "topleft"
            }
        }
    },
    "tutorialScreen": {
        "WIDTH": 600,
        "HEIGHT": 400,
        "BackGround": "Image/TutorialBackGround.png",
        "GUI": {
            "button": {
                "Function": "Leave",
                "Text": "X",
                "TextSize": 35,
                "TextColor": "White",
                "SizeX": 40,
                "SizeY": 40,
                "PosX": 550,
                "PosY": 10,
                "Color": "Red",
                "ShapeRect": "topleft"
            },
            "text1": {
                "Text": "TUTORIAL",
                "TextSize": 30,
                "Color": "Black",
                "Bold": True,
                "PosX": 300,
                "PosY": 50,
                "TextRect": "center",
            },
            "text2": {
                "Text": "Hello, Welcome to Shapes Tower Defense\nButton:\nButton 'MODE' for play with other map and gameplay.\nButton 'SET UP TEAM' for edit and manager your team.\nButton 'GACHA' for get random tower and upgrade your team !!!\n",
                "TextSize": 20,
                "Color": "Black",
                "Bold": True,
                "PosX": 300,
                "PosY": 100,
                "TextRect": "center",
            }
        }
    }
}
