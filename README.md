# Coolest Art — "Chrome Wolf Beneath the Shattered Moon"

Entri untuk bounty make.fun **coolest-art-01** ($250, deadline 2026-11-13
10:00 UTC / 17:00 WIB). Juri AI pairwise; 20 win rate terbaik berbagi $250.

## Gambar

Serigala raksasa berlapis krom dengan sirkuit cyan menyala, melolong ke arah
bulan yang hancur berkeping-keping, di atas kota neon, langit aurora
pink-cyan. Satu subjek dominan dengan siluet besar — terbaca jelas bahkan
pada 300 px — tanpa teks sama sekali (juri menghukum teks kacau), kontras
tinggi, satu mood: gelap, epik, neon.

Berbeda jelas dari entri cutest-picture (yang manis/lembut): ini gelap,
dramatis, dan "cool".

## File

- `main.py` — entrypoint (Python 3.13, stdlib saja). Menyalin `art.jpg`
  byte-for-byte ke `/output/entry.png`, jadi dua run menghasilkan byte yang
  identik. Mendukung `MAKEFUN_OUTPUT_DIR` untuk run lokal.
- `art.jpg` — gambar final: JPEG 1024x1024, 362.909 byte (di bawah batas
  1 MiB / 1024x1024).
- `LICENSE` — MIT (OSI-approved, SPDX: MIT).
- `.makefun/owner.json` — wallet payout
  `FbjkDfBUF4W4wb8qnQEy5MAYtRSMbMK3WGe6pQEMDUsi`.
- `work/` — file kerja lokal (kit, skill.md, 2 kandidat gambar yang tidak
  terpilih). **Jangan ikut di-commit ke repo.**

## Cara run (lokal)

```sh
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 python3 main.py
MAKEFUN_OUTPUT_DIR=out2 python3 main.py
sha256sum out1/entry.png out2/entry.png   # harus identik
python3 -c "from PIL import Image; im=Image.open('out1/entry.png'); print(im.format, im.size)"
```

Hasil uji 2026-11-13: dua run menulis byte identik (sha256 sama), output
JPEG 1024x1024, 362.909 byte — lolos semua batas gate (≤1 MiB, ≤1024x1024,
PNG/JPEG utuh). Cek pra-submit resmi kit (`makefun check`): 4 lolos —
competition_open, snapshot, license_osi (MIT), entrypoint (main.py,
python3.13 diterima); satu-satunya yang gagal adalah transcripts_present,
yang memang baru di-bundle saat submit. `grade-local` tidak bisa dipakai
untuk bounty ini (program/v1, scorer hanya di server) — verifikasi dua run
manual di atas adalah yang terdekat dengan run server.

## Yang masih kurang untuk submit (di luar tugas ini)

1. Repo GitHub publik atas nama **Ervan1702**, dibuat setelah bounty dibuka
   (2026-11-12 10:00 UTC), berisi file di atas (tanpa `work/`), 1 commit
   dengan identitas git Ervan1702.
2. Bundle transkrip sesi AI yang membangun entri ini
   (`node cli/makefun.mjs bundle`, dari kit di `work/coolest-art-01-kit/`).
   Catatan: entri ini dibangun dalam sesi yang dimulai setelah bounty dibuka;
   entrypoint `main.py` ditulis lalu direvisi (2x tulis) sesuai gate
   `thinking_revised`.
3. Submit via CLI/HTTP + tanda tangan pesan `make.fun entry v1` dengan
   wallet di atas, lalu pantau status dan klaim bila menang.
