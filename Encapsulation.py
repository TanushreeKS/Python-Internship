class InstagramAccount:

    def __init__(self, account_name, password):
        # Public Variable
        self.account_name = account_name

        # Protected Variable
        self._private_reels = []

        # Private Variable
        self.__archived_reels = []

        # Private Password
        self.__password = password


    # 1. Add Private Reel
    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)
        print(f"Private reel '{reel_name}' added.")


    # 2. Display Private Reels
    def display_private_reels(self, is_follower):

        if is_follower:
            print("\nPrivate Reels:")
            for reel in self._private_reels:
                print("-", reel)
        else:
            print("\nAccess Denied! Only followers can view private reels")


    # 3. Add Archived Reel
    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)
        print(f"Archived reel '{reel_name}' added.")


    # 4. Display Archived Reels
    def display_archived_reels(self, password):

        if password == self.__password:

            print("\nArchived Reels:")
            for reel in self.__archived_reels:
                print("-", reel)

        else:
            print("\nAccess Denied! Only account holder can view archived reels")


    # 5. Getter Method (for archived reels)
    def get_archived_reels(self, password):

        if password == self.__password:
            return self.__archived_reels

        else:
            print("\nWrong Password! Cannot access archived reels")
            return None


    # 6. Setter Method (update password)
    def set_password(self, old_password, new_password):

        if old_password == self.__password:
            self.__password = new_password
            print("\nPassword updated successfully")

        else:
            print("\nWrong old password! Cannot update password")



# ===============================
# Main Program (Task Part)
# ===============================

# Create Object
account = InstagramAccount("manvi_insta", "1234")


# Add Private Reels
account.add_private_reel("Travel Vlog")
account.add_private_reel("Birthday Party")


# Add Archived Reels
account.add_archived_reel("Old Dance Video")
account.add_archived_reel("School Memories")


# Display Private Reels (Follower)
account.display_private_reels(True)


# Display Private Reels (Non-Follower)
account.display_private_reels(False)


# Display Archived Reels (Correct Password)
account.display_archived_reels("1234")


# Display Archived Reels (Wrong Password)
account.display_archived_reels("0000")


# Getter Method Test
print("\nUsing Getter Method:")
data = account.get_archived_reels("1234")

if data:
    print(data)


# Update Password (Setter)
account.set_password("1234", "5678")


# Check With New Password
account.display_archived_reels("5678")
