from yt_dlp import YoutubeDL
from typing import TypedDict, NotRequired
from enum import Enum

class OutputFormat(Enum):
    MP3 = "mp3"
    MP4 = "mp4"

class DownloadOpts(TypedDict):
    format: str
    outtmpy: str
    output_format: OutputFormat
    no_playlist: bool

class Download:

    def __init__(self):
        pass


    def download(self):
        opts = {
            "format": "bv*+ba/b",

        }