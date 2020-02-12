from minecraft.authentication import AuthenticationToken
from minecraft.exceptions import YggdrasilError


def auth_account(account):
    token_obj = AuthenticationToken()
    try:
        token_obj.authenticate(account["username"], account["password"])
        return token_obj
    except Exception:
        return False
