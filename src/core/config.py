# En src/core/config.py
from python-dotenv-vault import load_dotenv
load_dotenv(override=True, vault_file=".env.vault")
