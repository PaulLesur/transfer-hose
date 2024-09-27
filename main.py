import logging
import hose

logging.basicConfig(filename='transfer-hose.log', level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Retrieve data from Prometheus server and send it ot Littlebock"""
    logger.info('Transfer-Hose started !')    

    # Exemple d'utilisation
    file = 'configuration/config.yaml'
    config = hose.read_yaml(file)
    if config:
        logger.info("Loaded configuration : %s", config)
        # TODO stuff
    logger.info('Transfer-Hose exited !')


if __name__ == "__main__":

    main()
