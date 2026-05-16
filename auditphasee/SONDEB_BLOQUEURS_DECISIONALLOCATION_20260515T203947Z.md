# SONDE B BLOQUEURS DECISIONALLOCATION

Date UTC: 2026-05-15T20:39:47.720696+00:00

## Doctrine
- Lecture pure.
- Aucun import métier.
- Aucun patch.
- Aucun cron/systemd/restart.
- Aucun ordre réel.
- Sorties seulement auditphasee.

## Verdicts
### aplomb.py
- verdict_sonde_b: WRITE_LEGACY_REEL_OU_PROBABLE
- parse_ok: true
- main_guard: true
- functions: load_mondes_state;load_m2_state;evaluate_aplomb
- write_hits: L72:with open(STATE_FILE, 'w') as f: || L73:json.dump(state, f, indent=2)
- real_hits: 
- legacy_state_hits: L11:STATE_FILE = BASE_DIR / "aplomb_state.json" || L16:# Exemple : mondes_paralleles_state.json || L17:bull_file = BASE_DIR / "mondes_paralleles_state.json"
- v1_hits: 

### demo/generator/decision_to_order.py
- verdict_sonde_b: RISQUE_REEL_A_ISOLER
- parse_ok: true
- main_guard: true
- functions: utc_iso;utc_compact;log_event;read_json;write_json_atomic;decision_hash;main
- write_hits: L74:with LOG_PATH.open("a", encoding="utf-8") as f: || L75:f.write(json.dumps(rec, ensure_ascii=False) + "\n") || L83:with tmp.open("w", encoding="utf-8") as f: || L84:json.dump(payload, f, ensure_ascii=False, indent=2)
- real_hits: L37:- aucun secret lu/écrit
- legacy_state_hits: L6:A7 V0 — Générateur d'ordres demo depuis MM position_nette + state.json.prix. || L15:1. Vérifie state.json + money_manager_state.json existent || L17:3. Lit state.json.prix (LIVE, clé canonique FR) || L20:6. Compare avec hash précédent dans demo/states/decision_to_order_state.json || L33:- lecture seule sur state.json + money_manager_state.json || L53:STATE_PATH    = ROOT / "state.json" || L54:MM_STATE_PATH = ROOT / "money_manager_state.json" || L58:HASH_STATE    = STATES_DIR / "decision_to_order_state.json"
- v1_hits: 

### demo/prudence/prudence_demo.py
- verdict_sonde_b: RISQUE_REEL_A_ISOLER
- parse_ok: true
- main_guard: true
- functions: now;read_json;write_json;mode_ok;block_reason;main
- write_hits: L27:Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8") || L125:with (LOGS / "prudence_demo.log").open("a", encoding="utf-8") as f: || L126:f.write(json.dumps(state, ensure_ascii=False) + "\n")
- real_hits: L18:FORBIDDEN_KEYS = {"api_key", "secret", "passphrase", "credential", "credentials", "exchange_target", "broker_real", "real_broker"}
- legacy_state_hits: L15:PRUDENCE_STATE = STATES / "prudence_demo_state.json"
- v1_hits: 

### demo/reports/RACCORDEMENT_CHAINE_REELLE_VERS_DEMO_20260507_211559/grep_ordre_execution_broker_head2000.txt
- verdict_sonde_b: RISQUE_REEL_A_ISOLER
- parse_ok: false
- main_guard: false
- functions: 
- write_hits: 
- real_hits: L730:./audit/packs/PACK_REPRISE_SERAGONE_DAY5.md:290:Le chemin réel OKX (bridge_execution → ccxt → OKX) reste FERMÉ. || L733:./audit/packs/PACK_REPRISE_SERAGONE_DAY5.md:300:- Pas d'appel réel à ccxt.create_order. || L830:./audit/mode_demo_meta_audit_20260507_201721/MODE_DEMO_META_AUDIT_20260507_201721.md:285:- functions: utcnow, iso_utc, read_json_safe, save_json_atomic, setup_logging, safe_float, clamp01, norm_key, normalize_row_keys, pick_first, append_hi || L831:./audit/sentinelle_exchange_readonly_confirmed_20260507_201149/SENTINELLE_EXCHANGE_READONLY_CONFIRMED_20260507_201149.md:15:- Aucun create_order détecté. || L924:./audit/decisions/phase_e_decisions_NOTES.md:276:- Découverte 18 : bridge_execution.py est le bras armé OKX (ccxt). || L1132:./audit/decisions/phase_e_decisions_NOTES.md:7471:- ccxt.create_order réel || L1192:./audit/decisions/phase_e_decisions_NOTES.md:8150:  dépenda
- legacy_state_hits: L307:./audit/modulesregistry_v0_manual/modulesregistry_candidate_v0.json:14881:        "/home/ubuntu/seragone/state/prudence_state.json" || L323:./audit/modulesregistry_v0_manual/modulesregistry_candidate_v0.json:17733:        "policy_state.json", || L337:./audit/modulesregistry_v0_manual/modulesregistry_candidate_v0.json:20555:        "policy_state.json", || L346:./audit/modulesregistry_v0_manual/modulesregistry_candidate_v0.json:20669:        "policy_state.json", || L365:./audit/modulesregistry_v0_manual/modulesregistry_candidate_v0.json:21677:        "/home/ubuntu/seragone/state/prudence_state.json" || L416:./audit/modulesregistry_v0_manual/modulesregistry_candidate_v0.json:31689:        "/home/ubuntu/seragone/state/prudence_state.json" || L432:./audit/modulesregistry_v0_manual/modulesregistry_candidate_v0.json:34541:        "policy_state.json", || L465:./audit/modulesregistry_v0_manu
- v1_hits: 

### doubletempo.py
- verdict_sonde_b: WRITE_LEGACY_REEL_OU_PROBABLE
- parse_ok: true
- main_guard: false
- functions: _now_iso;_load_state;_save_state;get_tempo_budgets
- write_hits: L54:with open(STATE_FILE, "w", encoding="utf-8") as f: || L55:json.dump(state, f, indent=2, ensure_ascii=False)
- real_hits: 
- legacy_state_hits: L9:STATE_FILE = BASE_DIR / "states" / "doubletempostate.json"
- v1_hits: 

### money_manager.py
- verdict_sonde_b: RISQUE_REEL_A_ISOLER
- parse_ok: true
- main_guard: true
- functions: read_json;get_aplomb_permission;get_tireur_direction;get_etincelle_state;get_brisance_active;get_v9_bear;calculer_positions_tireurs;sommer_avec_cap_progressif;compenser_books;appliquer_gardes_fous;load_clones_state;load_m4_state;load_m5_state;main
- write_hits: L659:with open(STATE_OUT, "w", encoding="utf-8") as f: || L660:json.dump(state, f, indent=2, default=str, ensure_ascii=False)
- real_hits: L398:"Exchange", "CASH — Binance instable ou retraits suspendus",
- legacy_state_hits: L27:STATE_OUT = BASE / "money_manager_state.json" || L88:"Aplomb": BASE / "aplombdailystate.json", || L89:"Presence": BASE / "presence1hstate.json", || L90:"Tenue": BASE / "tenue30mstate.json", || L91:"Vigie": BASE / "vigie15mstate.json", || L92:"Agilite": BASE / "tireurs_agilite_5m_state.json", || L93:"Precision": BASE / "tireurs_minute_state.json", || L94:"Fulgurance": BASE / "fulgurance_state.json", || L95:"Etincelle": BASE / "etincellestate.json", || L99:BRISANCE_STATE = BASE / "brisance_state.json" || L100:ETINCELLE_STATE = BASE / "etincellestate.json" || L128:BASE / "aplombdailystate.json", || L129:BASE / "aplombdailystate.json", || L130:BASE / "aplombstate.json", || L393:ex = json.load(open(BASE / "sentinelle_exchange_state.json", "r", encoding="utf-8")) || L439:f = BASE / "clones_v6_state.json" || L450:f = BASE / "states" / "ours_v2_state.json" || L465:f = BASE / "states" / "grap
- v1_hits: 

### money_manager_perplexity_97L.py
- verdict_sonde_b: WRITE_LEGACY_REEL_OU_PROBABLE
- parse_ok: true
- main_guard: true
- functions: load_aplomb_state;load_m3_state;load_m8_state;get_capital_total;run_money_manager
- write_hits: L91:with open(STATE_FILE, 'w') as f: || L92:json.dump(state, f, indent=2)
- real_hits: 
- legacy_state_hits: L14:STATE_FILE = BASE_DIR / "money_manager_state.json" || L17:f = BASE_DIR / "aplomb_state.json" || L24:f = BASE_DIR / "moteurs" / "m3_temperance_state.json" || L31:f = BASE_DIR / "moteurs" / "m8_tresorerie_state.json"
- v1_hits: 

### prudence_module.py
- verdict_sonde_b: WRITE_LEGACY_REEL_OU_PROBABLE
- parse_ok: true
- main_guard: true
- functions: prudence_parle;compter_convergence;ecrire_etat;log_ligne;main
- write_hits: L148:with open(path, 'w') as f: || L149:json.dump(etat, f, indent=2) || L155:with open(path, 'a') as f: || L156:f.write(f"{datetime.now().isoformat()} | {message}\n")
- real_hits: 
- legacy_state_hits: L52:STATE_PATH = '/home/ubuntu/seragone/state/prudence_state.json' || L139:# ÉCRITURE D'ÉTAT (lu par le chef via prudence_state.json)
- v1_hits: 

### tireur_aplomb.py
- verdict_sonde_b: WRITE_LEGACY_REEL_OU_PROBABLE
- parse_ok: true
- main_guard: true
- functions: load_json;load_first;infer_aplomb_input;decide_local;canonical_permission;save_policy_state_local;append_signal_log_local;main
- write_hits: L217:with open(POLICY_STATE_FILE, "w", encoding="utf-8") as f: || L218:json.dump(state, f, indent=2, ensure_ascii=False) || L233:with open(SIGNAL_LOG_FILE, "a", encoding="utf-8") as f: || L234:f.write(json.dumps(entry, ensure_ascii=False) + "\n") || L310:with open(out_file, "w", encoding="utf-8") as f: || L311:json.dump(state, f, indent=2, ensure_ascii=False) || L313:with open(POLICY_MONITOR_FILE, "w", encoding="utf-8") as f: || L314:json.dump(
- real_hits: 
- legacy_state_hits: L28:APL_STATE_FILE = BASE_DIR / "aplombstate.json" || L29:APL_DAILY_STATE_FILE = BASE_DIR / "aplombdailystate.json" || L30:POLICY_STATE_FILE = STATES_DIR / "policy_state.json" || L38:BASE_DIR / "mondesparallelesstate.json", || L39:BASE_DIR / "mondes_paralleles_state.json", || L46:BASE_DIR / "m2bearstate.json",
- v1_hits: 

## Décision
- Aucun branchement autorisé par cette sonde.
- Les fichiers RISQUE_REEL_A_ISOLER sont exclus de la démo.
- Les fichiers WRITE_LEGACY_REEL_OU_PROBABLE exigent wrapper pur ou exclusion.
- Les fichiers WRAPPER_POSSIBLE_LECTURE_PURE peuvent être proposés dans un décret séparé, après relecture.