import logging
import yaml

def read_yaml(file_yaml):
    """Function used to load a YAML configuration file"""
    with open(file_yaml, 'r', encoding="utf-8") as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(f"Error when reading yaml file: {e}")
            return None


def get_metric_value(metric_name: str) -> str:
    """
    Returns the value of a metric, fetched in a Prometheus server.
    metric_name -- name of the metric to fetch.
    """
    logger.info("Getting metric value for %s", metric_name)

    return metric_name

def format_payload_for_littlebock(temperature: str, battery: str, gravity: str) -> str:
    """
    Takes informations to send and format them into an objet to send to Littlebock
    """
    # Peut etre inutile si je fais ça proprement avec une structure de donnée appropriée
    return ""

def send_data_to_littlebock(temperature: str, battery: str, gravity: str):
    """
    Takes informations and send them to Littlebock
    """
    logger.info("Sending infos to Littlebock : temperature=%s , battery=%s , gravity=%s", temperature, battery, gravity)
    return

def main():
    """Retrieve data from Prometheus server and send it ot Littlebock"""
    logger.info('Transfer-Hose started !')    

    # Exemple d'utilisation
    file = 'configuration/config.yaml'
    config = read_yaml(file)
    if config:
        logger.info("Loaded configuration : %s", config)
        # TODO stuff
    logger.info('Transfer-Hose exited !')




logging.basicConfig(filename='transfer-hose.log', level=logging.INFO)
logger = logging.getLogger(__name__)
if __name__ == "__main__":

    main()
