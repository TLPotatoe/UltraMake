# ansi_codes.py

### RESET CODE ###

RESET = "\x1b[0m"

### CURSOR MOVEMENT CODES (CUP) ###

def CURSOR_UP(n: int) -> str:
	return f"\x1b[{n}A"

def CURSOR_DOWN(n: int) -> str:
	return f"\x1b[{n}B"

def CURSOR_FORWARD(n: int) -> str:
	return f"\x1b[{n}C"

def CURSOR_BACK(n: int) -> str:
	return f"\x1b[{n}D"

def CURSOR_NEXT_LINE(n: int) -> str:
	return f"\x1b[{n}E"

def CURSOR_PREVIOUS_LINE(n: int) -> str:
	return f"\x1b[{n}F"

def CURSOR_HORIZONTAL_ABSOLUTE(n: int) -> str:
	return f"\x1b[{n}G"

def CURSOR_TO(row: int, col: int) -> str:
	return f"\x1b[{row};{col}H"


def CLEAR(mode: int) -> str:
	return f"\x1b[{mode}J"

def CLEARL(mode: int) -> str:
	return f"\x1b[{mode}K"

HOME = "\x1b[H"
SAVE_CURSOR = "\x1b[s"
RESTORE_CURSOR = "\x1b[u"


### ERASING CODES (J & K) ###

# J - Erase in Display
ERASE_SCREEN_TO_END = "\x1b[0J"
ERASE_SCREEN_TO_BEGIN = "\x1b[1J"
ERASE_SCREEN_FULL = "\x1b[2J"
ERASE_SCREEN_WITH_BUFFER = "\x1b[3J"

# K - Erase in Line
ERASE_LINE_TO_END = "\x1b[0K"
ERASE_LINE_TO_BEGIN = "\x1b[1K"
ERASE_LINE_FULL = "\x1b[2K"


### TEXT STYLES (SGR) ###

BOLD = "\x1b[1m"
FAINT = "\x1b[2m"
ITALIC = "\x1b[3m"
UNDERLINE = "\x1b[4m"
BLINK_SLOW = "\x1b[5m"
BLINK_FAST = "\x1b[6m"
INVERSE = "\x1b[7m"
INVISIBLE = "\x1b[8m"
STRIKETHROUGH = "\x1b[9m"

# Style Off Codes
BOLD_FAINT_OFF = "\x1b[22m"
ITALIC_OFF = "\x1b[23m"
UNDERLINE_OFF = "\x1b[24m"
BLINK_OFF = "\x1b[25m"
INVERSE_OFF = "\x1b[27m"
INVISIBLE_OFF = "\x1b[28m"
STRIKETHROUGH_OFF = "\x1b[29m"


### FOREGROUND COLORS (TEXT) ###

# Standard (30-37)
FG_BLACK = "\x1b[30m"
FG_RED = "\x1b[31m"
FG_GREEN = "\x1b[32m"
FG_YELLOW = "\x1b[33m"
FG_BLUE = "\x1b[34m"
FG_MAGENTA = "\x1b[35m"
FG_CYAN = "\x1b[36m"
FG_WHITE = "\x1b[37m"
FG_DEFAULT = "\x1b[39m"

# Bright (90-97)
FG_BRIGHT_BLACK = "\x1b[90m"
FG_BRIGHT_RED = "\x1b[91m"
FG_BRIGHT_GREEN = "\x1b[92m"
FG_BRIGHT_YELLOW = "\x1b[93m"
FG_BRIGHT_BLUE = "\x1b[94m"
FG_BRIGHT_MAGENTA = "\x1b[95m"
FG_BRIGHT_CYAN = "\x1b[96m"
FG_BRIGHT_WHITE = "\x1b[97m"


### BACKGROUND COLORS (FOND) ###

# Standard (40-47)
BG_BLACK = "\x1b[40m"
BG_RED = "\x1b[41m"
BG_GREEN = "\x1b[42m"
BG_YELLOW = "\x1b[43m"
BG_BLUE = "\x1b[44m"
BG_MAGENTA = "\x1b[45m"
BG_CYAN = "\x1b[46m"
BG_WHITE = "\x1b[47m"
BG_DEFAULT = "\x1b[49m"

# Bright (100-107)
BG_BRIGHT_BLACK = "\x1b[100m"
BG_BRIGHT_RED = "\x1b[101m"
BG_BRIGHT_GREEN = "\x1b[102m"
BG_BRIGHT_YELLOW = "\x1b[103m"
BG_BRIGHT_BLUE = "\x1b[104m"
BG_BRIGHT_MAGENTA = "\x1b[105m"
BG_BRIGHT_CYAN = "\x1b[106m"
BG_BRIGHT_WHITE = "\x1b[107m"