# REGISTRE CHAINE REEXEC BORN_TEMPS_VALIDATION

## Etapes commitees ou archivees

| Etape | Date UTC | Verdict | Git | Notes |
|-------|----------|---------|-----|-------|
| V1ZH | 2026-05-05 19:53 | ECHEC pandas | (avant lots) | tentative initiale, manquait pandas user-site |
| V1ZI | 2026-05-05 ~19:53 | probe pandas user-site | 0589b809 | resolu via sitecustomize redirect |
| V1ZJ | 2026-05-05 19:54 | OK rc=0 | d1e34590 | exec OK, stdout_tail 7992 oct (= stdout complet en realite) |
| V1ZK | 2026-05-05 ~19:55 | read result | bf40279f | lecture sandbox V1ZJ |
| V1ZP_PRECHECK | 2026-05-05 ~19:50 | OK pret decret | e650751b | extrait params V1ZJ pour decret |
| V1ZL | 2026-05-05 19:59 | crosscheck (BUG) | (hors Git) | bugs path/regex, archive sur disque |
| V1ZM | 2026-05-05 ~20:00 | crosscheck OK | 04a4e939 | corrige V1ZL |
| V1ZN | 2026-05-05 ~20:00 | amendement nominal | b36d6f16 | re-enonce 6 garde-fous V1ZC |
| V1ZO | 2026-05-05 20:11 | inspect V1ZJ | (hors Git) | constat "REEXEC necessaire" |
| V1ZQ | 2026-05-05 20:23 | decret REEXEC | 72f9b18f | decret 3 phases signables |
| V1ZQ-bis | 2026-05-05 ~20:35 | durcissements obligatoires | 03fd4c75 | #1 #2 #3 #4 + variation #5 |
| INCIDENT | 2026-05-05 20:33 | sandbox partielle pre-durcissement | (hors Git) | lancement V1ZQ original avant signature |
| V1ZS | 2026-05-05 ~20:50 | archive incident DECRET | 9b41951f | renommage sandbox partielle DECRET |
| V1ZR (initial) | 2026-05-05 21:32 | sandbox partielle FORMATBUG | (hors Git, archivee) | bugs A (format hash) + B (0 inputs) |
| V1ZR-bis | 2026-05-05 21:38 | Phase 1 durci OK | e759ab84 | sandbox propre, sha256 conformes V1ZJ, non-pollution |
| V1ZT | 2026-05-05 21:48 | Phase 2 EXEC OK rc=0 duree 44s | baca8ccb | stdout 140 lignes 7997 oct, stderr vide, non-pollution, fidelite V1ZJ confirmee |

## Empreintes canoniques figees

- script born_temps_validation.py : sha256 d9acb122719206a370f1058254d1cfc6b51d3586cce1d379426915c2bac1367d (9401 octets, mtime 2026-04-17 15:42:00)
- sitecustomize.py : sha256 9abaa362fcb7b78eb2f2e933794a3df9e8413012a9edf3b212f9ae0298d0fedf (839 octets, mtime 2026-05-05 19:54:42)
- input banc_27d_enrichi_v4.csv : sha256 6850e7f0bb0673498c5db86910570dcf3f6dccb098422c8fd51754f1803ab634 (5020673 octets, mtime 2026-04-23 23:05:50)
- V1ZT stdout_full.log : sha256 9b43795f9c0dbb77dd1352ef02e1a233ab70897d6ef68991c1038fddb3fa86ba (7997 octets brut)
- V1ZT stderr_full.log : sha256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 (vide)

## 9 caches live monitores tout au long de la chaine (5 mesures, identiques)

- data/mondes_paralleles_cache.json : 6a7bd5a7... (present, stable)
- cache/mondes_paralleles_cache.json : bb9ca360... (present, stable)
- production/mondes/data/mondes_paralleles_cache.json : 23aca7f3... (present, stable)
- data/born_state.json : ABSENT (jamais cree pendant la chaine)
- data/born_temps_state.json : ABSENT
- data/multivers_state.json : ABSENT
- data/communicants_history.json : 4a8fca11... (present, stable)
- voix_seragone_92/seragone_92_state.json : ABSENT
- voix_seragone_92/data/seragone_92_state.json : ABSENT

## Posture maintenue

Phase 115 LIVE_TEST_TOTAL_EN_CAGE preservee tout au long de la chaine. decision_weight=0.0 maintenu.
vrais_yeux.py INTOUCHABLE.
Aucun ordre exchange. Aucun broker. Aucun cron edite. Aucun systemd modifie.
Aucune sortie Phase 115. Aucune ecriture caches live (5 mesures identiques).
