## Bio Time Query table missmatch

```sql
select trim(genus || coalesce(species,'')), count(*)
from species 
group by trim(genus || coalesce(species,''))
having count(*)>1
```

| Full Name          | Count |
|--------------------|-------|
| Trisopterusminutus | 2     |
| Asparagopsisarmata | 2     |


```sql
SELECT id, genus, species, genus_species
FROM species
WHERE TRIM(genus || COALESCE(species, '')) IN ('Trisopterusminutus', 'Chloroscombruschrysurus', 'Aulacomniumsp', 'Macrocystispyrifera', 'Asparagopsisarmata')
ORDER BY genus, species;
```

- Cases where genus + species != genus_species

| Genus           | Species               | Name                           | Number |
|-----------------|-----------------------|--------------------------------|--------|
| Aulacomnium     | sp                    | Aulacomnium sp                 | 19     |
| Cestrum         | schlechtendahlii      | Cestrum schechtendahlii        | 8      |
| Chloroscombrus  | chrysurus             | Chloroscombrus chrysurus       | 1      |
| Codium          | setchellii/hubbsii    | Codium setchellii              | 2      |
| Dussia          | sp1                   | Dussia atropurpurea            | 4      |
| Encrusting      | red-algae             | Encrusting red algae           | 731    |
| Filamentous     | green-algae           | Filamentous green algae        | 48     |
| Filamentous     | red-algae             | Filamentous red algae          | 117    |
| Gold            | encrusting-bryozoan   | Gold encrusting bryozoan       | 11     |
| Herrania        | pulcherrima.aff       | Herrania nycterodendron        | 4      |
| Macrocystis     | pyrifera              | Macrocystis pyrifera1          | 545    |
| Macrocystis     | pyrifera              | Macrocystis pyrifera2          | 450    |
| Orange          | encrusting-sponge     | Orange encrusting sponge       | 472    |
| Parchment       | tube-polychaete       | Parchment tube polychaete      | 36     |
| Pink            | encrusting-bryozoan   | Pink encrusting bryozoan       | 1156   |
| Red             | algae                 | Red algae sp                   | 20     |
| Red             | turf-algae            | Red turf algae                 | 63     |
| Rootbeer        | brown-sponge          | Rootbeer brown sponge          | 2      |


---