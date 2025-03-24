### FFmpeg Command Explanation

#### Command:
```
ffmpeg -i aspect43.mp4 -vf "scale=-1:720, pad=1280:720:(1280-iw)/2:0" output.mp4
```

#### Breakdown:
1. **`-i aspect43.mp4`**: Specifies the input file (`aspect43.mp4`).
2. **`-vf "scale=-1:720, pad=1280:720:(1280-iw)/2:0"`**:
   - `scale=-1:720`:
     - This resizes the video to a height of 720 pixels while preserving the aspect ratio.
     - `-1` tells FFmpeg to automatically calculate the width to maintain the original aspect ratio.
   - `pad=1280:720:(1280-iw)/2:0`:
     - This ensures the final video has a resolution of `1280x720` by adding padding if necessary.
     - `1280:720` sets the target width and height.
     - `(1280-iw)/2` horizontally centers the video by calculating the left padding based on the input width (`iw`).
     - `0` ensures no vertical padding is added.
3. **`output.mp4`**: Specifies the output file.

#### Purpose:
- This command is useful when converting a `4:3` aspect ratio video to `16:9` without distortion.
- It ensures the video is properly scaled to fit within `1280x720`, maintaining its original aspect ratio and adding black bars as needed.

#### Sample Output Metadata:
- Video is converted from `480x352` (4:3 aspect ratio) to `1280x720` with padding.
- Encoded using H.264 (`libx264`).
- Audio remains AAC at `22050 Hz, stereo`.
- Resulting bitrate: ~1222.8 kbps.

This command helps standardize video dimensions for platforms requiring `16:9` formats without stretching or cropping.


### Result of running the command:

**`➜ ffmpeg -i aspect43.mp4 -vf "scale=-1:720, pad=1280:720:(1280-iw)/2:0" output.mp4`**
<div style="max-height: 300px; overflow-y: auto;">
  <pre>

ffmpeg version 7.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 16.0.0 (clang-1600.0.26.4)
  configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/7.1_3 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
  libavutil      59. 39.100 / 59. 39.100
  libavcodec     61. 19.100 / 61. 19.100
  libavformat    61.  7.100 / 61.  7.100
  libavdevice    61.  3.100 / 61.  3.100
  libavfilter    10.  4.100 / 10.  4.100
  libswscale      8.  3.100 /  8.  3.100
  libswresample   5.  3.100 /  5.  3.100
  libpostproc    58.  3.100 / 58.  3.100
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'aspect43.mp4':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    encoder         : Lavf57.83.100
  Duration: 00:01:00.04, start: 0.000000, bitrate: 468 kb/s
  Stream #0:0[0x1](und): Video: h264 (Constrained Baseline) (avc1 / 0x31637661), yuv420p(progressive), 480x352 [SAR 44:45 DAR 4:3], 400 kb/s, 25 fps, 25 tbr, 90k tbn (default)
      Metadata:
        handler_name    : VideoHandler
        vendor_id       : [0][0][0][0]
  Stream #0:1[0x2](und): Audio: aac (LC) (mp4a / 0x6134706D), 22050 Hz, stereo, fltp, 64 kb/s (default)
      Metadata:
        handler_name    : SoundHandler
        vendor_id       : [0][0][0][0]
Stream mapping:
  Stream #0:0 -> #0:0 (h264 (native) -> h264 (libx264))
  Stream #0:1 -> #0:1 (aac (native) -> aac (native))
Press [q] to stop, [?] for help
[libx264 @ 0x14f00dca0] using SAR=480/491
[libx264 @ 0x14f00dca0] using cpu capabilities: ARMv8 NEON
[libx264 @ 0x14f00dca0] profile High, level 3.1, 4:2:0, 8-bit
[libx264 @ 0x14f00dca0] 264 - core 164 r3108 31e19f9 - H.264/MPEG-4 AVC codec - Copyleft 2003-2023 - http://www.videolan.org/x264.html - options: cabac=1 ref=3 deblock=1:0:0 analyse=0x3:0x113 me=hex subme=7 psy=1 psy_rd=1.00:0.00 mixed_ref=1 me_range=16 chroma_me=1 trellis=1 8x8dct=1 cqm=0 deadzone=21,11 fast_pskip=1 chroma_qp_offset=-2 threads=18 lookahead_threads=3 sliced_threads=0 nr=0 decimate=1 interlaced=0 bluray_compat=0 constrained_intra=0 bframes=3 b_pyramid=2 b_adapt=1 b_bias=0 direct=1 weightb=1 open_gop=0 weightp=2 keyint=250 keyint_min=25 scenecut=40 intra_refresh=0 rc_lookahead=40 rc=crf mbtree=1 crf=23.0 qcomp=0.60 qpmin=0 qpmax=69 qpstep=4 ip_ratio=1.40 aq=1:1.00
Output #0, mp4, to 'output.mp4':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    encoder         : Lavf61.7.100
  Stream #0:0(und): Video: h264 (avc1 / 0x31637661), yuv420p(tv, progressive), 1280x720 [SAR 480:491 DAR 2560:1473], q=2-31, 25 fps, 12800 tbn (default)
      Metadata:
        handler_name    : VideoHandler
        vendor_id       : [0][0][0][0]
        encoder         : Lavc61.19.100 libx264
      Side data:
        cpb: bitrate max/min/avg: 0/0/0 buffer size: 0 vbv_delay: N/A
  Stream #0:1(und): Audio: aac (LC) (mp4a / 0x6134706D), 22050 Hz, stereo, fltp, 128 kb/s (default)
      Metadata:
        handler_name    : SoundHandler
        vendor_id       : [0][0][0][0]
        encoder         : Lavc61.19.100 aac
[out#0/mp4 @ 0x600003884000] video:8040KiB audio:856KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: 0.432411%
frame= 1501 fps=248 q=-1.0 Lsize=    8935KiB time=00:00:59.86 bitrate=1222.8kbits/s speed=9.88x
[libx264 @ 0x14f00dca0] frame I:19    Avg QP:20.15  size: 22799
[libx264 @ 0x14f00dca0] frame P:450   Avg QP:22.54  size: 11192
[libx264 @ 0x14f00dca0] frame B:1032  Avg QP:25.86  size:  2678
[libx264 @ 0x14f00dca0] consecutive B-frames:  6.9%  2.4%  6.0% 84.7%
[libx264 @ 0x14f00dca0] mb I  I16..4: 11.9% 81.6%  6.4%
[libx264 @ 0x14f00dca0] mb P  I16..4:  2.4%  9.0%  0.5%  P16..4: 28.8% 13.3%  4.6%  0.0%  0.0%    skip:41.4%
[libx264 @ 0x14f00dca0] mb B  I16..4:  0.2%  0.4%  0.0%  B16..8: 29.8%  2.8%  0.4%  direct: 0.8%  skip:65.6%  L0:45.7% L1:50.2% BI: 4.1%
[libx264 @ 0x14f00dca0] 8x8 transform intra:76.5% inter:85.4%
[libx264 @ 0x14f00dca0] coded y,uvDC,uvAC intra: 46.3% 0.5% 0.0% inter: 9.2% 0.1% 0.0%
[libx264 @ 0x14f00dca0] i16 v,h,dc,p: 40% 22%  5% 33%
[libx264 @ 0x14f00dca0] i8 v,h,dc,ddl,ddr,vr,hd,vl,hu: 32% 15% 21%  3%  6%  7%  5%  5%  5%
[libx264 @ 0x14f00dca0] i4 v,h,dc,ddl,ddr,vr,hd,vl,hu: 31% 19% 13%  4%  8%  9%  7%  5%  4%
[libx264 @ 0x14f00dca0] i8c dc,h,v,p: 98%  1%  1%  0%
[libx264 @ 0x14f00dca0] Weighted P-Frames: Y:13.1% UV:0.4%
[libx264 @ 0x14f00dca0] ref P L0: 62.0% 12.8% 19.3%  5.2%  0.6%
[libx264 @ 0x14f00dca0] ref B L0: 91.2%  7.4%  1.4%
[libx264 @ 0x14f00dca0] ref B L1: 97.5%  2.5%
[libx264 @ 0x14f00dca0] kb/s:1096.97
[aac @ 0x14f0670b0] Qavg: 58341.344

  </pre>
</div>

