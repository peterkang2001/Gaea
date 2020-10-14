# from utils.yml_conf import Yml
# from huobi.client.account import AccountClient
# from huobi.constant import *
# from huobi.utils import *
#
#
#
# yml = Yml().get_application_conf("application.yml")
# user = yml["account"]["production_user1"]
#
# account_client = AccountClient(api_key=user["access_key"],
#                               secret_key=user["secret_key"])
# list_obj = account_client.get_balance(account_id=13117811)
# LogInfo.output_list(list_obj)