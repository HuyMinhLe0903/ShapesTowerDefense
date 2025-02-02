import data
screenUsing = "startScreen"

buttonActions = {
    "play game": "mainMenuScreen",
    "play mode": "modeScreen",
    "set up team": "setUpTeamScreen",
    "gacha": "gachaScreen",
    "tutorial": "tutorialScreen",
    "leave": "mainMenuScreen",
    "gacha basic": None,
    "gacha advanced": None,
    "buy basic": None,
    "buy advanced": None,
    "line": None,
    "play chapters": None
}

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
            },
            "text1": {
                "Text": f"Coin:{data.DATA['Coin']}",
                "TextSize": 30,
                "Color": "Yellow",
                "Bold": True,
                "PosX": 300,
                "PosY": 10,
                "TextRect": "center"
            }
        }
    },
    "setUpTeamScreen": {
        "WIDTH": 600,
        "HEIGHT": 400,
        "BackGround": "Image/SetUpTeamBackGround.png",
        "GUI": {
            "button": {
                "Function": "leave",
                "Text": "X",
                "TextSize": 35,
                "TextColor": "White",
                "SizeX": 20,
                "SizeY": 20,
                "PosX": 580,
                "PosY": 0,
                "Color": "Red",
                "ShapeRect": "topleft"
            },
            "netCharacters": {
                "Col": 10,
                "Row": 5,
                "LineColor": "Black",
                "SquareColor": "White", 
                "SquareWidth": 50,
                "SquareHeight": 50,
                "PosX": 50,
                "PosY": 20,
                "Rect": "topleft"
            },
            "netTeamUsing": {
                "Col": 5,
                "Row": 1,
                "LineColor": "Black",
                "SquareColor": "White", 
                "SquareWidth": 60,
                "SquareHeight": 60,
                "PosX": 150,
                "PosY": 330,
                "Rect": "topleft"
            },
            "text1": {
                "Text": "Your Team",
                "TextSize": 25,
                "Color": "Black",
                "Bold": True,
                "PosX": 300,
                "PosY": 310,
                "TextRect": "center"
            }
        }
    },
    "tutorialScreen": {
        "WIDTH": 600,
        "HEIGHT": 400,
        "BackGround": "Image/TutorialBackGround.png",
        "GUI": {
            "button": {
                "Function": "leave",
                "Text": "X",
                "TextSize": 35,
                "TextColor": "White",
                "SizeX": 20,
                "SizeY": 20,
                "PosX": 580,
                "PosY": 0,
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
                "TextRect": "center"
            },
            "text2": {
                "Text": "Hello, Welcome to Shapes Tower Defense",
                "TextSize": 20,
                "Color": "Black",
                "Bold": False,
                "PosX": 300,
                "PosY": 100,
                "TextRect": "center"
            },
            "text3": {
                "Text": "Button 'MODE' for play with other map and gameplay.",
                "TextSize": 20,
                "Color": "Black",
                "Bold": False,
                "PosX": 300,
                "PosY": 120,
                "TextRect": "center"
            },
            "text4": {
                "Text": "Button 'SET UP TEAM' for edit and manager your team.",
                "TextSize": 20,
                "Color": "Black",
                "Bold": False,
                "PosX": 300,
                "PosY": 140,
                "TextRect": "center"
            },
            "text5": {
                "Text": "Button 'GACHA' for get random tower and upgrade your team !!!",
                "TextSize": 20,
                "Color": "Black",
                "Bold": False,
                "PosX": 300,
                "PosY": 160,
                "TextRect": "center"
            },
            "text6": {
                "Text": "...",
                "TextSize": 30,
                "Color": "Black",
                "Bold": False,
                "PosX": 400,
                "PosY": 180,
                "TextRect": "center"
            }
        }
    },
    "gachaScreen": {
        "WIDTH": 600,
        "HEIGHT": 400,
        "BackGround": "Image/GachaBackGround.png",
        "GUI": {
            "button1": {
                "Function": "leave",
                "Text": "X",
                "TextSize": 35,
                "TextColor": "White",
                "SizeX": 20,
                "SizeY": 20,
                "PosX": 580,
                "PosY": 0,
                "Color": "Red",
                "ShapeRect": "topleft"
            },
            "button2": {
                "Function": "gacha basic",
                "Text": "Basic Tower",
                "TextSize": 35,
                "TextColor": "Black",
                "SizeX": 200,
                "SizeY": 200,
                "PosX": 150,
                "PosY": 200,
                "Color": "Yellow",
                "ShapeRect": "center"
            },
            "button3": {
                "Function": "gacha advanced",
                "Text": "Advanced Tower",
                "TextSize": 35,
                "TextColor": "Black",
                "SizeX": 200,
                "SizeY": 200,
                "PosX": 450,
                "PosY": 200,
                "Color": "Orange",
                "ShapeRect": "center"
            },
            "button4": {
                "Function": "line",
                "Text": "",
                "TextSize": 0,
                "TextColor": "Black",
                "SizeX": 5,
                "SizeY": 400,
                "PosX": 300,
                "PosY": 200,
                "Color": "Black",
                "ShapeRect": "center"
            },
            "button5": {
                "Function": "buy basic",
                "Text": "Buy: 500",
                "TextSize": 25,
                "TextColor": "Black",
                "SizeX": 100,
                "SizeY": 30,
                "PosX": 150,
                "PosY": 330,
                "Color": "Green",
                "ShapeRect": "center"
            },
            "button6": {
                "Function": "buy advanced",
                "Text": "Buy: 1200",
                "TextSize": 25,
                "TextColor": "Black",
                "SizeX": 100,
                "SizeY": 30,
                "PosX": 450,
                "PosY": 330,
                "Color": "Green",
                "ShapeRect": "center"
            }
        }
    },
    "modeScreen": {
        "WIDTH": 600,
        "HEIGHT": 400,
        "BackGround": "Image/ModeBackGround.png",
        "GUI": {
            "button1": {
                "Function": "leave",
                "Text": "X",
                "TextSize": 35,
                "TextColor": "White",
                "SizeX": 20,
                "SizeY": 20,
                "PosX": 580,
                "PosY": 0,
                "Color": "Red",
                "ShapeRect": "topleft"
            },
            "button2": {
                "Function": "play chapters",
                "Text": "CHAPTERS",
                "TextSize": 35,
                "TextColor": "Black",
                "SizeX": 200,
                "SizeY": 300,
                "PosX": 150,
                "PosY": 200,
                "Color": "Red",
                "ShapeRect": "center"
            },
            "button3": {
                "Function": "line",
                "Text": "",
                "TextSize": 0,
                "TextColor": "Black",
                "SizeX": 5,
                "SizeY": 400,
                "PosX": 300,
                "PosY": 200,
                "Color": "Black",
                "ShapeRect": "center"
            }
        }
    }
}
