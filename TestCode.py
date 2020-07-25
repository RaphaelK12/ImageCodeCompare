import os
from CmdLine import JPEG, JPEG2000, WebP, BPG

if __name__ == '__main__':
    bmpfile = 'testout.bmp'
    pngfile = 'net.png'

    jp2file = 'duankong_demo1.jp2'
    jpgfile = "duankong_demo1.jpg"
    webpfile = "duankong_webp.webp"
    bpgfile = "duankong-bpg.bpg"

    decodejp2 = "decode_jp2.bmp"
    decodejpg = "decode_jpg.bmp"
    decodewebp = "decode_webp.png"
    decodebpg = "decode_bpg.png"

    verbose = 1
    # JPEG
    # jpeg = JPEG()
    # jpeg.code_image(input=bmpfile, output=jpgfile)
    # jpeg.decode_image(input=jpgfile, output=decodejpg)
    # JPEG2000
    # code = JPEG2000()
    # code.code_image(input=bmpfile, output=jp2file)
    # code.decode_image(input=jp2file, output=decodejp2)
    # WebP
    # webp = WebP()
    # webp.code_image(input=pngfile, output=webpfile, verbose=verbose)
    # webp.decode_image(input=webpfile, output=decodewebp, verbose=verbose)
    # BPG
    bpg = BPG()
    bpg.code_image(input=pngfile, output=bpgfile, verbose=verbose)
    bpg.decode_image(input=bpgfile, output=decodebpg, verbose=verbose)

    print("[ ] Doen !")
