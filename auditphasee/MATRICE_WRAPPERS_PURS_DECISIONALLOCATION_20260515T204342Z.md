# MATRICE WRAPPERS PURS DECISIONALLOCATION

Date UTC: 2026-05-15T20:43:42.595565+00:00

## Doctrine
- Lecture statique uniquement.
- Aucun import métier.
- Aucun patch runtime.
- Aucun cron, systemd, restart ou process lancé.
- Aucune finance réelle.
- Sorties limitées à auditphasee.
- Cette matrice ne décrète aucun branchement.

## Sources documentaires
- auditphasee/SONDEFROIDE_DECISIONALLOCATION_V1_20260515T203830Z.manifest.json | exists=True | sha256=5b2bec2a6fa87a493c5a007367b087db25b95a86429a9b84f21d7298114d0bcd
- auditphasee/SONDEB_BLOQUEURS_DECISIONALLOCATION_20260515T203947Z.manifest.json | exists=True | sha256=7666d86fc325368bf9e02d2648afbbeb5bd418296a3154a4c4f5b6826ed9a18e
- auditdecisions/ATTESTATION_DECISIONALLOCATION_SONDEB_BLOCAGE_DIRECT_20260515T204042Z.md | exists=True | sha256=f81cc2cc2696ff373c6a63fe138c1a669f1e2681ac3fa9e75de473cb78b4c6a6
- auditphasee/CONTRATORCHESTRATEURDEMOV12026-05-132330VALIDATED.md | exists=False | sha256=
- auditdecisions/DECRETA73SEMANTIQUENEUTRALPOSITIONDEMO2026-05-15.md | exists=True | sha256=3eefcc21f9b1250222d30339bea7f81ba01008a0d13c8df16607fd2fcc0a1961

## Verdict par rôle
### APLOMB
- expected_memory_output: aplombcontext dict typé
- expected_v1_state: aplombstatev1.json
- contract_rule: calculateur sans write aplombstate.json legacy
- status: FONCTION_PURE_CANDIDATE_MAIS_SONDE_SEPAREE_REQUISE
- next_step: sonde ciblée de la ou des fonctions pures candidates
- pure_candidates: [{"file": "tireur_aplomb.py", "functions": "infer_aplomb_input;decide_local"}]

### PRUDENCE_MEASURE
- expected_memory_output: prudencemeasure dict veto/score en MEASUREONLY
- expected_v1_state: prudencemeasurev1.json
- contract_rule: mesure seulement, ne force pas la décision finale
- status: WRAPPER_NEUF_REQUIS_AVEC_EXCLUSION_SOURCE_RISQUE
- next_step: ne pas appeler la source; rédiger wrapper neuf inerte si besoin
- pure_candidates: [{"file": "prudence_module.py", "functions": "prudence_parle"}]

### DOUBLE_TEMPO
- expected_memory_output: tempobudgets dict consultatif
- expected_v1_state: pas de state dédié sans amendement
- contract_rule: budgets consultatifs, ne décide jamais la direction
- status: FONCTION_PURE_CANDIDATE_MAIS_SONDE_SEPAREE_REQUISE
- next_step: sonde ciblée de la ou des fonctions pures candidates
- pure_candidates: [{"file": "doubletempo.py", "functions": "get_tempo_budgets"}]

### POLICY_ENGINE
- expected_memory_output: policydecision dict action/sizing/raison
- expected_v1_state: policystatev1.json
- contract_rule: souveraineté décisionnelle bornée, sans write legacy
- status: SOURCE_ABSENTE_WRAPPER_NEUF_PROBABLE
- next_step: wrapper neuf inerte si le rôle est indispensable
- pure_candidates: []

### ALLOCATION
- expected_memory_output: allocationstate dict démo finale
- expected_v1_state: allocationstatev1.json
- contract_rule: allocation pure ou wrapper V1 sans capital hardcodé ni chemin legacy
- status: WRAPPER_NEUF_REQUIS_AVEC_EXCLUSION_SOURCE_RISQUE
- next_step: ne pas appeler la source; rédiger wrapper neuf inerte si besoin
- pure_candidates: [{"file": "money_manager_perplexity_97L.py", "functions": "load_aplomb_state"}, {"file": "money_manager.py", "functions": "get_aplomb_permission;calculer_positions_tireurs"}]

### DECISION_TO_ORDER
- expected_memory_output: hors branchement direct tant que CLOSE/ordre non décrété
- expected_v1_state: aucun
- contract_rule: exclu du branchement direct; risque ordre/exchange à isoler
- status: EXCLUSION_DIRECTE_JUSQU_A_DECRET_SPECIFIQUE
- next_step: conserver hors orchestrateur V1
- pure_candidates: [{"file": "demo/generator/decision_to_order.py", "functions": "decision_hash"}]

### DEMO_BROKER
- expected_memory_output: broker démo isolé seulement
- expected_v1_state: aucun hors contrat séparé
- contract_rule: pas de runtime automatique, pas d'exchange réel
- status: EXCLUSION_DIRECTE_JUSQU_A_DECRET_SPECIFIQUE
- next_step: conserver hors orchestrateur V1
- pure_candidates: [{"file": "demo/prudence/prudence_demo_runner.py", "functions": "is_already_prudenced"}]

## Détail fichiers
### APLOMB | .aplomb.py
- exists: false
- verdict_matrice: ABSENT
- functions: 
- pure_function_candidates: 
- top_level_effects: 
- write_hits: 
- real_hits: 
- process_hits: 
- legacy_state_hits: 

### APLOMB | aplomb.py
- exists: true
- verdict_matrice: WRAPPER_NEUF_REQUIS_WRITE_LEGACY
- functions: load_mondes_state;load_m2_state;evaluate_aplomb
- pure_function_candidates: 
- top_level_effects: '\nAplomb - Décideur souverain de Séragone\nIntègre les signaux des mondes parallèles long ET des mondes BEAR natifs (M2)\n'
- write_hits: L72:with open(STATE_FILE, 'w') as f: || L73:json.dump(state, f, indent=2)
- real_hits: 
- process_hits: 
- legacy_state_hits: L11:STATE_FILE = BASE_DIR / "aplomb_state.json" || L16:# Exemple : mondes_paralleles_state.json || L17:bull_file = BASE_DIR / "mondes_paralleles_state.json"

### APLOMB | tireur_aplomb.py
- exists: true
- verdict_matrice: WRAPPER_NEUF_REQUIS_WRITE_LEGACY
- functions: load_json;load_first;infer_aplomb_input;decide_local;canonical_permission;save_policy_state_local;append_signal_log_local;main
- pure_function_candidates: infer_aplomb_input;decide_local
- top_level_effects: LOGS_DIR.mkdir(parents=True, exist_ok=True) || STATES_DIR.mkdir(parents=True, exist_ok=True) || log.setLevel(logging.INFO) || if_non_main
- write_hits: L13:LOGS_DIR.mkdir(parents=True, exist_ok=True) || L14:STATES_DIR.mkdir(parents=True, exist_ok=True) || L217:with open(POLICY_STATE_FILE, "w", encoding="utf-8") as f: || L218:json.dump(state, f, indent=2, ensure_ascii=False) || L233:with open(SIGNAL_LOG_FILE, "a", encoding="utf-8") as f: || L234:f.write(json.dumps(entry, ensure_ascii=False) + "\n") || L310:with open(out_file, "w", encoding="utf-8") as f: || L311:json.dump(state, f, indent=2, ensure_ascii=False) || L313:with open(POLICY_MONITOR_FILE, "w", encoding="utf-8") as f: || L314:json.dump(
- real_hits: 
- process_hits: 
- legacy_state_hits: L28:APL_STATE_FILE = BASE_DIR / "aplombstate.json" || L29:APL_DAILY_STATE_FILE = BASE_DIR / "aplombdailystate.json" || L30:POLICY_STATE_FILE = STATES_DIR / "policy_state.json" || L38:BASE_DIR / "mondesparallelesstate.json", || L39:BASE_DIR / "mondes_paralleles_state.json", || L46:BASE_DIR / "m2bearstate.json",

### APLOMB | productiondecisionaplomb.py
- exists: false
- verdict_matrice: ABSENT
- functions: 
- pure_function_candidates: 
- top_level_effects: 
- write_hits: 
- real_hits: 
- process_hits: 
- legacy_state_hits: 

### PRUDENCE_MEASURE | productionprotectionprudencemodule.py
- exists: false
- verdict_matrice: ABSENT
- functions: 
- pure_function_candidates: 
- top_level_effects: 
- write_hits: 
- real_hits: 
- process_hits: 
- legacy_state_hits: 

### PRUDENCE_MEASURE | prudence_module.py
- exists: true
- verdict_matrice: EXCLURE_PROCESS_CRON_SYSTEMD_DIRECT
- functions: prudence_parle;compter_convergence;ecrire_etat;log_ligne;main
- pure_function_candidates: prudence_parle
- top_level_effects: "\nPRUDENCE — la voix qui refuse le consensus grégaire\n====================================================\n\nÊtre de pensée du Village de Séragone.\nFigée le 19 avril 2026 suite
- write_hits: L143:Path(path).parent.mkdir(parents=True, exist_ok=True) || L148:with open(path, 'w') as f: || L149:json.dump(etat, f, indent=2) || L154:Path(path).parent.mkdir(parents=True, exist_ok=True) || L155:with open(path, 'a') as f: || L156:f.write(f"{datetime.now().isoformat()} | {message}\n")
- real_hits: 
- process_hits: L160:# POINT D'ENTRÉE CRON (suggéré à 08:11, entre chef 08:10 et communicants 08:12)
- legacy_state_hits: L52:STATE_PATH = '/home/ubuntu/seragone/state/prudence_state.json' || L139:# ÉCRITURE D'ÉTAT (lu par le chef via prudence_state.json)

### PRUDENCE_MEASURE | demo/prudence/prudence_demo.py
- exists: true
- verdict_matrice: EXCLURE_RISQUE_REEL_DIRECT
- functions: now;read_json;write_json;mode_ok;block_reason;main
- pure_function_candidates: 
- top_level_effects: 
- write_hits: L27:Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8") || L90:d.mkdir(parents=True, exist_ok=True) || L126:f.write(json.dumps(state, ensure_ascii=False) + "\n")
- real_hits: L46:def block_reason(order): || L50:if order.get("mode") != "MODE_DEMO_TOTAL": || L52:if order.get("real_finance_allowed") is not False: || L55:if k in order: || L57:if order.get("prudence_status") == "BLOCKED": || L59:if not order.get("source"): || L61:if not order.get("reason"): || L63:if not order.get("symbol"): || L65:if order.get("side") not in ALLOWED_SIDES: || L68:q = float(order.get("quantity")) || L72:p = float(order.get("price_reference")) || L75:if order.get("side") == "HOLD": || L86:print("usage: demo/prudence/prudence_demo.py demo/orders/order.json", file=sys.stderr) || L93:order = read_json(in_path) || L94:order_id = order.get("order_id") or ("NO_ORDER_ID_" + uuid.uuid4().hex[:8]) || L95:reason = block_reason(order) || L97:checked = dict(order)
- process_hits: 
- legacy_state_hits: L15:PRUDENCE_STATE = STATES / "prudence_demo_state.json"

### DOUBLE_TEMPO | productionallocationdoubletempo.py
- exists: false
- verdict_matrice: ABSENT
- functions: 
- pure_function_candidates: 
- top_level_effects: 
- write_hits: 
- real_hits: 
- process_hits: 
- legacy_state_hits: 

### DOUBLE_TEMPO | doubletempo.py
- exists: true
- verdict_matrice: WRAPPER_NEUF_REQUIS_WRITE_LEGACY
- functions: _now_iso;_load_state;_save_state;get_tempo_budgets
- pure_function_candidates: get_tempo_budgets
- top_level_effects: 
- write_hits: L52:STATE_FILE.parent.mkdir(parents=True, exist_ok=True) || L54:with open(STATE_FILE, "w", encoding="utf-8") as f: || L55:json.dump(state, f, indent=2, ensure_ascii=False)
- real_hits: 
- process_hits: 
- legacy_state_hits: L9:STATE_FILE = BASE_DIR / "states" / "doubletempostate.json"

### POLICY_ENGINE | productiondecisionpolicyengine.py
- exists: false
- verdict_matrice: ABSENT
- functions: 
- pure_function_candidates: 
- top_level_effects: 
- write_hits: 
- real_hits: 
- process_hits: 
- legacy_state_hits: 

### POLICY_ENGINE | policy_engine.py
- exists: false
- verdict_matrice: ABSENT
- functions: 
- pure_function_candidates: 
- top_level_effects: 
- write_hits: 
- real_hits: 
- process_hits: 
- legacy_state_hits: 

### POLICY_ENGINE | productionpolicyengine.py
- exists: false
- verdict_matrice: ABSENT
- functions: 
- pure_function_candidates: 
- top_level_effects: 
- write_hits: 
- real_hits: 
- process_hits: 
- legacy_state_hits: 

### ALLOCATION | productiondecisionallocationmanager.py
- exists: false
- verdict_matrice: ABSENT
- functions: 
- pure_function_candidates: 
- top_level_effects: 
- write_hits: 
- real_hits: 
- process_hits: 
- legacy_state_hits: 

### ALLOCATION | productionallocationmoneymanager.py
- exists: false
- verdict_matrice: ABSENT
- functions: 
- pure_function_candidates: 
- top_level_effects: 
- write_hits: 
- real_hits: 
- process_hits: 
- legacy_state_hits: 

### ALLOCATION | productionallocationmetacontroller.py
- exists: false
- verdict_matrice: ABSENT
- functions: 
- pure_function_candidates: 
- top_level_effects: 
- write_hits: 
- real_hits: 
- process_hits: 
- legacy_state_hits: 

### ALLOCATION | money_manager_perplexity_97L.py
- exists: true
- verdict_matrice: WRAPPER_NEUF_REQUIS_WRITE_LEGACY
- functions: load_aplomb_state;load_m3_state;load_m8_state;get_capital_total;run_money_manager
- pure_function_candidates: load_aplomb_state
- top_level_effects: '\nMoney Manager - Agrégateur final de Séragone\nIntègre M3, M8 et Double Tempo\n' || sys.path.append(str(Path(__file__).parent))
- write_hits: L91:with open(STATE_FILE, 'w') as f: || L92:json.dump(state, f, indent=2)
- real_hits: 
- process_hits: 
- legacy_state_hits: L14:STATE_FILE = BASE_DIR / "money_manager_state.json" || L17:f = BASE_DIR / "aplomb_state.json" || L24:f = BASE_DIR / "moteurs" / "m3_temperance_state.json" || L31:f = BASE_DIR / "moteurs" / "m8_tresorerie_state.json"

### ALLOCATION | money_manager.py
- exists: true
- verdict_matrice: EXCLURE_RISQUE_REEL_DIRECT
- functions: read_json;get_aplomb_permission;get_tireur_direction;get_etincelle_state;get_brisance_active;get_v9_bear;calculer_positions_tireurs;sommer_avec_cap_progressif;compenser_books;appliquer_gardes_fous;load_clones_state;load_m4_state;load_m5_state;main
- pure_function_candidates: get_aplomb_permission;calculer_positions_tireurs
- top_level_effects: "\nMONEY MANAGER SÉRAGONE\n======================\n\nApplique l'allocation capital synthétisée à partir des 4 réponses IA.\nLit les états des tireurs + V9 + Aplomb + brisance + éti || LOG_PATH.parent.mkdir(parents=True, exist_ok=True) || log.setLevel(logging.INFO) || if_non_main
- write_hits: L29:LOG_PATH.parent.mkdir(parents=True, exist_ok=True) || L659:with open(STATE_OUT, "w", encoding="utf-8") as f: || L660:json.dump(state, f, indent=2, default=str, ensure_ascii=False)
- real_hits: L398:"Exchange", "CASH — Binance instable ou retraits suspendus",
- process_hits: 
- legacy_state_hits: L27:STATE_OUT = BASE / "money_manager_state.json" || L88:"Aplomb": BASE / "aplombdailystate.json", || L89:"Presence": BASE / "presence1hstate.json", || L90:"Tenue": BASE / "tenue30mstate.json", || L91:"Vigie": BASE / "vigie15mstate.json", || L92:"Agilite": BASE / "tireurs_agilite_5m_state.json", || L93:"Precision": BASE / "tireurs_minute_state.json", || L94:"Fulgurance": BASE / "fulgurance_state.json", || L95:"Etincelle": BASE / "etincellestate.json", || L99:BRISANCE_STATE = BASE / "brisance_state.json" || L100:ETINCELLE_STATE = BASE / "etincellestate.json" || L128:BASE / "aplombdailystate.json", || L129:BASE / "aplombdailystate.json", || L130:BASE / "aplombstate.json", || L393:ex = json.load(open(BASE / "sentinelle_exchange_state.json", "r", encoding="utf-8")) || L439:f = BASE / "clones_v6_state.json" || L450:f = BASE / "states" / "ours_v2_state.json" || L465:f = BASE / "states" / "grap

### DECISION_TO_ORDER | demo/generator/decision_to_order.py
- exists: true
- verdict_matrice: EXCLURE_RISQUE_REEL_DIRECT
- functions: utc_iso;utc_compact;log_event;read_json;write_json_atomic;decision_hash;main
- pure_function_candidates: decision_hash
- top_level_effects: "\nSÉRAGONE — decision_to_order.py\n================================\nA7 V0 — Générateur d'ordres demo depuis MM position_nette + state.json.prix.\n\nSpec       : DECRET_A7 §4 (sha
- write_hits: L72:LOGS_DIR.mkdir(parents=True, exist_ok=True) || L75:f.write(json.dumps(rec, ensure_ascii=False) + "\n") || L84:json.dump(payload, f, ensure_ascii=False, indent=2) || L128:ORDERS_DIR.mkdir(parents=True, exist_ok=True) || L129:STATES_DIR.mkdir(parents=True, exist_ok=True)
- real_hits: L148:order = { || L163:write_json_atomic(order_path, order)
- process_hits: L12:Phase      : 1 (PHASE 2 cron différée par §6)
- legacy_state_hits: L6:A7 V0 — Générateur d'ordres demo depuis MM position_nette + state.json.prix. || L15:1. Vérifie state.json + money_manager_state.json existent || L17:3. Lit state.json.prix (LIVE, clé canonique FR) || L20:6. Compare avec hash précédent dans demo/states/decision_to_order_state.json || L33:- lecture seule sur state.json + money_manager_state.json || L53:STATE_PATH    = ROOT / "state.json" || L54:MM_STATE_PATH = ROOT / "money_manager_state.json" || L58:HASH_STATE    = STATES_DIR / "decision_to_order_state.json"

### DECISION_TO_ORDER | demo/orders/test_order_demo.json
- exists: true
- verdict_matrice: LECTURE_STATE_OU_FIXTURE_SEULEMENT
- functions: 
- pure_function_candidates: 
- top_level_effects: 
- write_hits: 
- real_hits: 
- process_hits: 
- legacy_state_hits: 

### DECISION_TO_ORDER | demo/orders/test_order_danger.json
- exists: true
- verdict_matrice: LECTURE_STATE_OU_FIXTURE_SEULEMENT
- functions: 
- pure_function_candidates: 
- top_level_effects: 
- write_hits: 
- real_hits: 
- process_hits: 
- legacy_state_hits: 

### DEMO_BROKER | demo/broker/demobroker.py
- exists: true
- verdict_matrice: EXCLURE_RISQUE_REEL_DIRECT
- functions: now;load_json;write_json;mode_ok;reject;validate;execute;update_state;main
- pure_function_candidates: 
- top_level_effects: 
- write_hits: L27:Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8") || L137:d.mkdir(parents=True, exist_ok=True) || L154:f.write(logline + "\n")
- real_hits: L45:def reject(order, reason): || L48:"order_id": order.get("order_id"), || L51:"symbol": order.get("symbol"), || L52:"side": order.get("side"), || L53:"quantity": order.get("quantity"), || L64:def validate(order): || L68:if order.get("mode") != "MODE_DEMO_TOTAL": || L70:if order.get("real_finance_allowed") is not False: || L73:if k in order: || L76:missing = [k for k in required if k not in order] || L79:if order.get("prudence_status") == "BLOCKED": || L81:if order.get("side") not in ALLOWED_SIDES: || L84:q = float(order.get("quantity")) || L85:p = float(order.get("price_reference")) || L92:def execute(order): || L93:side = order["side"] || L94:qty = float(order["quantity"]) || L95:price = float(order["price_reference"]) || L100:"order_id": order["order_id"], || L103:"symbol": order["symbol"], || L109:"position_after_demo": {"symbol": order["symbol"], "side": side, "quantity": qty}, || 
- process_hits: 
- legacy_state_hits: 

### DEMO_BROKER | demo/broker/demobroker_runner.py
- exists: true
- verdict_matrice: EXCLURE_PROCESS_CRON_SYSTEMD_DIRECT
- functions: now;log;main
- pure_function_candidates: 
- top_level_effects: "\ndemobroker_runner.py — Poller aval minimal V0\nScanne demo/orders/validated/ et appelle demobroker.py pour chaque ordre.\nConforme à DECRET_A6 et CONTRAT_DEMOBROKER_V0.\n\nUsage
- write_hits: L47:LOGS.mkdir(parents=True, exist_ok=True) || L51:f.write(json.dumps(line, ensure_ascii=False) + "\n") || L60:d.mkdir(parents=True, exist_ok=True)
- real_hits: 
- process_hits: L21:Phase  : PHASE 1 V_γ (création + tests, sans cron) || L26:import subprocess || L73:result = subprocess.run( || L96:except subprocess.TimeoutExpired:
- legacy_state_hits: 

### DEMO_BROKER | demo/prudence/prudence_demo_runner.py
- exists: true
- verdict_matrice: EXCLURE_RISQUE_REEL_DIRECT
- functions: utc_iso;log_event;tail;is_already_prudenced;main
- pure_function_candidates: is_already_prudenced
- top_level_effects: '\nSÉRAGONE — prudence_demo_runner.py\n===================================\nA7 V2 — Runner subprocess pour prudence_demo.py.\n\nSpec       : DECRET_A7 §5 (sha256 543dcb9b20c82b8f…)
- write_hits: L76:LOGS_DIR.mkdir(parents=True, exist_ok=True) || L79:f.write(json.dumps(rec, ensure_ascii=False) + "\n") || L113:ORDERS_DIR.mkdir(parents=True, exist_ok=True)
- real_hits: L131:order=order_path.name, || L136:order=order_path.name) || L139:order=order_path.name, error=str(e)) || L151:order=order_path.name, || L157:order=order_path.name, || L161:order=order_path.name, error=str(e)) || L167:log_event("ORPHAN_UNLINKED", order=order_path.name) || L170:order=order_path.name, error=str(e))
- process_hits: L6:A7 V2 — Runner subprocess pour prudence_demo.py. || L13:Phase      : 2 (cron PHASE 2 activable post-fix) || L19:En cron PHASE 2, prudence_demo_runner ramassait || L22:Fix V2 : Avant subprocess, lire le JSON. Si prudence_checked == True || L34:- subprocess.run([python3, prudence_demo.py, path], timeout=30) || L36:- si le fichier source reste après le subprocess (anomalie) : || L42:(rôle exclusif de prudence_demo.py invoqué en subprocess) || L52:import subprocess || L68:SUBPROCESS_TIMEOUT_S = 30 || L123:# §5.2.5 — boucle subprocess || L145:res = subprocess.run( || L148:timeout=SUBPROCESS_TIMEOUT_S, || L155:except subprocess.TimeoutExpired: || L158:timeout_s=SUBPROCESS_TIMEOUT_S)
- legacy_state_hits: 

## Décision de matrice
- Aucun branchement direct autorisé.
- Tout rôle sans fonction pure candidate exige wrapper neuf inerte ou exclusion temporaire.
- Toute fonction pure candidate exige une sonde séparée avant décret.
- Les rôles DECISION_TO_ORDER et DEMO_BROKER restent hors orchestrateur V1 sans décret spécifique.
- TARGETFLAT / CLOSETOFLAT reste HOLDREADONLY tant que la chaîne démo complète n'est pas prouvée.