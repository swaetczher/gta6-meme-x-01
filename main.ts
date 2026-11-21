// gta6-meme-x-01 ronde 2 — ferry: copies POST.json into the output directory.
// The entry's only program job: hand the post's address to the harness.
// Deterministic by construction: no network, no clock, no randomness, no
// transformation of the bytes — the output file is the input file, so two
// runs in a row produce byte-identical output.
import { copyFileSync, existsSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? ".";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "out";

const source = join(botDir, "POST.json");
const target = join(outDir, "POST.json");

if (!existsSync(source)) {
  throw new Error(`POST.json not found in ${botDir}`);
}

// Fail fast on a malformed address file instead of ferrying garbage: the
// entry must name a post, so POST.json has to parse as an object carrying
// one string url. The check reads only; the bytes copied below are untouched.
const parsed: unknown = JSON.parse(readFileSync(source, "utf8"));
if (
  typeof parsed !== "object" ||
  parsed === null ||
  typeof (parsed as { url?: unknown }).url !== "string"
) {
  throw new Error("POST.json must be an object with a string url");
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);
console.log(`copied ${source} -> ${target}`);
