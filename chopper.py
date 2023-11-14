from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def generate_clips(video_path, how_many_clips, duration, output_path):

    if not os.path.exists(video_path):
        print("File does not exist")
        return

    if not os.path.exists("./segments"):
        try:
            os.mkdir("./segments")
        except Exception as e:
            print(f"failed to create a new directory for clips: {e}")
            return

    clipName = "clip_"

    start = 0
    inc = duration    # seconds per clip

    trueOutput = output_path+"segments/"+clipName

    videoFile = VideoFileClip(video_path)

    for i in range(how_many_clips):
        output = trueOutput+str(i)+".mp4"   # just naming the file

        try: 
            clip = videoFile.subclip(start, start+inc).without_audio()
            clip.write_videofile(output, audio=False)
        except Exception as e:
            print(f"an error occurred during clipping: {e}")
            return
        finally:
            clip.close()
        # increment the start of the next clip
        start += inc

    videoFile.close()

def main():
    import sys
    print(sys.executable)
    if len(sys.argv) != 4:
        print("Usage: python3 chopper.py <video_path> <how_many_clips> <duration (sec)>")
        return

    video_path = sys.argv[1]
    how_many_clips = int(sys.argv[2])
    clip_duration = int(sys.argv[3])
    output_path = "./"

    generate_clips(video_path, how_many_clips, clip_duration, output_path)

if __name__ == "__main__":
    main()