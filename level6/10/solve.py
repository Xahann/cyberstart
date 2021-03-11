
from PIL import Image
im = Image.open('qr.gif')
print("Number of frames: "+str(im.n_frames))

frames = im.n_frames

for i in range(frames):
    im.seek(i)
    im.save(f"frame{i}.png")
