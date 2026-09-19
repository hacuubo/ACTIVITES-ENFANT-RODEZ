#!/usr/bin/env python3
"""Génère les icônes PNG (ballon souriant) sans dépendance externe."""
import math, struct, zlib, pathlib

def png(width, height, pixels):
    raw = b''.join(b'\x00' + bytes(pixels[y]) for y in range(height))
    def chunk(tag, data):
        c = struct.pack('>I', len(data)) + tag + data
        return c + struct.pack('>I', zlib.crc32(tag + data) & 0xffffffff)
    return (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(raw, 9)) + chunk(b'IEND', b''))

def render(size, maskable=False):
    bg, sun, ink = (255, 122, 89), (255, 209, 102), (43, 33, 64)
    s = size / 512.0
    radius = 0 if maskable else 110 * s
    rows = []
    for y in range(size):
        row = []
        for x in range(size):
            # fond arrondi
            dx = max(radius - x, 0, x - (size - 1 - radius)); dy = max(radius - y, 0, y - (size - 1 - radius))
            inside = (dx * dx + dy * dy) <= radius * radius
            if not inside:
                row += [0, 0, 0, 0]; continue
            col = bg
            cx, cy = 256 * s, 236 * s
            if (x - cx) ** 2 + (y - cy) ** 2 <= (118 * s) ** 2: col = sun
            for ex in (214, 298):
                if (x - ex * s) ** 2 + (y - 222 * s) ** 2 <= (14 * s) ** 2: col = ink
            # sourire : arc
            t = (x - 200 * s) / (112 * s)
            if 0 <= t <= 1:
                yy = 272 * s + math.sin(t * math.pi) * 42 * s
                if abs(y - yy) <= 8 * s: col = ink
            # ficelle
            if abs(x - 256 * s) <= 6 * s and 354 * s <= y <= 430 * s: col = ink
            row += [col[0], col[1], col[2], 255]
        rows.append(row)
    return png(size, size, rows)

out = pathlib.Path(__file__).resolve().parent.parent / 'icons'
out.mkdir(exist_ok=True)
for n in (180, 192, 512):
    (out / f'icon-{n}.png').write_bytes(render(n))
(out / 'icon-maskable-512.png').write_bytes(render(512, maskable=True))
print('icons ok')
