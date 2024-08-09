from pathlib import Path

import pandas as pd
from empkins_io.datasets.d03.micro_gapvii import MicroBaseDataset
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import concatenate_videoclips


def slice_video_to_phases(subset: MicroBaseDataset):
    """
    Slice video to the given start and end time and save it to the output path.

    Args:
        subset (MicroBaseDataset): Subset containing the video file and timelog.
    """

    if not subset.is_single(["subject", "condition", "phase"]):
        raise ValueError("Subset must contain only one subject and one condition.")

    video = VideoFileClip(str(subset.face_video_path))
    timelog = subset.timelog_video
    phase = subset.phase

    if phase == "Talk":
        talk_1 = video.subclip(timelog["start_talk_1"], timelog["start_pause_2"])
        talk_2 = video.subclip(timelog["start_talk_2"], timelog["start_pause_3"])
        sliced_video = concatenate_videoclips([talk_1, talk_2])
    elif phase == "Math":
        math_1 = video.subclip(timelog["start_math_1"], timelog["start_pause_4"])
        math_2 = video.subclip(timelog["start_math_2"], timelog["start_pause_5"])
        sliced_video = concatenate_videoclips([math_1, math_2])
    else:
        raise ValueError(f"Phase '{phase}' not in ['Talk', 'Math'].")

    sliced_video.write_videofile(str(subset.face_video_path_sliced), audio_codec="aac", ffmpeg_params=["-c:v", "h264_videotoolbox"])


def slice_video_conditions(video_path: Path, timelog: pd.DataFrame, output_path: Path):
    """
    Slice video to the given start and end time and save it to the output path.

    Args:
        video_path (Path): Path to the video file.
        timelog (pd.DataFrame): Timelog DataFrame.
        output_path (Path): Path to save the sliced video.
    """

    if not video_path.exists():
        raise FileNotFoundError(f"Video file not found in {video_path}.")

    video = VideoFileClip(str(video_path))

    if timelog.drop("Infos").isna().any():
        raise ValueError("Timelog contains NaN values.")

    talk_1 = video.subclip(timelog["start_talk_1"], timelog["start_pause_2"])
    talk_2 = video.subclip(timelog["start_talk_2"], timelog["start_pause_3"])
    math_1 = video.subclip(timelog["start_math_1"], timelog["start_pause_4"])
    math_2 = video.subclip(timelog["start_math_2"], timelog["start_pause_5"])

    sliced_video = concatenate_videoclips([talk_1, talk_2, math_1, math_2])
    sliced_video.write_videofile(str(output_path), audio_codec="aac", ffmpeg_params=["-c:v", "h264_videotoolbox"])
