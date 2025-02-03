# Obis table general report

## OBIS DOCS: 
### https://manual.obis.org/common_formatissues.html#temporal-dates-and-times


- Columns: 226
- Rows: 108 504 421
- To inspect schema in PgAdmin:

```sql
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public'
AND table_name   = 'obis_20230208';
```


### dataset_id column
- NULL values: 0
- UUID values


### decimallongitude column

- No NULL values
- Float type


### decimallatitude column

- No NULL values
- Float type

### date_start column:

-  NULL values = 5 124 689
-  Min: 0001-03-17 00:00:00  (-62129116800000)  Max: 2023-02-03 00:00:00 (1675382400000)
-  second smallest value: -62127216000000 (0001-04-08 00:00:00)
-  unix time stamp
```shell
>>> from datetime import datetime, timedelta
>>> timestamp_ms = -1789257600000
>>> timestamp_s = timestamp_ms / 1000
>>> epoch = datetime(1970, 1, 1)
>>> delta = timedelta(seconds=timestamp_s)
>>> date_time = epoch + delta
>>> print(f"The date and time is: {date_time}")
    The date and time is: 1913-04-21 00:00:00
```

```sql
SELECT MIN(date_start), MAX(date_start) FROM obis_20230208;
```
```-62129116800000	1675382400000```

- 10 smallest unique timestamps
```python
dates = [
    -62129116800000,
    -62127216000000,
    -62126956800000,
    -62126179200000,
    -62123846400000,
    -62123760000000,
    -62122550400000,
    -62122204800000,
    -62122118400000,
    -62121513600000,
]

"""
The date and time is: 0001-03-17 00:00:00
The date and time is: 0001-04-08 00:00:00
The date and time is: 0001-04-11 00:00:00
The date and time is: 0001-04-20 00:00:00
The date and time is: 0001-05-17 00:00:00
The date and time is: 0001-05-18 00:00:00
The date and time is: 0001-06-01 00:00:00
The date and time is: 0001-06-05 00:00:00
The date and time is: 0001-06-06 00:00:00
The date and time is: 0001-06-13 00:00:00
"""
```


```sql
SELECT to_timestamp(date_start / 1000.0) FROM obis_20230208;
```
`This can convert timestampt to datetime objects without errors`

- 10 most common dates:

| Date                    | Count  |
|-------------------------|--------|
| NULL                    |5124689 |
| 2016-09-15 00:00:00+00  | 275118 |
| 2016-09-14 00:00:00+00  | 262079 |
| 2016-09-13 00:00:00+00  | 232034 |
| 2016-09-20 00:00:00+00  | 226551 |
| 2016-06-22 00:00:00+00  | 182293 |
| 2016-06-15 00:00:00+00  | 174025 |
| 2016-09-08 00:00:00+00  | 173459 |
| 2016-09-16 00:00:00+00  | 171840 |
| 2016-09-06 00:00:00+00  | 169249 |


### date_mid column:

- NULL values: 5 124 689
- Min: 0001-03-17 00:00:00  (-62129116800000)  Max: 2023-02-03 00:00:00 (1675382400000)
- unix time stamp
- all can be converted to datetime format
- 10 smallest unique timestamps

```python
dates = [
    - 62129116800000,
    - 62127216000000,
    - 62126956800000,
    - 62126179200000,
    - 62123846400000,
    - 62123760000000,
    - 62122550400000,
    - 62122204800000,
    - 62122118400000,
    - 62121513600000,
]

"""
The date and time is: 0001-03-17 00:00:00
The date and time is: 0001-04-08 00:00:00
The date and time is: 0001-04-11 00:00:00
The date and time is: 0001-04-20 00:00:00
The date and time is: 0001-05-17 00:00:00
The date and time is: 0001-05-18 00:00:00
The date and time is: 0001-06-01 00:00:00
The date and time is: 0001-06-05 00:00:00
The date and time is: 0001-06-06 00:00:00
The date and time is: 0001-06-13 00:00:00
"""
```

### date_end column
- NULL values: 5 124 689
- Min: 0001-03-17 00:00:00  (-62129116800000)  Max: 2023-02-03 00:00:00 (1675382400000)
- unix time stamp
- all can be converted to datetime format
- 10 smallest unique timestamps
```python
dates = [
    - 62129116800000,
    - 62127216000000,
    - 62126956800000,
    - 62126179200000,
    - 62123846400000,
    - 62123760000000,
    - 62122550400000,
    - 62122204800000,
    - 62122118400000,
    - 62121513600000,
]

"""
The date and time is: 0001-03-17 00:00:00
The date and time is: 0001-04-08 00:00:00
The date and time is: 0001-04-11 00:00:00
The date and time is: 0001-04-20 00:00:00
The date and time is: 0001-05-17 00:00:00
The date and time is: 0001-05-18 00:00:00
The date and time is: 0001-06-01 00:00:00
The date and time is: 0001-06-05 00:00:00
The date and time is: 0001-06-06 00:00:00
The date and time is: 0001-06-13 00:00:00
"""
```


### date_year column
- NULL values: 5 124 689
- Min: 1  Max: 2023
- Integer data type column
- 10 smallest years

| date_year | count 
|-----------|-------|
| 1         | 47    | 
| 196       | 5     |
| 1064      |  2    |
| 1071      | 2     |
| 1073      | 2     |
| 1076      |  1    |
| 1103      | 1     |
| 1104      | 1     |
| 1119      | 2     |
| 1152      | 1     |



### scientificname column
- NULL values: 32 193
- 10 most common values

| Scientific Name        | Count    |
|------------------------|----------|
| Alphaproteobacteria    | 4215851  |
| Larus fuscus           | 2007870  |
| Clupea pallasii        | 1957113  |
| Thermoplasmata         | 1951299  |
| Bacteria               | 1544122  |
| Larus argentatus       | 1323735  |
| Syndiniales            | 1279933  |
| Cyanobacteria          | 1278625  |
| Gadus morhua           | 1236510  |
| Mirounga leonina       | 1157714  |


### originalscientificname column
- NULL values: 32 193
- 10 most common values

| Original Scientific Name | Count    |
|--------------------------|----------|
| Alphaproteobacteria      | 4215842  |
| Larus fuscus             | 2005649  |
| Clupea pallasii          | 1956966  |
| Thermoplasmata           | 1951299  |
| Bacteria                 | 1535071  |
| Larus argentatus         | 1323178  |
| Syndiniales              | 1279933  |
| Cyanobacteria            | 1274611  |
| Gadus morhua             | 1228739  |
| Mirounga leonina         | 1157712  |


### minimumdepthinmeters column
- NULL values: 49 924 796
- Float data type column
- Distinct values: 136 981
- 10 most common values:

| Minimum Depth in Meters | Count    |
|-------------------------|----------|
| NULL                    | 49924796 |
| 0                       | 13876679 |
| 5                       | 3117349  |
| 10                      | 2203641  |
| 50                      | 1775683  |
| 20                      | 1729945  |
| 100                     | 1029237  |
| 75                      | 920205   |
| 30                      | 895681   |
| 25                      | 878899   |


### maximumdepthinmeters column
- NULL values: 45 536 177
- Float data type column
- Distinct values: 136 981
- 10 most common values:

| Maximum Depth in Meters | Count    |
|-------------------------|----------|
| NULL                    | 45536177 |
| 0                       | 8126705  |
| 10                      | 5030700  |
| 20                      | 2434665  |
| 50                      | 1942380  |
| 100                     | 1293067  |
| 75                      | 1076011  |
| 30                      | 1064312  |
| 5                       | 1001552  |
| 40                      | 987863   |


### depth column
- NULL values: 43 176 428
- double precision (float) column type

| Depth | Count    |
|-------|----------|
| NULL  | 43176428 |
| 0     | 8550417  |
| 10    | 2662775  |
| 7.5   | 2335369  |
| 50    | 1952635  |
| 20    | 1805403  |
| 5     | 1599348  |
| 100   | 1202236  |
| 75    | 1116301  |
| 30    | 958897   |


### coordinateuncertaintyinmeters column
- NULL values: 52 903 997
- double precision column data type


### flags column
- NULL Values: 291 487
- 10 most common values:

| Flags                        | Count    |
|------------------------------|----------|
| {}                           | 58829399 |
| {NO_DEPTH}                   | 28069119 |
| {no_depth}                   | 5129380  |
| {ON_LAND,NO_DEPTH}           | 4128522  |
| {NO_DEPTH,ON_LAND}           | 3497062  |
| {ON_LAND}                    | 2673668  |
| {no_depth,on_land}           | 1751781  |
| {DEPTH_EXCEEDS_BATH}         | 1046076  |
| {NO_ACCEPTED_NAME}           | 606637   |
| {DEPTH_EXCEEDS_BATH,ON_LAND} | 550831   |

- char data type for now, but can be converted to list if necessary
```sql
SELECT string_to_array(trim(flags, '{}'), ',') AS flags_array, count(*)
FROM obis_20230208
GROUP BY flags
ORDER BY count(*) DESC;
```

### dropped column
- NULL values : 0
- column data tpe: boolean
- all values =  False


### absence column
- NULL values: 0
- column type boolean
- all values =  False


### shoredistance column
* find out is it meters or what ? 
- NULL values: 0
- column type: double precision
- 10 most common values:

| shoredistance | Count    |
|---------------|----------|
| 5060          | 2552507  |
| 6160          | 2534776  |
| 7753          | 2293236  |
| 3903          | 1498001  |
| 18574         | 1037847  |
| 8916          | 525261   |
| 3649          | 481719   |
| 234           | 290661   |
| 21            | 275144   |
| -1097         | 202690   |


### bathymetrty column:
* what is the measure... ? 

- NULL Valuse: 1716
- column type double precision
- 10 most common values

| Bathymetry | Count   |
|------------|---------|
| 110        | 3176194 |
| -1         | 2792584 |
| 63.98      | 2551612 |
| 85         | 2438135 |
| 2          | 2163988 |
| 43         | 1696036 |
| -2         | 1533419 |
| 1          | 1485514 |
| -3         | 1185940 |
| 28.42      | 1047866 |


### sst column
* sea surface temperature ?

- NULL Values: 5 570 771
- column type: double precision
- 10 most common values:

| SST   | Count   |
|-------|---------|
| NULL  | 5570771 |
| 20.37 | 2705106 |
| 23.45 | 2639427 |
| 14.65 | 2310803 |
| 20.89 | 1517678 |
| 25.57 | 1078015 |
| 28.52 | 558608  |
| 17.2  | 536089  |
| 12.47 | 534454  |
| 11.88 | 409757  |


### sss column
- NULL Values: 5 570 771
- Column type: double precision
- Most common values

| SSS   | Count   |
|-------|---------|
| NULL  | 5570771 |
| 35.4  | 3080868 |
| 35.54 | 3014826 |
| 35.3  | 2752507 |
| 35.53 | 2498254 |
| 35.25 | 1475736 |
| 35.58 | 734365  |
| 33.78 | 688241  |
| 32.01 | 635906  |
| 35.47 | 607161  |



### marine column
- NULL Values: 834 009
- Column type: boolean
- Values
  - True = 106 848 793
  - False = 821 619


### brackish column
- NULL Values: 39 808 017
- Column type: boolean
- Values
  - True = 35 892 419
  - False = 32 803 985


### freshwater column
- NULL Values: 38 204 417
- Column type: boolean


### terrestrial column
- NULL Values: 38 995 811
- Column type: boolean


### taxonrank column
- NULL Values: 119 486
- Column type: Char V 
- Distinct values count: 34
- All distinct values:

| Taxonomic Rank                | Count    |
|-------------------------------|----------|
| Species                       | 73469997 |
| Genus                         | 9774910  |
| Class                         | 9071125  |
| Order                         | 4798586  |
| Family                        | 4596026  |
| Phylum                        | 2526502  |
| Kingdom                       | 1935325  |
| Subspecies                    | 528615   |
| Subclass                      | 341772   |
| Infraorder                    | 167132   |
| Suborder                      | 140769   |
| Superclass                    | 126934   |
| Subphylum                     | 126497   |
| NULL                          | 119486   |
| Infraclass                    | 105840   |
| Infraphylum                   | 105342   |
| Phylum (Division)             | 84509    |
| Subgenus                      | 82350    |
| Subfamily                     | 75990    |
| Superfamily                   | 75585    |
| Variety                       | 74458    |
| Gigaclass                     | 65796    |
| Forma                         | 60016    |
| Superorder                    | 28370    |
| Parvphylum                    | 9813     |
| Subkingdom                    | 4248     |
| Tribe                         | 3899     |
| Subterclass                   | 3813     |
| Infrakingdom                  | 298      |
| Subsection                    | 164      |
| Subphylum (Subdivision)       | 151      |
| Superphylum                   | 56       |
| Parvorder                     | 45       |
| Subvariety                    | 2        |


### aphiaid column
- NULL Values: 0
- Column type: integer
- Min: 1  , Max:  1 634 952


### redlist_category column
- NULL Values: 98 826 521
- Column type: Char V
- Distinct values:

| redlist_category | Count    |
|--------|----------|
| NULL   | 98826521 |
| VU     | 4827236  |
| NT     | 3351039  |
| EN     | 1240370  |
| CR     | 219694   |
| LR/nt  | 26560    |
| LR/cd  | 12451    |
| EW     | 510      |
| EX     | 40       |


### superdomain column
- NULL Values: 11947
- Column type: Char V
- All distinct values:

| superdomain | Count     |
|----------|-----------|
| Biota    | 108492474 |
| NULL     | 11947     |



### domain column
- NULL Values: 108 504 421
- Column type: Char
- All NULL values


### kingdom column
- NULL Values: 87 804
- Column type: Char V
- All distinct values:

| kingdom            | Count    |
|---------------------|----------|
| Animalia            | 78726643 |
| Chromista           | 12451783 |
| Bacteria            | 12169474 |
| Archaea             | 2787986  |
| Plantae             | 1835006  |
| Protozoa            | 366924   |
| NULL                | 87804    |
| Fungi               | 77870    |
| Biota incertae sedis | 914     |
| Protista            | 15       |
| Viruses             | 2        |



### subkingdom column
- NULL Values: 92 608 057
- Column type: Char V
- All distinct values:

| subkingdom                  | Count    |
|---------------------------|----------|
| NULL                      | 92608057 |
| Harosa                    | 11710240 |
| Gracilicutes              | 1432829  |
| Biliphyta                 | 989899   |
| Viridiplantae             | 812119   |
| Hacrobia                  | 735082   |
| Sarcomastigota            | 97386    |
| Eozoa                     | 79744    |
| Protozoa incertae sedis   | 36204    |
| Chromobiota               | 2557     |
| Cryptista                 | 159      |
| Chromista incertae sedis  | 143      |
| Animalia incertae sedis   | 2        |



### infrakingdom column
- NULL Values: 96 404 460
- Column type: Char V
- All distinct values:

| infrakingdom     | Count   |
|--------------|---------|
| NULL         | 96404460|
| Alveolata    | 5079478 |
| Heterokonta  | 5002355 |
| Rhizaria     | 1626761 |
| Streptophyta | 311623  |
| Euglenozoa   | 71912   |
| Excavata     | 7832    |


### phylum column
- NULL Values: 3 943 834
- Column type: Char V
- All distinct values:

| phylum                    | Count    |
|-----------------------------|----------|
| Chordata                    | 51843668 |
| Arthropoda                  | 11553301 |
| Proteobacteria              | 7161804  |
| Ochrophyta                  | 4934665  |
| Mollusca                    | 4672453  |
| Myzozoa                     | 4490903  |
| NULL                        | 3943834  |
| Annelida                    | 3769652  |
| Cnidaria                    | 2916135  |
| Euryarchaeota               | 1959929  |
| Cyanobacteria               | 1432829  |
| Echinodermata               | 1337840  |
| Bacteroidetes               | 1334081  |
| Foraminifera                | 1270338  |
| Porifera                    | 925226   |
| Thaumarchaeota              | 820577   |
| Ciliophora                  | 588559   |
| Haptophyta                  | 457316   |
| Bryozoa                     | 452769   |
| Chaetognatha                | 372705   |
| Verrucomicrobia             | 280978   |
| Cryptophyta                 | 264484   |
| Radiozoa                    | 254862   |
| Nematoda                    | 195185   |
| Planctomycetes              | 176385   |
| Nemertea                    | 139691   |
| Cercozoa                    | 101320   |
| Choanozoa                   | 94138    |
| Euglenozoa                  | 71856    |
| Picozoa                     | 68507    |
| Bigyra                      | 66008    |
| Platyhelminthes             | 63935    |
| Phoronida                   | 51675    |
| Lentisphaerae               | 45769    |
| Chloroflexi                 | 44731    |
| Ctenophora                  | 43866    |
| Rotifera                    | 42221    |
| Actinobacteria              | 37332    |
| Acidobacteria               | 27229    |
| Firmicutes                  | 27070    |
| Priapulida                  | 18310    |
| Brachiopoda                 | 18076    |
| Heliozoa                    | 13282    |
| Deferribacteres             | 12355    |
| Hemichordata                | 12089    |
| Sarcomastigophora           | 10013    |
| Nitrospirae                 | 8650     |
| Loukozoa                    | 7788     |
| Fibrobacteres               | 7429     |
| Chlamydiae                  | 6034     |
| Gemmatimonadetes            | 5871     |
| Crenarchaeota               | 4746     |
| Spirochaetes                | 4483     |
| Bacteria incertae sedis     | 3968     |
| Entoprocta                  | 3794     |
| Gastrotricha                | 3723     |
| Kinorhyncha                 | 3667     |
| Discomitochondria           | 3490     |
| Tenericutes                 | 3063     |
| Amoebozoa                   | 2744     |
| Tardigrada                  | 2512     |
| Xenacoelomorpha             | 2109     |
| Deinococcus-Thermus         | 1689     |
| Chlorobi                    | 1412     |
| Bacillariophyta             | 1161     |
| Loricifera                  | 985      |
| Fusobacteria                | 944      |
| Acanthocephala              | 835      |
| Elusimicrobia               | 657      |
| Oomycota                    | 514      |
| Apusozoa                    | 454      |
| Coelenterata                | 322      |
| Aquificae                   | 193      |
| Synergistetes               | 187      |
| Acritarcha                  | 162      |
| Cryptophycophyta            | 159      |
| Thermotogae                 | 108      |
| Thermodesulfobacteria       | 101      |
| Gnathostomulida             | 96       |
| Korarchaeota                | 85       |
| Nematomorpha                | 83       |
| Dicyemida                   | 66       |
| Sulcozoa                    | 50       |
| Rhizopoda                   | 48       |
| Cephalorhyncha              | 34       |
| Percolozoa                  | 27       |
| Metamonada                  | 17       |
| Cycliophora                 | 5        |
| Orthonectida                | 5        |



### phylum_division column
- NULL Values: 106 624 485
- Column type: Char V
- All distinct values:

| phylum_division                | Count     |
|-------------------------|-----------|
| NULL                    | 106624485 |
| Rhodophyta              | 989899    |
| Chlorophyta             | 500491    |
| Tracheophyta            | 297891    |
| Ascomycota              | 72920     |
| Charophyta              | 11851     |
| Basidiomycota           | 3383      |
| Bryophyta               | 1842      |
| Chytridiomycota         | 691       |
| Craspedophyta_          | 516       |
| Plantae incertae sedis  | 352       |
| Zygomycota              | 37        |
| Magnoliophyta           | 31        |
| Microsporidia           | 15        |
| Glomeromycota           | 12        |
| Marchantiophyta         | 5         |


### subphylum_subdivision column
- NULL Values: 106 847 349
- Column type: Char V
- All distinct values:

| Subphylum/Subdivision   | Count     |
|-------------------------|-----------|
| NULL                    | 106847349 |
| Eurhodophytina          | 939342    |
| Chlorophytina           | 343180    |
| Spermatophytina         | 297007    |
| Pezizomycotina          | 71229     |
| Agaricomycotina         | 2018      |
| Proteorhodophytina      | 1912      |
| Saccharomycotina        | 969       |
| Pucciniomycotina        | 664       |
| Polypodiophytina        | 353       |
| Ustilaginomycotina      | 207       |
| Lycopodiophytina        | 142       |
| Mucoromycotina          | 32        |
| Taphrinomycotina        | 7         |
| Marchantiophytina       | 5         |
| Mortierellomycotina     | 4         |
| Kickxellomycotina       | 1         |



# subphylum column
- NULL Values: 33 642 322
- Column type: Char V
- All distinct values:


| Subphylum                       | Count    |
|---------------------------------|----------|
| Vertebrata                      | 51280531 |
| NULL                            | 33642322 |
| Crustacea                       | 11485487 |
| Dinozoa                         | 4485940  |
| Khakista                        | 3304488  |
| Phaeista                        | 1586284  |
| Asterozoa                       | 778827   |
| Intramacronucleata              | 545729   |
| Tunicata                        | 523497   |
| Echinozoa                       | 435640   |
| Choanofila                      | 93954    |
| Sagenista                       | 62944    |
| Chelicerata                     | 62222    |
| Crinozoa                        | 59031    |
| Filosa                          | 57773    |
| Rhabditophora                   | 41791    |
| Cephalochordata                 | 12992    |
| Rhynchonelliformea              | 9352     |
| Mastigophora                    | 9107     |
| Postciliodesmatophora           | 4153     |
| Apicomplexa                     | 3758     |
| Bicosoecia                      | 3061     |
| Euglenoida                      | 2569     |
| Lobosa                          | 2082     |
| Acoelomorpha                    | 2014     |
| Endomyxa                        | 1853     |
| Craniiformea                    | 1334     |
| Myriapoda                       | 1250     |
| Bacillariophytina               | 1158     |
| Sarcodina                       | 897      |
| Linguliformea                   | 771      |
| Cercozoa incertae sedis         | 719      |
| Ochrophyta incertae sedis       | 287      |
| Catenulida                      | 262      |
| Amoebozoa incertae sedis        | 138      |
| Varisulca                       | 50       |
| Xenoturbellida                  | 39       |
| Tetramitia                      | 27       |
| Platyhelminthes incertae sedis  | 25       |
| Conosa                          | 23       |
| Trichozoa                       | 15       |
| Cristidiscoidia                 | 8        |
| Cryptomonada                    | 7        |
| Coscinodiscophytina             | 3        |
| Opalozoa                        | 3        |
| Aculifera                       | 2        |
| Anaeromonada                    | 2        |


### infraphylum column
- NULL Values: 50 884 914
- Column type: Char V
- All distinct values:


| Infraphylum                          | Count    |
|--------------------------------------|----------|
| Gnathostomata                        | 51248568 |
| NULL                                 | 50884914 |
| Dinoflagellata                       | 4477913  |
| Limnista                             | 1421377  |
| Monista                              | 160394   |
| Ventrata                             | 128912   |
| Rhabdophora                          | 71320    |
| Spirotrichia                         | 69567    |
| Agnatha                              | 29509    |
| Protalveolata                        | 8027     |
| Sporozoa                             | 3611     |
| Intramacronucleata incertae sedis    | 286      |
| Archamoebae                          | 21       |
| Mycetozoa                            | 2        |



### parvphylum column
- NULL Values: 75 171 972
- Column type: Char V
- All distinct values:

| Parvphylum       | Count    |
|------------------|----------|
| NULL             | 75171972 |
| Osteichthyes     | 30568602 |
| Chondrichthyes   | 2763847  |



### gigaclass column
- NULL Values: 77 945 231
- Column type: Char V
- All distinct values:

| Gigaclass       | Count    |
|-----------------|----------|
| NULL            | 77945231 |
| Actinopterygii  | 30559102 |
| Sarcopterygii   | 88       |



### megaclass column
- NULL Values: 90 712 423
- Column type: Char V
- All distinct values:

| Megaclass   | Count    |
|-------------|----------|
| NULL        | 90712423 |
| Tetrapoda   | 17791998 |


### superclass column
- NULL Values: 80 943 143
- Column type: Char V
- All distinct values:


| Superclass             | Count    |
|------------------------|----------|
| NULL                   | 80943143 |
| Reptilia               | 13786602 |
| Multicrustacea         | 10948546 |
| Fucistia               | 1333439  |
| Actinopteri            | 657172   |
| Oligostraca            | 225769   |
| Allotriocarida         | 224006   |
| Hypogyristia           | 146546   |
| Pisces                 | 123005   |
| Ventrifilosa           | 45263    |
| Cyclostomi             | 29507    |
| Neodermata             | 24193    |
| Raphidoistia           | 13848    |
| Aplacophora            | 2136     |
| Monadofilosa           | 852      |
| Annelida incertae sedis | 376     |
| Eopharyngia            | 14       |
| Nucleohelea            | 3        |
| Parabasalia            | 1        |


### class_ column
- NULL Values: 5 764 726
- Column type: Char V
- Total distinct values count: 310
- 10 most common distinct: 

| Class                 | Count    |
|-----------------------|----------|
| Actinopteri           | 29784676 |
| Aves                  | 13279072 |
| Malacostraca          | 6573170  |
| NULL                  | 5764726  |
| Alphaproteobacteria   | 5130372  |
| Dinophyceae           | 4313027  |
| Copepoda              | 4159590  |
| Mammalia              | 4004529  |
| Polychaeta            | 3529845  |
| Bacillariophyceae     | 3253161  |


### subclass column
- NULL Values: 45 154 979
- Column type: Char V
- Total distinct values count: 181
- 10 most common distinct: 

| Class                 | Count    |
|-----------------------|----------|
| Actinopteri           | 29784676 |
| Aves                  | 13279072 |
| Malacostraca          | 6573170  |
| NULL                  | 5764726  |
| Alphaproteobacteria   | 5130372  |
| Dinophyceae           | 4313027  |
| Copepoda              | 4159590  |
| Mammalia              | 4004529  |
| Polychaeta            | 3529845  |
| Bacillariophyceae     | 3253161  |



### infraclass column
- NULL Values: 97 006 824
- Column type: Char V
- Total distinct values count: 181
- All distinct: 

| Infraclass                           | Count    |
|--------------------------------------|----------|
| NULL                                 | 97006824 |
| Neocopepoda                          | 3786565  |
| Selachii                             | 1847881  |
| Canalipalpata                        | 1271890  |
| Heteroconchia                        | 1155127  |
| Batoidea                             | 773320   |
| Scolecida                            | 593456   |
| Pteriomorphia                        | 454222   |
| Euthyneura                           | 434376   |
| Neoasteroidea                        | 350762   |
| Metophiurida                         | 338778   |
| Thoracica                            | 155724   |
| Carinacea                            | 122923   |
| Irregularia                          | 96899    |
| Pterygota                            | 73763    |
| Aulodonta                            | 26314    |
| "Lower Heterobranchia"               | 6539     |
| Rhizocephala                         | 2978     |
| Euhirudinea                          | 2127     |
| Opisthobranchia                      | 1799     |
| Helminthomorpha                      | 823      |
| Mesoneura                            | 772      |
| Acrothoracica                        | 270      |
| Apterygota                           | 215      |
| Neoophora                            | 20       |
| Pulmonata                            | 15       |
| Copepoda incertae sedis              | 12       |
| Polychaeta fossils incertae sedis    | 10       |
| Concentricycloidea                   | 9        |
| [unassigned] Heterobranchia          | 8        |



### subterclass column
- NULL Values: 106 694 426
- Column type: Char V
- All distinct: 


| Subterclass         | Count    |
|---------------------|----------|
| NULL                | 106694426|
| Euheterodonta       | 1113698  |
| Tectipleura         | 246170   |
| Ringipleura         | 181570   |
| Echinacea           | 122923   |
| Atelostomata        | 55401    |
| Neognathostomata    | 41356    |
| Archiheterodonta    | 39295    |
| Acteonimorpha       | 6636     |
| Palaeoheterodonta   | 2114     |
| Eugnatha            | 818      |
| Heterodonta         | 9        |
| Sorbeoconcha        | 5        |


### superorder column
- NULL Values: 89 652 463
- Column type: Char V
- All distinct: 

| Superorder                           | Count    |
|--------------------------------------|----------|
| NULL                                 | 89652463 |
| Eucarida                             | 5001263  |
| Gymnoplea                            | 3057722  |
| Peracarida                           | 1521846  |
| Galeomorphi                          | 1334627  |
| Imparidentia                         | 1070171  |
| Podoplea                             | 728840   |
| Decapodiformes                       | 709791   |
| Chaetocerotanae                      | 632948   |
| Bacillariophycanae                   | 565812   |
| Thalassiosiranae                     | 428099   |
| Squalomorphi                         | 422003   |
| Rhizosolenianae                      | 402347   |
| Fragilariophycanae                   | 307324   |
| Coscinodiscanae                      | 277797   |
| Elopomorpha                          | 225232   |
| Biddulphianae                        | 218246   |
| Ophintegrida                         | 194400   |
| Nudipleura                           | 180496   |
| Valvatacea                           | 172835   |
| Lilianae                             | 170847   |
| Thoracicalcarea                      | 146412   |
| Euryophiurida                        | 144372   |
| Diplostraca                          | 143154   |
| Forcipulatacea                       | 138175   |
| Bacillariophycidae incertae sedis    | 99716    |
| Rosanae                              | 74483    |
| Lithodesmiophycanae                  | 69464    |
| Octopodiformes                       | 52391    |
| Asteranae                            | 43889    |
| Anomalodesmata                       | 43527    |
| Luminacea                            | 40754    |
| Actinochrysia                        | 33748    |
| Pylopulmonata                        | 31494    |
| Pseudotrocha                         | 31207    |
| Spinulosacea                         | 30965    |
| Diadematacea                         | 18563    |
| Corethranae                          | 17599    |
| Cymatosirophycanae                   | 11499    |
| Siphonarimorpha                      | 9978     |
| Eupulmonata                          | 8942     |
| Echinothuriacea                      | 7751     |
| Sacoglossa                           | 6692     |
| Hygrophila                           | 5818     |
| Saxifraganae                         | 4274     |
| Acariformes                          | 4179     |
| Cyathobodoniae                       | 3044     |
| Caryophyllanae                       | 1382     |
| Ceratophyllanae                      | 1260     |
| Ringiculimorpha                      | 1074     |
| Merocheta                            | 810      |
| Macrostomorpha                       | 657      |
| Ranunculanae                         | 646      |
| Eunotiophycanae                      | 378      |
| Gnesiotrocha                         | 376      |
| Parasitiformes                       | 149      |
| Myrothamnanae                        | 121      |
| Phosphatothoracica                   | 115      |
| Acochlidiimorpha                     | 103      |
| Calmanostraca                        | 101      |
| Hypsogastropoda                      | 14       |
| Pachytegmentaria                     | 14       |
| Juliformia                           | 8        |
| Syncarida                            | 5        |
| Cerithiimorpha                       | 4        |
| Ammonoida                            | 2        |
| Magnolianae                          | 2        |
| Proteanae                            | 1        |



### order column
- NULL Values: 15 977 675
- Column type: Char V
- Total distinct count: 1185 
- 10 most common distinct: 

| Order                      | Count    |
|----------------------------|----------|
| NULL                       | 15977675 |
| Charadriiformes            | 7490973  |
| Gadiformes                 | 4942489  |
| Eupercaria incertae sedis  | 4672525  |
| Decapoda                   | 4584076  |
| Pleuronectiformes          | 3760960  |
| Clupeiformes               | 3734194  |
| Perciformes                | 3649842  |
| Calanoida                  | 3056715  |
| Carnivora                  | 2458392  |



### suborder
- NULL Values: 92 109 745
- Column type: Char V
- Total distinct count: 333
- 10 most common distinct: 


| Suborder         | Count   |
|------------------|---------|
| NULL             | 92109745|
| Pleocyemata      | 4196058 |
| Caniformia       | 2458347 |
| Cetancodonta     | 1484225 |
| Globigerinina    | 724208  |
| Spioniformia     | 459983  |
| Cryptodira       | 395383  |
| Senticaudata     | 394566  |
| Amphilochidea    | 383524  |
| Nereidiformia    | 379187  |


### infraorder column
- NULL Values: 99 224 673
- Column type: Char V
- Total distinct count: 89
- 10 most common distinct: 

| Infraorder    | Count    |
|---------------|----------|
| NULL          | 99224673 |
| Pinnipedia    | 2444220  |
| Caridea       | 2041364  |
| Cetacea       | 1484225  |
| Brachyura     | 925485   |
| Astacidea     | 624492   |
| Anomura       | 304687   |
| Lysianassida  | 285868   |
| Achelata      | 262046   |
| Corophiida    | 227389   |


### parvorder column
- NULL Values: 107 650 819
- Column type: Char V
- Distinct values:

| Parvorder               | Count     |
|-------------------------|-----------|
| NULL                    | 107650819 |
| Corophiidira            | 131819    |
| Synopiidira             | 124423    |
| Haustoriidira           | 109393    |
| Caprellidira            | 95528     |
| Gammaridira             | 89793     |
| Physocephalatidira      | 67589     |
| Hadziidira              | 65140     |
| Lysianassidira          | 51975     |
| Oedicerotidira          | 42295     |
| Amphilochidira          | 40681     |
| Eusiridira              | 14650     |
| Talitridira             | 11491     |
| Physosomatidira         | 5739      |
| Colomastigidira         | 1548      |
| Thalassotyphloplanida   | 852       |
| Limnotyphloplanida      | 312       |
| Crangonyctidira         | 140       |
| Ingolfiellidira         | 105       |
| Hyperiopsidira          | 34        |
| Pagetinidira            | 34        |
| Bogidiellidira          | 32        |
| Maxillipiidira          | 26        |
| Podosiridira            | 3         |



### superfamily column
- NULL Values: 94 896 440
- Column type: Char V
- Total distinct count: 723
- 10 most common distinct: 


| Superfamily       | Count   |
|-------------------|---------|
| NULL              | 94896440|
| Pandaloidea       | 1716553 |
| Mysticeti         | 789367  |
| Nephropoidea      | 624309  |
| Odontoceti        | 576163  |
| Chelonioidea      | 395229  |
| Globigerinoidea   | 341607  |
| Tellinoidea       | 329732  |
| Portunoidea       | 318949  |
| Globorotalioidea  | 307132  |



### family column
- NULL Values: 20 037 638
- Column type: Char V
- Total distinct count: 5808
- 10 most common distinct: 

| Family          | Count   |
|-----------------|---------|
| NULL            | 20037638|
| Laridae         | 5035780 |
| Gadidae         | 3621998 |
| Clupeidae       | 3456950 |
| Pleuronectidae  | 3127981 |
| Phocidae        | 2068827 |
| Pandalidae      | 1716317 |
| Procellariidae  | 1313063 |
| Sparidae        | 1282595 |
| Charadriidae    | 1191846 |



### subfamily column
- NULL Values: 91 483 870
- Column type: Char V
- Total distinct count: 1854
- 10 most common distinct: 

| Subfamily         | Count    |
|-------------------|----------|
| NULL              | 91483870 |
| Pleuronectinae    | 3101901  |
| Scombrinae        | 941616   |
| Sebastinae        | 887470   |
| Merlucciinae      | 680313   |
| Salmoninae        | 660465   |
| Scarinae          | 304892   |
| Gobiinae          | 303203   |
| Epinephelinae     | 302079   |
| Globigerininae    | 289762   |



### supertribe column 
- NULL Values: 108 504 413
- Column type: Char V
- Distinct values:

| Supertribe    | Count    |
|---------------|----------|
| NULL          | 108504413|
| Goniaceritae  | 8        |



### tribe column
- NULL Values: 107 188 328
- Column type: Char V
- Total distinct count: 264
- 10 most common distinct: 


| Tribe          | Count    |
|----------------|----------|
| NULL           | 107188328|
| Labiata        | 92289    |
| Ceramieae      | 66765    |
| Corophiini     | 59576    |
| Zonarieae      | 58604    |
| Lanicini       | 54372    |
| Conchoeciini   | 52352    |
| Dictyoteae     | 51880    |
| Palliolini     | 48368    |
| Streblocladieae| 48044    |



### subtribe column
- NULL Values: 108 500 150
- Column type: Char V
- All distinct:

| Subtribe         | Count    |
|------------------|----------|
| NULL             | 108500150|
| Siphonoecetina   | 3431     |
| Bubocorophiina   | 577      |
| Caribboecetina   | 183      |
| Baccharidinae    | 39       |
| Philonthina      | 21       |
| Engelmanniinae   | 6        |
| Solidagininae    | 6        |
| Quediina         | 5        |
| Staphylinina     | 3        |


### genus column
- NULL Values: 24 488 651
- Column type: Char V
- Total distinct count: 30 9969
- 10 most common distinct: 

| Genus           | Count    |
|-----------------|----------|
| NULL            | 24488651 |
| Larus           | 4076949  |
| Clupea          | 2942089  |
| Pandalus        | 1687541  |
| Gadus           | 1400396  |
| Mirounga        | 1166144  |
| Haematopus      | 1148189  |
| Melanogrammus   | 910637   |
| Limanda         | 907767   |
| Sebastes        | 822219   |



### subgenus column
- NULL Values: 107 811 696
- Column type: Char V
- Total distinct count: 646
- 10 most common distinct:

| Subgenus                       | Count     |
|--------------------------------|-----------|
| NULL                           | 107811696 |
| Acartia (Acartiura)            | 90425     |
| Chaetoceros (Hyalochaete)      | 63143     |
| Acartia (Odontacartia)         | 33574     |
| Acartia (Acanthacartia)        | 28805     |
| Caryophyllia (Caryophyllia)    | 26611     |
| Zostera subg. Zostera          | 22136     |
| Lolliguncula (Lolliguncula)    | 21550     |
| Aricidea (Acmira)              | 18282     |
| Globorotalia (Truncorotalia)   | 18179     |


### section column
- NULL Values: 107 600 998
- Column type: Char V
- All distinct values:

| Section                    | Count    |
|----------------------------|----------|
| NULL                       | 107600998|
| Eubrachyura                | 889023   |
| Podotremata                | 14086    |
| Schizophora                | 207      |
| Aplanulata incertae sedis  | 73       |
| Crinocheta                 | 18       |
| Aschiza                    | 16       |



### subsection column
- NULL Values: 107 615 191
- Column type: Char V
- All distinct:

| Subsection     | Count    |
|----------------|----------|
| NULL           | 107615191|
| Heterotremata  | 851965   |
| Thoracotremata | 37058    |
| Acalyptrata    | 146      |
| Calyptrata     | 61       |



### series column
- NULL Values: 108 504 421
- Column type: Char V
- All NULL


### species column
- NULL Values: 34 351 704
- Column type: Char V
- Total distinct count: 146 568
- 10 most common distinct:

| Species                 | Count   |
|-------------------------|---------|
| NULL                    | 34351704|
| Larus fuscus            | 2008150 |
| Clupea pallasii         | 1965805 |
| Larus argentatus        | 1323866 |
| Gadus morhua            | 1236510 |
| Mirounga leonina        | 1157714 |
| Haematopus ostralegus   | 1050027 |
| Clupea harengus         | 976188  |
| Melanogrammus aeglefinus| 910634  |
| Pandalus jordani        | 865454  |



### subspecies column
- NULL Values: 107 971 159
- Column type: Char V
- Total distinct count: 1946
- 10 most common distinct:


| Subspecies                                  | Count     |
|---------------------------------------------|-----------|
| NULL                                        | 107971159 |
| Metridia lucens lucens                      | 87567     |
| Paracalanus parvus parvus                   | 59863     |
| Trichechus manatus latirostris              | 29876     |
| Clausocalanus arcuicornis arcuicornis       | 25659     |
| Arctocephalus australis forsteri            | 24288     |
| Pleuromamma robusta robusta                 | 21203     |
| Eurytemora affinis affinis                  | 17864     |
| Scolecithricella minor minor                | 17582     |
| Pleuromamma gracilis gracilis               | 16236     |



### natio column
- NULL Values: 108 504 421
- Column type: Char V
- ALL NULL


### variety column
- NULL Values: 108 426 668
- Column type: Char 
- Total distinct count: 996
- 10 most common distinct:

| Variety                                      | Count     |
|----------------------------------------------|-----------|
| NULL                                         | 108426668 |
| Actinocyclus octonarius var. octonarius      | 8313      |
| Plagiogramma brockmanni var. brockmanni      | 5456      |
| Pyxidicula compressa var. compressa          | 5354      |
| Chaetoceros subtilis var. subtilis           | 3694      |
| Chaetoceros ceratosporus var. ceratosporus   | 3236      |
| Leptocylindrus danicus var. danicus          | 2285      |
| Ceratium fusus var. fusus                    | 2226      |
| Ceratium gibberum var. dispar                | 2128      |
| Coscinodiscus angstii var. angstii           | 1742      |



### subvariety column
- NULL Values: 108 504 419
- Column type: Char 
- All distinct

| Subvariety                                     | Count     |
|------------------------------------------------|-----------|
| NULL                                           | 108504419 |
| Cardium partschi var. subrostrata transversa   | 1         |
| Stichopathes variabilis var. longispina minor  | 1         |



### forma column
- NULL Values: 108 444 257
- Column type: Char 
- Total distinct count: 362
- 10 most common distinct:

| Forma                                      | Count    |
|--------------------------------------------|----------|
| NULL                                       | 108444257|
| Rhizosolenia fragilissima f. fragilissima  | 30621    |
| Triceratium alternans f. alternans         | 5747     |
| Synedra nitzschioides f. nitzschioides     | 2753     |
| Cheilosporum sagittatum f. minor           | 2675     |
| Fragilaria oceanica f. oceanica            | 1719     |
| Rhizosolenia setigera f. pungens           | 1655     |
| Chaetoceros convolutus f. trisetosa        | 1606     |
| Nitzschia panduriformis f. panduriformis   | 1454     |
| Proboscia alata f. gracillima              | 1317     |


### subforma column
- NULL Values: 108 504 421
- Column type: Char 
- ALL NULL


### type column
- NULL Values: 92 505 716
- Column type: Char 
- All distinct

| Type                         | Count    |
|------------------------------|----------|
| NULL                         | 92505716 |
| Event                        | 10498229 |
| Collection                   | 1844329  |
| sample level information     | 1137902  |
| Dataset                      | 894566   |
| PhysicalObject               | 784726   |
| Physical Object              | 245598   |
| Evento                       | 236150   |
| Set/tow level information    | 172582   |
| event                        | 89824    |
| sample                       | 36934    |
| Text                         | 27684    |
| Objeto físico                | 18772    |
| individual sample            | 2459     |
| Catch                        | 2007     |
| StillImage                   | 1751     |
| trip level information       | 1630     |
| Sample                       | 918      |
| checklist                    | 775      |
| bacterial strain culture     | 410      |
| station                      | 408      |
| Objeto físco                 | 258      |
| Occurrence                   | 214      |
| text                         | 200      |
| MovingImage                  | 90       |
| Imagen estática              | 61       |
| Deploy                       | 47       |
| Track                        | 47       |
| Imagén estática              | 46       |
| Accession                    | 29       |
| Objeto f�sico                | 27       |
| cruise                       | 13       |
| Transect                     | 11       |
| Imagen en movimiento         | 7        |
| Identification               | 1        |


### modified column
- NULL Values: 32 945 083
- Column type: Char 
- Total distinct count: 1 474 500
- 10 most common distinct:

| Modified                | Count    |
|-------------------------|----------|
| NULL                    | 32945083 |
| 2011-01-01 00:00:00     | 4352791  |
| 2022-01-18 09:29:51     | 3360950  |
| 2020-08-04              | 2783422  |
| 2018-04-09 15:18:52     | 2235981  |
| 2020-09-01 12:26:06     | 2112490  |
| 2017-01-15              | 1531079  |
| 2022-01-17              | 1510107  |
| 2021-07-06 10:44:36     | 1021952  |
| 2015-07-22 14:03:01     | 793076   |


### language column
- NULL Values: 89 489 197
- Column type: Char
- All distinct:

| Language | Count    |
|----------|----------|
| NULL     | 89489197 |
| en       | 16109468 |
| En       | 2605872  |
| es       | 254544   |
| pt       | 39130    |
| Engish   | 2818     |
| English  | 2459     |
| ES       | 905      |
| EN       | 27       |
| x`       | 1        |



### license column
- NULL Values: 78 710 567
- Column type: Char 
- Total distinct count: 69
- Licences (Code or URl)
* Copyright Turks and Caicos Islands Whale Project. No use without permission.
* CC-BY-SA
* UNSPECIFIED


###  rightsholder column
- NULL Values: 90 070 930
- Column type: Char 
- Total distinct count: 8560
- 10 most common distinct:

| rightsholder                                                                                                     | Count    |
|------------------------------------------------------------------------------------------------------------------|----------|
| Her Majesty the Queen in right of Canada, as represented by the Minister of Fisheries and Oceans                | 7905592  |
| INBO                                                                                                             | 3143481  |
| Her Majesty the Queen in right of Canada                                                                         | 1923172  |
| NIOO-KNAW                                                                                                        | 656050   |
| Fishermen and Scientists Research Society (FSRS)                                                                 | 491668   |
| Her Majesty the Queen in right of Canada, as represented by the Minister of Fisheries and Oceans'               | 481043   |
| Ministry for Primary Industries                                                                                  | 423993   |
| Sovon                                                                                                            | 361033   |
| Her Majesty the Queen in right of Canada, as represented by the Minister of Environment Canada                   | 210034   |
| Departament of Planing and Natural Resources of the U.S. Virgin Islands and the University of Virgin Islands     | 163220   |


### accessrights column
- NULL Values: 107 703 486
- Column type: Char 
- Total distinct count: 898
- 10 most common distinct:

| accessrights                                                                                                                                                                | Count   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Creative Commons Attribution 3.0 New Zealand Licence                                                                                                                   | 411926  |
| http://vertnet.org/resources/norms.html                                                                                                                                | 170258  |
| Subject to Term and Conditions of Use of the International Seabed Authority Website https://www.isa.org.jm/authority/term-and-conditions-use-international-seabed-authority-website | 46721   |
| http://www.vertnet.org/resources/norms.html                                                                                                                            | 38713   |
| http://biodiversity.ku.edu/research/university-kansas-biodiversity-institute-data-publication-and-use-norms                                                           | 32870   |
| Sólo para uso no comercial citando la fuente                                                                                                                           | 27319   |
| http://creativecommons.org/publicdomain/zero/1.0/ & http://www.canadensys.net/norms                                                                                   | 22137   |
| Sólo para uso no comercial                                                                                                                                            | 10245   |
| To the extent possible under law, the authors have waived all copyright and related or neighboring rights to this data CC0 1.0 Universal (CC0 1.0)                   | 4563    |



### bibliographiccitation column
- NULL Values: 69 041 100
- Column type: Char 

| Bibliographic Citation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Count    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| Brown, M. V. et al. Continental scale monitoring of marine microbiota by the Australian Marine Microbial Biodiversity Initiative. Sci. Data 5:180130 doi: 10.1038/sdata.2018.130 (2018).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 10900182 |
| Oceanographic boundaries constrain microbial diversity gradients in the South Pacific Ocean. Eric J. Raes, Levente Bodrossy, Jodie van de Kamp, Andrew Bissett, Martin Ostrowski, Mark V. Brown, Swan L. S. Sow, Bernadette Sloyan, Anya M. Waite. Proceedings of the National Academy of Sciences Aug 2018, 201719335; doi: 10.1073/pnas.1719335115 Brown, M. V. et al. Continental scale monitoring of marine microbiota by the Australian Marine Microbial Biodiversity Initiative. Sci. Data 5:180130 doi: 10.1038/sdata.2018.130 2018). Raes, Eric J.,van de Kamp, Jodie,Bodrossy, Levente,Fong, Allison A.,Riekenberg, Jessica,Holmes, Bronwyn H.,Erler, Dirk V.,Eyre, Bradley D.,Weil, Sarah-Sophie,Waite, A. M. (2020) N2 Fixation and New Insights Into Nitrification From the Ice-Edge to the Equator in the South Pacific Ocean. Frontiers in Marine Science 7 pp-. https://doi.org/10.3389/fmars.2020.00389 | 3868632  |
| North Sea International Bottom Trawl Survey                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 2960129  |



### references column
- NULL Values: 101 193 246
- Column type: Char 
- Total distinct count: 1 809 453
- 10 most common distinct:

| Reference                                                                                                                                                                                                                                                       | Count    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| doi:10.1016/j.fishres.2011.01.012                                                                                                                                                                                                                               | 1616667  |
| https://accession.nodc.noaa.gov/0162472. https://accession.nodc.noaa.gov/0178974. https://doi.org/10.7289/v5tb1564. https://doi.org/10.7289/v58c9tkb. https://doi.org/10.7289/v5c827m0. https://doi.org/10.7289/v59c6vr5. doi:10.7289/V5SN06ZT                     | 698900   |
| https://github.com/HakaiInstitute/jsp-data                                                                                                                                                                                                                      | 311595   |
| Coral Reef Ecosystem Program; Pacific Islands Fisheries Science Center (2016). Pacific Reef Assessment and Monitoring Program: Rapid Ecological Assessments of Fish Belt Transect Surveys (BLT) at Coral Reef Sites across the Pacific Ocean from 2000 to 2009. | 245139   |
| https://sites.google.com/site/usvitcrmp/publications?authuser=0                                                                                                                                                                                                 | 163220   |
| https://doi.pangaea.de/10.1594/PANGAEA.917680                                                                                                                                                                                                                   | 80990    |
| Departament of Natural and Environmental Resources (DNER) and NOAA Coral Reef Conservation and Management Program (CRCP). 2001, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2014, 2015, 2016, 2017, 2018. Puerto Rico Coral Reef Monitoring Program Reports | 74892    |
| http://www.oilandgasuk.co.uk/knowledgecentre/uk_benthos_database.cfm                                                                                                                                                                                            | 56200    |
| https://accession.nodc.noaa.gov/0162463.; Houk P. Camacho R. Johnson S. McLean M. Maxin S. Anson J. et al. (2015) The Micronesia Challenge: Assessing the Relative Contribution of Stressors on Coral Reefs to Facilitate Science-to-Management Feedback.       | 47236    |


### institutionid column
- NULL Values: 94 933 653
- Column type: Char 
- Total distinct count: 5515
- 10 most common distinct:


| InstitutionID                                                                                                                                                            | Count    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| NULL                                                                                                                                                          | 94933653 |
| [https://edmo.seadatanet.org/report/4180](https://edmo.seadatanet.org/report/4180)                                                                                       | 5645507  |
| [https://edmo.seadatanet.org/report/1811](https://edmo.seadatanet.org/report/1811)                                                                                       | 2521420  |
| ESD                                                                                                                                                                      | 727645   |
| DFO-NAFC                                                                                                                                                                 | 541940   |
| FSRS                                                                                                                                                                     | 491668   |
| [https://www.gbif.org/publisher/55897143-3f69-42f1-810d-ae94b55fde24](https://www.gbif.org/publisher/55897143-3f69-42f1-810d-ae94b55fde24), [https://oceanexpert.org/institution/20121](https://oceanexpert.org/institution/20121), [https://edmo.seadatanet.org/report/5148](https://edmo.seadatanet.org/report/5148) | 311595   |
| BIO                                                                                                                                                                      | 292017   |
| [https://ror.org/02apffz65](https://ror.org/02apffz65)                                                                                                                   | 245139   |
| [http://grscicoll.org/institution/california-academy-sciences](http://grscicoll.org/institution/california-academy-sciences)                                             | 244674   |


### collectionid column
- NULL Values: 105 991 199
- Column type: Char 
- Total distinct count: 7125
- 10 most common distinct:


| Collection ID                                                                  | Count   |
|--------------------------------------------------------------------------------|---------|
| NULL                                                                           | 105991199 |
| 14                                                                             | 158179  |
| 25                                                                             | 148572  |
| urn:lsid:biocol.org:col:35205                                                  | 148444  |
| 70                                                                             | 144201  |
| http://grscicoll.org/institutional-collection/cas-ichthyology                  | 142510  |
| 56bf7b66-ed07-4b91-9f0d-1f00de11fab8                                           | 141136  |
| 62                                                                             | 129938  |
| 10                                                                             | 125316  |
| https://www.gbif.org/grscicoll/collection/5d4a63d3-e994-4b19-b592-e853a8e3b470 | 102164  |


### datasetid column
- NULL Values: 58 297 911
- Column type: Char 
- Total distinct count: 20 042
- 10 most common distinct:

| Dataset ID                             | Count    |
|----------------------------------------|----------|
| NULL                                   | 58297911 |
| https://marineinfo.org/id/dataset/2763 | 2960129  |
| https://marineinfo.org/id/dataset/216  | 2112490  |
| https://doi.org/10.5281/zenodo.6579497 | 1749504  |
| 427                                    | 1122012  |
| https://doi.org/10.5281/zenodo.6594838 | 1120105  |
| https://marineinfo.org/id/dataset/5922 | 1104255  |
| https://marineinfo.org/id/dataset/4494 | 793076   |
| https://marineinfo.org/id/dataset/8015 | 772508   |
| https://marineinfo.org/id/dataset/2760 | 768630   |



### institutioncode column
- NULL Values: 21 546 582
- Column type: Char 
- Total distinct count: 27553
- 10 most common distinct:

| Institution Code                        | Count    |
|-----------------------------------------|----------|
| NULL                                    | 21546582 |
| BioPlatforms                            | 18170940 |
| ICES                                    | 7191258  |
| PBS                                     | 5708478  |
| MPIAB                                   | 4166777  |
| MCM                                     | 3036751  |
| Bedford Institute of Oceanography (BIO) | 2529883  |
| IMOS                                    | 1749800  |
| CLO                                     | 1471592  |
| Pangaea                                 | 1303564  |



### collectioncode coolumn
- NULL Values: 26 892 130
- Column type: Char 
- Total distinct count: 57425
- most common distinct:

| Collection Code                             | Count    |
|---------------------------------------------|----------|
| NULL                                        | 26892130 |
| Movebank                                    | 4166777  |
| BioPlatforms Marine microbes in2016_v03     | 3868632  |
| DATRAS-NS-IBTS                              | 2960129  |
| LINE                                        | 2744112  |
| BioPlatforms Marine microbes NRS NSI        | 2537024  |
| BioPlatforms Marine microbes NRS PHB        | 2533383  |
| BioPlatforms Marine microbes NRS MAI        | 2291980  |
| BioPlatforms Marine microbes in2016_v04     | 2137795  |
| CPR                                         | 2112490  |
| IMOS_ATF_AD                                 | 1517914  |
| BioPlatforms Marine microbes NRS ROT        | 1495964  |
| 427                                         | 1122012  |
| BioPlatforms Marine microbes NRS YON        | 1037262  |


### datasetname column
- NULL Values: 70 199 340
- Column type: Char 
- Total distinct count: 7775
- most common distinct:

| Dataset Name                                                                                                    | Count    |
|-----------------------------------------------------------------------------------------------------------------|----------|
| NULL                                                                                                            | 70199340 |
| CPR                                                                                                             | 2112490  |
| Herring Biosample Database                                                                                      | 1923172  |
| LBBG_ZEEBRUGGE - Lesser black-backed gulls (Larus fuscus, Laridae) breeding at the southern North Sea coast    | 1749504  |
| MARITIMES SUMMER RESEARCH VESSEL SURVEY                                                                         | 1519459  |
| JNCC seabird distribution and abundance data (all trips) from ESAS database                                    | 1122012  |
| HG_OOSTENDE - Herring gulls (Larus argentatus, Laridae) breeding at the southern North Sea coast (Belgium)      | 1120105  |
| RSMP Baseline Dataset                                                                                           | 1104255  |
| Marine Recorder Snapshot extract of surveys entered by JNCC                                                     | 772508   |
| Marine Recorder Snapshot extract of surveys entered by SeaSearch                                                | 727614   |


### ownerinstitutioncode column
- NULL Values: 98 291 929
- Column type: Char 
- Total distinct count: 3587
- most common distinct:

| Owner Institution Code                | Count    |
|---------------------------------------|----------|
| NULL                                  | 98291929 |
| NOAA FKNMS                            | 1616667  |
| NOAA                                  | 1231041  |
| European Seabirds at Sea              | 1122012  |
| HARC                                  | 633661   |
| NMFS                                  | 564982   |
| Washington Dept. of Fish and Wildlife | 469111   |
| NORMANDEAU                            | 435776   |
| Ministry for Primary Industries       | 412987   |
| USGS-FWS                              | 374584   |


### basisofrecord column
- NULL Values:  90
- Column type: Char 
- Total distinct count: 146
- most common distinct:

| Basis of Record            | Count    |
|----------------------------|----------|
| HumanObservation           | 46314571 |
| Occurrence                 | 21167987 |
| MaterialSample             | 18517070 |
| MachineObservation         | 11726993 |
| PreservedSpecimen          | 10098970 |
| Human observation          | 543538   |
| LivingSpecimen             | 60780    |
| humanobservation           | 18382    |
| S                          | 17345    |
| O                          | 16973    |
| preservedspecimen          | 3455     |
| humanObservation           | 3317     |
| materialSample             | 2559     |
| D                          | 2474     |
| NomenclaturalChecklist     | 2265     |
| Humanobservation           | 2237     |
| DerivedFromLiterature      | 1242     |
| preservedSpecimen          | 634      |
| Human Observation          | 383      |
| FossilSpecimen             | 316      |
| machineobservation         | 297      |
| 123                        | 120      |
| 122.5                      | 109      |
| 123.25                     | 90       |
| NULL                       | 90       |
| 122                        | 89       |
| Marine Species             | 88       |
| 121.75                     | 76       |
| 123.5                      | 69       |
| 121.5                      | 58       |
| 124                        | 57       |



### informationwithheld column
- NULL Values:  103 800 229
- Column type: Char 
- Total distinct count: 103
- most common distinct:

| Information Withheld                                                   | Count    |
|------------------------------------------------------------------------|----------|
| NULL                                                                   | 103800229|
| see metadata                                                           | 4166391  |
| collector identities withheld                                          | 276600   |
| Detection functions to determine densities                             | 210019   |
| HumanObservation                                                       | 23669    |
| This dataset contains presence information only. Abundance (numbers per cubic metre) is not provided at this time. | 13162 |
| Contact data provider for information on abundance, sizes and biomass. | 6537     |
| No information is withheld.                                            | 4437     |
| Dataset only contains species identified to species level and where catch count has been recorded. | 2809  |
| original publication contains detailed information                     | 213      |
| mask specimen remarks                                                  | 139      |
| Observadores                                                           | 11       |
| Dataset contains size measurements. Number of individuals measured =1  | 10       |
| Dataset contains size measurements. Number of individuals measured =11 | 10       |
| Dataset contains size measurements. Number of individuals measured =2  | 10       |



### datageneralizations column
- NULL Values: 102 976 207
- Column type: Char 
- Total distinct count: 1004
- most common distinct:


| Data Generalizations                                                                                                                              | Count     |
|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| NULL                                                                                                                                             | 102976207 |
| subsampled by hour: first of 3 record(s)                                                                                                          | 1634828   |
| subsampled by hour: first of 1 record(s)                                                                                                          | 808462    |
| Surveys were conducted during the daytime hours between 08:00 and 16:00 local time. The "eventDate" UTC time was set to represent 08:00 local time, while the actual survey time may have actually occurred later. | 698900    |
| subsampled by hour: first of 2 record(s)                                                                                                          | 425992    |
| Decimal latitude and longitude represent the approximate geographic centre of each Pacific Fishery Management Area (PFMA)                        | 314364    |
| subsampled by hour: first of 4 record(s)                                                                                                          | 246405    |
| Surveys were conducted during the daytime hours between 08:00 and 16:00 local time. The "eventDate" UTC time was set to represent 08:00 local time while the actual survey time may have actually occurred later. | 245139    |
| subsampled by hour: first of 6 record(s)                                                                                                          | 239501    |
| subsampled by hour: first of 20 record(s)                                                                                                         | 203178    |
| subsampled by hour: first of 12 record(s)                                                                                                         | 169193    |
| subsampled by hour: first of 13 record(s)                                                                                                         | 69434     |



### dynamicproperties column
- NULL Values: 97 196 156
- Column type: Char 
- Total distinct count: 540536
- most common distinct:

| Dynamic Properties                               | Count   |
|--------------------------------------------------|---------|
| NULL                                             | 97196156|
| observedindividualcount=1;                       | 642786  |
| SampleSize=%;                                    | 460673  |
| SampleSize=#;                                    | 308514  |
| SampleSize=3704 meters;                          | 193989  |
| SampleSize=1 m²;                                 | 168171  |
| observedindividualcount=2;                       | 129181  |
| observedindividualcount=0;                       | 88045   |
| project=DigIn                                    | 87196   |
| SampleSize=3519 meters;                          | 85469   |
| observedindividualcount=3;                       | 71950   |
| SampleSize=0.1 m²;                               | 69400   |
| Sample size = ; Classification=WoRMS             | 68061   |
| SampleSize=10 nautical mile samples (abundance per cubic metre); | 62881   |
| SampleSize=#/g;                                  | 60004   |



### materialsampleid column 
- NULL Values: 89 525 557
- Column type: Char 
- Total distinct count: 414 451
- most common distinct:

| Material Sample ID    | Count   |
|-----------------------|---------|
| NULL                  | 89525557|
| NA                    | 110539  |
| 102.100.100/21757     | 13336   |
| 102.100.100/139935    | 13283   |
| 102.100.100/21743     | 13128   |
| 102.100.100/139933    | 12650   |
| 102.100.100/21742     | 12359   |
| 102.100.100/21733     | 12300   |
| 102.100.100/21740     | 12283   |
| 102.100.100/21751     | 12035   |
| 102.100.100/21763     | 12028   |
| 102.100.100/141270    | 11738   |
| 102.100.100/21825     | 11717   |
| 102.100.100/139916    | 11597   |


### occurrenceid column
- NULL Values: 9 978 445
- Column type: Char 
- Total distinct count: 414 451
- most common distinct:


### occurrenceid 
- Null Values: 9 978 445

| Occurrence ID                              |
|--------------------------------------------|
| 0                                          |
| 0000000000000000050207-nodc.ogs.trieste.it |
| 0000000000000000050316-nodc.ogs.trieste.it |
| 0000000000000000050352-nodc.ogs.trieste.it |
| 0000000000000000050353-nodc.ogs.trieste.it |
| 0000000000000000050354-nodc.ogs.trieste.it |
| 0000000000000000050397-nodc.ogs.trieste.it |
| 0000000000000000050422-nodc.ogs.trieste.it |
| 0000000000000000050441-nodc.ogs.trieste.it |
| 0000000000000000050464-nodc.ogs.trieste.it |



### catalognumber 
- NULL Values: 31 091 594
- Data:

| Catalog Number                                   |
|--------------------------------------------------|
| Trawl tan0709/7 HTH                              |
| 2.00709e+21                                      |
| MRMCS01900004862                                 |
| Bramber, NS_2013-05-24_Blueback Herring          |
| MRCON04200006A97                                 |
| 2013-50360                                       |
| 20000002154167                                   |


### occurrenceremarks
- NULL Values: 80 960 982
- Column type: Char 
- Total distinct count: 3 045 144
- most common distinct:

| Occurrence Remarks                                      | Count    |
|---------------------------------------------------------|----------|
| NULL                                                    | 80960982 |
| GOV Trawl                                                | 3578456  |
| Visual; boat                                             | 1886939  |
| Visual; plane                                            | 1360886  |
| Telemetry                                                | 1082784  |
| Taxonomic name derived from genomic sequence comparisons | 853365   |
| NA                                                       | 541538   |
| Instantaneous observation                                | 485346   |
| Occurrence Type: Catch measurement                       | 353065   |
| Acoustic detection                                       | 297063   |



### recordnumber 
- NULL Values: 100 449 310
- Column type: Char 
- Total distinct count: 6 917 662
- most common distinct:

| Record Number | Count     |
|---------------|-----------|
| NULL          | 100449310 |
| 870           | 52716     |
| 120472        | 35980     |
| 287           | 28586     |
| 40564         | 22703     |
| 900           | 18129     |
| 53785         | 17071     |
| 11CF_RSP084   | 13089     |
| 11CF_RSP018   | 12022     |
| 2006P9        | 10899     |


### recordedby
- NULL Values: 64 179 896
- Column type: Char 
- Total distinct count: 162 058
- most common distinct:

| Recorded By                                  | Count    |
|---------------------------------------------|----------|
| NULL                                        | 64179896 |
| Jodie van de Kamp                           | 13417487 |
| North Sea International Bottom Trawl Survey | 2960129  |
| Martin Ostrowski                            | 2137795  |
| nan                                         | 1605543  |
| Mark Brown                                  | 832574   |
| Contact: MarineRecorder@jncc.gov.uk         | 772508   |
| Baltic International Trawl Survey           | 768630   |
| Contact: info@seasearch.org.uk              | 727614   |
| BFCG (Bundesforschungsanstalt fnr Fischerei)| 574548   |
| ADCNR/GCRL                                  | 564982   |



### recordedbyid
- NULL Values: 108 486 960
- Column type: Char 
- Total distinct count: 30
- most common distinct:

| RecordedByID                                                                                      | Count     |
|---------------------------------------------------------------------------------------------------|-----------|
| NULL                                                                                              | 108486960 |
| https://orcid.org/0000-0003-3556-006X                                                             | 5187      |
| https://orcid.org/0000-0002-9223-9750                                                             | 3481      |
| https://orcid.org/0000-0003-3610-8155                                                             | 2559      |
| https://orcid.org/0000-0002-7535-3228                                                             | 2531      |
| https://orcid.org/0000-0003-3819-2004 \| https://orcid.org/0000-0001-8852-0796                    | 528       |
| https://www.wikidata.org/wiki/Q29167703                                                           | 498       |
| https://orcid.org/0000-0001-5915-2816                                                             | 350       |
| https://orcid.org/0000-0002-3154-8832 \| https://orcid.org/0000-0003-1474-1654                    | 346       |
| https://orcid.org/0000-0002-2393-7328 \| https://orcid.org/0000-0001-5089-6472                    | 321       |



### individualcount

- CAN BE CAST TO FLOAT

```sql
SELECT individualcount::double precision
FROM obis_20230208
WHERE pg_input_is_valid(individualcount, 'double precision');
```

- NULL Values: 81 587 212
- Column type: Char 
- Total distinct count: 150224
- most common distinct:

| Individual Count | Count    |
|------------------|----------|
| NULL             | 81587212 |
| 1                | 8849664  |
| 1.0              | 2327157  |
| 2                | 1492522  |
| 3                | 779925   |
| 2.0              | 756952   |
| 4                | 468285   |
| 3.0              | 399746   |
| 5                | 360913   |
| 15000.0          | 356199   |



### organismquantity

-> Non numeric values in column: NA, present, unknown, 40-80%, middle, sparse, dense, Individuals, 5001 - 10000, <5, >80%, n/a

- NULL Values: 80 017 248
- Column type: Char 
- Total distinct count: 235 445
- most common distinct:

| Organism Quantity | Count    |
|-------------------|----------|
| NULL              | 80017248 |
| 1                 | 7643567  |
| 2                 | 3015471  |
| 3                 | 2000149  |
| 4                 | 1443934  |
| 5                 | 1114226  |
| 6                 | 888587   |
| 7                 | 709867   |
| NA                | 651339   |
| 8                 | 610710   |



### organismquantitytype
- NULL Values: 79 284 334
- Column type: Char 
- Total distinct count:  205
- most common distinct:

| Quantity Type                          | Count    |
|----------------------------------------|----------|
| NULL                                   | 79284334 |
| DNA sequence reads                     | 18241773 |
| individuals                            | 5245607  |
| detections per day                     | 1525914  |
| individual                             | 1110085  |
| Biomass kg wet per sq m                | 649286   |
| Relative Abundance                     | 375694   |
| Individuals                            | 251040   |
| Cells per litre                        | 181654   |
| number of individuals per 120 m3       | 153944   |


### sex
- NULL Values: 86 008 149
- Column type: Char 
- Total distinct count:  639
- most common distinct:

| Sex      | Count   |
|----------|---------|
| NULL     | 86008149|
| U        | 7824983 |
| female   | 3395087 |
| male     | 3263200 |
| F        | 1398673 |
| M        | 1045618 |
| Male     | 738909  |
| FEMALE   | 615759  |
| Unknown  | 550708  |
| Female   | 498219  |



### lifestage
- NULL Values: 96 865 562
- Column type: Char 
- Total distinct count:  3037
- most common distinct:

| Life Stage                 | Count     |
|----------------------------|-----------|
| NULL                       | 96865562  |
| NA                         | 2689469   |
| Adult                      | 1675270   |
| U                          | 800304    |
| adult                      | 685412    |
| Mixed for pooled specimens | 554072    |
| juvenile                   | 365239    |
| Subadult                   | 242827    |
| Not specified              | 214197    |
| LV                         | 201118    |



### reproductivecondition
- NULL Values: 108 244 059
- Column type: Char 
- Total distinct count:  168
- most common distinct:

| Reproductive Status       | Count     |
|--------------------------|-----------|
| NULL                     | 108244059 |
| not berried              | 201525    |
| berried                  | 44317     |
| NA                       | 8959      |
| reproductive             | 3883      |
| non-reproductive         | 725       |
| --                       | 402       |
| unknown                  | 180       |
| [no gonad data]          | 97        |
| Reproductivo             | 26        |
| ova <1mm                 | 18        |



### behavior
- NULL Values: 107 903 640
- Column type: Char 
- Total distinct count:  291
- most common distinct:

| behavior                              | Count    |
|---------------------------------------|----------|
| NULL                                  | 107903640|
| NA                                    | 178252   |
| F=Flying and W=on water: F            | 116482   |
| F=Flying and W=on water: W            | 93164    |
| FLYING                                | 52407    |
| SITTING                               | 31637    |
| 8                                     | 24913    |
| F                                     | 23368    |
| 1                                     | 13533    |
| Alimentandose                         | 7875     |


### establishmentmeans
- NULL Values: 108 314 194
- Column type: Char 
- Total distinct count:  14
- All distinct:

| establishmentmeans           | Count   |
|------------------|---------|
| NULL             | 108314194|
| native           | 166088  |
| wild             | 21557   |
| Wild Observation | 1274    |
| introduced       | 287     |
| Native           | 199     |
| invasive         | 193     |
| Silvestre        | 173     |
| Introduced       | 159     |
| Silvestre, Exótico | 156   |
| unknown          | 137     |
| managed          | 2       |
| Criptogénica     | 1       |
| Introducida      | 1       |



### occurrencestatus
- NULL Values: 15 050 824
- Column type: Char 
- Total distinct count:  30
- Distinct values:

| occurrencestatus           | Count      |
|------------------|------------|
| present          | 88977059   |
| Present          | 15050824   |
| P                | 3038361    |
| Q                | 1054572    |
| Presence         | 297049     |
| Presente         | 40508      |
| NA               | 36525      |
| 1                | 4431       |
| presence         | 2550       |
| Rare             | 835        |
| Occasional       | 553        |
| Occurrence       | 359        |
| Frequent         | 150        |
| Common           | 140        |
| alive            | 88         |
| Absence          | 60         |
| Abundant         | 56         |
| null             | 55         |
| common           | 33         |
| Ausent           | 24         |
| frequent         | 20         |
| rare             | 18         |
| abundant         | 8          |
| Historic         | 6          |
| ND               | 6          |
| dead             | 5          |
| Dead             | 5          |
| few              | 5          |
| Occasional-Abundant | 1      |


### preparations
- NULL Values: 103 618 764
- Column type: Char 
- Total distinct count:  12 625
- Distinct values:

| Preparations                              |   Count |
|------------------------------------------|---------|
| null                                     | 103618764 |
| Frozen                                   |  1818579 |
| Alcohol (Ethanol)                        |   411435 |
| PreservationMethodCode: Acid lugol       |   326651 |
| PreservationMethodCode: Formaldehyde     |   233036 |
| NMBAQC                                   |   165259 |
| NA                                       |   115054 |
| Fresh                                    |    95512 |
| alcohol-75% EtOH                        |    94695 |
| PreservationMethodCode: Fomaldehye - 4% buffered formaldehyde (ph 7-8) |    79178 |


### disposition
- NULL Values: 108 391 847
- Column type: Char 
- Total distinct count:  309
- Distinct values:

| Disposition                              |   Count |
|-----------------------------------------|---------|
| null                                    | 108391847 |
| in collection                           |    41718 |
| En colección                            |    36220 |
| Material disponível                     |    19975 |
| Discarded                               |     3521 |
| Frozen                                  |     2858 |
| Introducido a su medio natural          |     2650 |
| En colecci�n                            |     1064 |
| Deaccessioned                           |      605 |
| voucher elsewhere                       |      492 |



### othercatalognumbers
- NULL Values: 108 069 304
- Column type: Char 
- Total distinct count: 325 284
- Distinct values:


| OtherCatalogNumbers              |   Count |
|---------------------------------|---------|
| null                            | 108069304 |
| urn:catalog:RBINS:IG:28177      |     4436 |
| urn:catalog:RBINS:IG:30275      |     3344 |
| colecta personal                 |     1770 |
| Colecta personal                 |     1744 |
| urn:catalog:RBINS:IG:30736      |     1424 |
| urn:catalog:RBINS:IG:26080      |     1389 |
| urn:catalog:RBINS:IG:27838      |     1382 |
| 1                               |     1353 |
| 2                               |     1286 |
| urn:catalog:RBINS:IG:9154       |     1215 |



### associatedmedia
- NULL Values: 107 937 974
- Column type: Char 
- Total distinct count: 482 692
- Distinct values:

| AssociatedMedia                                                                                  |    Count |
|--------------------------------------------------------------------------------------------------|----------|
| null                                                                                             | 107937974 |
| photo vouchers of individual fishes and small invertebrates on lab server                         |     1642 |
| Francianne Pellizzari. Kamilla Matos Simão. ir Yokoya and Silvia Guimarães Pita                    |      562 |
| Doi:10.1051/alr/2010027                                                                          |      208 |
| [Flickr](https:/www.flickr.com/photos/140572903@N04/29510402143/in/album-72157673636209350)     |      174 |
| [JSTAGE](https://www.jstage.jst.go.jp/article/pbr/13/2/13_B130204/_supplement/_download/13_B130204_2.pdf) |      137 |
| [JSTAGE](https://www.jstage.jst.go.jp/article/pbr/14/4/14_B140401/_supplement/_download/14_B140401_1.pdf) |      132 |
| [SIAM](http://siam.invemar.org.co/sibm-busqueda-avanzada)                                          |      130 |
| [DOI](http://dx.doi.org/10.11646/zootaxa.3710.2.1)                                                |      123 |
| [Flickr](https:/www.flickr.com/photos/140572903@N04/29510401043/in/album-72157673636209350)     |      123 |


### associatedreferences
- NULL Values: 102 299 877
- Column type: Char 
- Total distinct count:  4952
- Distinct values:

| AssociatedReferences                                                                                         |   Count |
|-------------------------------------------------------------------------------------------------------------|---------|
| null                                                                                                        | 102299877 |
| [{"crossref":{"citeinfo":{"origin":"Halpin, P.N., A.J. Read, E. Fujioka, B.D. Best, B. Donnelly, L.J. Hazen, C. Kot, K. Urian, E. LaBrecque, A. Dimatteo, J. Cleary, C. Good, L.B. Crowder, and K.D. Hyrenbach","pubdate":"2009","title_html":"OBIS-SEAMAP: The world data center for marine mammal, sea bird, and sea turtle distributions","title":"OBIS-SEAMAP: The world data center for marine mammal, sea bird, and sea turtle distributions","serinfo":{"sername":"Oceanography","issue":"22(2):104-115"},"onlink":"http:\/\/www.tos.org\/oceanography\/article\/obis-seamap-the-world-data-center-for-marine-mammal-sea-bird-and-sea-turtle"}}}] | 1165217 |
| [{"crossref":{"citeinfo":{"origin":"Stone, C. J., A. Webb, C. Barton, N. Ratcliffe, T.C. Reed, M.L. Tasker, C.J. Camphuysen, and M.W. Pienkowski","pubdate":"1995","title_html":"An atlas of seabird distribution in north-west European waters","title":"An atlas of seabird distribution in north-west European waters","serinfo":{"sername":"Joint Nature Conservation Committee report, Peterborough, ISBN 1 873701 94 2"}}}},{"crossref":{"citeinfo":{"origin":"Halpin, P.N., A.J. Read, E. Fujioka, B.D. Best, B. Donnelly, L.J. Hazen, C. Kot, K. Urian, E. LaBrecque, A. Dimatteo, J. Cleary, C. Good, L.B. Crowder, and K.D. Hyrenbach","pubdate":"2009","title_html":"OBIS-SEAMAP: The world data center for marine mammal, sea bird, and sea turtle distributions","title":"OBIS-SEAMAP: The world data center for marine mammal, sea bird, and sea turtle distributions","serinfo":{"sername":"Oceanography","issue":"22(2):104-115"},"onlink":"http:\/\/www.tos.org\/oceanography\/article\/obis-seamap-the-world-data-center-for-marine-mammal-sea-bird-and-sea-turtle"}}}] | 1122012 |
| National Museum of Natural History, Smithsonian Institution                                                       |  640910 |
| [{"crossref":{"citeinfo":{"origin":"Zavalaga CB, Halls JN, Mori GP, Taylor SA, Dell'omo G","pubdate":"2010","title_html":"At-sea movement patterns and diving behavior of Peruvian boobies Sula variegata in northern Peru","title":"At-sea movement patterns and diving behavior of Peruvian boobies Sula variegata in northern Peru","serinfo":{"sername":"Mar Ecol Prog Ser","issue":"404:259-274"},"onlink":"http:\/\/www.int-res.com\/abstracts\/meps\/v404\/p259-274\/"}}},{"crossref":{"citeinfo":{"origin":"Halpin, P.N., A.J. Read, E. Fujioka, B.D. Best, B. Donnelly, L.J. Hazen, C. Kot, K. Urian, E. LaBrecque, A. Dimatteo, J. Cleary, C. Good, L.B. Crowder, and K.D. Hyrenbach","pubdate":"2009","title_html":"OBIS-SEAMAP: The world data center for marine mammal, sea bird, and sea turtle distributions","title":"OBIS-SEAMAP: The world data center for marine mammal, sea bird, and sea turtle distributions","serinfo":{"sername":"Oceanography","issue":"22(2):104-115"},"onlink":"http:\/\/www.tos.org\/oceanography\/article\/obis-seamap-the-world-data-center-for-marine-mammal-sea-bird-and-sea-turtle"}}}] |  299901 |



### associatedsequences
- NULL Values: 108 412 729
- Column type: Char 
- Total distinct count: 21202
- Distinct values:

| Associated Sequences                             | Count    |
|--------------------------------------------------|----------|
| null                                             | 108412729|
| NCBI BioProject accession number PRJNA433203     | 31168    |
| acapla_CR_all                                    | 1695     |
| trispp_COI_all                                   | 1326     |
| Prifil_CyB_MG                                    | 1214     |
| Panint_CO1_MI                                    | 1099     |
| Panpen_COI_MI                                    | 826      |
| ptevol_CR_rb                                     | 798      |
| Ceparg_CyB_MG                                    | 775      |
| nerpli_CO1_EC                                    | 760      |



### associatedtaxa
- NULL Values: 108 482 004
- Column type: Char 
- Total distinct count: 2612
- Distinct values:

| associatedtaxa                                                                   | Count    |
|-------------------------------------------------------------------------------|----------|
| null                                                                          | 108482004|
| Lemaeocera                                                                    | 9940     |
| "parasite of":"Salmo salar"                                                   | 4207     |
| "host to":"Caligidae" \| "host to":"Lepeophtheirus salmonis" \| "host to":"Caligus clemensi" | 1261 |
| Fauna associated with: Durvillea antarctica \| Holdfast                       | 740      |
| coletado em: No meio de agregado de Petaloconchus varians.                    | 421      |
| organism is epibiotic on the scallop (Placopecten magellanicus Gmelin, 1791)  | 371      |
| Host-Linckia laevigata                                                        | 312      |
| coletado em: Conteúdo digestivo de Holothuria grisea.                         | 64       |
| Host: Macrourus holotrachys                                                   | 59       |


### organismid
- NULL Values:  100 015 728
- Column type: Char 
- Total distinct count: 621 395
- Distinct values:

| organismid | Count    |
|------------|----------|
| null       | 100015728|
| L901531    | 53821    |
| H900926    | 49560    |
| H903183    | 48309    |
| H903169    | 46914    |
| H903134    | 46091    |
| L911715    | 44710    |
| H903132    | 44377    |
| L909206    | 43656    |
| H903644    | 43006    |


### organismname
- NULL Values: 105 575 900
- Column type: Char 
- Total distinct count: 702
- Distinct values:

| Organism Name | Count    |
|---------------|----------|
| null          | 105575900|
| Peter         | 56068    |
| Sjarel        | 53821    |
| Hilde         | 49560    |
| Wilma         | 48309    |
| Luc           | 46914    |
| Suk-hyo       | 46091    |
| Yente         | 44710    |
| Hein          | 44377    |
| Roland-Jan    | 43656    |


### organismscope
- NULL Values: 108 260 852
- Column type: Char
- All Distinct values:

| Organism Scope           | Count    |
|--------------------------|----------|
| null                     | 108260852|
| individual - tagged animal | 242046  |
| Organismo multicelular   | 843      |
| Cardumen                 | 397      |
| individual               | 259      |
| Colonia                  | 17       |


### associatedoccurrences
- NULL Values: 108 495 102
- Column type: Char 
- Total distinct count: 4859
- Distinct values:

| Associated Occurrences                                           | Count     |
|------------------------------------------------------------------|-----------|
| null                                                             | 108495102 |
| Colonyestimation1_adults                                         | 447       |
| Cortes histológicos de: CBUMAG:NEM:00002                         | 11        |
| Cortes histológicos de: CBUMAG:NEM:00027                         | 10        |
| BBA14-640_sample                                                 | 9         |
| BBA14-473_sample                                                 | 8         |
| Cortes histológicos de: CBUMAG:NEM:00049                         | 8         |
| prey to: B91-032:1830:potential-predator:pacific_hake:3          | 8         |
| BBA14-425_sample                                                 | 7         |
| BBA14-567_sample                                                 | 7         |


### associatedorganisms
- NULL Values: 108 504 404
- Column type: Char
- All Distinct values:


| Associated Organisms                   | Count     |
|----------------------------------------|-----------|
| null                                   | 108504404 |
| Hermano de INV:TRA1-2-3                | 3         |
| Hermano de INV:TRA4-5-6                | 3         |
| Asociado UDEA:CEMUA:ANNE:              | 2         |
| Thalassia                              | 2         |
| Asoaciado UCES:CBUCES:E:1166           | 1         |
| Asoaciado UDEA:CEMUA:ANNE:001700       | 1         |
| Asociado UCES:CBUCES:E:1142            | 1         |
| Asociado UCES:CBUCES:E:1165            | 1         |
| Dasya sp.                              | 1         |
| Udotea                                 | 1         |
| Udotea \| Halimeda                     | 1         |


### previousidentifications
- NULL Values: 108 045 822
- Column type: Char 
- Total distinct count: 24880
- Distinct values:

| Previous Identifications   | Count    |
|----------------------------|----------|
| null                       | 108045822|
| Pocillopora damicornis     | 29620    |
| Montastraea faveolata      | 18788    |
| Florideophyceae            | 17167    |
| Dictyota sp.               | 15132    |
| Montastraea annularis      | 14376    |
| Pocillopora capitata       | 12765    |
| Siderastrea siderea        | 11471    |
| Diploria strigosa          | 9691     |
| Agaricia tenuifolia        | 8971     |


### organismremarks
- NULL Values: 107 148 139
- Column type: Char 
- Total distinct count: 14231
- Distinct values:

| Organism Remarks                                                                                                      | Count     |
|-----------------------------------------------------------------------------------------------------------------------|-----------|
| null                                                                                                                  | 107148139 |
| Tagged animal. organismID may refer to the ID of the telemetry device.                                                | 1106698   |
| This whale is known from research conducted by [Cascadia Research Collective](http://www.cascadiaresearch.org/) and collaborators | 2517      |
| Known to be male from the [SPLASH study](https://www.cascadiaresearch.org/projects/splash-structure-populations-levels-abundance-and-status-humpback-whales-north-pacific). | 2095      |
| This whale is known from research conducted by [ECOBAC](http://www.ecobac.org/) from the [photo-identification catalog of humpback whale of Banderas Bay, Mexico (FIBB catalog)](http://www.whalephoto.org/) | 1990      |
| This whale is known from research conducted by [Cascadia Research Collective](http://www.cascadiaresearch.org/) and collaborators, and is known in Mexico to [ECOBAC](http://www.ecobac.org/) from the [photo-identification catalog of humpback whale of Banderas Bay, Mexico (FIBB catalog)](http://www.whalephoto.org/) | 1672      |
| associated with roots of Rhizophora mangle                                                                            | 1414      |
| found dead                                                                                                            | 1383      |
| Known to be female from the [SPLASH study](https://www.cascadiaresearch.org/projects/splash-structure-populations-levels-abundance-and-status-humpback-whales-north-pacific). | 1110      |
| Known to be male from the [SPLASH study](https://www.cascadiaresearch.org/projects/splash-structure-populations-levels-abundance-and-status-humpback-whales-north-pacific) | 1041      |


### eventid
- NULL Values: 53 314 683
- Column type: Char 
- Total distinct count: 6674254
- Distinct values:

| Event ID              | Count    |
|-----------------------|----------|
| null                  | 53314683 |
| JE143N1               | 17001    |
| 102.100.100/21757     | 13336    |
| 102.100.100/139935    | 13283    |
| 102.100.100/21743     | 13128    |
| 102.100.100/139933    | 12650    |
| 102.100.100/21742     | 12359    |
| 102.100.100/21733     | 12300    |
| 102.100.100/21740     | 12283    |
| 102.100.100/21751     | 12035    |


### parenteventid
- NULL Values: 93 771 262
- Column type: Char 
- Total distinct count: 186 876
- Distinct values:

| Parent Event ID | Count   |
|-----------------|---------|
| null            | 93771262|
| NED2016016      | 90662   |
| NED2017020      | 82282   |
| NED2019030      | 80250   |
| NED2015017      | 73463   |
| NED2014018      | 67480   |
| NED2020025      | 61161   |
| L901531_4045    | 53821   |
| H900926_6005    | 49560   |
| H903183_783     | 48309   |



### samplingprotocol
- NULL Values: 62 254 607
- Column type: Char 
- Total distinct count: 24873
- Distinct values:

| Sampling Protocol                                           | Count    |
|-------------------------------------------------------------|----------|
| null                                                        | 62254607 |
| Should point to voyage CTD bottle cast methods.             | 18165329 |
| gps                                                         | 4165966  |
| Seine                                                       | 1639226  |
| Reef Fish Visual Census doi:10.1016/j.fishres.2011.01.012   | 1616667  |
| Benthos Samplers                                            | 793076   |
| nSPC                                                        | 698900   |
| Species subsampled and individual lengths recorded.         | 564982   |


### samplesizevalue
- NULL Values: 87 874 611
- Column type: Char 
- Total distinct count: 14 077
- Distinct values:

| Sample Size Value | Count    |
|-------------------|----------|
| null              | 87874611 |
| 7.5               | 699113   |
| 50                | 338317   |
| 0.03              | 200698   |
| 10                | 146679   |
| 60                | 116219   |
| 40                | 58287    |
| 1                 | 56814    |
| 150               | 56418    |
| 20                | 50325    |


- Can be converted to float
```sql
SELECT samplesizevalue::double precision
FROM obis_20230208
WHERE pg_input_is_valid(samplesizevalue, 'double precision');
```

- Total converted rows: 20 553 568


### samplesizeunit
- NULL Values: 87 849 989
- Column type: Char 
- Total distinct count: 338
- Distinct values:

| Sample Size Unit      | Count    |
|-----------------------|----------|
| null                  | 87849989 |
| DNA sequence reads    | 18241773 |
| meter radius          | 774881   |
| metros                | 288984   |
| square meters         | 246079   |
| hectares              | 220177   |
| Km                    | 210019   |
| trap-hours            | 126431   |
| square metre          | 107843   |
| metros cuadrados      | 80770    |
| square meter          | 71597    |


### samplingeffort
- NULL Values: 96 362 293
- Column type: Char 
- Total distinct count: 51443
- Distinct values:

| Sampling Effort               | Count    |
|-------------------------------|----------|
| null                          | 96362293 |
| 20 observer-minutes           | 1616667  |
| Duration = 10 minutes         | 564982   |
| %                             | 460673   |
| #                             | 308514   |
| 0,0143 m²                     | 272587   |
| 300 survey width in meters    | 260502   |
| 0,0123 m²                     | 254668   |
| 10-15 minutes per transect    | 237709   |
| Duration=10 minutes           | 231003   |


### eventdate
- NULL Values: 40 18 157
- Column type: Char 
- Total distinct count: 11 863 425
- Distinct values:

- Potentially can be converted to date!

| Event Date               | Count   |
|--------------------------|---------|
| null                     | 4018157 |
| 0000-00-00               | 225656  |
| NA                       | 153869  |
| 2000                     | 104946  |
| 2001                     | 102453  |
| 1996                     | 98495   |
| 2016-09-20T18:10:49Z     | 92891   |
| 2002                     | 84418   |
| 1999                     | 72629   |
| 2003                     | 70515   |
| 2004                     | 65589   |
| 2012-05-17T13:33:00Z     | 57299   |
| 1998                     | 56769   |
| 2016-09-20T10:18:00Z     | 54554   |


### eventtime
- NULL Values: 86 089 248
- Column type: Char 
- Total distinct count: 470 923
- Distinct values:

- Potentially can be converted to time!

| Event Time         | Count    |
|--------------------|----------|
| null               | 86089248 |
| 00:00:00           | 261698   |
| 00:00:00+00:00     | 235747   |
| 12:00:00+00:00     | 113029   |
| 03:48:00Z          | 97215    |
| 00:00              | 75827    |
| 08:00:00+00:00     | 41330    |
| 09:00:00+00:00     | 39217    |
| 10:00:00+00:00     | 38767    |
| 07:00:00+00:00     | 37183    |


### startdayofyear
- NULL Values: 106 262 596
- Column type: Char 
- Total distinct count: 631
- Distinct values:

| Start Day of Year | Count     |
|-------------------|-----------|
| null              | 106262596 |
| 311               | 19648     |
| 309               | 19460     |
| 310               | 16721     |
| 307               | 15307     |
| 308               | 13390     |
| 312               | 11512     |
| 183               | 10892     |
| 314               | 10728     |


- Can be converter to int!
- Total converted rows: 2 241 824
```sql
SELECT startdayofyear::integer
FROM obis_20230208
WHERE pg_input_is_valid(startdayofyear, 'integer');
```


### enddayofyear
- NULL Values: 107 703 399
- Column type: Char 
- Total distinct count: 370
- Distinct values:

| End Day of Year | Count     |
|-----------------|-----------|
| null            | 107703399 |
| 311             | 15031     |
| 309             | 14106     |
| 307             | 12508     |
| 310             | 11766     |
| 308             | 10635     |
| 314             | 7458      |
| 312             | 7140      |
| 305             | 6006      |
| 287             | 5681      |


- Can be converter to int!
- Total converted rows: 801 022

```sql
SELECT enddayofyear::integer
FROM obis_20230208
WHERE pg_input_is_valid(enddayofyear, 'integer');
```



### year
- NULL Values: 58 537 943
- Column type: Char 
- Total distinct count: 743
- Distinct values:

| Year | Count    |
|------|----------|
| null | 58537943 |
| 2008 | 1902000  |
| 2010 | 1794424  |
| 2007 | 1686765  |
| 2009 | 1647484  |
| 2004 | 1558677  |
| 2011 | 1525340  |
| 2000 | 1519145  |
| 2005 | 1456143  |
| 2012 | 1398527  |


- Can be converter to int!
- Total converted rows:49948620
```sql
SELECT year::integer
FROM obis_20230208
WHERE pg_input_is_valid(year, 'integer');
```

### month
- NULL Values: 64 597 027
- Column type: Char 
- Total distinct count: 52
- Distinct values:

| Month      | Count    |
|------------|----------|
| null       | 64597027 |
| 8          | 5026436  |
| 5          | 4591806  |
| 9          | 4299691  |
| 6          | 3961138  |
| 7          | 3931375  |
| 2          | 3441158  |
| 11         | 3364058  |
| 10         | 3317886  |
| 4          | 3187050  |
| 3          | 3029243  |
| 1          | 2795808  |
| 12         | 2096842  |
| 09         | 124582   |
| 06         | 118774   |
| 07         | 108808   |
| 08         | 107792   |
| 03         | 99735    |
| 05         | 84559    |
| 01         | 82152    |
| 04         | 66525    |
| 02         | 63815    |
| NA         | 4010     |
| -10        | 1028     |
| #VALUE!    | 620      |
| 30         | 370      |
| 22         | 351      |
| 13         | 297      |
| 23         | 268      |
| 18         | 223      |
| 17         | 142      |
| 25         | 142      |
| 26         | 135      |
| 21         | 103      |
| 24         | 102      |
| 19         | 96       |
| 15         | 69       |
| 29         | 35       |
| 2001       | 33       |
| 27         | 32       |
| 20         | 27       |
| 14         | 24       |
| 31         | 19       |
| 16         | 10       |
| 28         | 7        |
| 0          | 6        |
| 1, 2       | 6        |
| 03-Feb     | 2        |
| 12.0       | 1        |
| 1977       | 1        |
| 32007      | 1        |
| 9, 12, 2, 3| 1        |

- Column need to be cleand before casting to int


### day
- NULL Values: 65 620 602
- Column type: Char 
- Total distinct count: 58
- Distinct values:

| Day      | Count    |
|----------|----------|
| null     | 65620602 |
| 1        | 2069153  |
| 15       | 1534470  |
| 10       | 1509954  |
| 13       | 1449270  |
| 14       | 1441936  |
| 11       | 1435762  |
| 7        | 1426074  |
| 19       | 1423702  |
| 20       | 1420768  |
| -88      | 651      |
| #VALUE!  | 620      |
| -13      | 105      |
| 0        | 99       |
| -12      | 98       |
| -11      | 90       |
| -14      | 50       |
| 23.-23.  | 6        |
| 1982     | 2        |
| 14-21    | 1        |


### verbatimeventdate
- NULL Values: 101 114 120
- Column type: Char 
- Total distinct count: 2666473
- Distinct values:

| Verbatim Event Date             | Count    |
|---------------------------------|----------|
| null                            | 101114120|
| NA                              | 110539   |
| 1962 and 1963                   | 12418    |
| no verbatim date recorded       | 9846     |
| Date unk'n                      | 4677     |
| 1913-01-01 00:00:00             | 3738     |
| July to August, 1979            | 3709     |
| 1913-08-01 00:00:00             | 3559     |
| 1913-07-01 00:00:00             | 3530     |
| 2019-09-27 08:35:46             | 3249     |



### habitat
- NULL Values: 104 195 529
- Column type: Char 
- Total distinct count: 28871
- Distinct values:

| Habitat                              | Count     |
|--------------------------------------|-----------|
| null                                 | 104195529 |
| Forereef : AGR : Aggregate Reef      | 315921    |
| Nearshore marine                     | 311595    |
| Continuous Low Relief                | 295207    |
| Isolated Medium Relief (Patch)       | 279992    |
| Spur and Groove low Relief           | 276762    |
| Spur and Groove High Relief          | 261229    |
| Shallow coral reef : Forereef        | 227284    |
| Area coralina                        | 161779    |
| Continuous Medium Relief             | 155608    |



### fieldnumber
- NULL Values: 93 172 137
- Column type: Char 
- Total distinct count: 1 515 163
- Distinct values:

| Field Number | Count    |
|--------------|----------|
| null         | 93172137 |
| 3            | 29460    |
| 1            | 29143    |
| 1mm          | 27677    |
| 2            | 27254    |
| 0            | 22868    |
| Transect 2   | 22322    |
| 7            | 20132    |
| 4b           | 19890    |
| 1b           | 19697    |


### fieldnotes
- NULL Values: 107 936 781
- Column type: Char 
- Total distinct count: 
- Distinct values:

| Field Notes                                                                 | Count     |
|----------------------------------------------------------------------------|-----------|
| null                                                                       | 107936781 |
| OSPOTB                                                                     | 206938    |
| El número junto a letra que indica la parcela (S, M, P) corresponde al transecto evaluado. | 162628    |
| YDNSSW                                                                     | 32890     |
| Bird banded on this day. The band identifer is the Collector Number       | 12906     |
| YDRSSW                                                                     | 7335      |
| Nest site locations from handheld GPS ground surveys, with differential correction | 5588      |
| YDFSSW                                                                     | 5099      |
| YEFSSW                                                                     | 5073      |
| Nest site locations from handheld GPS ground surveys                      | 5056      |


### eventremarks
- NULL Values: 88 571 756
- Column type: Char 
- Total distinct count: 276428
- Distinct values:

| Event Remarks                          | Count    |
|----------------------------------------|----------|
| null                                   | 88571756 |
| sample                                 | 6475536  |
| Collection                             | 2112490  |
| Source of data: Research Catch         | 1510505  |
| Section                                | 502531   |
| Sample                                 | 441485   |
| Source of data: ByCatch Program        | 206303   |
| Vessel: N \| Cruise Number: 2 \| Season: SPRING | 166582 |
| NA                                     | 147437   |
| subSample                              | 146446   |



### locationid
- NULL Values: 103 010 809
- Column type: Char 
- Total distinct count: 127754
- Distinct values:



| locationid                                            | count |
|-------------------------------------------------------|------|
| `null`                                                | 103010809`|
| 23536                                                 | 540848|
| http://marineregions.org/mrgid/25303                  | 331620|
| 33                                                    | 127250|
| http://marineregions.org/mrgid/17536                  | 114592|
| 27                                                    | 105231|
| 34                                                    | 95699 |
| http://marineregions.org/mrgid/25567                  | 81804 |
| https://www.marineregions.org/gazetteer.php?p=details&id=3319 | 60188 |
| 29                                                    | 39316 |
| NA                                                    | 35177 |



### highergeographyid
- NULL Values: 108 494 779
- Column type: Char 
- Total distinct count: 63
- Distinct values:

| highergeographyid                                                               | count  |
|---------------------------------------------------------------------------------|--------|
| null                                                                            | 108494779 |
| [https://data.aad.gov.au/aadc/gaz/scar/display_name.cfm?gaz_id=107532](https://data.aad.gov.au/aadc/gaz/scar/display_name.cfm?gaz_id=107532) | 1762   |
| [https://data.aad.gov.au/aadc/gaz/scar/display_name.cfm?gaz_id=111296](https://data.aad.gov.au/aadc/gaz/scar/display_name.cfm?gaz_id=111296) | 1188   |
| TGN:1002111                                                                     | 1145   |
| [https://data.aad.gov.au/aadc/gaz/scar/display_name.cfm?gaz_id=114651](https://data.aad.gov.au/aadc/gaz/scar/display_name.cfm?gaz_id=114651) | 723    |
| TGN:1012974                                                                     | 517    |
| 13                                                                               | 488    |
| [http://vocab.nerc.ac.uk/collection/C19/current/1/1/](http://vocab.nerc.ac.uk/collection/C19/current/1/1/) | 378    |
| [http://marineregions.org/mrgid/3338](http://marineregions.org/mrgid/3338)       | 356    |
| Según PNIBM, ISBN 958-96972-0-8                                                  | 316    |


### highergeography
- NULL Values: 107 326 558
- Column type: Char 
- Total distinct count: 9042
- Distinct values:

| highergeography                                                                                            | count     |
|------------------------------------------------------------------------------------------------------------|-----------|
| null                                                                                                       | 107326558 |
| EASTERN NORTH PACIFIC \| USA \| ALASKA \| \| \| \| \|                                                      | 119987    |
| Saint Thomas                                                                                               | 79741     |
| Saint Croix                                                                                                | 72528     |
| West Puerto Rico                                                                                           | 26709     |
| North America, North Pacific Ocean, United States, California, San Francisco Estuary, San Francisco Bay    | 21120     |
| Eastern Indo-Pacific                                                                                       | 17770     |
| United States                                                                                              | 16570     |
| Pacific Ocean, Indo-West Pacific                                                                           | 15697     |
| Africa \|South Africa \|KwaZulu-Natal                                                                      | 15123     |


### continent
- NULL Values: 103 729 146
- Column type: Char 
- Total distinct count: 1447
- Distinct values:

| continent                      | count     |
|--------------------------------|-----------|
| null                           | 103729146 |
| Europe                         | 716368    |
| SA                             | 443281    |
| North America                  | 399068    |
| North East Atlantic            | 317345    |
| Pacific Ocean                  | 184925    |
| Azores Exclusive Economic Zone | 174813    |
| Azores (several wb)            | 157762    |
| Oceania                        | 155135    |
| Black Sea                      | 139423    |


### waterbody
- NULL Values: 87 623 300
- Column type: Char 
- Total distinct count: 4917
- Distinct values:

| waterbody                                                                                              | count    |
|--------------------------------------------------------------------------------------------------------|----------|
| null                                                                                                   | 87623300 |
| Gulf of Mexico                                                                                         | 1957487  |
| Indian                                                                                                 | 1818202  |
| Northwest Atlantic                                                                                     | 1555986  |
| Pacific Ocean                                                                                          | 1393073  |
| Atlantic                                                                                               | 1335875  |
| North Pacific Ocean                                                                                    | 1201233  |
| North Atlantic Ocean                                                                                   | 1190554  |
| north; west; offshore; European; Atlantic; Irish; Channel; Celtic; shelf; oceanic; Skaggerak; Kategat; Belt; Irish; English; Bristol; Biscay; oceanic | 1122012  |
| Southern Ocean                                                                                         | 997999   |


### islandgroup
- NULL Values: 106 965 245
- Column type: Char 
- Total distinct count: 601
- Distinct values:

| islandgroup                                               | count     |
|-----------------------------------------------------------|-----------|
| null                                                      | 106965245 |
| Pacific Remote Island Areas                               | 204939    |
| American Samoa                                            | 203006    |
| Northwestern Hawaiian Islands                             | 201978    |
| Mariana Archipelago                                       | 195234    |
| Main Hawaiian Islands                                     | 165921    |
| Archipiélago Corales del Rosario y San Bernardo           | 123435    |
| NA                                                        | 110539    |
| Archipiélago de San Andrés, Providencia y Santa Catalina  | 83849     |
| Caroline Islands                                          | 30534     |


### island
- NULL Values: 106 823 640
- Column type: Char 
- Total distinct count: 2430
- Distinct values:


| island         | count     |
|----------------|-----------|
| null           | 106823640 |
| NA             | 110539    |
| Tutuila        | 88245     |
| Gorgona        | 52789     |
| Hawaii         | 46884     |
| Guam           | 44999     |
| San Andrés Isla| 43384     |
| Palmyra        | 42693     |
| Jarvis         | 42670     |
| Pearl & Hermes | 40845     |


### country
- NULL Values: 49 150 804
- Column type: Char 
- Total distinct count: 1947
- Distinct values:

| country                   | count     |
|---------------------------|-----------|
| null                      | 49150804  |
| Australia                 | 27509811  |
| United States             | 5830077   |
| Canada                    | 3215086   |
| South Africa              | 3158167   |
| Sweden                    | 2394100   |
| Germany                   | 1383455   |
| SOVIET UNION              | 1146324   |
| United Kingdom (Scotland) | 988013    |


### countrycode
- NULL Values: 102 756 397
- Column type: Char 
- Total distinct count: 187
- Distinct values:


| countrycode | count      |
|-------------|------------|
| null        | 102756397  |
| CA          | 2667797    |
| US          | 1576475    |
| CO          | 486185     |
| VI          | 163278     |
| BR          | 94158      |
| NC          | 88811      |
| TO          | 84880      |
| PR          | 83046      |
| NZ          | 56555      |


### stateprovince
- NULL Values: 97 785 228
- Column type: Char 
- Total distinct count: 4357
- Distinct values:


| stateprovince     | count    |
|-------------------|----------|
| null              | 97785228 |
| Florida           | 1871445  |
| Queensland        | 875429   |
| Victoria          | 690942   |
| New South Wales   | 670251   |
| Texas             | 639037   |
| Alabama           | 568554   |
| Tasmania          | 430757   |
| Azores            | 329502   |
| British Columbia  | 326161   |


### county
- NULL Values: 107 174 684
- Column type: Char 
- Total distinct count: 6187
- Distinct values:

| county              | count     |
|---------------------|-----------|
| null                | 107174684 |
| Cartagena de Indias | 125841    |
| NA                  | 112221    |
| Santa Marta         | 82654     |
| Balearic Islands    | 81415     |
| Guapi               | 55052     |
| San Andrés          | 46499     |
| Providencia         | 37207     |
| Sevastopol          | 25376     |
| Acandí              | 16748     |


### municipality
- NULL Values:  106 323 803
- Column type: Char 
- Total distinct count: 733
- Distinct values:

| municipality     | count     |
|------------------|-----------|
| null             | 106323803 |
| British Columbia | 1943246   |
| NA               | 110539    |
| Capurganá        | 16695     |
| Cabo Rojo        | 14240     |
| Rincon           | 9387      |
| Isla Desecheo    | 9323      |
| Ponce            | 7345      |
| Isla Vieques     | 6117      |
| La Parguera      | 5173      |


### locality
- NULL Values:  56 751 662
- Column type: Char 
- Total distinct count: 799792
- Distinct values:

| locality                | count    |
|-------------------------|----------|
| null                    | 56751662 |
| Port Hacking            | 2585970  |
| North Stradbroke Island | 2552385  |
| Maria Island            | 2301289  |
| Rottnest Island         | 1509022  |
| Yongala                 | 1047729  |
| Drift Study - EAC       | 657757   |
| Kangaroo Island         | 529009   |
| Southern Ocean          | 505409   |


### verbatimlocality
- NULL Values:  106 711 244
- Column type: Char 
- Total distinct count: 42013
- Distinct values:

| verbatimlocality                     | count     |
|--------------------------------------|-----------|
| null                                 | 106711244 |
| 3L                                   | 156270    |
| 3K                                   | 89256     |
| EASTERN NORTH PACIFIC \| USA \| ALASKA | 80168     |
| 3P                                   | 73627     |
| 3O                                   | 66360     |
| 2J                                   | 65435     |
| 3N                                   | 58199     |
| Pavitos                              | 23524     |
| Tesoro 1                             | 20867     |


### verbatimelevation
- NULL Values:  108 494 704
- Column type: Char 
- Total distinct count: 351
- Distinct values:


| verbatimelevation | count     |
|-------------------|-----------|
| null              | 108494704 |
| 0-100             | 5466      |
| 0                 | 589       |
| 0-1.3 m           | 317       |
| 0-0.2 m           | 290       |
| 0m-0m             | 290       |
| 0-0.5 m           | 211       |
| 0-0.7 m           | 168       |
| 0-0,6 m           | 141       |
| 0-1,75 m          | 116       |



### minimumelevationinmeters
- NULL Values: 106 324 387
- Column type: Char 
- Total distinct count: 398
- Distinct values:

| minimumelevationinmeters                       | count     |
|------------------------------------------------|-----------|
| 0                                              | 2134284   |
| 0.0                                            | 39961     |
| 4                                              | 104       |
| 5                                              | 86        |
| cave                                           | 58        |
| small cave; overhang; puka or hole in the rock | 55        |
| 2                                              | 54        |
| 550.0000000000                                 | 47        |
| 11                                             | 41        |
| 9                                              | 41        |
| 195.072                                        | 32        |
| 5.0000000000                                   | 30        |
| 10.0000000000                                  | 29        |
| 525.0000000000                                 | 29        |
| reef crest                                     | 29        |
| 18.0                                           | 27        |
| 1130.0000000000                                | 22        |
| 16                                             | 22        |
| reef flats                                     | 22        |
| 1100.0000000000                                | 21        |
| 15                                             | 20        |
| 20.0                                           | 20        |
| 14                                             | 19        |
| Lagoon                                         | 19        |
| 10.0                                           | 18        |
| 1025.0000000000                                | 18        |
| 80.0000000000                                  | 18        |
| 30.0000000000                                  | 15        |
| 13                                             | 14        |
| 14.0                                           | 14        |
| 30.0                                           | 14        |
| 80                                             | 450       |
| 1                                              | 448       |
| 3                                              | 328       |
| 10                                             | 324       |
| 19                                             | 292       |
| 7                                              | 286       |
| 29                                             | 281       |


- can be converted to float after cleaning


### maximumelevationinmeters
- NULL Values: 106 236 535
- Column type: Char 
- Total distinct count: 535
- Distinct values:

| maximumelevationinmeters | count     |
|--------------------------|-----------|
| null                     | 106236535 |
| 0                        | 2208150   |
| 0.0                      | 39930     |
| 100                      | 5466      |
| 200                      | 1345      |
| 50                       | 940       |
| 20                       | 847       |
| 37                       | 647       |
| 1                        | 563       |
| 80                       | 450       |


- non numeric values: Ngati kuri, Te Aupouri, 
- can be converted to float after cleaning

### locationaccordingto
- NULL Values: 106 495 285
- Column type: Char 
- Total distinct count: 110
- Distinct values:

| locationaccordingto                                                                                   | count     |
|-------------------------------------------------------------------------------------------------------|-----------|
| null                                                                                                  | 106495285 |
| Marine Regions - MRGID                                                                                | 540848    |
| DFO Lobster Fishing Area                                                                              | 491668    |
| Dato in situ usando GPS \| Estandarización político andministrativa Colombia DANE - Divipola \| Marine Regions Gazetteer - MRG | 276444    |
| MarineRegions.org (MRG)                                                                               | 242047    |
| MarineRegions -MRGID                                                                                  | 236592    |
| Monitoring program stations                                                                           | 39219     |
| marineregions.org MRGID                                                                               | 34027     |
| Canadian Geonames Database (CGNDB)                                                                    | 15131     |
| MarineRegions.org                                                                                     | 14309     |


### locationremarks
- NULL Values: 99 938 945
- Column type: Char 
- Total distinct count: 15082
- Distinct values:

| locationremarks                                                   | count      |
|------------------------------------------------------------------|------------|
| NULL                                                             | 99938945   |
| "Strait of Georgia"                                              | 683576     |
| "Central Coast"                                                  | 326592     |
| "W.C. Vancouver Is."                                            | 310483     |
| "Prince Rupert"                                                 | 283844     |
| "Pacific States Marine Fisheries Commission Area 5C: SOUTHERN HECATE STRAIT" | 228211     |
| "Pacific States Marine Fisheries Commission Area 5B: NORTHERN Q.C. SOUND" | 219609     |
| "Pacific States Marine Fisheries Commission Area 5D: NORTHERN HECATE STRAIT" | 185519     |
| "Pacific States Marine Fisheries Commission Area 5E: WEST COAST Q.C. ISLANDS" | 184528     |
| "Pacific States Marine Fisheries Commission Area 3C: S.W. VANCOUVER ISLAND" | 176181     |


### verbatimcoordinates
- NULL Values: 107 708 171
- Column type: Char 
- Total distinct count: 31098
- Distinct values:

| verbatimcoordinates                                                                                      | count  |
|----------------------------------------------------------------------------------------------------------|--------|
| NULL                                                                                                     | 107708 |
| NA                                                                                                       | 110539 |
| slon: -68.5833282470703, elon: -68.5833282470703, slat: 48.6666717529297, elat: 48.6666717529297         | 4186   |
| 45° 36.69' N, 60° 49.19' W                                                                               | 3622   |
| slon: -94.9000015258789, elon: -94.9000015258789, slat: 74.6600036621094, elat: 74.6600036621094         | 3428   |
| 45.272361, -66.073899                                                                                    | 3227   |
| 44° 48.79' N, 62° 34.26' W                                                                               | 3044   |
| "11° 19' 32.1"" N 74° 7' 42"" W"                                                                         | 2966   |
| slon: -63.310001373291, elon: -63.310001373291, slat: 44.2599983215332, elat: 44.2599983215332           | 2931   |
| 11°16'41.16"N 73°51'52.88"O                                                                              | 2771   |
| "12° 30' 1.5"" N 81° 43' 59.9"" W"                                                                       | 2720   |
| "12° 30' 47.2"" N 81° 43' 52.4"" W"                                                                      | 2711   |


### verbatimlatitude
- NULL Values: 107 822 312
- Column type: Char 
- Total distinct count: 56025
- Distinct values:

| verbatimlatitude               | count     |
|--------------------------------|-----------|
| NULL                           | 107822312 |
| 33°41′N                        | 45450     |
| "12° 30' 47.2"" N"             | 13425     |
| "10° 10' 29.4"" N"             | 13292     |
| "11° 19' 47.4"" N"             | 13066     |
| "12° 30' 1.5"" N"              | 11961     |
| "10° 14' 3"" N"                | 11898     |
| "11° 19' 32.1"" N"             | 11734     |
| 32°12'N                        | 5788      |
| "2° 57' 30.6"" N"              | 5186      |


### verbatimlongitude
- NULL Values: 107 829 410
- Column type: Char 
- Total distinct count: 59524
- Distinct values:

| verbatimlongitude            | count     |
|------------------------------|-----------|
| NULL                         | 107829410 |
| 135°20′E                     | 45450     |
| "81° 43' 52.4"" W"           | 13425     |
| "75° 46' 14.3"" W"           | 13292     |
| "74° 7' 42.9"" W"            | 13066     |
| "81° 43' 59.9"" W"           | 11961     |
| "75° 44' 47.1"" W"           | 11898     |
| "74° 7' 42"" W"              | 11734     |
| 64°36'W                      | 5802      |
| "78° 10' 40.9"" W"           | 5186      |


### verbatimcoordinatesystem
 NULL Values: 108 115 198
- Column type: Char 
- Total distinct count:  25
- Distinct values:

| verbatimcoordinatesystem              | count     |
|---------------------------------------|-----------|
| NULL                                  | 108115198 |
| decimal degrees                       | 181605    |
| NA                                    | 110539    |
| degrees minutes seconds               | 35238     |
| Grados, minutos, segundos             | 22448     |
| WGS84                                 | 13644     |
| grados minutos segundos               | 8546      |
| Grados decimales                      | 5028      |
| Coordenadas proyectadas               | 4633      |
| degrees minutes                       | 1632      |
| Grados, Minutos, Segundos - GMS       | 1607      |
| degrees decimal minutes               | 1503      |
| Grados Minutos Segundos               | 765       |
| degrees                               | 698       |


### verbatimsrs
 NULL Values: 108 235 058
- Column type: Char 
- Total distinct count:  18
- Distinct values:

| verbatimsrs                  | count     |
|------------------------------|-----------|
| NULL                         | 108235058 |
| WGS84                        | 137931    |
| NA                           | 110539    |
| NAD 83                       | 11674     |
| MAGNA-SIRGAS origen CTM-12   | 4059      |
| TOKYO                        | 2095      |
| Tokyo Datum                  | 1945      |
| MAGNA-SIRGAS origen Bogotá   | 574       |
| EPSG:4326                    | 378       |
| SIRGAS                       | 150       |
| Grados, minutos, segundos    | 10        |


### geodeticdatum
- NULL Values: 56 324 406
- Column type: Char 
- Total distinct count:  18
- Distinct values:

| geodeticdatum                          | count    |
|----------------------------------------|----------|
| NULL                                   | 56324406 |
| EPSG:4326                              | 28569910 |
| WGS84                                  | 12370099 |
| EPSG:4326 WGS84                        | 5862707  |
| WGS 84                                 | 2741548  |
| EPSG:4326 WGS 84                       | 1422497  |
| ESPG:4326 WGS84 decimal degrees        | 972784   |
| not recorded (forced WGS84)            | 148444   |
| WGS84_EPSG:4326                        | 51378    |
| World Geodetic System 1984             | 8681     |


### coordinateprecision
- NULL Values: 97 623 799
- Column type: Char 
- Total distinct count:  
- Distinct values:

| coordinateprecision             | count    |
|---------------------------------|----------|
| NULL                            | 97623799 |
| 9.99999999999999955e-07         | 2772562  |
| 0.000100000000000000005         | 1179728  |
| 0.01667                         | 957297   |
| 1.00000000000000008e-05         | 699838   |
| 0.0009                          | 663144   |
| 0.0018                          | 642363   |
| 0.0179                          | 357208   |
| 100.0                           | 348922   |
| 0.0004                          | 326589   |


### pointradiusspatialfit
- NULL Values: 61 429 050
- Column type: double precision
- Total distinct count:  
- Distinct values: 7213290


| footprintwkt                  | count    |
|-------------------------------|----------|
| NULL                          | 61429050 |
| POINT(153.562 -27.345)        | 2537024  |
| POINT(151.22667 -34.11923)    | 2533383  |
| POINT(148.23333 -42.59667)    | 2291980  |
| POINT(115.41667 -32.0)        | 1495964  |
| POINT ( )                     | 1413105  |
| MULTIPOLYGON (((-124.576907943641 49.5172678603206,-124.647824626891 49.4838140698403,-124.685095085765 49.4722579040976,-124.724994684329 49.4672021632683,-124.722560520936 49.4609580466264,-124.778607982738 49.4229759780448,-125.094620150874 49.7126698855909,-124.859683180294 49.7009822284496,-124.589644103201 49.5263530505814,-124.587614793274 49.5249979187244,-124.576907943641 49.5172678603206))) | 202053     |



### footprintsrs
- NULL Values: 96 556 230
- Column type: Char 
- Total distinct count:  
- All Distinct values: 

| footprintsrs                                                                                                         | count    |
|----------------------------------------------------------------------------------------------------------------------|----------|
| NULL                                                                                                                 | 96556230 |
| EPSG:4326                                                                                                            | 11488823 |
| GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.0174532925199433]] | 407876   |
| GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]] | 51378    |
| epsg:4326                                                                                                            | 79       |
| WGS84                                                                                                                | 35       |



### footprintspatialfit
- NULL Values: 108 504 203
- Column type: Char 
- Total distinct count:  
- All Distinct values: 

| footprintspatialfit | count     |
|---------------------|-----------|
| NULL                | 108504203 |
| 0                   | 218       |



### georeferencedby
- NULL Values: 106 303 420
- Column type: Char 
- Total distinct count:  250
- Distinct values: 

| georeferencedby          | count     |
|--------------------------|-----------|
| NULL                     | 106303420 |
| Small boat operator      | 972784    |
| ADCNR/GCRL               | 564982    |
| USGS                     | 374584    |
| NA                       | 110539    |
| Lead Biologist           | 54464     |
| Watt and Scrosati, 2014  | 11615     |
| B.C.A. FERREIRA (MNRJ)   | 11447     |
| unknown                  | 10007     |
| OBIS Canada              | 9904      |


### georeferenceddate
- NULL Values: 103 518 312
- Column type: Char 
- Total distinct count:  2512004
- Distinct values: 

| georeferenceddate       | count     |
|-------------------------|-----------|
| NULL                    | 103518312 |
| 2000-01-01 00:00:00     | 7870      |
| 2014-10/2014-12         | 6876      |
| 2019-06-01              | 5611      |
| 2016-06                 | 4571      |
| 2001                    | 4010      |
| 1913-01-01T00:00:00     | 3738      |
| 1913-08-01T00:00:00     | 3550      |
| 1913-07-01T00:00:00     | 3526      |
| 2019-09-27T08:35:46     | 3249      |
| 1913-12-01T00:00:00     | 3237      |


### georeferenceprotocol
- NULL Values: 102 923 233
- Column type: Char 
- Total distinct count: 
- Distinct values: 


| georeferenceprotocol                                                                                       | count     |
|------------------------------------------------------------------------------------------------------------|-----------|
| NULL                                                                                                       | 102923233 |
| ArgosLocation (http://www.argos-system.org/manual/3-location/34_location_classes.htm)                     | 2331595   |
| Small boat-based GPS                                                                                       | 972784    |
| Handheld GPS                                                                                               | 633816    |
| Coordinate uncertainty is based on starting point plus travel during trawl.                               | 564982    |
| Shipboard mounted GPS                                                                                      | 374584    |
| Exact lon/lat if provided else centriod of research grid area or statitical unit areas                     | 242046    |
| GPS locations are verified using ArcGIS and repeat visits                                                 | 116163    |
| FishNet Collaborative Georeferencing Project                                                               | 60473     |
| Coordinates obtained  based on orthophotography inspection, personal communication and previous studies on sites | 58222     |


### georeferencesources
- NULL Values: 108 302 870
- Column type: Char 
- Total distinct count: 154
- Distinct values: 

| georeferencesources | count     |
|---------------------|-----------|
| NULL                | 108302870 |
| GPS                 | 84057     |
| GEOLocate           | 24582     |
| GeoLocate           | 19392     |
| GEOLOCATE           | 7159      |
| Google Earth        | 6645      |
| MarineRegions.org   | 6281      |
| Provided georef     | 5966      |
| Map                 | 5792      |
| Browne (2001)       | 5602      |


### georeferenceverificationstatus
- NULL Values: 108 259 213
- Column type: Char 
- Total distinct count: 28
- Distinct values: 


| georeferenceverificationstatus            | count     |
|-------------------------------------------|-----------|
| NULL                                      | 108259213 |
| requires verification                     | 166659    |
| verified by curator                       | 32514     |
| unverified                                | 20648     |
| Verificado por el proveedor de los datos  | 6484      |
| verified by Onuminya, TO                  | 3271      |
| Verificado por Curador                    | 2452      |
| Verificado por el custodio de los datos   | 2199      |
| Unverified                                | 1901      |
| Verificado por el custodio                | 1433      |



### georeferenceremarks
- NULL Values: 105 864 513
- Column type: Char 
- Total distinct count: 4548
- Distinct values: 

| georeferenceremarks                                                                         | count     |
|---------------------------------------------------------------------------------------------|-----------|
| NULL                                                                                        | 105864513 |
| place of animal capture                                                                     | 2331595   |
| latitude and longitude coordinates provided in units of decimal degrees in the database view | 93811     |
| Coordinate Precision: 0,0001°                                                               | 26993     |
| Coordinate Precision: 0,00001°                                                              | 25094     |
| Derived from googlemaps Geographic datum = EPSG:3857                                        | 22187     |
| station coordinates                                                                         | 21699     |
| latitude and longitude were calculated as the middle of the trawl                           | 15183     |
| Coordinate Precision: 0,01°                                                                 | 11239     |


### geologicalcontextid
- NULL Values: 108 504 421
- Column type: Char 
- Total distinct count: 



### earliesteonorlowesteonothem
- NULL Values: 108504421
- Column type: Char 
- Total distinct count: 
- ALL NULL 


### latesteonorhighesteonothem
- NULL Values: 108 504 421
- Column type: Char 
- Total distinct count: 
- ALL NULL 


### earliesteraorlowesterathem
- NULL Values: 108 504 421
- Column type: Char 
- Total distinct count: 
- ALL NULL 


### latesteraorhighesterathem
- NULL Values: 108 504 421
- Column type: Char 
- Total distinct count: 
- ALL NULL 


### earliestperiodorlowestsystem
- NULL Values: 108 504 420
- Column type: Char 
- Total distinct count: 2
- Distinct values:

| earliestperiodorlowestsystem | count     |
|------------------------------|-----------|
| NULL                         | 108504420 |
| Cretaceous                   | 1         |



### latestperiodorhighestsystem
- NULL Values: 108 504 421
- Column type: Char 
- Total distinct count: 
- ALL NULL


### earliestperiodorlowestsystem
- NULL Values: 108 504 420
- Column type: Char 
- Total distinct count: 2
- Distinct values:

| earliestperiodorlowestsystem | count     |
|------------------------------|-----------|
| NULL                         | 108504420 |
| Cretaceous                   | 1         |



### latestperiodorhighestsystem
- NULL Values: 108 504 421
- Column type: Char 
- Total distinct count: 
- ALL NULL

### earliestepochorlowestseries
- NULL Values: 108 504 390
- Column type: Char 
- Total distinct count: 4
- Distinct values:

| earliestepochorlowestseries | count     |
|-----------------------------|-----------|
| NULL                        | 108504390 |
| Pliocene                    | 22        |
| Miocene                     | 6         |
| Pleistocene                 | 3         |


### latestepochorhighestseries
- NULL Values: 108 504 421
- Column type: Char 
- Total distinct count: 
- ALL NULL


### earliestageorloweststage
- NULL Values: 108 504 420
- Column type: Char 
- Total distinct count: 2
- Distinct values:

| earliestageorloweststage | count     |
|--------------------------|-----------|
| NULL                     | 108504420 |
| Lutetian                 | 1         |



### latestageorhigheststage
- NULL Values: 108 504 421
- Column type: Char 
- Total distinct count: 
- ALL NULL


### lowestbiostratigraphiczone
- NULL Values: 108 504 195
- Column type: Char 
- Total distinct count: 2
- Distinct values:

| lowestbiostratigraphiczone | count     |
|----------------------------|-----------|
| NULL                       | 108504195 |
| LOWTIDE                    | 226       |


### highestbiostratigraphiczone
- NULL Values: 108 504 421
- Column type: Char 
- Total distinct count: 
- ALL NULL


### lithostratigraphicterms
- NULL Values: 108 504 421
- Column type: Char 
- Total distinct count: 
- ALL NULL


### group
- NULL Values: 108 504 421
- Column type: Char 
- Total distinct count: 
- ALL NULL


### formation
- NULL Values: 108 504 421
- Column type: Char 
- Total distinct count: 
- ALL NULL



### member
- NULL Values: 108 504 421
- Column type: Char 
- Total distinct count: 
- ALL NULL


### bed
- NULL Values: 108 504 421
- Column type: Char 
- Total distinct count: 
- ALL NULL


### identificationid
- NULL Values: 108 366 114
- Column type: Char 
- Total distinct count: 128 883
- Distinct values:

| identificationid                                     | count     |
|------------------------------------------------------|-----------|
| NULL                                                 | 108366114 |
| 4                                                    | 713       |
| 3                                                    | 611       |
| 1                                                    | 609       |
| 135426                                               | 20        |
| 117080                                               | 15        |
| 117568                                               | 15        |
| 207072                                               | 14        |
| ABYSSLINE 02 (AB02)_TN319_UK1-AB2-Annelida           | 10        |
| ABYSSLINE 02 (AB02)_TN319_UK1-AB2-Copepoda           | 10        |
| ABYSSLINE 02 (AB02)_TN319_UK1-AB2-Loricifera         | 10        |
| ABYSSLINE 02 (AB02)_TN319_UK1-AB2-Nematoda           | 10        |
| ABYSSLINE 02 (AB02)_TN319_UK1-AB2-Ostracoda          | 10        |
| ABYSSLINE 02 (AB02)_TN319_UK1-AB2-Rotifera           | 10        |
| SO239_1_192                                          | 10        |
| 221223                                               | 9         |
| SO239_1_158                                          | 7         |
| 430663                                               | 6         |
| ABYSSLINE 02 (AB02)_TN319_UK1-AB2-Isopoda            | 6         |
| DY125-27_2_0-1cm                                     | 6         |
| ABYSSLINE 02 (AB02)_TN319_UK1-AB2-Coelenterata       | 5         |
| DY125-27_2_4-6cm                                     | 5         |
| SO239_1_99                                           | 5         |
| 117529                                               | 4         |


### identifiedby
- NULL Values: 97 706 513
- Column type: Char 
- Total distinct count: 42360
- Distinct values:

| identifiedby        | count   |
|---------------------|---------|
| NULL                | 97706513|
| ADCNR/GCRL          | 564982  |
| NA                  | 293720  |
| DFO-NAFC            | 242046  |
| Redacted            | 224494  |
| NIEA/WMU            | 165010  |
| José Gomes-Pereira  | 148143  |



### identifiedbyid
- NULL Values: 108 488 544
- Column type: Char 
- Total distinct count: 50
- Distinct values:

| identifiedbyid                                                                       | count     |
|--------------------------------------------------------------------------------------|-----------|
| NULL                                                                                 | 108488544 |
| [https://orcid.org/0000-0002-9223-9750](https://orcid.org/0000-0002-9223-9750)       | 3481      |
| [https://orcid.org/0000-0003-3610-8155](https://orcid.org/0000-0003-3610-8155)       | 2559      |
| [https://orcid.org/0000-0002-7535-3228](https://orcid.org/0000-0002-7535-3228)       | 2531      |
| [https://orcid.org/0000-0002-2408-4849](https://orcid.org/0000-0002-2408-4849)       | 1276      |
| 0000-0002-0981-7442                                                                  | 1266      |
| [https://orcid.org/0000-0003-3819-2004](https://orcid.org/0000-0003-3819-2004) \| [https://orcid.org/0000-0001-8852-0796](https://orcid.org/0000-0001-8852-0796) | 528       |
| [https://www.wikidata.org/wiki/Q29167703](https://www.wikidata.org/wiki/Q29167703)   | 488       |



### dateidentified
- NULL Values: 99 851 112
- Column type: Char 
- Total distinct count: 2545466
- Distinct values:

| dateidentified | count   |
|----------------|---------|
| NULL           | 99851112|
| NA             | 111594  |
| 2004-06-27     | 20060   |
| 0-00-00        | 18915   |
| 1987-03-11     | 18153   |
| 2005           | 15689   |
| 2008           | 13951   |
| 2004           | 13770   |
| 2007           | 12889   |
| 1995-07-07     | 11488   |
| 2010           | 8485    |
| 2001           | 2604    |
| 1999           | 1350    |



### identificationreferences
- NULL Values: 90 187 286
- Column type: Char 
- Total distinct count: 431
- Distinct values:

| identificationreferences                                    | count     |
|-------------------------------------------------------------|-----------|
| NULL                                                        | 90187286  |
| [https://github.com/AusMicrobiome/scientific_manual](https://github.com/AusMicrobiome/scientific_manual)         | 18165329  |
| [https://github.com/MBARI-BOG/BOG-Banzai-Dada2-Pipeline](https://github.com/MBARI-BOG/BOG-Banzai-Dada2-Pipeline) | 33673     |


### identificationremarks
- NULL Values: 84 976 750
- Column type: Char 
- Total distinct count: 14059
- Distinct values:

| identificationremarks                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | count    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| NULL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 84976750 |
| Identification Type:Visual sighting                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 3336654  |
| Australian Microbiome OTU Database - tabular export --- Amplicon filter: amplicon is '27f519r_bacteria' Taxonomy filter: taxonomy_source is 'silva138 SKlearn' r1 is 'd__Bacteria' r2 is not 'd__Bacteria_unclassified' Traits filter: (no trait filter applied) Contextual filter: Voyage Code contains "in2016_v03" Australian Microbiome Database Metadata: Dataset methodology=bpaotu_1.33.0__analysis_2.2.0__AM_db_v3.2_202203021355.db__AM_data_submit_202205160949.tar.gz Dataset analysis url=[https://github.com/AusMicrobiome/amplicon/raw/2.2.0/docs/amplicon_analysis_workflow.docx](https://github.com/AusMicrobiome/amplicon/raw/2.2.0/docs/amplicon_analysis_workflow.docx) Dataset revision date=2022-05-24 --- How to cite Australian Microbiome data: [https://www.australianmicrobiome.com/protocols/acknowledgements/](https://www.australianmicrobiome.com/protocols/acknowledgements/) Australian Microbiome data use policy: [https://www.australianmicrobiome.com/protocols/data-policy/](https://www.australianmicrobiome.com/protocols/data-policy/) | 2121491  |



### identificationqualifier
- NULL Values: 106 899 279
- Column type: Char 
- Total distinct count: 14887
- Distinct values:

| identificationqualifier | count     |
|-------------------------|-----------|
| NULL                    | 106899279 |
| NA                      | 280042    |
| SP.                     | 204436    |
| SPP                     | 181069    |
| sp                      | 74631     |
| sp.                     | 71072     |
| SP                      | 68122     |
| qualifier: uncertain    | 30309     |
| qualifier: sp.          | 25398     |
| A                       | 21660     |


### identificationverificationstatus
- NULL Values: 108 054 734
- Column type: Char 
- Total distinct count: 23
- Distinct values:

| identificationverificationstatus | count     |
|-----------------------------------|-----------|
| NULL                              | 108054734 |
| Verificado                        | 340609    |
| 0                                 | 46721     |
| Verificado por especialista       | 32335     |
| features                          | 7772      |
| revised taxonomy                  | 7771      |
| unknown                           | 6253      |
| 1 - good                          | 3697      |
| Verificado por curador            | 1433      


### typestatus
- NULL Values: 108 148 009
- Column type: Char 
- Total distinct count: 650
- Distinct values:


| typestatus | count     |
|------------|-----------|
| NULL       | 108148009 |
| NA         | 110723    |
| specimen   | 57109     |
| Accepted   | 41339     |
| holotype   | 36089     |
| Uncertain  | 34625     |
| Paratype   | 23249     |
| PARATYPE   | 10663     |
| Holotype   | 10264     |
| paratype   | 8800      |


### taxonid
- NULL Values: 106 886 664
- Column type: Char 
- Total distinct count: 49516
- Distinct values:

| taxonid        | count     |
|----------------|-----------|
| NULL           | 106886664 |
| 232231         | 36785     |
| 1              | 19752     |
| 282054         | 19354     |
| aphiaID 273579 | 18752     |
| aphiaID 219640 | 17601     |
| 281130         | 16711     |
| 282753         | 16535     |
| 275798         | 15324     |


### scientificnameid
- NULL Values: 6 688 252
- Column type: Char 
- Total distinct count: 213047
- Distinct values:


| scientificnameid                                  | count    |
|---------------------------------------------------|----------|
| NULL                                              | 6688252  |
| urn:lsid:marinespecies.org:taxname:392750         | 4215851  |
| urn:lsid:marinespecies.org:taxname:151159         | 1956864  |
| urn:lsid:marinespecies.org:taxname:416268         | 1951299  |
| urn:lsid:marinespecies.org:taxname:6              | 1528488  |
| urn:lsid:marinespecies.org:taxname:146213         | 1279933  |
| urn:lsid:marinespecies.org:taxname:146537         | 1278151  |


### acceptednameusageid
- NULL Values: 108 408 341
- Column type: Char 
- Total distinct count: 4693
- Distinct values:

| acceptednameusageid                           | count     |
|-----------------------------------------------|-----------|
| NULL                                          | 108408341 |
| urn:lsid:marinespecies.org:taxname:1292       | 3249      |
| urn:lsid:marinespecies.org:taxname:558        | 2607      |
| urn:lsid:marinespecies.org:taxname:207516     | 2229      |
| urn:lsid:marinespecies.org:taxname:210726     | 2219      |
| urn:lsid:marinespecies.org:taxname:288889     | 2013      |
| urn:lsid:marinespecies.org:taxname:758259     | 1788      |
| urn:lsid:marinespecies.org:taxname:287962     | 1589      |



### parentnameusageid
- NULL Values: 108 474 912
- Column type: Char 
- Total distinct count: 2701
- Distinct values:

| parentnameusageid | count     |
|-------------------|-----------|
| NULL              | 108474912 |
| 370435            | 3371      |
| 11676             | 1004      |
| 1341              | 748       |
| 173828            | 660       |
| 239391            | 472       |
| 1                 | 318       |
| 129096            | 288       |


- Can be converted to int
```sql
SELECT parentnameusageid::integer
FROM obis_20230208
WHERE pg_input_is_valid(parentnameusageid, 'integer');
```
- selected rows: 29504


### originalnameusageid
- NULL Values: 108 504 416
- Column type: Char 
- Total distinct count: 2
- Distinct values:

| originalnameusageid                 | count     |
|-------------------------------------|-----------|
| NULL                                | 108504416 |
| 28D73F00-F8E0-4997-9E02-FF70B2571CE5 | 5         |



### nameaccordingtoid
- NULL Values: 108 107 275
- Column type: Char 
- Total distinct count: 3155
- Distinct values:

| nameaccordingtoid                                                    | count     |
|----------------------------------------------------------------------|-----------|
| NULL                                                                 | 108107275 |
| [http://www.marinespecies.org/aphia.php?p=taxdetails&id=368670](http://www.marinespecies.org/aphia.php?p=taxdetails&id=368670) | 30928     |
| [http://www.marinespecies.org/aphia.php?p=taxdetails&id=206953](http://www.marinespecies.org/aphia.php?p=taxdetails&id=206953) | 29620     |
| [http://www.marinespecies.org/aphia.php?p=taxdetails&id=144086](http://www.marinespecies.org/aphia.php?p=taxdetails&id=144086) | 15181     |
| [http://www.marinespecies.org/aphia.php?p=taxdetails&id=758261](http://www.marinespecies.org/aphia.php?p=taxdetails&id=758261) | 14537     |
| [http://www.marinespecies.org/aphia.php?p=taxdetails&id=289246](http://www.marinespecies.org/aphia.php?p=taxdetails&id=289246) | 12765     |
| [http://www.marinespecies.org/aphia.php?p=taxdetails&id=207516](http://www.marinespecies.org/aphia.php?p=taxdetails&id=207516) | 11471     |
| [http://www.marinespecies.org/aphia.php?p=taxdetails&id=758260](http://www.marinespecies.org/aphia.php?p=taxdetails&id=758260) | 10370     |
| [http://www.marinespecies.org/aphia.php?p=taxdetails&id=287916](http://www.marinespecies.org/aphia.php?p=taxdetails&id=287916) | 8971      |



### namepublishedinid
- NULL Values: 108 500 072
- Column type: Char 
- Total distinct count: 892
- Distinct values:

| namepublishedinid                    | count     |
|--------------------------------------|-----------|
| NULL                                 | 108500072 |
| de18f134-2b4c-4ce6-8c2b-8244977469d5 | 339       |
| 2c6327e1-5560-4db4-b9ca-76a0fa03d975 | 121       |
| 4f233817-7167-40c5-b0fe-35a6148b416a | 120       |
| 0e5a74d8-d5ce-4f6d-afd1-20e945b1628f | 95        |
| 216530e4-8ea8-440f-a19c-17b4c129aeb4 | 75        |


### taxonconceptid
- NULL Values: 107 399 045
- Column type: Char 
- Total distinct count: 14681
- Distinct values:

| taxonconceptid                                                            | count     |
|---------------------------------------------------------------------------|-----------|
| NULL                                                                      | 107399045 |
| urn:lsid:biodiversity.org.au:afd.taxon:803a6245-e23d-444c-a2ac-4b8a09e69c3a | 79680     |
| urn:lsid:biodiversity.org.au:afd.taxon:2e0b8093-273f-4291-80f7-d99d15a84bbd | 65043     |
| urn:lsid:biodiversity.org.au:afd.taxon:c46afabe-2ea4-43e5-8f4d-4075e7f82589 | 53027     |
| urn:lsid:biodiversity.org.au:afd.taxon:ba624e08-5847-4c34-96cf-c3b414f00117 | 47676     |



### acceptednameusage
- NULL Values: 108 332 343
- Column type: Char 
- Total distinct count: 6879
- Distinct values:

| acceptednameusage                            | count     |
|----------------------------------------------|-----------|
| NULL                                         | 108332343 |
| Ctenochaetus striatus; (Quoy & Gaimard, 1825) | 10602     |
| Chlorurus sordidus; (Forsskål, 1775)          | 4319      |
| Anthozoa                                      | 3254      |
| Acanthurus nigricans; (Linnaeus, 1758)        | 2731      |


### parentnameusage
- NULL Values: 108 504 281
- Column type: Char 
- Total distinct count: 65
- Distinct values:

| parentnameusage                    | count     |
|------------------------------------|-----------|
| NULL                               | 108504281 |
| Cryptogonimidae Ward, 1917         | 14        |
| Diplostomidae Poirier, 1886        | 9         |
| Hydrocharitaceae                   | 7         |
| Neoechinorhynchidae Ward, 1917     | 7         |
| Homalometron Stafford, 1904        | 5         |
| Stephanostomum Looss, 1899         | 5         |



### originalnameusage
- NULL Values: 108 456 454
- Column type: Char 
- Total distinct count: 5962
- Distinct values:

| originalnameusage                    | count     |
|--------------------------------------|-----------|
| NULL                                 | 108456454 |
| Metridia gerlachei                   | 567       |
| Calanoides acutus                    | 555       |
| Euchaeta                             | 509       |
| Halimeda opuntia                     | 452       |
| Laurencia                            | 451       |
| Metridia sp.                         | 391       |
| Lobophora variegata                  | 347       |
| Fusitriton magellanicus laudandus    | 341       |


### nameaccordingto
- NULL Values: 107 485 018
- Column type: Char 
- Total distinct count: 5096
- Distinct values:

| nameaccordingto                                                                                                                                                                                                                                                         | count     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| NULL                                                                                                                                                                                                                                                                    | 107485018 |
| WoRMS                                                                                                                                                                                                                                                                   | 373575    |
| Hoeksema, B. W.; Cairns, S. (2021). World List of Scleractinia. Pocillopora damicornis (Linnaeus, 1758). Accessed through: World Register of Marine Species at: http://www.marinespecies.org/aphia.php?p=taxdetails&id=206953 on 2021-11-16                            | 19053     |
| WoRMS (2021). Florideophyceae. Accessed at: http://www.marinespecies.org/aphia.php?p=taxdetails&id=368670 on 2021-02-18                                                                                                                                                 | 17140     |
| WoRMS (2021). Florideophyceae. Accessed at: http://www.marinespecies.org/aphia.php?p=taxdetails&id=368670 on 2021-11-16                                                                                                                                                 | 13762     |



### namepublishedin
- NULL Values: 108 490 574
- Column type: Char 
- Total distinct count: 1183
- Distinct values:

| namepublishedin                                                                                                                                                                                                                                                                                      | count     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| NULL                                                                                                                                                                                                                                                                                                 | 108490574 |
| Rosenberg, G.; Huber, M. (2010). Philobrya sublaevis. In: MolluscaBase (2017). Accessed through: World Register of Marine Species at http://www.marinespecies.org/aphia.php?p=taxdetails&id=197365 on 2018-02-07                                                                                       | 251       |
| Bouchet, P.; Huber, M. (2013). Lissarca notorcadensis Melvill & Standen, 1907. In: MolluscaBase (2017). Accessed through: World Register of Marine Species at http://www.marinespecies.org/aphia.php?p=taxdetails&id=197241 on 2018-02-07                                                              | 230       |
| Huber, M. (2010). Adacnarca nitens. In: MolluscaBase (2017). Accessed through: World Register of Marine Species at http://www.marinespecies.org/aphia.php?p=taxdetails&id=197020 on 2018-02-07                                                                                                         | 213       |


### namepublishedinyear
- NULL Values: 108 503 918
- Column type: Int 
- Total distinct count: 76
- Distinct values:

| namepublishedinyear | count     |
|---------------------|-----------|
| NULL                | 108503918 |
| 1910                | 72        |
| 1902                | 38        |
| 1859                | 33        |
| 1912                | 27        |
| 1936                | 23        |
| 1934                | 18        |
| 1974                | 17        |
| 1914                | 15        |
| 1860                | 14        |
| 1954                | 13        |


- can be converted to int


### higherclassification
- NULL Values: 107 993 994
- Column type: Char 
- Total distinct count: 14107
- Distinct values:

| higherclassification                                                           | count     |
|--------------------------------------------------------------------------------|-----------|
| NULL                                                                           | 107993994 |
| ANIMALIA \| CHORDATA \| ACTINOPTERYGII \| ANGUILLIFORMES \| GADIDAE \|  \| THERAGRA | 19897     |
| ANIMALIA \| CHORDATA \| ACTINOPTERYGII \| ANGUILLIFORMES \| PLEURONECTIDAE \|  \| HIPPOGLOSSOIDES | 12149     |
| ANIMALIA \| CHORDATA \| ACTINOPTERYGII \| ANGUILLIFORMES \| AMMODYTIDAE \|  \| AMMODYTES | 8648      |
| ANIMALIA \| CHORDATA \| ACTINOPTERYGII \| ANGUILLIFORMES \| SCORPAENIDAE \|  \| SEBASTES | 7380      |
| Animalia, Chordata, Actinopteri, Gobiiformes, Gobiidae, Gobiinae                | 7337      |
| Animalia, Chordata, Actinopteri, Perciformes, Labroidei, Labridae               | 6473      |
| ANIMALIA \| CHORDATA \| ACTINOPTERYGII \| ANGUILLIFORMES \| HEXAGRAMMIDAE \|  \| HEXAGRAMMOS | 5813      |
| ANIMALIA \| CHORDATA \| ACTINOPTERYGII \| ANGUILLIFORMES \| MYCTOPHIDAE \|  \| STENOBRACHIUS | 5559      |
| Animalia, Chordata, Actinopteri, Kurtiformes, Apogonidae, Apogoninae            | 5421      |


### specificepithet
- NULL Values: 73 463 489
- Column type: Char 
- Total distinct count: 67861
- Distinct values:

| specificepithet | count    |
|-----------------|----------|
| NULL            | 73463489 |
| pallasii        | 1952739  |
| NA              | 1687623  |
| morhua          | 1186295  |
| aeglefinus      | 891001   |
| jordani         | 890028   |
| limanda         | 701161   |
| harengus        | 699817   |
| merlangus       | 685559   |
| americanus      | 683675   |
| platessoides    | 502727   |
| glacialis       | 435669   |


### infraspecificepithet
- NULL Values: 108 254 387
- Column type: Char 
- Total distinct count: 1870
- Distinct values:

| infraspecificepithet | count     |
|----------------------|-----------|
| NULL                 | 108254387 |
| NA                   | 118396    |
| latirostris          | 29875     |
| borealis             | 15489     |
| microrhyncha         | 11178     |
| michahellis          | 10633     |
| elongatus            | 6548      |
| finmarchicus         | 4474      |
| pallasii             | 4146      |
| glaucoides           | 2339      |
| mordax                | 2153      |



### verbatimtaxonrank
- NULL Values: 108 460 396
- Column type: Char 
- Total distinct count: 220
- Distinct values:

| verbatimtaxonrank | count  |
|-------------------|--------|
| NULL              | 108460396 |
| sp.               | 37806  |
| sp. 1             | 1485   |
| sp. 2             | 698    |
| Morfoespecie 1    | 472    |
| sp. 3             | 329    |
| spp.              | 233    |
| sp. 4             | 206    |
| sp 1              | 184    |



### scientificnameauthorship
- NULL Values: 70 141 063
- Column type: Char 
- Total distinct count: 84133
- Distinct values:


| scientificnameauthorship     | count    |
|------------------------------|----------|
| NULL                         | 70141063 |
| (Linnaeus, 1758)             | 5748734  |
| Linnaeus, 1758               | 3562796  |
| Valenciennes, 1847           | 1949849  |
| Rathbun 1902                 | 1217995  |
| (Walbaum, 1792)              | 1027647  |
| (Mitchill, 1814)             | 539002   |
| (Fabricius, 1780)            | 499275   |
| (Linnaeus, 1761)             | 442674   |
| Cuvier, 1829                 | 323202   |
| (Tschudi, 1843)              | 299901   |


### vernacularname
- NULL Values: 82 679 473
- Column type: Char 
- Total distinct count: 29079
- Distinct values:

| vernacularname            | count   |
|---------------------------|---------|
| NULL                      | 82679473|
| Pacific herring           | 1923437 |
| Southern elephant seal    | 914197  |
| PINK SHRIMP (SMOOTH)      | 863348  |
| Little penguin            | 493956  |
| Northern Fulmar           | 458965  |
| HADDOCK                   | 382487  |
| SIDESTRIPE SHRIMP         | 351551  |
| Weddell seal              | 342737  |
| Peruvian Booby            | 299901  |
| NA                        | 288790  |


### nomenclaturalcode
- NULL Values: 103 072 222
- Column type: Char 
- Total distinct count: 11
- All Distinct values:

| nomenclaturalcode | count    |
|-------------------|----------|
| NULL              | 103072222|
| WoRMS LSID        | 4909789  |
| ICZN              | 502889   |
| ICN               | 9485     |
| NULL              | 5370     |
| WoRMS             | 2341     |
| ICNZ              | 1267     |
| ICBN              | 614      |
| ICNB              | 375      |
| LSID              | 65       |
| PhyloCode         | 4        |



### taxonomicstatus
- NULL Values: 100 727 661
- Column type: Char 
- Total distinct count: 45
- Distinct values:


| taxonomicstatus            | count    |
|----------------------------|----------|
| NULL                       | 100727661|
| valid                      | 4923636  |
| accepted                   | 2294104  |
| Aceptado                   | 304891   |
| Válido                     | 117107   |
| alternate representation   | 45451    |
| Uncertain                  | 34625    |
| unaccepted                 | 24369    |
| Inválido                   | 18247    |
| aceptado                   | 8751     |



### nomenclaturalstatus
- NULL Values: 108 504 182
- Column type: Char 
- Total distinct count: 2
- All Distinct values:

| nomenclaturalstatus | count     |
|---------------------|-----------|
| NULL                | 108504182 |
| Aceptado            | 239       |


### taxonremarks
- NULL Values: 103 005 119
- Column type: Char 
- Total distinct count: 25346
- Distinct values:

| taxonremarks                                                        | count     |
|---------------------------------------------------------------------|-----------|
| NULL                                                                | 103005119 |
| Taxon recorded as "220" by the provider                             | 332283    |
| Taxon recorded as "PEBO" by the provider                            | 299901    |
| Taxon recorded as "Balaenoptera acutorostrata" by the provider      | 224734    |
| Taxon recorded as "Grey seal" by the provider                       | 210129    |
| Taxon recorded as "6340" by the provider                            | 188958    |
| Taxon recorded as "Humpback Whale" by the provider                  | 152935    |
| Taxon recorded as "Brown booby" by the provider                     | 149513    |
| Taxon recorded as "6020" by the provider                            | 132661    |
| Taxon recorded as "710" by the provider                             | 131817    |
| Taxon recorded as "Unidentified Gull" by the provider               | 78937     |
