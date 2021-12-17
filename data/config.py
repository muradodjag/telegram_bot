import os
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

TOKEN = str(os.getenv('TOKEN'))
db_user = str(os.getenv("DB_USER"))
db_pass = str(os.getenv("DB_PASS"))
DATABASE = str(os.getenv("DB_NAME"))
host = str(os.getenv('host'))

POSTGRES_URI = f"postgresql://{db_user}:{db_pass}@{host}/{DATABASE}"

I18N_DOMAIN = "ocaqexpress"
BASE_DIR = Path(__file__).parent.parent
print(BASE_DIR)
LOCALES_DIR = BASE_DIR / 'locales'