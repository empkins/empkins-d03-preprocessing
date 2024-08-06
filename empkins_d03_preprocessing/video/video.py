from pathlib import Path

import pandas as pd
from moviepy.video.io.VideoFileClip import VideoFileClip


def slice_video_to_phases(video_path: str, timelog_video: pd.DataFrame, output_path: str):
    """
    Slice video to the given start and end time and save it to the output path.

    Args:
        video_path (Path): Path to the video file.
        timelog_video (pd.DataFrame): Timelog DataFrame.
        output_path (Path): Path to save the sliced video.
    """
    video = VideoFileClip(video_path)


    start_time = timelog_video["start_talk_1"]
    end_time = timelog_video["start_pause_3"]
    pause_start = timelog_video["start_pause_2"]
    pause_end = timelog_video["start_talk_2"]

    sliced_video = video.subclip(start_time, end_time).cutout(pause_start - start_time, pause_end - start_time)
    sliced_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

def slice_video_conditions(video_path: str, timelog: pd.DataFrame, output_path: str):
    """
    Slice video to the given start and end time and save it to the output path.

    Args:
        video_path (Path): Path to the video file.
        timelog (pd.DataFrame): Timelog DataFrame.
        output_path (Path): Path to save the sliced video.
    """
    video = VideoFileClip(video_path)

    start_time = timelog["start_talk_1"]
    end_time = timelog["start_pause_5"]
    timelog_relative = timelog - start_time
    pause_2_start = timelog_relative["start_pause_2"]
    pause_2_end = timelog_relative["start_talk_2"]
    duration_pause_2 = pause_2_end - pause_2_start
    pause_3_start = timelog_relative["start_pause_3"] - duration_pause_2
    pause_3_end = timelog_relative["start_math_1"] - duration_pause_2
    duration_pause_3 = pause_3_end - pause_3_start
    pause_4_start = timelog_relative["start_pause_4"] - duration_pause_2 - duration_pause_3
    pause_4_end = timelog_relative["start_math_2"] - duration_pause_2 - duration_pause_3

    sliced_video = video.subclip(start_time, end_time).cutout(pause_2_start, pause_2_end).cutout(pause_3_start, pause_3_end).cutout(pause_4_start, pause_4_end)
    sliced_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

