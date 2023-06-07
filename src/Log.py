#! /usr/bin/env python3

try:
    from ANSI import *
except:
    print("ERROR:   Missing library:    ANSI")
    exit(1)

class LVL:
    INFO = 0
    WARN = 1
    FAIL = 2

class LOG:
    logs = []

    def Log(lvl, txt): # Example: [TYPE]	Message
        print(UTIL.CLEARLINE, end="")
        
        match lvl:
            case LVL.INFO:      msg = f"{FG.GREEN}{UTIL.BOLD}{UTIL.REVERSE}[ OK ]{UTIL.RESET}\t{txt}"
            case LVL.WARN:      msg = f"{FG.YELLOW}{UTIL.BOLD}{UTIL.REVERSE}[WARN]{UTIL.RESET}\t{txt}"
            case LVL.FAIL:      msg = f"{FG.RED}{UTIL.BOLD}{UTIL.REVERSE}[FAIL]{UTIL.RESET}\t{txt}"
            case _:             msg = f"{UTIL.REVERSE}{txt}{UTIL.RESET}"
        
        LOG.logs.append(msg)
        print(msg)
        if lvl == LVL.FAIL:
            exit(1)


def Log(lvl, txt): # Example: [TYPE]	Message
    LOG.Log(lvl,txt)

def PrintLogs():
    print(LOG.logs)
