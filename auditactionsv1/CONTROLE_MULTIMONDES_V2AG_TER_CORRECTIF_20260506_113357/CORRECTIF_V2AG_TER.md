# V2AG-ter CORRECTIF - vrai caviardage cette fois

## Pourquoi un correctif

Le commit fe97428d (V2AG-ter) avait 3 defauts cumules :

1. **Caviardage echoue silencieusement** : regex sed `'TOKEN=ghp_LcNK[^"]*'`
   sans guillemet ouvrant, alors que le fichier contient `TOKEN="ghp_LcNK..."`
   avec guillemet. Le sed n'a rien match. sha256 fichier inchange (8b420db).

2. **Backup contient aussi le token** : `push_bulletin_sh_content_AVANT_caviardage.backup`
   est une copie verbatim du fichier d'origine, donc contient aussi le token.
   En le commitant, on a duplique la presence du token sur GitHub HEAD au lieu de la supprimer.

3. **Subject commit fige en "OK"** alors que le manifest disait "KO". Trace Git
   incoherente entre subject et contenu manifest.

## Correctif applique

- Caviardage Python (regex robuste avec guillemets) appliquee aux 2 fichiers
- Verdict CALCULE depuis grep -c
- Subject commit lu depuis verdict.txt (pas fige)
- Verification globale : `grep -r ghp_LcNK auditactionsv1/` doit retourner 0

## Statut historique

Les commits 40d572ac (V2ACBIS), 2a5b3285 (V2AG-bis errone) et fe97428d
(V2AG-ter rate) restent dans l'historique avec le token original.
Token revoque depuis 08:30 UTC, donc inoffensif. Visibles uniquement via
`git show`. La vue normale du repo HEAD montre desormais les versions caviardees.

## Verdict

Calcule depuis le test mecanique (voir manifest.json).
