import asyncio
import logging

from src.infraestructure.database.seeds import run as run_seeds

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def seeder():
    logger.info("Creating Fake data...")
    asyncio.run(run_seeds())
    logger.info("Created data successfully!")

if __name__ == "__main__":
    seeder()
