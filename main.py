import logging
import time
from datetime import timedelta
import schedule
import hose

logging.basicConfig(filename='transfer-hose.log', level=logging.INFO)
logger = logging.getLogger(__name__)

def job(config):
    """Default behaviour : retrive metrics from Prometheus and send them to Littlebock"""
    data_to_send = {
        "temperature" : hose.get_metric_value(config=config, metric_name="temperature"),
        "gravity" : hose.get_metric_value(config=config, metric_name="gravity"),
        "battery" : hose.get_metric_value(config=config, metric_name="battery")
    }
    hose.send_data_to_littlebock(config=config, data=data_to_send)

def main():
    """Retrieve data from Prometheus server and send it to Littlebock periodicaly"""
    logger.info('Transfer-Hose started !')    

    file = 'configuration/config.yaml'
    config = hose.read_yaml(file)
    if config:
        logger.info("Loaded configuration : %s", config)
        schedule.every(config['ispindel']['synchronisation']['intervalMinutes']).minutes.until(timedelta(days=config['ispindel']['synchronisation']['timeoutDays'])).do(job, config=config)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
