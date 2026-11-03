from locust import events

ASSETSYNC_HOST = None
CSAFSYNC_HOST = None
REGISTERED_USER_CLASSES: list[tuple[type, str]] = []


def register_user_class(target: str):
    def decorator(cls):
        REGISTERED_USER_CLASSES.append((cls, target))
        return cls

    return decorator


@events.init_command_line_parser.add_listener
def add_custom_args(parser):
    existing = set(parser._option_string_actions.keys())

    if "--assetsync-host" not in existing:
        parser.add_argument(
            "--assetsync-host",
            type=str,
            default="http://localhost:8992",
            help="Base URL for assetsync_api",
        )

    if "--csafsync-host" not in existing:
        parser.add_argument(
            "--csafsync-host",
            type=str,
            default="http://localhost:8991",
            help="Base URL for csafsync_api",
        )

    if "--matcher-host" not in existing:
        parser.add_argument(
            "--matcher-host",
            type=str,
            default="http://localhost:8998",
            help="Base URL for matcher",
        )


@events.init.add_listener
def store_custom_args(environment, **kwargs):
    global ASSETSYNC_HOST, CSAFSYNC_HOST

    ASSETSYNC_HOST = environment.parsed_options.assetsync_host
    CSAFSYNC_HOST = environment.parsed_options.csafsync_host
    MATCHER_HOST = environment.parsed_options.matcher_host

    for cls, target in REGISTERED_USER_CLASSES:
        if target == "assetsync":
            cls.host = ASSETSYNC_HOST
        elif target == "csafsync":
            cls.host = CSAFSYNC_HOST
        elif target == "matcher":
            cls.host = MATCHER_HOST
