
import os  
basedir = os.path.abspath(os.path.dirname(__file__))

# load environmental configurations 
from dotenv import load_dotenv 
load_dotenv(os.path.join(basedir, '.env'))
