#CONSTANTS
CELL = 8
DIM_IMG = (800,800)

START_BTN_CORD = (296,432)
START_BTN_DIM = (239,121)
LEVEL_BTN_CORD = (296,578)
LEVEL_BTN_DIM = (239,121)


LEVEL1 = [
    "ooooooooooooooooooooooooooooooooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
    "ooooooooooooooooooooooooooooooooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
    "o+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
    "o+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
    "o+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
    "o+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
    "o+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooooooooooooooooooooooooooooooooooo+++",
    "o+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooooooooooooooooooooooooooooooooooo+++",
    "o+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooooooooooooooooooooooooooooooooooo+++",
    "o+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "o+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "o+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "oooooooooooooooooooo++++++++++ooo+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "oooooooooooooooooooo++++++++++ooo+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "oooooooooooooooooooo++++++++++ooo+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+++++++++++++++++++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooooooooooooooooooooooooooooooo+++++++++ooooooooooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooooooooooooooooooooooooooooooo+++++++++ooooooooooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooooooooooooooooooooooooooooooo+++++++++ooooooooooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooo+++++++++++++++++++++++++++++++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooo+++++++++++++++++++++++++++++++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooo+++++++++++++++++++++++++++++++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooo+++++++++++++++++++++++++++++++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooo+++++++++++++++++++++++++++++++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooo+++++++++++++++++++++++++++++++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+oo++++++++++++++++++++++++++++++++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+ooo+++++++++++++++++++++++++++++++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooo+oo++++++++++++++++++++++++++++++++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooooooo++++++++++ooooooooooooooooo++++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooooooo+++++++++ooooooooooooooooooo+++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++ooooooo+++++++++ooooooooooooooooooo+++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++++++++++++++++++ooo+++++++++++++ooo+++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++++++++++++++++++ooo+++++++++++++ooo+++++++++ooooooooooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++++++++++++++++++ooo+++++++++++++ooo+++++++++ooooooooooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++++++++++++++++++ooo+++++++++++++ooo+++++++++ooooooooooo+++++++++ooo+++",
    "++++++++++++++++++oo++++++++++++++++++++++++++ooo+++++++++++++oo++++++++++++++++++++++++++++++ooo+++",
    "o+++++++++++++++++oo++++++++++++++++++++++++++ooo+++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++++++++++++++++++ooo+++++++++++++oo++++++++++++++++++++++++++++++ooo+++",
    "o+++++++++++++++++oo++++++++++++++++++++++++++ooo+++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++oo++++++++++++++++++++++++++ooo+++++++++++++oo++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++ooooooooooooooooooooooooooo+ooo+++++++++++++ooo+++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++ooooooooooooooooooooooooooooooo+++++++++++++oo++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++ooooooooooooooooooooooooooooooo+++++++++++++oo++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oo++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oo+++++++++++oooooooooooooooooooooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oo++++++++++ooooooooooooooooooooooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++++++++ooooooooooooooooooooooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oo++++++++++ooo+++++++++++++++++++++++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oo++++++++++ooo+++++++++++++++++++++++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oo++++++++++ooo+++++++++++++++++++++++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++++++++ooo+++++++++++++++++++++++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oo++++++++++ooo+++++++++++++++++++++++",
    "++++++++++++++ooooooooooooooooooooooooooooooooooooooooooooooooooo+++++++++ooo+++++++++++++++++++++++",
    "++++++++++++++ooooooooooooooooooooooooooooooooooooooooooooooooooo+++++++++ooo+++++++++++++++++++++++",
    "++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooooooooooooooooooooooo+++",
    "++++++++++++++oo++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooooooooooooooooooooooo+++",
    "++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++oo++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++ooo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++oo++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++ooo++++++++++ooooooooooooooooooooooooooooooooooooo+++++++++++ooooooooo++++++++++ooo+++",
    "++++++++++++++oo++++++++++ooooooooooooooooooooooooooooooooooooooo+++++++++ooooooooooo+++++++++ooo+++",
    "o+++++++++++++ooo+++++++++ooooooooooooooooooooooooooooooooooooooo+++++++++oooooooooo++++++++++ooo+++",
    "++++++++++++++oo++++++++++ooo+++++++++++++++++++++++++++++++++oo++++++++++ooo+++++oo++++++++++ooo+++",
    "++++++++++++++ooo+++++++++ooo+++++++++++++++++++++++++++++++++ooo+++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++oo++++++++++ooo+++++++++++++++++++++++++++++++++oo++++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++ooo+++++++++ooo+++++++++++++++++++++++++++++++++ooo+++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++ooo+++++++++ooo+++++++++++++++++++++++++++++++++ooo+++++++++ooo+++++oo++++++++++ooo+++",
    "++++++++++++++ooo+++++++++ooo+++++++++++++++++++++++++++++++++ooo+++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++ooo+++++++++ooo+++++++++++++++++++++++++++++++++ooo+++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++ooo+++++++++ooo+++++++++++++++++++++++++++++++++ooo+++++++++ooo+++++ooo+++++++++ooo+++",
    "++++++++++++++oo+++++++++++oo+++++++++++++++++++++++++++++++++oo++++++++++ooo+++++oo++++++++++ooo+++",
    "++++++++++++++ooooooooooo+ooo+++++++++++++++++++++++++++++++++ooooooooooooooo+++++ooo+++++++++ooo+++",
    "++++++++++++++ooooooooooooooo+++++++++++++++++++++++++++++++++ooooooooooooooo+++++oo++++++++++ooo+++",
    "++++++++++++++ooooooooooooooo+++++++++++++++++++++++++++++++++ooooooooooooooo+++++ooo+++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oo++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++oo++++++++++ooo+++",
    "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo+++++++++ooo+++",
    "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo+++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ooo+++",
    "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo+++",
    "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo+++",
    "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo+++",
    "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
]