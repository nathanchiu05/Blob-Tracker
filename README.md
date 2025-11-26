# Blob-Tracker

Blob tracking is a computer vision technique that detects and outlines regions of a video/photo. A unique application of blob tracking is its use as a visual effect in video editing. A common way to achieve this effect is through TouchDesigner, an application used for creating real-time interactive multimedia. I've always wanted to use this visual effect in my video editing, until I realized how difficult TouchDesigner was, so I decided to create this effect myself using Haar cascades in OpenCV. 

# cars.xml
Trained XML classifier used to identify cars.

# TouchDesign Blob Track
<img width="446" height="356" alt="my_blobtracking" src="https://github.com/user-attachments/assets/94b0e43b-0bb3-495c-a282-121569618b00" />

# My Blob Track
<img width="446" height="356" alt="my_blobtracking" src="https://github.com/user-attachments/assets/b9fe0e64-bd7b-408f-bbb6-852c85168bd0" />

# Dependencies
<u>opencv-contrib<u>
<pre>
```bash
pip install opencv-contrib-python
```
</pre>

<u>Video Codecs<u>
- To ensure video reading/writing, inputs must be in MP4 format 
