import json
from pathlib import Path

ns = {}
exec(Path('ai_engine.py').read_text(encoding='utf-8'), ns)

samples = [
    '{"module":"notes","action":"add","data":{"text":"Buy milk"},"reply":"Note saved!"}',
    'Sure — {"module":"notes","action":"add","data":{"text":"Buy milk"},"reply":"Note saved!"} extra',
    '```json\n{"module":"notes","action":"add","data":{"text":"Buy milk"},"reply":"Note saved!"}\n```',
    '{"module":"reminder","action":"add","data":{"task":"call Mom","time":"17:00"},"reply":"Reminder set for 5 PM!"}'
]

for raw in samples:
    obj = json.loads(ns['extract_json_object'](raw))
    normalized = ns['normalize_result'](obj)
    print(raw)
    print(normalized)
    print('---')
