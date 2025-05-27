from abc import ABC, abstractmethod


class MediaPlayer(ABC):
    def __init__(self, filename: str):
        self.filename = filename

    @abstractmethod
    def play(self) -> None:
        pass


class AudioPlayer(MediaPlayer):
    def play(self) -> None:
        print(f"🎵 Playing Song: {self.filename}")


class VideoPlayer(MediaPlayer):
    def play(self) -> None:
        print(f"🎬 Playing Movie: {self.filename}")

audio = AudioPlayer("Mamontovas.mp3")
video = VideoPlayer("ScaryMovie.mp4")

media_players = [audio, video]

for player in media_players:
    player.play()
    