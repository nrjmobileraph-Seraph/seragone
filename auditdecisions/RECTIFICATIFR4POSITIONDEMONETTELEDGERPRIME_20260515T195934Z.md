# RECTIFICATIF R4 — POSITION DEMO NETTE / LEDGER PRIME

Référence : RECTIFICATIFR4POSITIONDEMONETTELEDGERPRIME  
Date UTC : 2026-05-15T19:59:34Z  
Type : rectificatif documentaire pur  
Statut : À SIGNER / GRAVER  
Portée : MODE_DEMO_TOTAL uniquement  
Activation : AUCUNE  
Runtime : AUCUN TOUCHÉ  
Ordre : AUCUN CRÉÉ  
Cron / systemd : AUCUN MODIFIÉ  
State runtime : AUCUN ÉCRIT  

## 1. Objet

Le présent rectificatif scelle la lecture canonique de la position démo nette dans le contexte A73 / R3.

Il clarifie que, pour décider si la cible TARGETFLAT est atteinte, la source canonique de vérité est le ledger net reconstruit depuis les exécutions démo, et non la seule valeur `position_after_demo` exposée dans le dernier état broker démo.

Ce rectificatif ne crée aucun ordre, ne valide aucune exécution, ne modifie aucun module Python, ne modifie aucun cron, ne touche aucun state runtime et n’autorise aucune finance réelle.

## 2. Contexte canonique

A73 a posé que `NEUTRAL finale 0.0` signifie TARGETFLAT.

R3 a exécuté une sonde froide de contrat CLOSETOFLAT et consommateurs position démo.

R3 a constaté un ledger net démo de `-0.081 BTC`.

R3 a produit un candidat froid `BUY 0.081 BTC` dont l’effet attendu serait `expected_ledger_after_if_filled = 0.0`.

R3 a explicitement marqué ce candidat comme `DRYRUNONLY`, `DONOTWRITETHISFILE`, `runtimeaction NONE`, `writes NONE`.

## 3. Problème rectifié

Le champ `position_after_demo` produit par demobroker est une sortie de dernière exécution broker démo.

Il ne doit pas être interprété seul comme position nette cumulée du portefeuille démo.

Une exécution `BUY 0.081` après un ledger net `-0.081` peut apparaître localement comme dernier fill BUY, mais son effet ledger est une couverture de short menant à TARGETFLAT.

Sans ce rectificatif, une session future pourrait confondre le dernier fill `BUY 0.081` avec une ouverture LONG, alors que le contexte R3 le définit comme fermeture de short démo.

## 4. Règle canonique R4

Pour MODE_DEMO_TOTAL, la position demo nette canonique se calcule par somme signée des exécutions `FILLED_DEMO`.

Convention de signe :

- `BUY` et `LONG` augmentent le ledger net.
- `SELL` et `SHORT` diminuent le ledger net.
- `HOLD` n’a pas d’effet de position.
- Toute sémantique `CLOSE` future doit être rattachée explicitement à son effet de couverture avant exécution.

Le champ `demo/states/statedemo.json` et les sous-champs de dernière exécution restent utiles comme photographie broker démo, mais ne priment pas sur le ledger net reconstruit depuis `demo/executions`.

## 5. Application à R3

Dans le cas R3 :

- Ledger net avant candidat : `-0.081 BTC`.
- Side candidat : `BUY`.
- Quantité candidate : `0.081 BTC`.
- Effet attendu si rempli : `0.0 BTC`.
- Sémantique canonique : couverture de short démo vers TARGETFLAT.
- Non-sémantique : ouverture LONG.

Le candidat R3 reste un candidat froid.

Il n’est pas transformé en ordre par le présent rectificatif.

## 6. Garde-fous

Le présent rectificatif interdit toute lecture future selon laquelle R4 autoriserait directement une exécution.

Toute exécution ultérieure exige un décret séparé, une sonde froide immédiatement préalable, et une validation explicite de la chaîne Prudence → orders/validated → demobroker_runner → demobroker.

Le présent rectificatif ne donne aucun droit nouveau sur finance réelle.

Le présent rectificatif ne change pas le contrat d’interdiction `realfinanceallowed=false`.

Le présent rectificatif ne touche pas `bridgeexecution.py`, aucun secret, aucun fichier exchange, aucun cron, aucun service systemd.

## 7. Statuts canoniques séparés

Découverte nouvelle : ambiguïté de lecture entre `position_after_demo` dernière exécution et ledger net cumulé.

Redécouverte : A73 avait déjà posé TARGETFLAT pour `NEUTRAL finale 0.0`.

Correction : la cible flat doit être mesurée par ledger net, pas par lecture naïve du dernier fill.

Décision canonique déjà scellée : aucune finance réelle, aucun exchange réel, aucun runtime modifié par A73/R3/R4.

Hypothèse non vérifiée : exécution effective d’un ordre de couverture, qui reste hors scope R4.

## 8. Formule de signature

Je signe le rectificatif R4 POSITION DEMO NETTE / LEDGER PRIME.

Je reconnais que TARGETFLAT se mesure par ledger net démo reconstruit depuis les exécutions FILLED_DEMO.

Je reconnais que `position_after_demo` est une photographie de dernière exécution broker démo et ne prime pas sur le ledger net.

Je reconnais que `BUY 0.081 BTC` dans le contexte R3 signifie candidat de couverture de short vers flat, pas ouverture LONG.

Je reconnais qu’aucun ordre n’est créé par R4.

Je reconnais qu’aucun runtime, cron, state, module Python, service systemd, bridge réel ou finance réelle n’est touché par R4.

Signataire : Raphaël Boussy  
Date UTC de signature : 2026-05-15T19:59:34Z  
Statut : SIGNÉ SI VALIDÉ PAR RAPHAËL / GRAVER DANS INDEXCANON
