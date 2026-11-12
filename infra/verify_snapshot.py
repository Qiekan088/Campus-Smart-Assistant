from pathlib import Path
import hashlib
root = Path(__file__).resolve().parent.parent
manifest = root / 'implementation/evidence/ENV-0.2-files.sha256'
failures = []
for line in manifest.read_text(encoding='utf-8-sig').splitlines():
    expected, name = line.split('  ', 1)
    path = (root / name.replace('\\', '/').replace(chr(92), '/')).resolve()
    if not path.is_relative_to(root) or not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest().lower() != expected.lower():
        failures.append(name)
if failures:
    raise SystemExit('Mismatch: ' + ', '.join(failures))
print('Snapshot verified')
