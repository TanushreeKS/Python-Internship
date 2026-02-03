# Class and object

class Instagram:
    def __init__(self, title, description, creator_name, location):
        self.title = title
        self.description = description
        self.creator_name = creator_name
        self.location = location
        self.likes = 0
        self.comments = []   # list of strings

    def display_title(self):
        print("The title of the reel is", self.title)

    def display_description(self):
        print("The description of the reel is", self.description)

    def display_creator_name(self):
        print("The creator of the reel is", self.creator_name)

    def display_location(self):
        print("The location of the reel is", self.location)

    def display_likes(self):
        print("The likes of the reel is", self.likes)

    def display_comments(self):
        print("Comments on the reel:")
        for comment in self.comments:
            print("-", comment)

    def liked(self):
        self.likes += 1

    def disliked(self):
        if self.likes > 0:
            self.likes -= 1

    def add_comment(self, comment):
        self.comments.append(comment)

    # New Method Added
    def delete_last_comment(self):
        if len(self.comments) > 0:
            self.comments.pop()
        else:
            print("No comments to delete")


# Creating objects
reel1 = Instagram(
    "dancing",
    "dancing with friends",
    "Rahul",
    "Mumbai"
)

reel1.disliked()   # 0
reel1.liked()      # 1

reel1.add_comment("Nice video!")
reel1.add_comment("Loved the dance!")

#Delete last comment
reel1.delete_last_comment()

reel2 = Instagram(
    "finance minister conference",
    "finance minister conference with friends",
    "Anita",
    "Delhi"
)

reel1.liked()      # 2
reel2.liked()      # 1
reel1.disliked()   # 1

reel1.display_likes()
reel2.display_likes()

reel1.display_comments()

print(id(reel1))
print(id(reel2))

