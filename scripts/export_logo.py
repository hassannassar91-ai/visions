"""One-off export of Visions Tech logo assets from brand PDF."""
import fitz
from PIL import Image, ImageChops
from pathlib import Path

PDF = Path(
    r"c:\Users\Fujitsu\AppData\Roaming\Cursor\User\workspaceStorage"
    r"\1cbdb3c2c102828f9c3e7a78c4c0384a\pdfs"
    r"\c353170c-622d-4983-88e3-b96f23e5480a\Visions_Tech_A4_White_Background.pdf"
)
OUT = Path(__file__).resolve().parents[1] / "website" / "static" / "website" / "images"


def trim(im: Image.Image) -> Image.Image:
    bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
    bbox = ImageChops.difference(im, bg).getbbox()
    return im.crop(bbox) if bbox else im


def white_transparent(img: Image.Image, threshold: int = 242) -> Image.Image:
    px = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = px[x, y]
            if r >= threshold and g >= threshold and b >= threshold:
                px[x, y] = (255, 255, 255, 0)
    return img


def export(clip, dest: Path) -> None:
    doc = fitz.open(PDF)
    page = doc[0]
    pix = page.get_pixmap(matrix=fitz.Matrix(4, 4), clip=clip, alpha=False)
    raw = OUT / "_tmp_logo.png"
    pix.save(raw)
    doc.close()
    img = white_transparent(trim(Image.open(raw).convert("RGBA")))
    img.save(dest, optimize=True)
    raw.unlink(missing_ok=True)
    print(dest.name, img.size)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    export(fitz.Rect(28, 148, 720, 258), OUT / "visions-tech-logo.png")
    export(fitz.Rect(28, 150, 178, 242), OUT / "visions-tech-icon.png")
