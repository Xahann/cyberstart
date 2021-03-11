retep@desktop:~/ctf/cyberstart/level9/9$ ls | xargs file
challenge-bearwatch-pic-01.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 72x72, segment length 16, progressive, precision 8, 1000x660, components 3
challenge-bearwatch-pic-02.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 72x72, segment length 16, progressive, precision 8, 1000x750, components 3
challenge-bearwatch-pic-03.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 72x72, segment length 16, progressive, precision 8, 1000x750, components 3
challenge-bearwatch-pic-04.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 72x72, segment length 16, progressive, precision 8, 1000x680, components 3
challenge-bearwatch-pic-05.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 72x72, segment length 16, progressive, precision 8, 1000x630, components 3
challenge-bearwatch-pic-06.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 72x72, segment length 16, Exif Standard: [TIFF image data, big-endian, direntries=1], progressive, precision 8, 1000x750, components 3
challenge-bearwatch-pic-07.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 72x72, segment length 16, progressive, precision 8, 1000x1020, components 3
challenge-bearwatch-pic-08.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 72x72, segment length 16, progressive, precision 8, 1000x660, components 3


binwalk --dd=".*" challenge-bearwalk-pic-06.jpg

ran executable found in zip of binwalk
