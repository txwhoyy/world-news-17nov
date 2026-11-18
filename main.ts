// The World Today — a one-page newspaper front page summing up the world
// news of Tuesday 17 November 2026 (competition news-image-20261117).
//
// The front page itself is drawn by render.py (kept in this repository) and
// committed as entry.png beside this file. This program's whole job is to
// deliver those exact bytes to the grader: it copies entry.png to
// <output>/entry.png, where <output> is MAKEFUN_OUTPUT_DIR when set and
// /output otherwise. Node 22, standard library only, no network, and every
// run writes the same bytes.

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const source = new URL('./entry.png', import.meta.url);
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

// Guard the one thing that can silently ruin the entry: never deliver a
// file that is not the whole PNG we committed, or one over the gate's
// limits (a whole PNG, at most 1 MiB and 1024 by 1024 pixels).
const bytes = readFileSync(source);
const PNG_SIGNATURE = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];
if (!PNG_SIGNATURE.every((b, i) => bytes[i] === b)) {
  throw new Error('entry.png does not start with the PNG signature');
}
if (bytes.length > 1_048_576) {
  throw new Error(`entry.png is ${bytes.length} bytes, over the 1 MiB limit`);
}
const width = bytes.readUInt32BE(16); // IHDR width, after signature + chunk header
const height = bytes.readUInt32BE(20);
if (width > 1024 || height > 1024) {
  throw new Error(`entry.png is ${width}x${height}, over the 1024x1024 limit`);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, join(outDir, 'entry.png'));
console.log(`wrote entry.png (${bytes.length} bytes, ${width}x${height})`);
