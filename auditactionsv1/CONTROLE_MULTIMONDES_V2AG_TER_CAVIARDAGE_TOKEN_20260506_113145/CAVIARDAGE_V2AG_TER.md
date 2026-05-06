# V2AG-ter - Caviardage ancien token revoque

## Contexte

Le fichier V2ACBIS/push_bulletin_sh_content.txt contenait en clair
l'ancien token GitHub PAT ghp_LcNK... revoque le 06/05/2026 a 08:30 UTC.

GitHub Push Protection a detecte ce token au push V2AH Phase 6-bis et
l'a bloque. Le push a ete debloque via Option delta (URL unblock GitHub)
en V2AH Phase 6-ter.

Pour propre lecture humaine sur la page principale du repo GitHub, la
version HEAD du fichier est maintenant caviardee.

## Caviardage applique

Avant : TOKEN=ghp_LcNK... (token en clair)
Apres : TOKEN=ghp_***REDACTED_REVOKED_2026-05-06_08-30-UTC_voir_V2AG_TER***

## Statut historique

Le commit 40d572ac (V2ACBIS) reste dans l'historique Git avec le token
original. Pour le voir : `git show 40d572ac`.

La version HEAD du fichier (vue normale du repo sur GitHub) montre
desormais la version caviardee. Le token ghp_LcNK est revoque cote
GitHub depuis 08:30 UTC, donc inoperant. Sa presence dans l'historique
Git profond est documentaire uniquement.

## Verdict

V2AG_TER_CAVIARDAGE_TOKEN_OK
