import logging
import hose

logging.basicConfig(filename='transfer-hose.log', level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Retrieve data from Prometheus server and send it ot Littlebock"""
    logger.info('Transfer-Hose started !')    

    file = 'configuration/config.yaml'
    config = hose.read_yaml(file)
    if config:
        logger.info("Loaded configuration : %s", config)
        # TODO stuff
        data_to_send = {
            "temperature" : hose.get_metric_value(config=config, metric_name="temperature"),
            "gravity" : hose.get_metric_value(config=config, metric_name="gravity"),
            "battery" : hose.get_metric_value(config=config, metric_name="battery")
        }
        hose.send_data_to_littlebock(config=config, data=data_to_send)

    logger.info('Transfer-Hose exited !')


if __name__ == "__main__":

    main()
