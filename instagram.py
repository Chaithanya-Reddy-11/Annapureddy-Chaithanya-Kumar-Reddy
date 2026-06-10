class Instagram:
    total_accounts = 0
    usernames = []

    def __init__(self, name, password):
        if name in Instagram.usernames:
            raise ValueError("Username already exists")
        if not Instagram.is_valid_password(password):
            raise ValueError("Invalid password")
        self.name = name
        self.password = password
        self.follower_count = 0
        self.followed_count = 0
        self.follower_list = []
        self.followed_list = []
        Instagram.usernames.append(name)
        Instagram.total_accounts += 1

    def follow(self, other_user):
        if other_user.name not in self.followed_list:
            self.followed_list.append(other_user.name)
            self.followed_count += 1
            other_user.follower_list.append(self.name)
            other_user.follower_count += 1
        else:
            print("Already following")

    def unfollow(self, other_user):
        if other_user.name in self.followed_list:
            self.followed_list.remove(other_user.name)
            self.followed_count -= 1
            if self.name in other_user.follower_list:
                other_user.follower_list.remove(self.name)
                other_user.follower_count -= 1
        else:
            print("Not following this user")

    def display(self, entered_password):
        if self.password == entered_password:
            print("Username:", self.name)
            print("Followers:", self.follower_count)
            print("Follower List:", self.follower_list)
            print("Following:", self.followed_count)
            print("Following List:", self.followed_list)
        else:
            print("Invalid password")

    @classmethod
    def get_total_accounts(cls):
        print(f"Total registered accounts: {cls.total_accounts}")
        return cls.total_accounts

    @staticmethod
    def is_valid_password(password):
        return len(password) > 6


u1 = Instagram("chaithanya", "1234567")
u2 = Instagram("reddy", "abcdefg")
u1.follow(u2)
u1.display("1234567")
u2.display("abcdefg")
Instagram.get_total_accounts()
