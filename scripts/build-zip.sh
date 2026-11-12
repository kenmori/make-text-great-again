#!/usr/bin/env bash
# Build make-text-great-again.zip for upload to claude.ai (Customize > Skills).
# The archive holds one folder named after the skill, with SKILL.md inside it.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
out="${1:-$root/dist/make-text-great-again.zip}"
name="make-text-great-again"
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

mkdir -p "$work/$name" "$(dirname "$out")"
cp "$root/SKILL.md" "$root/LICENSE" "$work/$name/"
cp -R "$root/references" "$root/examples" "$root/tests" "$work/$name/"

rm -f "$out"
(cd "$work" && zip -q -r -X "$out" "$name")
echo "Built $out"
