# S3_PIPE_05 — Log line pipeline (parse → filter → extract)

def parse_line(line):
    """
    Example line:
    "INFO: user=42 action=login"
    -> {"level":"INFO", "user":"42", "action":"login"}
    """
    if not isinstance(line, str):
        return None

    line = line.strip()
    if ":" not in line:
        return None

    level_part, rest = line.split(":", 1)
    level = level_part.strip()
    fields = {"level": level}

    for token in rest.strip().split():
        if "=" in token:
            k, v = token.split("=", 1)
            fields[k] = v

    return fields


def extract_user_id(entry):
    try:
        return int(entry.get("user"))
    except (TypeError, ValueError, AttributeError):
        return None


def main():
    lines = [
        "INFO: user=42 action=login",
        "DEBUG: user=10 action=test",
        "INFO: user=7 action=logout",
        "INFO: user=abc action=login",
        "BROKEN LINE",
        None,
    ]

    parsed = (parse_line(l) for l in lines)
    parsed_ok = (p for p in parsed if p is not None)
    info_only = (p for p in parsed_ok if p.get("level") == "INFO")
    user_ids = (extract_user_id(p) for p in info_only)
    user_ids_clean = [uid for uid in user_ids if uid is not None]

    print("user ids:", user_ids_clean)


if __name__ == "__main__":
    main()
