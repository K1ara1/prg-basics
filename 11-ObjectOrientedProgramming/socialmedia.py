class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print('Hello, world!')
        print('Had a great day at the park!')
        print('Whats up, Natalie? How are you?')
    
def main():
    user = SocialMediaProfile('johndoe')
    
    print({user.display_timeline()})

if __name__ == "__main__":
    main()