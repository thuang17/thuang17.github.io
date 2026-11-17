"""Re-cut the ChamberUp demo video: same recording, but the caption bar under the phone is removed (height now equals the 590x1277 screenshots)
and each caption is shown as a small pill inside the picture: fades in at the start of its scene, stays CAP_HOLD seconds, fades out.
usage: python3 make_demo_video.py <source_with_bar.mp4> <out.mp4> <poster.jpg> [bottom|top]"""
import sys, subprocess, os, tempfile
from PIL import Image, ImageDraw, ImageFont

W, H = 590, 1276                     # screenshots are 800x1732 = 590x1277 (1 px dropped, yuv420p needs an even height)
CAPS = [(0.4, 10.2, 'Sign in with a one-time email code'), (10.6, 15.8, 'Popular venues, ranked by check-ins'),
        (16.2, 22.8, 'Browse and search partner venues'), (23.2, 29.4, 'Tap a pin to open a venue'),
        (29.8, 38.8, 'Check in with the venue code'), (39.4, 46.4, 'Find members and view their profiles'),
        (46.8, 59.6, 'Invite a member to meet'), (60.2, 66.2, 'Track every invitation'),
        (66.8, 70.2, 'Earn points for every check-in'), (70.6, 78.8, 'Staff dashboard: members, activity, venue reach')]
CAP_HOLD, FADE_IN, FADE_OUT = 3.6, 0.3, 0.35
FONT = '/System/Library/Fonts/HelveticaNeue.ttc'

def pill(text, path, size=27, max_w=W - 40):
    """Small rounded caption pill (semi-transparent navy), centred; placed above the tab bar so the status bar and the Dynamic Island stay untouched."""
    while True:
        f = ImageFont.truetype(FONT, size); tw = int(f.getlength(text)); pad_x, h = 24, 54
        if tw + 2 * pad_x <= max_w or size <= 18: break
        size -= 1
    w = tw + 2 * pad_x; s = 4
    im = Image.new('RGBA', (w * s, h * s), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w * s - 1, h * s - 1], radius=h * s // 2, fill=(10, 25, 49, 225))
    d.text((pad_x * s, h * s // 2), text, font=ImageFont.truetype(FONT, size * s), fill=(255, 255, 255, 255), anchor='lm')
    im = im.resize((w, h), Image.LANCZOS); im.save(path); return w, h

def main(src, out, poster, pos='top'):
    tmp = tempfile.mkdtemp(); inputs = ['-i', src]; chains = []; last = '[base]'
    chains.append(f'[0:v]crop={W}:{H}:0:0[base]')
    for i, (a, b, text) in enumerate(CAPS):
        p = os.path.join(tmp, f'c{i}.png'); w, h = pill(text, p)
        end = min(a + CAP_HOLD, b - 0.15)
        inputs += ['-framerate', '30', '-loop', '1', '-t', '80', '-i', p]
        y = 1086 if pos == 'bottom' else 12
        chains.append(f'[{i + 1}:v]format=rgba,fade=t=in:st={a}:d={FADE_IN}:alpha=1,fade=t=out:st={end:.2f}:d={FADE_OUT}:alpha=1[c{i}]')
        chains.append(f'{last}[c{i}]overlay=x=(W-w)/2:y={y}:enable=\'between(t,{a},{end + FADE_OUT:.2f})\'[o{i}]'); last = f'[o{i}]'
    dur = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', src], capture_output=True, text=True).stdout.strip()
    cmd = ['ffmpeg', '-y', '-v', 'error', *inputs, '-filter_complex', ';'.join(chains), '-map', last, '-c:v', 'libx264', '-preset', 'slow', '-crf', '25',
           '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-an', '-t', dur, out]
    subprocess.run(cmd, check=True)
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', '0', '-i', out, '-frames:v', '1', '-vf', 'scale=800:-2', '-q:v', '3', poster], check=True)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else 'bottom')
