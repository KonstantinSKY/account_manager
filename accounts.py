from typing import Dict, Any, Optional
from databases import ConnectDB

class Account:
    """Secure account credential management logic."""
    accounts: Dict[int, 'Account'] = {}
    table: str = 'accounts'

    def __init__(self, account_obj: Dict[str, Any], id_: Optional[int] = None, db: Optional[ConnectDB] = None):
        """
        Initialize an Account object.
        :param account_obj: Data (login, password, id_service).
        :param id_: Optional record ID.
        :param db: Database connection for persistence.
        """
        self.id_ = id_
        self.login: str = account_obj.get("login", "")
        self.password: str = account_obj.get("password", "")
        self.id_service: int = account_obj.get("id_service", 0)
        
        # Persistence Logic
        if db and not self.id_:
            self.id_ = db.insert(Account.table, account_obj)
            if self.id_:
                db.commit()
        
        # Cache Update
        if self.id_:
            Account.accounts[self.id_] = self

    def __repr__(self) -> str:
        return f"<Account(id={self.id_}, login='{self.login}')>"

    @classmethod
    def show_all(cls) -> None:
        """Securely display all accounts with masked passwords."""
        if not cls.accounts:
            print("No accounts found.")
            return

        print("\n" + "="*80)
        print(f"{'ID':<5} | {'Login':<20} | {'Service ID':<10} | {'Password':<20}")
        print("-" * 80)
        for _, acc in cls.accounts.items():
            masked_pwd = "*" * 8  # Masking password for safe display
            print(f"{acc.id_:<5} | {acc.login:<20} | {acc.id_service:<10} | {masked_pwd:<20}")
        print("="*80 + "\n")
