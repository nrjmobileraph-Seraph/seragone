# ADDENDUM V2AG - RECTIFICATION CAGE STATIQUE VS RUNTIME

Addendum documentaire meta-rectification. Ne mute pas les commits anciens. Complete les manifests V1ZW->V2AA par une rectification honnete suite aux decouvertes mecaniques V2AC + V2AC'.

## I. OBJET
Les 9 manifests des commits V1ZW->V2AA inscrivaient la formule "Phase 115 LIVE_TEST_TOTAL_EN_CAGE preservee, decision_weight=0.0 preservee". Cette assertion etait mecaniquement non sourcee : la chaine 27D ne verifiait que la cage statique (sha256 fichiers source), pas la cage runtime (daemons, crons, timers).

V2AC (6 daemons up, timer 35j, 81 crons) et V2AC' (16091 commits auto, cron actif depuis 15 avril) ont revele mecaniquement que le runtime tournait en production live continue pendant toute la chaine 27D.

## II. RECTIFICATION

### Formule originale (dans 9 manifests V1ZW->V2AA)
"Phase 115 LIVE_TEST_TOTAL_EN_CAGE preservee, decision_weight=0.0 preservee"

### Formule rectifiee
"Phase 115 LIVE_TEST_AUDIT_STATIQUE_DANS_RUNTIME_ACTIF preservee, runtime non gele, cage statique seule attestee mecaniquement, decision_weight=0.0 dans verdict statique fige (non verifie a l'execution dans les daemons vivants)"

## III. CE QUI RESTE MECANIQUEMENT VRAI DANS V1ZW->V2AA
- sha256 fichiers source canoniques inchanges
- diff caches surveilles vides sur perimetres V1ZW
- ancrages git valides 9 SHA stables 4f2a18c3 -> 782a6f70
- vrais_yeux.py sha256 f8de03b6...e5850 inchange
- execution sandbox isolee de test_27d_4approches.py
- verdict statique D12 VALIDATED only

## IV. CE QUI ETAIT DECORATIF
- Interpretation runtime de la formule "LIVE_TEST_TOTAL_EN_CAGE"
- Aucun mecanisme ne verifiait l'arret des daemons Seragone
- Aucun mecanisme ne verifiait la desactivation des crons
- Aucun mecanisme ne verifiait l'inactivite des timers systemd
- decision_weight=0.0 etait assertion sur fichier verdict fige, pas execution daemons

## V. PRINCIPE MANIFESTS FUTURS
1. Distinguer explicitement cage statique attestee de cage runtime non attestee
2. Preciser perimetre exact de la cage (liste fichiers + criteres)
3. Si cage runtime cible, la verifier mecaniquement (ps, cron, systemctl, lsof)
4. Si cage Git cible, la verifier mecaniquement (git log auteur, frequence commits)
5. Ne pas inscrire d'assertion non sourcee

## VI. PORTEE
Cet addendum NE MUTE PAS les commits 4f2a18c3 -> 782a6f70. Il les complete par un commit additionnel V2AG portant le tag V2AG_ADDENDUM_RECTIF_CAGE.

L'historique git reste lisible : la chaine 27D figure telle qu'elle a ete posee, avec ses formules d'origine. L'addendum V2AG documente la rectification posterieure.

## VII. VERDICT
V2AG_ADDENDUM_RECTIF_CAGE_OK

## VIII. ATTESTATIONS
Aucune mutation. HEAD 782a6f70 ancre. vrais_yeux.py sha256 f8de03b6...e5850 inchange. 9 ancetres 27D OK. References V2AC, V2AC', V2AF dans manifest.json.
