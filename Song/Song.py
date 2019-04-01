class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        turtle = self
        rabbit = self

        while (turtle and rabbit and rabbit.next):
            turtle = turtle.next
            rabbit = rabbit.next.next
            if turtle == rabbit:
                return True

        return False

            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second);
second.next_song(first);
    
print(first.is_repeating_playlist())

