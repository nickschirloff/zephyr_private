from typing import TypedDict
from enum import Enum

class OutputFormat(Enum):
    MP3 = "mp3"
    MP4 = "mp4"

class DLOptions(TypedDict):
    format: str
    output_format: OutputFormat
    outtmpl: str # Output filename template
    noplaylist: bool
    embed_thumbnail: bool
    extract_audio: bool

default_options: DLOptions = {
    "format": "bestvideo+bestaudio/best",
    "audio_format": "mp3",
    "outtmpl": "%(title)s.%(ext)s",
    "noplaylist": False,
    "embed_thumbnail": True,
    "extract_audio": True
}