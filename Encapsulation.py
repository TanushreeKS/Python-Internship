class InstagramAccount:

    def __init__(self, account_name, password):
        self.account_name = account_name
        self._private_reels = []
        self.__archived_reels = []
        self.__password = password

    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)
        print(f"Private reel '{reel_name}' added.")

    def display_private_reels(self, is_follower):
        if is_follower:
            print("\nPrivate Reels:")
            for reel in self._private_reels:
                print("-", reel)
        else:
            print("\nAccess Denied! Only followers can view private reels")

    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)
        print(f"Archived reel '{reel_name}' added.")

    def display_archived_reels(self, password):
        if password == self.__password:
            print("\nArchived Reels:")
            for reel in self.__archived_reels:
                print("-", reel)
        else:
            print("\nAccess Denied! Only account holder can view archived reels")

    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            print("\nWrong Password! Cannot access archived reels")
            return None

    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("\nPassword updated successfully")
        else:
            print("\nWrong old password! Cannot update password")


account = InstagramAccount("manvi_insta", "1234")

account.add_private_reel("Travel Vlog")
account.add_private_reel("Birthday Party")

account.add_archived_reel("Old Dance Video")
account.add_archived_reel("School Memories")

account.display_private_reels(True)
account.display_private_reels
