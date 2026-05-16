# SONDE FROIDE DECISIONALLOCATION V1

Date UTC: 2026-05-15T20:38:31.011456+00:00

## Doctrine
- Lecture statique uniquement.
- Aucun import métier.
- Aucun patch.
- Aucun cron, systemd, restart ou process lancé.
- Aucune finance réelle.
- Sorties limitées à auditphasee.

## Verdict provisoire
- Fichiers candidats lus: 42
- Bloqueurs statiques à vérifier avant branchement: 9
- Candidats démo isolée: 4
- Candidats calculateurs/wrappers: 11

## Statuts
- CANON_OR_DOC_READONLY: 15
- CANDIDAT_CALCULATEUR_OU_WRAPPER: 11
- BLOQUER_VERIFIER_WRITE_LEGACY: 8
- CANDIDAT_DEMO_ISOLE: 4
- A_CLASSER: 3
- BLOQUER_VERIFIER_RISQUE_REEL: 1

## Rôles
- DEMO_BROKER: 11
- APLOMB: 9
- DECISION_TO_ORDER: 6
- ALLOCATION: 4
- MONEY_MANAGER: 3
- PRUDENCE_MEASURE: 3
- DOUBLE_TEMPO: 3
- POLICY_ENGINE: 2
- CANON_DOC: 1

## Tags
- DEMO_WORDS: 23
- LEGACY_WRITE_WORDS: 20
- CLOSE_WORDS: 10
- CRON_SYSTEMD: 10
- SECRET_ENV: 7
- REAL_EXCHANGE: 3
- SUBPROCESS: 3
- REAL_ORDER: 1

## Fiches
### aplomb.py
- role_guess: APLOMB
- status_guess: BLOQUER_VERIFIER_WRITE_LEGACY
- tags: LEGACY_WRITE_WORDS
- functions_top: load_mondes_state;load_m2_state;evaluate_aplomb
- states_or_paths: aplomb_state.json;m2_bear_state_v2.json;mondes_paralleles_state.json
- line_hits: L3:Aplomb - Décideur souverain de Séragone || L11:STATE_FILE = BASE_DIR / "aplomb_state.json" || L13:def load_mondes_state(): || L15:# À adapter au nom exact du fichier de state des mondes bull || L16:# Exemple : mondes_paralleles_state.json || L17:bull_file = BASE_DIR / "mondes_paralleles_state.json" || L23:def load_m2_state(): || L25:m2_file = BASE_DIR / "m2_bear_state_v2.json" || L31:def evaluate_aplomb(): || L33:bull = load_mondes_state() || L34:bear = load_m2_state() || L61:state = { || L72:with open(STATE_FILE, 'w') as f: || L73:json.dump(state, f, indent=2) || L75:print(f"Aplomb: {direction} (perm={permission:.2f})") || L76:return state || L79:evaluate_aplomb()

### aplomb_state.json
- role_guess: APLOMB
- status_guess: CANDIDAT_CALCULATEUR_OU_WRAPPER
- tags: NONE
- functions_top: 
- states_or_paths: 
- line_hits: 

### aplombdailycheckpoint.json
- role_guess: APLOMB
- status_guess: CANDIDAT_CALCULATEUR_OU_WRAPPER
- tags: NONE
- functions_top: 
- states_or_paths: 
- line_hits: L3:"enginestate": "READY", || L823:"lastenginestate": "READY"

### aplombdailyevents.jsonl
- role_guess: APLOMB
- status_guess: CANDIDAT_CALCULATEUR_OU_WRAPPER
- tags: NONE
- functions_top: 
- states_or_paths: 
- line_hits: L1:{"ts": "2026-04-22T00:41:40.164846+00:00", "engine": "APLOMBDAILYV6", "version": "6.0", "kind": "decision", "enginestate": "IDLE", "data": {"permission": "INTERDIT", "direction": "ATTENDRE", "regime": "NEUTRE", "diagnost || L2:{"ts": "2026-04-22T06:44:40.556624+00:00", "engine": "APLOMBDAILYV6", "version": "6.0", "kind": "crash", "enginestate": "CRASH", "data": {"error": "name 'STATEINGARDIEN' is not defined"}} || L3:{"ts": "2026-04-22T06:45:39.624906+00:00", "engine": "APLOMBDAILYV6", "version": "6.0", "kind": "crash", "enginestate": "CRASH", "data": {"error": "name 'cq' is not defined"}} || L4:{"ts": "2026-04-22T06:46:46.173374+00:00", "engine": "APLOMBDAILYV6", "version": "6.0", "kind": "crash", "enginestate": "CRASH", "data": {"error": "name 'chaines_voix' is not defined"}} || L5:{"ts": "2026-04-22T06:47:49.828236+00:00", "engine": "APLOMBDAILYV6", "version": "6.0", "kind": "crash

### aplombdailyheartbeat.json
- role_guess: APLOMB
- status_guess: CANDIDAT_CALCULATEUR_OU_WRAPPER
- tags: NONE
- functions_top: 
- states_or_paths: 
- line_hits: L4:"engine": "APLOMBDAILYV6", || L8:"state": "READY", || L9:"lastenginestate": "READY",

### aplombdailypersist.json
- role_guess: APLOMB
- status_guess: CANDIDAT_CALCULATEUR_OU_WRAPPER
- tags: NONE
- functions_top: 
- states_or_paths: 
- line_hits: L820:"lastenginestate": "READY"

### aplombdailystate.json
- role_guess: APLOMB
- status_guess: CANDIDAT_CALCULATEUR_OU_WRAPPER
- tags: NONE
- functions_top: 
- states_or_paths: 
- line_hits: L3:"module": "aplomb", || L4:"source": "canonical_engine_aplomb", || L22:"bull_state": { || L3177:"bear_state": {

### aplombstate.json
- role_guess: APLOMB
- status_guess: CANDIDAT_CALCULATEUR_OU_WRAPPER
- tags: NONE
- functions_top: 
- states_or_paths: 
- line_hits: L3:"module": "aplomb", || L4:"source": "canonical_engine_aplomb", || L22:"bull_state": { || L3177:"bear_state": {

### auditdecisions/ATTESTATIONA73PNLLATENTPOSITIONDEMONONCLOSE2026-05-15.md
- role_guess: DECISION_TO_ORDER
- status_guess: CANON_OR_DOC_READONLY
- tags: LEGACY_WRITE_WORDS;DEMO_WORDS;CLOSE_WORDS
- functions_top: 
- states_or_paths: state.json
- line_hits: L1:# ATTESTATION A7.3 — PNL LATENT POSITION DEMO NON CLOSE — 2026-05-15 || L9:- Prix spot `state.json` : 79105.64 || L10:- Exécutions `FILLED_DEMO` reconnues : 89 || L13:- Position nette ledger demo : -0.081 BTC SHORT || L15:- Frais demo cumulés : 3.62022253 USD || L18:- Money Manager actuel : NEUTRAL finale 0.0 || L23:POSITION DEMO NON CLOSE. || L24:LEDGER DEMO SHORT OUVERT ALORS QUE CIBLE MONEY MANAGER EST FLAT. || L29:La divergence canonique est : cible Money Manager flat / ledger demo short ouvert. || L35:- Aucun patch `decisiontoorder.py`. || L36:- Aucun patch `demobroker.py`. || L42:Décréter la sémantique `NEUTRAL => HOLD / SKIP / CLOSE`.

### auditdecisions/DECISION_V1_5B_CORRECTION_IMPORT_DATACLASS_POLICYENGINE_2026-05-13_2233UTC.md
- role_guess: POLICY_ENGINE
- status_guess: CANON_OR_DOC_READONLY
- tags: CRON_SYSTEMD;LEGACY_WRITE_WORDS;DEMO_WORDS
- functions_top: 
- states_or_paths: state.json
- line_hits: L1:# DECISION_V1_5B_CORRECTION_IMPORT_DATACLASS_POLICYENGINE || L8:- V1-5 a tente de charger policyengine via importlib. || L17:- Corriger uniquement demo_v1/adapters/policyengine_adapter.py. || L19:- En cas d'echec import/appel, retourner un state V1 explicite au lieu de crasher. || L20:- Garder broker paper only, size zero. || L24:- Ne pas ecrire state.json racine. || L28:- D9: un writer par state V1. || L34:- policyengine_state documente soit called true, soit refus propre.

### auditdecisions/DECISION_V1_5C_MAPPING_EXPLICITE_GESTE_NATIF_POLICYENGINE_2026-05-13_2234UTC.md
- role_guess: POLICY_ENGINE
- status_guess: CANON_OR_DOC_READONLY
- tags: LEGACY_WRITE_WORDS
- functions_top: 
- states_or_paths: state.json
- line_hits: L1:# DECISION_V1_5C_MAPPING_EXPLICITE_GESTE_NATIF_POLICYENGINE || L9:- policyengine source cible chargee: production/decision/policy_engine.py. || L20:- Ne pas lire state.json racine. || L22:- Ecrire uniquement states V1. || L23:- Broker reste paper only, size zero. || L27:- D9: un writer par state V1. || L32:- policyengine_called true si decide accepte FLAT. || L34:- broker reste SIMULATED_ONLY.

### auditdecisions/DECISION_V1_5_BRANCHAGE_POLICYENGINE_PAPER_ONLY_2026-05-13_2232UTC.md
- role_guess: DEMO_BROKER
- status_guess: CANON_OR_DOC_READONLY
- tags: REAL_EXCHANGE;CRON_SYSTEMD;LEGACY_WRITE_WORDS;DEMO_WORDS
- functions_top: 
- states_or_paths: demo_v1/states/policyengine_state.json;state.json
- line_hits: L1:# DECISION_V1_5_BRANCHAGE_POLICYENGINE_PAPER_ONLY || L9:- Le couloir demo_v1 existe. || L10:- Les states V1 sont separes. || L11:- Le broker est demobroker_paper_only. || L15:- Brancher le premier organe reel qualifie: policyengine. || L16:- Source cible: productiondecisionpolicyengine.py seulement. || L19:- Ecrire le resultat dans demo_v1/states/policyengine_state.json. || L20:- Garder l'ordre broker en simulation seulement. || L25:- Aucun ccxt actif dans demo_v1. || L29:- Aucune ecriture state.json racine. || L33:- D9: un writer par state V1. || L35:- D11_ARBITRAGES_V1: policyengine cible = productiondecisionpolicyengine.py seul. || L38:- V1-5 produit une pulsation paper only avec policyengine_state. || L39:- Le broker reste SIMULATED_ONLY.

### auditdecisions/DECISION_V1_6A_ALLOCATION_PAPER_SHADOW_EXPLICITE_2026-05-13_2237UTC.md
- role_guess: MONEY_MANAGER
- status_guess: CANON_OR_DOC_READONLY
- tags: CRON_SYSTEMD;LEGACY_WRITE_WORDS;DEMO_WORDS
- functions_top: 
- states_or_paths: state.json
- line_hits: L1:# DECISION_V1_6A_ALLOCATION_PAPER_SHADOW_EXPLICITE || L9:- policyengine est appele reellement. || L10:- policyengine produit raw_policy_action LONG et sizing 0.05 depuis entree placeholder. || L12:- broker reste FLAT, size 0.0, real_order_sent false. || L20:- Creer allocation_adapter.py dans demo_v1/adapters. || L21:- Calculer une allocation paper shadow depuis raw_result.sizing. || L24:- max_policy_sizing explicite: 0.20. || L25:- Calculer raw_policy_notional_paper pour observation. || L28:- Broker side force FLAT si allocated_size=0.0. || L30:- Ne pas lire state.json racine. || L35:- D9: un writer par state V1. || L37:- D11_ARBITRAGES_V1: capital parametre explicite, pas demostate implicite. || L42:- policyengine_called true. || L43:- raw_policy_action LONG possible. || L45:- raw_policy_sizing 0.05 observe. || L46:- raw_policy_notional_paper 1750.0 possible. || L48:- broker side FLA

### auditdecisions/DECISION_V1_6A_FIX_INTERFACE_DEMOBROKER_2026-05-13_2238UTC.md
- role_guess: DEMO_BROKER
- status_guess: CANON_OR_DOC_READONLY
- tags: CRON_SYSTEMD;LEGACY_WRITE_WORDS;DEMO_WORDS
- functions_top: 
- states_or_paths: state.json
- line_hits: L1:# DECISION_V1_6A_FIX_INTERFACE_DEMOBROKER || L11:AttributeError: module adapters.demobroker has no attribute execute_paper_order || L12:- Cause: mismatch de contrat entre orchestrateur_demo_total_v1_6.py et demobroker.py. || L17:- Corriger uniquement demo_v1/adapters/demobroker.py. || L18:- Exposer execute_paper_order comme contrat canonique V1. || L19:- Garder broker paper only. || L20:- Forcer real_order_sent false. || L23:- Ajouter alias compatibles pour anciens appels demo. || L25:- Ne pas lire state.json racine. || L30:- D9: un writer par state V1. || L36:- broker_side FLAT. || L38:- real_order_sent false.

### auditdecisions/DECISION_V1_6C_H_REAL_POLICYENGINE_CAPACITEOK_2026-05-13_2245UTC.md
- role_guess: MONEY_MANAGER
- status_guess: CANON_OR_DOC_READONLY
- tags: CRON_SYSTEMD;LEGACY_WRITE_WORDS
- functions_top: 
- states_or_paths: state.json
- line_hits: L1:# DECISION_V1_6C_H_REAL_POLICYENGINE_CAPACITEOK || L10:- decision_state transmet meteo_traceabilityid. || L11:- allocation reste zero. || L12:- broker reste FLAT. || L13:- real_order_sent reste false. || L14:- Un premier passage V1-6C avait perdu la preuve d'appel reel policyengine. || L16:- policyengine_state.real_call_ok est true. || L17:- policyengine_state.signature est non null. || L19:- raw_policy_action LONG est observe depuis policyengine reel. || L24:- Conserver l'appel reel policyengine avec real_call_ok obligatoire. || L25:- Conserver CAPACITEOK strict avec check POLICYENGINE_real_call. || L28:- Garder l'allocation en shadow paper. || L29:- Garder le broker paper FLAT. || L31:- Ne pas lire state.json racine. || L33:- Ecrire uniquement states V1. || L37:- D9: un writer par state V1. || L45:- policyengine_state.real_call_ok true. || L46:- policyengine_state.signature non null

### auditdecisions/DECISION_V1_6D_MONEYMANAGER_WRAPPER_EXPLICITE_2026-05-13_2248UTC.md
- role_guess: MONEY_MANAGER
- status_guess: CANON_OR_DOC_READONLY
- tags: CRON_SYSTEMD;LEGACY_WRITE_WORDS;DEMO_WORDS
- functions_top: 
- states_or_paths: demo_v1/states/moneymanager_state.json;state.json;statedemo.json
- line_hits: L9:- policyengine est appele reellement. || L11:- allocation reste zero. || L12:- broker reste FLAT. || L13:- real_order_sent reste false. || L17:- BASEDIR aplomb incoherent. || L21:- aplomb explicite. || L27:- Creer demo_v1/adapters/moneymanager_adapter.py. || L28:- Ne pas importer production/allocation/moneymanager.py. || L33:- Passer tempo_state explicitement. || L34:- Passer aplomb_state explicitement. || L35:- Ecrire demo_v1/states/moneymanager_state.json uniquement via orchestrateur. || L36:- Integrer moneymanager_state dans statedemo.json. || L43:- Garder broker FLAT. || L44:- Garder real_order_sent false. || L46:- Ne pas lire state.json racine. || L51:- moneymanager_state.present true. || L52:- moneymanager_state.explicit_inputs true. || L53:- moneymanager_state.legacy_imported false. || L54:- moneymanager_state.executable_size 0.0. || L55:- allocation_state.allocated_size 0.0. |

### auditdecisions/DECRETA73SEMANTIQUENEUTRALPOSITIONDEMO2026-05-15.md
- role_guess: DECISION_TO_ORDER
- status_guess: CANON_OR_DOC_READONLY
- tags: LEGACY_WRITE_WORDS;DEMO_WORDS;CLOSE_WORDS
- functions_top: 
- states_or_paths: moneymanagerstate.json;state.json
- line_hits: L1:# DECRET A7.3 — SEMANTIQUE NEUTRAL POSITION DEMO — 2026-05-15 || L5:Définir la sémantique canonique de `Money Manager = NEUTRAL finale 0.0` lorsqu'un ledger démo contient encore une position ouverte. || L9:La sonde A7.3 établit une position demo nette de -0.081 BTC SHORT. || L10:Le Money Manager actuel expose une cible NEUTRAL finale 0.0. || L16:`NEUTRAL finale 0.0` signifie `TARGET_FLAT`. || L19:Il ne signifie pas ignorer le ledger démo. || L24:- Si `target = 0` et `ledger_net = 0`, alors action sémantique : `SKIP`. || L25:- Si `target = 0` et `ledger_net < 0`, alors action sémantique : `CLOSE_TO_FLAT` par rachat/couverture candidat. || L26:- Si `target = 0` et `ledger_net > 0`, alors action sémantique : `CLOSE_TO_FLAT` par vente/réduction candidat. || L32:- `ledger_net = -0.081 BTC` || L34:- Sémantique décrétée : `CLOSE_TO_FLAT` || L37:- Suite autorisée : sonde froide de faisabilité

### auditdecisions/INDEXATIONA73NEUTRALPOSITIONDEMO20260515T20260515T193822Z.md
- role_guess: CANON_DOC
- status_guess: CANON_OR_DOC_READONLY
- tags: DEMO_WORDS;CLOSE_WORDS
- functions_top: 
- states_or_paths: 
- line_hits: L1:# INDEXATION A73 — NEUTRAL POSITION DEMO — 2026-05-15 || L13:- DECRETA73SEMANTIQUENEUTRALPOSITIONDEMO2026-05-15.md || L14:- ATTESTATIONA73PNLLATENTPOSITIONDEMONONCLOSE2026-05-15.md || L26:A73 definit que NEUTRAL finale 0.0 signifie TARGET_FLAT. || L36:A73 ne modifie aucun state.

### auditdecisions/RECTIFICATIFR4POSITIONDEMONETTELEDGERPRIME_20260515T195934Z.md
- role_guess: DEMO_BROKER
- status_guess: CANON_OR_DOC_READONLY
- tags: SECRET_ENV;CRON_SYSTEMD;DEMO_WORDS;CLOSE_WORDS
- functions_top: 
- states_or_paths: demo/states/statedemo.json
- line_hits: L1:# RECTIFICATIF R4 — POSITION DEMO NETTE / LEDGER PRIME || L3:Référence : RECTIFICATIFR4POSITIONDEMONETTELEDGERPRIME || L7:Portée : MODE_DEMO_TOTAL uniquement || L12:State runtime : AUCUN ÉCRIT || L18:Il clarifie que, pour décider si la cible TARGETFLAT est atteinte, la source canonique de vérité est le ledger net reconstruit depuis les exécutions démo, et non la seule valeur `position_after_demo` exposée dans le dern || L20:Ce rectificatif ne crée aucun ordre, ne valide aucune exécution, ne modifie aucun module Python, ne modifie aucun cron, ne touche aucun state runtime et n’autorise aucune finance réelle. || L24:A73 a posé que `NEUTRAL finale 0.0` signifie TARGETFLAT. || L26:R3 a exécuté une sonde froide de contrat CLOSETOFLAT et consommateurs position démo. || L28:R3 a constaté un ledger net démo de `-0.081 BTC`. || L30:R3 a produit un candidat froid `BUY 0.081 BTC` dont l’effet at

### demo/broker/demobroker.py
- role_guess: DEMO_BROKER
- status_guess: CANDIDAT_DEMO_ISOLE
- tags: SECRET_ENV;DEMO_WORDS;CLOSE_WORDS
- functions_top: now;load_json;write_json;mode_ok;reject;validate;execute;update_state;main
- states_or_paths: demo/orders/order.json;statedemo.json
- line_hits: L9:DEMO = ROOT / "demo" || L10:ORDERS = DEMO / "orders" || L11:EXECUTIONS = DEMO / "executions" || L12:STATES = DEMO / "states" || L13:LOGS = DEMO / "logs" || L14:MODE_LOCK = DEMO / "config" / "mode.lock" || L15:STATEDEMO = STATES / "statedemo.json" || L17:ALLOWED_SIDES = {"BUY", "SELL", "LONG", "SHORT", "CLOSE", "HOLD"} || L18:FORBIDDEN_KEYS = {"api_key", "secret", "passphrase", "credential", "credentials", "exchange_target", "broker_real", "real_broker"} || L34:"MODE=MODE_DEMO_TOTAL", || L38:"EXECUTION_DEMO=AUTORISEE", || L45:def reject(order, reason): || L47:"execution_id": "DEMO_REJECT_" + uuid.uuid4().hex[:12], || L48:"order_id": order.get("order_id"), || L50:"mode": "MODE_DEMO_TOTAL", || L51:"symbol": order.get("symbol"), || L52:"side": order.get("side"), || L53:"quantity": order.get("quantity"), || L54:"fill_price_demo": None, || L55:"fees_demo": 0.0, || L56:"pnl_demo": 0.0, || L5

### demo/broker/demobroker_runner.py
- role_guess: DEMO_BROKER
- status_guess: CANDIDAT_DEMO_ISOLE
- tags: SUBPROCESS;DEMO_WORDS
- functions_top: now;log;main
- states_or_paths: 
- line_hits: L3:demobroker_runner.py — Poller aval minimal V0 || L4:Scanne demo/orders/validated/ et appelle demobroker.py pour chaque ordre. || L5:Conforme à DECRET_A6 et CONTRAT_DEMOBROKER_V0. || L7:Usage : python3 demo/broker/demobroker_runner.py || L8:(aucun argument ; lit demo/orders/validated/) || L11:Crée demo/orders/processed/ et demo/orders/failed/ si absents. || L15:- CONTRAT_DEMOBROKER_V0 (fichiers autorisés en écriture) || L16:- CONTRAT_PRUDENCE_DEMO_V0 (lit après validation prudence) || L32:DEMO = ROOT / "demo" || L33:ORDERS = DEMO / "orders" || L34:VALIDATED = ORDERS / "validated" || L35:PROCESSED = ORDERS / "processed" || L36:FAILED = ORDERS / "failed" || L37:LOGS = DEMO / "logs" || L38:RUNNER_LOG = LOGS / "demobroker_runner.log" || L39:DEMOBROKER = DEMO / "broker" / "demobroker.py" || L55:if not DEMOBROKER.exists(): || L56:log({"event": "DEMOBROKER_MISSING", "level": "ERROR"}) || L62:

### demo/contracts/AMENDEMENT_CONTRAT_DEMOBROKER_V0_1_CODE_EXISTE_2026-05-12.md
- role_guess: DEMO_BROKER
- status_guess: CANON_OR_DOC_READONLY
- tags: CRON_SYSTEMD;DEMO_WORDS
- functions_top: 
- states_or_paths: demo/states/statedemo.json;statedemo.json
- line_hits: L1:# AMENDEMENT CONTRAT_DEMOBROKER V0.1 — CODE_EXISTE || L6:**Source collecte** : audit/rapports/COLLECTE_CONTRAT_DEMOBROKER_20260512_074143.txt || L11:CONTRAT_DEMOBROKER_V0.md (7 mai 21:10, 2107 o, gravé pré-A6/A7) déclare || L12:`CONTRAT_POSE / CODE_NON_ECRIT / BROKER_REEL_INTERDIT / BROKER_DEMO_AUTORISE`. || L23:| Demobroker | `demo/broker/demobroker.py` 5585 o (7 mai 21:11) | || L24:| Runner aval (A6) | `demo/broker/demobroker_runner.py` 3505 o (10 mai 18:19) | || L25:| Prudence | `demo/prudence/prudence_demo.py` 4164 o (7 mai 21:13) | || L26:| Prudence runner V2 OPT_γ (post-D85) | `demo/prudence/prudence_demo_runner.py` 7340 o (10 mai 20:44) | || L27:| Générateur ordres (A7) | `demo/generator/decision_to_order.py` 7218 o (10 mai 19:53) | || L28:| State | `demo/states/statedemo.json` 1489 o | || L29:| Exécutions tracées | 18 `DEMO_EXEC_*.json` + 1 `DEMO_REJECT_*.json` dans `demo/exec

### demo/contracts/CONTRAT_DEMOBROKER_V0.md
- role_guess: DEMO_BROKER
- status_guess: CANON_OR_DOC_READONLY
- tags: SECRET_ENV;CRON_SYSTEMD;LEGACY_WRITE_WORDS;DEMO_WORDS;CLOSE_WORDS
- functions_top: 
- states_or_paths: state.json
- line_hits: L1:# CONTRAT DEMOBROKER V0 — 2026-05-07 || L5:Le demobroker reçoit les ordres internes réels produits par Séragone. || L15:Le demobroker est le dernier connecteur simulé. || L20:- prudence ; || L33:- historique broker. || L38:- order_id ; || L43:- order_type ; || L47:- prudence_status ; || L52:Le demobroker refuse tout ordre si : || L56:- broker réel est demandé ; || L57:- mode n'est pas MODE_DEMO_TOTAL ; || L58:- prudence_status vaut BLOCKED ; || L60:- side n'est pas BUY, SELL, LONG, SHORT, CLOSE ou HOLD. || L66:- order_id ; || L68:- mode MODE_DEMO_TOTAL ; || L72:- fill_price_demo ; || L73:- fees_demo ; || L74:- pnl_demo ; || L75:- position_after_demo ; || L76:- cash_after_demo ; || L77:- status FILLED_DEMO, REJECTED_DEMO ou HELD_DEMO ; || L82:Le demobroker peut écrire uniquement dans : || L83:- demo/executions/ || L84:- demo/orders/ || L85:- demo/states/

### demo/contracts/CONTRAT_PRUDENCE_DEMO_V0.md
- role_guess: DEMO_BROKER
- status_guess: CANON_OR_DOC_READONLY
- tags: SECRET_ENV;DEMO_WORDS
- functions_top: 
- states_or_paths: 
- line_hits: L1:# CONTRAT PRUDENCE DEMO V0 — 2026-05-07 || L5:Prudence Démo V0 est placée au-dessus du demobroker. || L7:Elle valide ou bloque un ordre interne avant qu'il atteigne demo/broker/demobroker.py. || L11:Prudence n'est pas décorative. || L12:Prudence n'est pas seulement une note canonique. || L13:Prudence doit être lue, produire un état, et empêcher mécaniquement un ordre dangereux d'atteindre le broker démo. || L17:Ordres internes MODE_DEMO_TOTAL. || L31:Mode différent de MODE_DEMO_TOTAL. || L37:Ordre déjà marqué prudence_status BLOCKED. || L42:- l'ordre est écrit dans demo/orders/validated/ || L43:- prudence_status devient PASS || L44:- prudence_checked vaut true || L45:- prudence_checked_at est rempli || L48:- l'ordre est écrit dans demo/orders/rejected/ || L49:- prudence_status devient BLOCKED || L50:- prudence_block_reason est rempli || L51:- aucun passage broker ne doit suivre || L56

### demo/generator/decision_to_order.py
- role_guess: DECISION_TO_ORDER
- status_guess: BLOQUER_VERIFIER_WRITE_LEGACY
- tags: SECRET_ENV;LEGACY_WRITE_WORDS;DEMO_WORDS
- functions_top: utc_iso;utc_compact;log_event;read_json;write_json_atomic;decision_hash;main
- states_or_paths: decision_to_order_state.json;demo/states/decision_to_order_state.json;money_manager_state.json;state.json
- line_hits: L4:SÉRAGONE — decision_to_order.py || L6:A7 V0 — Générateur d'ordres demo depuis MM position_nette + state.json.prix. || L15:1. Vérifie state.json + money_manager_state.json existent || L17:3. Lit state.json.prix (LIVE, clé canonique FR) || L18:4. Crée demo/{generator,states,orders,logs}/ si absents || L20:6. Compare avec hash précédent dans demo/states/decision_to_order_state.json || L22:8. Différent → écrit ordre 12 champs + update hash + ORDER_GENERATED || L29:- pas de pnl_demo / cash_after_demo simulés || L33:- lecture seule sur state.json + money_manager_state.json || L34:- écrit UNIQUEMENT dans demo/orders/, demo/states/, demo/logs/ || L35:- n'écrit jamais dans validated/ ni rejected/ (rôle de prudence_demo_runner) || L49:# Chemins canoniques (script à demo/generator/, root = ~/seragone) || L53:STATE_PATH = ROOT / "state.json" || L54:MM_STATE_PATH = ROOT / "money_manager_state.json

### demo/orders/test_order_danger.json
- role_guess: DECISION_TO_ORDER
- status_guess: A_CLASSER
- tags: DEMO_WORDS
- functions_top: 
- states_or_paths: 
- line_hits: L2:"mode": "MODE_DEMO_TOTAL", || L3:"order_id": "TEST_DANGER_20260507_001", || L8:"order_type": "MARKET_DEMO", || L12:"prudence_status": "PASS",

### demo/orders/test_order_demo.json
- role_guess: DECISION_TO_ORDER
- status_guess: A_CLASSER
- tags: DEMO_WORDS
- functions_top: 
- states_or_paths: 
- line_hits: L2:"mode": "MODE_DEMO_TOTAL", || L3:"order_id": "TEST_DEMO_20260507_001", || L5:"source": "MANUAL_TEST_DEMO", || L8:"order_type": "MARKET_DEMO", || L11:"reason": "test demobroker v0", || L12:"prudence_status": "PASS",

### demo/prudence/prudence_demo.py
- role_guess: PRUDENCE_MEASURE
- status_guess: BLOQUER_VERIFIER_WRITE_LEGACY
- tags: SECRET_ENV;LEGACY_WRITE_WORDS;DEMO_WORDS;CLOSE_WORDS
- functions_top: now;read_json;write_json;mode_ok;block_reason;main
- states_or_paths: demo/orders/order.json;prudence_demo_state.json
- line_hits: L9:DEMO = ROOT / "demo" || L10:VALIDATED = DEMO / "orders" / "validated" || L11:REJECTED = DEMO / "orders" / "rejected" || L12:STATES = DEMO / "states" || L13:LOGS = DEMO / "logs" || L14:MODE_LOCK = DEMO / "config" / "mode.lock" || L15:PRUDENCE_STATE = STATES / "prudence_demo_state.json" || L17:ALLOWED_SIDES = {"BUY", "SELL", "LONG", "SHORT", "CLOSE", "HOLD"} || L18:FORBIDDEN_KEYS = {"api_key", "secret", "passphrase", "credential", "credentials", "exchange_target", "broker_real", "real_broker"} || L34:"MODE=MODE_DEMO_TOTAL", || L39:"EXECUTION_DEMO=AUTORISEE", || L46:def block_reason(order): || L50:if order.get("mode") != "MODE_DEMO_TOTAL": || L51:return "mode différent de MODE_DEMO_TOTAL" || L52:if order.get("real_finance_allowed") is not False: || L55:if k in order: || L57:if order.get("prudence_status") == "BLOCKED": || L59:if not order.get("source"): || L61:if not order.get("reason"):

### demo/prudence/prudence_demo_runner.py
- role_guess: DEMO_BROKER
- status_guess: CANDIDAT_DEMO_ISOLE
- tags: SUBPROCESS;DEMO_WORDS
- functions_top: utc_iso;log_event;tail;is_already_prudenced;main
- states_or_paths: 
- line_hits: L4:SÉRAGONE — prudence_demo_runner.py || L6:A7 V2 — Runner subprocess pour prudence_demo.py. || L16:Cause racine : demobroker.py L138 archive l'ordre exécuté en || L17:demo/orders/ top-level (effet de bord du broker || L19:En cron PHASE 2, prudence_demo_runner ramassait || L20:ce résidu post-prudence → boucle infinie de re-prudence. || L22:Fix V2 : Avant subprocess, lire le JSON. Si prudence_checked == True || L23:OU prudence_status ∈ {"PASS","BLOCKED"} → log || L24:SKIP_ALREADY_PRUDENCED + unlink résidu + continue. || L25:Évite la boucle sans toucher l'invariant demobroker. || L28:1. Vérifie prudence_demo.py existe à demo/prudence/ || L29:2. Crée demo/orders/, demo/logs/ si absents || L30:3. Liste demo/orders/AUTO_A7_*.json (top-level seulement, pas récursif) || L31:4. Si vide : log IDLE_NO_ORDER + exit 0 || L34:- subprocess.run([python3, prudence_demo.py, path], timeout=30) || L35:- lo

### demo/reports/RACCORDEMENT_CHAINE_REELLE_VERS_DEMO_20260507_211559/fichiers_execution_broker_router.txt
- role_guess: DEMO_BROKER
- status_guess: CANDIDAT_DEMO_ISOLE
- tags: DEMO_WORDS
- functions_top: 
- states_or_paths: 
- line_hits: L1:./.venv/lib/python3.12/site-packages/pandas/tests/frame/methods/test_reorder_levels.py || L2:./.venv/lib/python3.12/site-packages/pandas/tests/reshape/merge/test_merge_ordered.py || L3:./.venv/lib/python3.12/site-packages/scipy/io/matlab/_byteordercodes.py || L4:./.venv/lib/python3.12/site-packages/scipy/io/matlab/byteordercodes.py || L5:./.venv/lib/python3.12/site-packages/scipy/io/matlab/tests/test_byteordercodes.py || L6:./.venv/lib/python3.12/site-packages/scipy/sparse/csgraph/tests/test_reordering.py || L49:./AUDIT_CHRONO_SERAGONE_TOTAL_20260501_101502/contenu/scripts/validators/fix_lot_b_date_order.py || L50:./AUDIT_CHRONO_SERAGONE_TOTAL_20260501_101502/contenu/scripts/validators/fix_lot_b_date_order_v2.py || L80:./demo/broker/demobroker.py || L96:./scripts/validators/fix_lot_b_date_order.py || L97:./scripts/validators/fix_lot_b_date_order_v2.py

### demo/reports/RACCORDEMENT_CHAINE_REELLE_VERS_DEMO_20260507_211559/grep_ordre_execution_broker_head2000.txt
- role_guess: ALLOCATION
- status_guess: BLOQUER_VERIFIER_RISQUE_REEL
- tags: REAL_EXCHANGE;REAL_ORDER;SECRET_ENV;CRON_SYSTEMD;SUBPROCESS;LEGACY_WRITE_WORDS;DEMO_WORDS;CLOSE_WORDS
- functions_top: 
- states_or_paths: ./audit/m2_v2_refresh_for_demo_20260507_201306/before/m2_bear_state_v2.json;./audit/m2_v2_refresh_for_demo_20260507_201306/before/m2bearstatev2.json;./audit/mode_demo_ready_warn97_20260507_201400/aplombstate.json;./audit/mode_demo_ready_warn97_20260507_201400/m2_bear_state_v2.json;./audit/mode_demo_ready_warn97_20260507_201400/mondes_paralleles_state.json;./audit/mode_demo_ready_warn97_20260507_201400/seragone_demo_health_state.json;./audit/paralleles_schema_native_closed_20260507_200025/mondes_paralleles_state.json;./audit/paralleles_schema_native_closed_20260507_200025/seragone_demo_health_state.json;/home/ubuntu/seragone/state/prudence_state.json;audit/mode_demo_ready_warn97_20260507_2014
- line_hits: L1:./app_cockpit_v63.py:41: border: 2px solid #C4922A !important; || L2:./app_cockpit_v63.py:43: border-radius: 8px !important; || L3:./app_cockpit_v63.py:53: border: 2px solid #FFD060 !important; || L4:./app_cockpit_v63.py:66:pre, code, .stCodeBlock, [data-testid="stCode"] {background:#1A0D12 !important; color:#FFD060 !important; border:1px solid #C4922A !important; border-radius:8px !important;} || L5:./app_cockpit_v63.py:70:pre, code, .stCodeBlock {background:#1A0D12 !important; color:#FFD060 !important; border:1px solid #C4922A !important; border-radius:8px !important;} || L6:./app_cockpit_v63.py:84: .kpi { background:linear-gradient(145deg, #1A0D12 0%, #150A10 100%); border-radius:12px; padding:18px 20px; border-left:4px solid #C4922A; margin-bottom:6px; } || L7:./app_cockpit_v63.py:85: .kpi.vert { border-left-color:#1A6B4B; } || L8:./app_cockpit_v63.py:86: .kpi.orange{ border-left-

### demo/reports/RAPPORT_DEMOBROKER_V0_20260507.md
- role_guess: DEMO_BROKER
- status_guess: CANON_OR_DOC_READONLY
- tags: LEGACY_WRITE_WORDS;DEMO_WORDS
- functions_top: 
- states_or_paths: state.json
- line_hits: L1:# RAPPORT DEMOBROKER V0 — 2026-05-07 || L5:DEMOBROKER_V0_FONCTIONNEL. || L9:Un ordre interne démo a été fourni à demo/broker/demobroker.py. || L12:- order_id : TEST_DEMO_20260507_001 || L13:- source : MANUAL_TEST_DEMO || L18:- prudence_status : PASS || L23:Le demobroker a produit une exécution démo complète. || L26:- status : FILLED_DEMO || L28:- state démo mis à jour : oui || L34:Ce test prouve que MODE_DEMO_TOTAL peut recevoir un ordre interne réel dans Séragone et produire une exécution complète sans argent réel ni connexion financière externe. || L39:Séragone complet, broker simulé. || L43:DEMOBROKER_V0 n'est pas encore branché au cerveau Séragone. || L44:DEMOBROKER_V0 n'est pas encore derrière Prudence complète. || L45:DEMOBROKER_V0 ne lit pas encore un flux d'ordres réel continu. || L46:DEMOBROKER_V0 ne calcule pas encore un portefeuille démo complet. || L47:DEMOBROKER_V0 ne met

### demo/states/decision_to_order_state.json
- role_guess: DECISION_TO_ORDER
- status_guess: A_CLASSER
- tags: NONE
- functions_top: 
- states_or_paths: 
- line_hits: L3:"last_order_id": "AUTO_A7_20260515T071702",

### demo/states/prudence_demo_state.json
- role_guess: PRUDENCE_MEASURE
- status_guess: CANDIDAT_CALCULATEUR_OU_WRAPPER
- tags: DEMO_WORDS
- functions_top: 
- states_or_paths: /home/ubuntu/seragone/demo/orders/validated/AUTO_A7_20260515T071702.json;/home/ubuntu/seragone/demo/orders/validated/AUTO_A7_20260515T071702.json
- line_hits: L2:"mode": "MODE_DEMO_TOTAL", || L4:"last_order_id": "AUTO_A7_20260515T071702", || L7:"last_output": "/home/ubuntu/seragone/demo/orders/validated/AUTO_A7_20260515T071702.json",

### doubletempo.py
- role_guess: DOUBLE_TEMPO
- status_guess: BLOQUER_VERIFIER_WRITE_LEGACY
- tags: LEGACY_WRITE_WORDS
- functions_top: _now_iso;_load_state;_save_state;get_tempo_budgets
- states_or_paths: doubletempostate.json
- line_hits: L9:STATE_FILE = BASE_DIR / "states" / "doubletempostate.json" || L16:def _load_state() -> Dict: || L17:if not STATE_FILE.exists(): || L31:with open(STATE_FILE, "r", encoding="utf-8") as f: || L51:def _save_state(state: Dict) -> None: || L52:STATE_FILE.parent.mkdir(parents=True, exist_ok=True) || L53:state["updatedat"] = _now_iso() || L54:with open(STATE_FILE, "w", encoding="utf-8") as f: || L55:json.dump(state, f, indent=2, ensure_ascii=False) || L59:state = _load_state() || L62:capital_peak = max(float(state.get("capitalpeak", 0.0) or 0.0), capital_total) || L65:daysabove220 = int(state.get("daysabove220", 0) or 0) + 1 if capital_total > 220000 else 0 || L66:daysbelow180 = int(state.get("daysbelow180", 0) or 0) + 1 if capital_total < 180000 else 0 || L67:daysabove400 = int(state.get("daysabove400", 0) or 0) + 1 if capital_total > 400000 else 0 || L68:daysbelow320 = int(state.get("daysbe

### doubletempostate.json
- role_guess: DOUBLE_TEMPO
- status_guess: CANDIDAT_CALCULATEUR_OU_WRAPPER
- tags: NONE
- functions_top: 
- states_or_paths: 
- line_hits: 

### money_manager.py
- role_guess: DOUBLE_TEMPO
- status_guess: BLOQUER_VERIFIER_WRITE_LEGACY
- tags: REAL_EXCHANGE;LEGACY_WRITE_WORDS;CLOSE_WORDS
- functions_top: read_json;get_aplomb_permission;get_tireur_direction;get_etincelle_state;get_brisance_active;get_v9_bear;calculer_positions_tireurs;sommer_avec_cap_progressif;compenser_books;appliquer_gardes_fous;load_clones_state;load_m4_state;load_m5_state;main
- states_or_paths: aplombdailystate.json;aplombstate.json;brisance_state.json;clones_v6_state.json;etincellestate.json;fulgurance_state.json;grappillage_state.json;money_manager_state.json;ours_v2_state.json;presence1hstate.json;sentinelle_exchange_state.json;state.json;tenue30mstate.json;tireurs_agilite_5m_state.json;tireurs_minute_state.json;tireurs_state.json;vigie15mstate.json
- line_hits: L8:Applique l'allocation capital synthétisée à partir des 4 réponses IA. || L9:Lit les états des tireurs + V9 + Aplomb + brisance + étincelle. || L27:STATE_OUT = BASE / "money_manager_state.json" || L40:TIREURS_ALLOCATION = { || L48:"Aplomb": 0.03, || L56:MULT_APLOMB = { || L87:TIREURS_STATE_FILES = { || L88:"Aplomb": BASE / "aplombdailystate.json", || L89:"Presence": BASE / "presence1hstate.json", || L90:"Tenue": BASE / "tenue30mstate.json", || L91:"Vigie": BASE / "vigie15mstate.json", || L92:"Agilite": BASE / "tireurs_agilite_5m_state.json", || L93:"Precision": BASE / "tireurs_minute_state.json", || L94:"Fulgurance": BASE / "fulgurance_state.json", || L95:"Etincelle": BASE / "etincellestate.json", || L99:BRISANCE_STATE = BASE / "brisance_state.json" || L100:ETINCELLE_STATE = BASE / "etincellestate.json" || L126:def get_aplomb_permission() -> str: || L128:BASE / "aplombdailystate.json",

### money_manager_perplexity_97L.py
- role_guess: ALLOCATION
- status_guess: BLOQUER_VERIFIER_WRITE_LEGACY
- tags: LEGACY_WRITE_WORDS
- functions_top: load_aplomb_state;load_m3_state;load_m8_state;get_capital_total;run_money_manager
- states_or_paths: aplomb_state.json;m3_temperance_state.json;m8_tresorerie_state.json;money_manager_state.json
- line_hits: L14:STATE_FILE = BASE_DIR / "money_manager_state.json" || L16:def load_aplomb_state(): || L17:f = BASE_DIR / "aplomb_state.json" || L23:def load_m3_state(): || L24:f = BASE_DIR / "moteurs" / "m3_temperance_state.json" || L30:def load_m8_state(): || L31:f = BASE_DIR / "moteurs" / "m8_tresorerie_state.json" || L35:return {"cash_tactique_allocation": 0.0} || L44:aplomb = load_aplomb_state() || L45:m3 = load_m3_state() || L46:m8 = load_m8_state() || L48:direction = aplomb.get("direction", "NEUTRE") || L49:perm = aplomb.get("permission", 0.0) || L52:tempo_state, budgets = get_tempo_budgets(capital) || L66:# Application de M8 (Trésorerie active) - allocation delta-neutre || L67:budget_tresorerie = m8.get("cash_tactique_allocation", 0.0) * capital || L78:state = { || L91:with open(STATE_FILE, 'w') as f: || L92:json.dump(state, f, indent=2) || L95:return state

### money_manager_state.json
- role_guess: ALLOCATION
- status_guess: CANDIDAT_CALCULATEUR_OU_WRAPPER
- tags: CLOSE_WORDS
- functions_top: 
- states_or_paths: 
- line_hits: L4:"version": "1.1-aplomb-canon", || L19:"permission_aplomb": "SHORT", || L31:"allocation_eur": 4235.0, || L32:"multiplicateur_aplomb": 0.0, || L40:"allocation_eur": 3465.0, || L41:"multiplicateur_aplomb": 0.0, || L49:"allocation_eur": 2887.5, || L50:"multiplicateur_aplomb": 0.0, || L58:"allocation_eur": 2502.5, || L59:"multiplicateur_aplomb": 0.0, || L67:"allocation_eur": 2117.5, || L68:"multiplicateur_aplomb": 0.0, || L76:"allocation_eur": 1540.0, || L77:"multiplicateur_aplomb": 0.0, || L85:"allocation_eur": 1925.0, || L86:"multiplicateur_aplomb": 0.0, || L101:"direction": "NEUTRAL",

### money_manager_state_production.json
- role_guess: ALLOCATION
- status_guess: CANDIDAT_CALCULATEUR_OU_WRAPPER
- tags: NONE
- functions_top: 
- states_or_paths: 
- line_hits: L19:"permission_aplomb": "SHORTFORT", || L31:"allocation_eur": 4235.0, || L32:"multiplicateur_aplomb": 0.0, || L40:"allocation_eur": 3465.0, || L41:"multiplicateur_aplomb": 0.0, || L49:"allocation_eur": 2887.5, || L50:"multiplicateur_aplomb": 0.0, || L58:"allocation_eur": 2502.5, || L59:"multiplicateur_aplomb": 0.0, || L67:"allocation_eur": 2117.5, || L68:"multiplicateur_aplomb": 0.0, || L76:"allocation_eur": 1540.0, || L77:"multiplicateur_aplomb": 0.0, || L85:"allocation_eur": 1925.0, || L86:"multiplicateur_aplomb": 0.0, || L91:"nom": "Aplomb", || L94:"allocation_eur": 577.5, || L95:"multiplicateur_aplomb": 0.0, || L103:"allocation_eur": 5103.0, || L104:"multiplicateur_aplomb": 1.0, || L112:"allocation_eur": 6300.0, || L113:"multiplicateur_aplomb": 1.0, || L121:"allocation_eur": 3500.0, || L122:"multiplicateur_aplomb": 1.0,

### prudence_module.py
- role_guess: PRUDENCE_MEASURE
- status_guess: BLOQUER_VERIFIER_WRITE_LEGACY
- tags: LEGACY_WRITE_WORDS
- functions_top: prudence_parle;compter_convergence;ecrire_etat;log_ligne;main
- states_or_paths: /home/ubuntu/seragone/state/prudence_state.json;prudence_state.json;/home/ubuntu/seragone/data/mondes_recursifs_100m.csv;/home/ubuntu/seragone/logs/prudence.log;/home/ubuntu/seragone/state/prudence_state.json
- line_hits: L2:PRUDENCE — la voix qui refuse le consensus grégaire || L10:Prudence surveille le nombre de mondes récursifs qui convergent sur OUVRIR || L24:Quand Prudence parle, le geste final du chef est forcé à ATTENDRE, || L46:PRUDENCE_ZONE_MIN = 55 || L47:PRUDENCE_ZONE_MAX = 65 || L48:PRUDENCE_FENETRE = 180 || L49:PRUDENCE_QUANTILE = 0.20 || L50:PRUDENCE_N_MONDES = 100 || L52:STATE_PATH = '/home/ubuntu/seragone/state/prudence_state.json' || L53:LOG_PATH = '/home/ubuntu/seragone/logs/prudence.log' || L60:def prudence_parle(n_mondes_convergents: int) -> dict: || L62:Prudence parle-t-elle ? || L81:if PRUDENCE_ZONE_MIN <= n_mondes_convergents <= PRUDENCE_ZONE_MAX: || L85:'zone_min': PRUDENCE_ZONE_MIN, || L86:'zone_max': PRUDENCE_ZONE_MAX, || L92:'zone_min': PRUDENCE_ZONE_MIN, || L93:'zone_max': PRUDENCE_ZONE_MAX, || L124:for k in range(PRUDENCE_N_MONDES): || L131:window = vals[-PRUDENCE_FENETRE:] if

### tireur_aplomb.py
- role_guess: APLOMB
- status_guess: BLOQUER_VERIFIER_WRITE_LEGACY
- tags: LEGACY_WRITE_WORDS
- functions_top: load_json;load_first;infer_aplomb_input;decide_local;canonical_permission;save_policy_state_local;append_signal_log_local;main
- states_or_paths: aplombdailystate.json;aplombstate.json;m2_bear_state_v2.json;m2bearstate.json;m2bearstatev2.json;mondes_paralleles_state.json;mondesparallelesstate.json;policy_state.json
- line_hits: L11:STATES_DIR = BASE_DIR / "states" || L14:STATES_DIR.mkdir(parents=True, exist_ok=True) || L16:log = logging.getLogger("TIREUR_APLOMB") || L21:_fh = logging.FileHandler(LOGS_DIR / "tireur_aplomb.log", encoding="utf-8") || L28:APL_STATE_FILE = BASE_DIR / "aplombstate.json" || L29:APL_DAILY_STATE_FILE = BASE_DIR / "aplombdailystate.json" || L30:POLICY_STATE_FILE = STATES_DIR / "policy_state.json" || L32:POLICY_MONITOR_FILE = BASE_DIR / "policy_monitor.json" || L38:BASE_DIR / "mondesparallelesstate.json", || L39:BASE_DIR / "mondes_paralleles_state.json", || L44:BASE_DIR / "m2bearstatev2.json", || L45:BASE_DIR / "m2_bear_state_v2.json", || L46:BASE_DIR / "m2bearstate.json", || L68:log.info("State chargé : %s", path.name) || L73:def infer_aplomb_input(): || L118:"bull_state": bull, || L119:"bear_state": bear, || L202:def save_policy_state_local(payload: dict, date_str: str, regime_fond: str

## Décision de sonde
- Cette sonde ne donne pas droit à activation.
- Si bloqueur réel ou write legacy apparaît, produire un rectificatif ou wrapper pur avant tout branchement.
- Si les candidats calculateurs sont purs, la suite sera un décret de branchement démo séparé, puis seulement une activation démo bornée.
- Le réel reste interdit tant que la démo complète n’est pas prouvée.