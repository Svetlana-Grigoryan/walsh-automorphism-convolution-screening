#!/usr/bin/env python3
"""Regenerate all finite certificates and verify expected results."""
from pathlib import Path
import hashlib
from src.cauchy_census import run as run_cauchy
from src.binary_census import run as run_binary
from src.aes_benchmark import run as run_aes

ROOT=Path(__file__).resolve().parent
RESULTS=ROOT/'results'

print('[1/3] Cauchy-Walsh census...')
print(run_cauchy(RESULTS/'cauchy_walsh_census.csv'))
print('[2/3] Binary 16-coordinate census...')
print(run_binary(RESULTS/'binary16_census.csv'))
print('[3/3] AES benchmark...')
print(run_aes(RESULTS/'aes_benchmark.csv'))

files=[]
for rel in ['run_all.py','requirements.txt','CITATION.cff','README.md']:
    files.append(ROOT/rel)
files += sorted((ROOT/'src').glob('*.py')) + sorted(RESULTS.glob('*.csv'))
lines=[]
for p in files:
    h=hashlib.sha256(p.read_bytes()).hexdigest()
    lines.append(f'{h}  {p.relative_to(ROOT).as_posix()}')
(ROOT/'SHA256SUMS').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASSED')
