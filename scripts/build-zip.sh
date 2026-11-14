#!/usr/bin/env bash
# Build make-text-great-again.zip for upload to claude.ai (Customize > Skills).
# The archive holds one folder named after the skill, containing only what the
# skill needs at run time: SKILL.md, the style guide and the license.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
out="${1:-$root/dist/make-text-great-again.zip}"
name="make-text-great-again"

# Resolve the output path before changing directory, so a relative path works.
mkdir -p "$(dirname "$out")"
out="$(cd "$(dirname "$out")" && pwd)/$(basename "$out")"

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

mkdir -p "$work/$name/references"
cp "$root/SKILL.md" "$root/LICENSE" "$work/$name/"
cp "$root/references/style-guide.md" "$work/$name/references/"

rm -f "$out"
(cd "$work" && zip -q -r -X -y "$out" "$name")
echo "Built $out"
