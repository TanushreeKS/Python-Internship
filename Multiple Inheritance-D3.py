#Multiple Inheritance branch
# Parent Class 1
class Camera:
    def __init__(self, camera_quality):
        self.camera_quality = camera_quality

    def display_camera_details(self):
        print("Camera Quality:", self.camera_quality)


# Parent Class 2
class MusicPlayer:
    def __init__(self, sound_quality):
        self.sound_quality = sound_quality

    def display_music_details(self):
        print("Sound Quality:", self.sound_quality)


# Child Class
class SmartPhone(Camera, MusicPlayer):
    def __init__(self, camera_quality, sound_quality, brand):
        Camera.__init__(self, camera_quality)
        MusicPlayer.__init__(self, sound_quality)
        self.brand = brand

    def display_smartphone_details(self):
        print("Brand:", self.brand)


# Object Creation
phone = SmartPhone("108 MP", "Dolby Atmos", "Samsung")

phone.display_camera_details()
phone.display_music_details()
phone.display_smartphone_details()
