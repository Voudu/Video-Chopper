# Video Chopper
Creates clips of an .mp4 video using moviepy. Creates any number of clips of any duration from a .mp4 video. Does not include
audio in the clips but could easily be made to.

## Installation and Usage
Create a virtual environment and install dependencies using the following commands:

### Installation:
```
python -m venv videnv
videnv\Scripts\Activate.ps1 (depends on OS)
pip install -r requirements.txt
```

### Usage:
```
py chopper.py <video_path> <how_many_clips> <duration (sec)>
```
Note: the output will be in the root directory and create a folder called 'segments'
