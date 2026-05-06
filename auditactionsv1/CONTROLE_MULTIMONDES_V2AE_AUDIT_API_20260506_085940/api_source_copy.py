#!/usr/bin/env python3
"""
SÉRAGONE — API REST + DASHBOARD
Port 5000. Lecture seule sur les états du système.
"""
import sys
sys.path.insert(0, '/home/ubuntu/seragone')

from flask import Flask, jsonify, send_from_directory
import json, os, glob

from production.utils.config_manager import CFG

app = Flask(__name__)
BASE = CFG['paths']['base']
STATIC = os.path.join(os.path.dirname(__file__), 'static')

def load_json(name):
    fpath = os.path.join(BASE, name)
    if not os.path.exists(fpath):
        return {'erreur': f'{name} absent'}
    with open(fpath) as f:
        return json.load(f)

@app.route('/')
def index():
    return send_from_directory(STATIC, 'index.html')

@app.route('/api/state_canon')
def api_state_canon():
    return jsonify(load_json('state_canon.json'))

@app.route('/api/state')
def api_state():
    return jsonify(load_json('state.json'))

@app.route('/api/health')
def api_health():
    return jsonify(load_json('health_state.json'))

@app.route('/api/meta')
def api_meta():
    return jsonify(load_json('meta_state.json'))

@app.route('/api/drift')
def api_drift():
    return jsonify(load_json('drift_state.json'))

@app.route('/api/sniper')
def api_sniper():
    return jsonify(load_json('sniper_state.json'))

@app.route('/api/nc')
def api_nc():
    return jsonify(load_json('nc_state.json'))

@app.route('/api/resume')
def api_resume():
    s = load_json('state.json')
    h = load_json('health_state.json')
    m = load_json('meta_state.json')
    return jsonify({
        'prix': s.get('prix'),
        'geste': s.get('geste'),
        'shannon': s.get('shannon'),
        'distance': s.get('mondes', {}).get('distanceglobale'),
        'tore': s.get('tore', {}).get('signal'),
        'attestation': s.get('attestation', {}).get('n_voix'),
        'health': h.get('status'),
        'meta_mode': m.get('recommendations', {}).get('mode'),
        'timestamp': s.get('timestamp')
    })

@app.route('/api/all_states')
def api_all():
    from flask import request
    summary = str(request.args.get("summary", "")).lower() in {"1", "true", "yes"}
    states = {}
    skipped = {}
    files = sorted(set(
        glob.glob(os.path.join(BASE, '*state*.json')) +
        glob.glob(os.path.join(BASE, '*_state.json'))
    ))

    for f in files:
        name = os.path.basename(f)
        try:
            size = os.path.getsize(f)
            if size > 2_000_000:
                skipped[name] = {"reason": "too_large", "bytes": size}
                continue

            if summary:
                states[name] = {"bytes": size}
                continue

            with open(f) as fh:
                states[name] = json.load(fh)
        except Exception as e:
            skipped[name] = {"reason": "error", "error": str(e)[:200]}

    return {
        "states": states,
        "skipped": skipped,
        "summary": summary,
        "count_states": len(states),
        "count_skipped": len(skipped),
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
