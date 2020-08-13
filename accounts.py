from typing import Dict, Any, Optional
from init_app import conn

class Account:
    """Secure account credential management logic."""
    accounts: Dict[int, 'Account'] = {}
    table: str = 'accounts'

    def __init__(self, account_obj: Dict[str, Any], id_: Optional[int] = None):
        self.id_ = id_
        self.login: str = account_obj["login"]
        self.password: str = account_obj["password"]
        self.id_service: int = account_obj.get("id_service", 0)
        
        if not self.id_:
            self.id_ = conn.insert(Account.table, account_obj)
        
        if self.id_:
            conn.commit()
            Account.accounts.update({self.id_: self})

    @classmethod
    def show_all(cls) -> None:
        """Securely display all accounts."""
        for key, acc in cls.accounts.items():
            print(f"[{acc.id_}] Login: {acc.login} | Service ID: {acc.id_service}")
