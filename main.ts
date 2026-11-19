// gta6-meme-x-01 — entry program (Node 22, standard library only).
//
// The judged artifact is the X post named in POST.json, not this program:
// the program only ferries the post's address to the grader, reading
// POST.json from the repository root and writing it out byte for byte.
// It touches no clock and no network, so its two grading runs agree.
//
// A ferry, not a factory: the joke lives in the picture on X, and this file
// only carries the picture's address. Keeping the ferry to one read and one
// write is what makes the two grading runs land on identical bytes.
//
// Run locally:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

function readPost(path: string): Buffer {
  try {
    return readFileSync(path);
  } catch (err) {
    console.error(`cannot read ${path}: ${(err as Error).message}`);
    process.exit(1);
  }
}

mkdirSync(OUTPUT_DIR, { recursive: true });
const post = readPost(join(BOT_DIR, "POST.json"));
writeFileSync(join(OUTPUT_DIR, "POST.json"), post);
