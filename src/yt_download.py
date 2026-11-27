from yt_dlp import YoutubeDL
from typing import TypedDict, NotRequired
from enum import Enum
from dl_options import DLOptions

class OutputFormat(Enum):
    MP3 = "mp3"
    MP4 = "mp4"

class DownloadOpts(TypedDict):
    format: str
    outtmpy: str
    output_format: OutputFormat
    is_playlist: bool

class Download:

    def __init__(self):
        pass


    def download(self, url, options: DownloadOpts):
        opts = {
            "format": "bv*+ba/b",
            "noplaylist": options["is_playlist"]
        }

        with YoutubeDL(opts) as ydl:
            ydl.download([url])

class VideoDL:

    def __init__(self, opts: DLOptions):
        self.opts = opts

    def download(self, url):
        with YoutubeDL(self.opts) as ydl:
            ydl.download([url])
