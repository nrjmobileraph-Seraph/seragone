# RECTIFICATIF MATRICE WRAPPERS PURS DECISIONALLOCATION

Date UTC: 20260515T204439Z

## Source
- MATRICE_WRAPPERS_PURS_DECISIONALLOCATION_20260515T204342Z
- SONDEFROIDE_DECISIONALLOCATION_V1_20260515T203830Z
- SONDEB_BLOQUEURS_DECISIONALLOCATION_20260515T203947Z
- ATTESTATION_DECISIONALLOCATION_SONDEB_BLOCAGE_DIRECT_20260515T204042Z
- CONTRATORCHESTRATEURDEMOV1
- DECRETA73SEMANTIQUENEUTRALPOSITIONDEMO2026-05-15

## Objet
Rectifier l'interprétation possible des champs pure_function_candidates.

## Rectification canonique
Une fonction détectée comme pure candidate par analyse lexicale ne rend pas son fichier parent conforme.

Si le fichier parent est classé:
- WRITE_LEGACY_REEL_OU_PROBABLE
- WRAPPER_NEUF_REQUIS_WRITE_LEGACY
- EXCLURE_RISQUE_REEL_DIRECT
- EXCLURE_PROCESS_CRON_SYSTEMD_DIRECT

alors aucune importation métier directe n'est autorisée.

La fonction peut seulement servir d'indice documentaire pour rédiger ultérieurement un wrapper neuf, inerte, relu et sondé séparément.

## Application aux rôles

### APLOMB
tireur_aplomb.py contient des fonctions candidates lexicales:
- infer_aplomb_input
- decide_local

Mais tireur_aplomb.py reste classé WRAPPER_NEUF_REQUIS_WRITE_LEGACY.
Décision: pas d'import direct, pas d'appel direct, wrapper neuf requis si ce rôle est conservé.

### DOUBLE_TEMPO
doubletempo.py contient une fonction candidate lexicale:
- get_tempo_budgets

Mais doubletempo.py reste classé WRAPPER_NEUF_REQUIS_WRITE_LEGACY.
Décision: pas d'import direct, pas d'appel direct, wrapper neuf requis si ce rôle est conservé.

### PRUDENCE_MEASURE
prudence_module.py contient une fonction candidate lexicale:
- prudence_parle

Mais prudence_module.py reste classé EXCLURE_PROCESS_CRON_SYSTEMD_DIRECT.
Décision: pas d'import direct, pas d'appel direct, wrapper neuf requis ou exclusion temporaire.

### ALLOCATION
money_manager.py et money_manager_perplexity_97L.py contiennent des fonctions candidates lexicales.
Mais les fichiers parents sont classés EXCLURE_RISQUE_REEL_DIRECT ou WRAPPER_NEUF_REQUIS_WRITE_LEGACY.
Décision: pas d'import direct, pas d'appel direct, wrapper neuf requis ou exclusion temporaire.

### DECISION_TO_ORDER
decision_to_order.py contient une fonction candidate lexicale:
- decision_hash

Mais le rôle DECISION_TO_ORDER reste exclu de l'orchestrateur V1 jusqu'à décret spécifique.
Décision: hors branchement V1.

### DEMO_BROKER
prudence_demo_runner.py contient une fonction candidate lexicale:
- is_already_prudenced

Mais DEMO_BROKER reste hors orchestrateur V1 jusqu'à décret spécifique.
Décision: hors branchement V1.

## Chemin contrat V1
La matrice a testé un chemin de contrat absent:
auditphasee/CONTRATORCHESTRATEURDEMOV12026-05-132330VALIDATED.md

Avant tout décret futur, le chemin mécanique exact du contrat V1 devra être résolu par sonde froide.
Ce rectificatif ne décrète aucun branchement.

## Statut final
- Aucun branchement autorisé
- Aucun import métier autorisé
- Aucun appel direct des fichiers legacy autorisé
- Aucun patch runtime
- Aucun cron modifié
- Aucun systemd modifié
- Aucun process lancé
- Aucune finance réelle
- TARGETFLAT / CLOSETOFLAT reste HOLDREADONLY

## Suite autorisée
Produire une sonde froide ciblée RESOLUTION_CHEMIN_CONTRAT_V1.
Produire ensuite seulement une matrice de wrappers neufs inertes, sans import métier.
