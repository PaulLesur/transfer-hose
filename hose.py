import sys
import logging
import requests
import yaml

logging.basicConfig(filename='transfer-hose.log', level=logging.INFO)
logger = logging.getLogger(__name__)

def read_yaml(file_yaml):
    """Function used to load a YAML configuration file"""
    with open(file_yaml, 'r', encoding="utf-8") as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(f"Error when reading yaml file: {e}")
            return None

def get_metric_value(config, metric_name: str) -> str:
    """
    Returns the value of a metric, fetched in a Prometheus server.
    metric_name -- name of the metric to fetch.
    """
    logger.info("Getting metric value for %s", metric_name)
    logger.info( f"GET {config['ispindel']['prometheus']['host']}:{config['ispindel']['prometheus']['port']}/api/v1/query?query={metric_name}")
    try:
        fetched_data = requests.get(
            f"{config['ispindel']['prometheus']['host']}:{config['ispindel']['prometheus']['port']}/api/v1/query?query={metric_name}",
            timeout=10
            )
        #TODO find a better way to retrieve this data
        logger.info(fetched_data.json()['data']['result'][0]['value'][1])
    except KeyError:
        logger.error("Unable to fetch data, exiting...")
        sys.exit(1)
    return fetched_data.json()['data']['result'][0]['value'][1]

def send_data_to_littlebock(config, data: object):
    """
    Takes informations and send them to Littlebock
    """
    url = f"{config['ispindel']['littlebock']['serverAdress']}{config['ispindel']['littlebock']['serverUrl']}"
    logger.info("Sending data to Littlebock : %s , %s", url, data)
    response = requests.post(url, data, timeout=10)

    if "not attached" in response.json()['message']:
        logger.error("This device is not attached to a brew session. Exiting...")
        sys.exit(2)
    else:
        logger.info("data sent to littlebock")
