import sda
va = sda.VideoAnimator(gpu=0, model_path="grid")# Instantiate the animator
vid, aud = va("example/sample.jpg", "example/scissorhands.wav")
va.save_video(vid, aud, "generated.mp4", scale=10)
