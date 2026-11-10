from moviepy.editor import VideoFileClip

def export_clip(input_path: str, start: float, end: float, output_path: str):
    clip = VideoFileClip(input_path).subclip(start, end)
    clip.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=30)
    clip.close()
