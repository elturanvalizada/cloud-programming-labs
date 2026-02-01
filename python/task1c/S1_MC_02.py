# S1_MC_02 — Command router using match/case (Python 3.10+)

def run_command(cmd: str):
    match cmd:
        case "start":
            return "STARTED"
        case "stop":
            return "STOPPED"
        case "status":
            return "STATUS_OK"
        case _:
            return "UNKNOWN_COMMAND"


def main():
    tests = ["start", "stop", "status", "restart", "", None]

    for t in tests:
        print(f"run_command({t!r}) -> {run_command(t)}")


if __name__ == "__main__":
    main()
