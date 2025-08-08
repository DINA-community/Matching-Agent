from dina.common import logging

logger = logging.get_logger(__name__)


def main():
    # TODO: Implement the api generator.
    # It must fetch the yaml spec from a provided url with a token
    # It must then use the python openapi_python_client to generate the api client
    # This client should be stored in a "generated" directory which is then imported by the
    # netbox plugin.
    logging.configure_logging()
    logger.info("Generating API")


if __name__ == "__main__":
    main()
