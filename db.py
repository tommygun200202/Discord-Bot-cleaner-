import motor.motor_asyncio
import config
import pymongo

database = motor.motor_asyncio.AsyncIOMotorClient(config.mongoString, connect=True)['hackathon']
