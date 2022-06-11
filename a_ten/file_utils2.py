# -*- coding:utf-8 -*-
# @Author: lyp
# @Desc  : todo
# @Time  : 22/04/03 17:04
import os

music_suffix = [".wav", ".mp3", ".wma", ".ape", ".aac", ".flac", ".alac", ".m4a", ".mpeg-4", ".mpeg"]
img_suffix = [".bmp", ".jpg", ".jpeg", ".png", ".tif", ".gif", ".pcx", ".tga", ".exif", ".fpx", ".svg", ".psd", ".cdr", ".pcd", ".dxf", ".ufo", ".eps", ".ai", ".raw", ".wmf",
              ".webp", ".avif", ".apng"]

video_suffix = [".mp4", ".flv", ".f4v", ".webm", ".m4v", ".mov", ".3gp", ".3g2", ".rm", ".rmvb", ".wmv", ".avi", ".asf", ".mpg", ".mpeg", ".mpe", ".ts", ".div", ".dv", ".divx",
                ".vob", ".dat", ".mkv", ".lavf", ".cpk", ".dirac", ".ram", ".qt", ".fli", ".flc", ".mod"]


def is_music(file_name):
    return os.path.splitext(file_name)[1].lower() in music_suffix


def is_imagine(file_name):
    return os.path.splitext(file_name)[1].lower() in img_suffix


def is_video(file_name):
    return os.path.splitext(file_name)[1].lower() in video_suffix


def is_image_video(file_name):
    ext = os.path.splitext(file_name)[1].lower()
    return ext in img_suffix or ext in video_suffix
