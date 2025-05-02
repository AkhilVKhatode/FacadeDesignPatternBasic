class MusicPlayer:
    def initialize_audio_drivers(self):
        print("Audio drivers initialized.")

    def decode_audio(self):
        print("Audio decoded.")

    def start_playback(self):
        print("Music playback started.")


class VideoPlayer:
    def setup_rendering_engine(self):
        print("Rendering engine set up.")

    def load_video_file(self):
        print("Video file loaded.")

    def play_video(self):
        print("Video playback started.")


class ImageViewer:
    def load_image_file(self):
        print("Image file loaded.")

    def apply_scaling(self):
        print("Image scaled.")

    def display_image(self):
        print("Image displayed.")


class MediaFacade:
    def __init__(self):
        self.music_player = MusicPlayer()
        self.video_player = VideoPlayer()
        self.image_viewer = ImageViewer()

    def perform_action(self, action):
        action = action.lower()
        if action == "playmusic":
            self.music_player.initialize_audio_drivers()
            self.music_player.decode_audio()
            self.music_player.start_playback()
        elif action == "playvideo":
            self.video_player.setup_rendering_engine()
            self.video_player.load_video_file()
            self.video_player.play_video()
        elif action == "viewimage":
            self.image_viewer.load_image_file()
            self.image_viewer.apply_scaling()
            self.image_viewer.display_image()
        else:
            print("Invalid action!")


if __name__ == "__main__":
    media_facade = MediaFacade()
    action = input("Welcome to Multimedia App!\nChoose an action: playMusic, playVideo, viewImage\n")
    media_facade.perform_action(action)
