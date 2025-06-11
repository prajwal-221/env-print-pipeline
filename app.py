import os

env = os.getenv('DEPLOY_ENV', 'development')
print(f"We are in the {env} environment.")
