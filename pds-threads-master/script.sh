#!/bin/bash
# Exemple de script shell qui mesure le temps d'exécution de
# "macommande" avec des arguments différents

echo "# Taille NThreads Temps" > "res.dat"

for ((j = 100; j <= 10**9; j *= 10)); do
    ./aleazard $j > "data.dat"
  for ((i = 1; i <= 2**5; i *= 2)); do
      /usr/bin/time -o "res.dat" -a -f "$j $i %e" ./compteur-gc_t "data.dat" $i > /dev/null
    done
  done

rm "data.dat"