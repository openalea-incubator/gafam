# Erreurs

### p3.txt
^+S298.12

p9.txt: ln 395 (v346)
p97= <665.1(type=BL,_line=2667)'
p140: Args  478)S103. of vertex  414 of type  _line is not of type 
p141: Args  1376)B70. of vertex  1280 of type  _line is not of type
p146: Args  1241)B38. of vertex  1131 of type




## En tête
Change entete de tous les fichiers
Noeud et erreur last line

## MTG

### p03
* ^<S298.12 -> +S298.12
* SB22.1 -> B22.1
* 128.7 -> S128.7

* Replce /S235.2-9 par <S235.2-9
		^/S235.1																	BL												
		^/S235.2																													
			+S235.3								2019					0.2			VG								53.924	53.924			
		^/S235.4																	BL												
		^/S235.5																	BL												
		^/S235.6																	BL												
		^/S235.7																	BL												
		^/S235.8																	BL												
		^/S235.9																	BL												
* ^:S246 -> ^/S246
* S41.1 : add a tab

### p04
* ^<S183.10 -> +S183.10
* ^<S294.1 -> +S294.1
* ^/213.1 -> ^/S213.1
* ^:S344 -> ^/S344
* /452 -> / S452

### p09
* ^<S328.12 : ERROR ^<S328.12(realisation=2019,length=20.5,type=FL,length_bourse=1,leaf_area_2019=167.23195,leaf_area_2019b=228.5461505,_line=1268)
Fix: ^<S328.12 -> +S328.12

* Args  394)201 of vertex  346 of type  _line is not of type  <type 'int'>
+S49.21 sur la ligne suivante
* NODE  +135.30(realisation=2019,length=7.8,type=FL,leaf_area_2019=71.78002,

Fix: +135.30 -> +S135.30

* NODE  <189.1(type=BL,_line=855) False
<189.1 -> <S189.1

### p12

 ^B24.1 -> ^<B24.1

### p23
OK

### p27
* ERROR ^+S411.1(realisation=2019,length=2.3,type=FL,leaf_area_2019=66.56147,leaf_area_2019b=66.56147,_line=1362)

Fix: ^+S411.1 -> +S411.1
* Args  166) of vertex  118 of type  _line is not of type  <type 'int'>

Fix: S62.1 caractère etrange devant

* Args  923)' of vertex  874 of type  _line is not of type  <type 'int'>

Fix: ^/S264
* Args  1359)' of vertex  1311 of type  _line is not of type  <type 'int'>

Fix: ^<B33.1


### p28

Args  728)/239. of vertex  679 of type  _line is not of type  <type 'int'>
Fix = /239.1 -> /S239.1

### p30

Several errors 
    +S624
    ^/S624.1										

### p32
^B61.1	-> ^<B61.1	
### p34
OK

### p43
rgs  366)B17. 

### p49
NODE  <132(_line=619) False
<132 -> <S132

### p52

Args  188)201 of vertex  140 of type  _line is not of type  <type 'int'>
Args  883)/311. of vertex  834 of type  _line is not of type  <type 'int'>
Args  1169)� of vertex  1118 of type  _line is not of type  <type 'int'>
Args  1170)� of vertex  1120 of type  _line is not of type  <type 'int'>
Args  1171)� of vertex  1121 of type  _line is not of type  <type 'int'>
Args  1172)� of vertex  1122 of type  _line is not of type  <type 'int'>
Args  1872)/666. of vertex  1822 of type  _line is not of type  <type 'int'>
NODE  <923.2(type=BL,_line=2607) False
NODE  <923.3(type=BL,_line=2608) False

### p53
ERROR ^<S14.1(realisation=2019,length=0.6,type=FL,leaf_area_2019=17.66554,leaf_area_2019b=17.66554,_line=145)
ERROR ^S720.1(realisation=2019,length=7.5,type=FL,leaf_area_2019=69.52525,leaf_area_2019b=69.52525,_line=2036)
Args  119)S5. of vertex  69 of type  _line is not of type  <type 'int'>
Args  144) of vertex  87 of type  _line is not of type  <type 'int'>
Args  860)C11 of vertex  804 of type  _line is not of type  <type 'int'>
Args  2035)^S720. of vertex  1976 of type  _line is not of type  <type 'int'>
ERROR: Missing component for vertex 4

### p60
2 termes sur même ligne

### p68
NODE  <62.2(_line=213) False
NODE  <62.4(type=BL,_line=215) False
NODE  <62.5(type=BL,_line=216) False
NODE  <62.6(type=BL,_line=217) False
NODE  <62.7(type=BL,_line=218) False

### p77
ERROR ^<S18.6(realisation=2019,length=0.4,type=VG,leaf_area_2019=85.7604,leaf_area_2019b=85.7604,_line=145)
ERROR ^<S18.9(realisation=2019,length=0.2,type=VG,leaf_area_2019=84.3322,leaf_area_2019b=84.3322,_line=148)
ERROR ^<S18.16(realisation=2019,length=1.1,type=VG,leaf_area_2019=90.7591,leaf_area_2019b=90.7591,_line=155)
ERROR ^<S18.18(realisation=2019,length=1.1,type=VG,leaf_area_2019=90.7591,leaf_area_2019b=90.7591,_line=157)
ERROR ^<S18.20(realisation=2019,length=9.6,type=VG,leaf_area_2019=151.4576,leaf_area_2019b=151.4576,_line=159)
ERROR ^<S18.22(realisation=2019,length=33.1,type=VG,leaf_area_2019=319.2711,leaf_area_2019b=319.2711,_line=161)
Args  144) of vertex  96 of type  _line is not of type  <type 'int'>
Args  147) of vertex  99 of type  _line is not of type  <type 'int'>
Args  154) of vertex  106 of type  _line is not of type  <type 'int'>
Args  156) of vertex  108 of type  _line is not of type  <type 'int'>
Args  158) of vertex  110 of type  _line is not of type  <type 'int'>
Args  160) of vertex  112 of type  _line is not of type  <type 'int'>

### p78
Args  596)S117. of vertex  548 of type  _line is not of type  <type 'int'>
TODO:
Autre erreurs entre 2018 et 2019 +s/s au lieu de +s<s

### p92
Args  #REF! of vertex  0 of type  leaf_area_2018 is not of type  <type 'float'>
Args  391)/127. of vertex  342 of type  _line is not of type  <type 'int'>

TODO: Remplacer #REF! dans ligne 1 (49) sous diameter_b

### p95

ERROR ^/S15.1

### p96
Args  923)B of vertex  875 of type  _line is not of type  <type 'int'>

TODO: Ligne 925 : manque symbole

### p97
ERROR ^<C79(realisation=2018,length=15.1,type=FL,nb_leaves=9,nb_flowers=6,nb_fruits=1,fruit_drops=1,leaf_area_2018=126.64609,leaf_area_2018b=202.1444202,_line=759)
ERROR ^<S423.2(realisation=2019,length=1.2,type=VG,leaf_area_2019=91.4732,leaf_area_2019b=91.4732,_line=1728)
ERROR ^<S423.4(realisation=2019,length=0.4,type=VG,leaf_area_2019=85.7604,leaf_area_2019b=85.7604,_line=1730)
ERROR ^<S423.9(realisation=2019,length=2.7,type=FL,length_bourse=1.5,leaf_area_2019=33.44893,leaf_area_2019b=94.76313052,_line=1735)
ERROR ^<S423.11(realisation=2019,length=2.5,type=VG,leaf_area_2019=100.7565,leaf_area_2019b=100.7565,_line=1737)
ERROR ^<S423.13(realisation=2019,length=1.6,type=VG,leaf_area_2019=94.3296,leaf_area_2019b=94.3296,_line=1739)
ERROR ^<S423.18(realisation=2019,length=29.6,type=VG,leaf_area_2019=294.2776,leaf_area_2019b=294.2776,_line=1744)
ERROR ^<S423.20(realisation=2019,length=1.5,type=VG,leaf_area_2019=93.6155,leaf_area_2019b=93.6155,_line=1746)
ERROR ^<S423.22(realisation=2019,length=34.4,type=VG,leaf_area_2019=328.5544,leaf_area_2019b=328.5544,_line=1748)
Args  758) of vertex  698 of type  _line is not of type  <type 'int'>
Args  1727) of vertex  1678 of type  _line is not of type  <type 'int'>
Args  1729) of vertex  1681 of type  _line is not of type  <type 'int'>
Args  1734) of vertex  1686 of type  _line is not of type  <type 'int'>
Args  1736) of vertex  1688 of type  _line is not of type  <type 'int'>
Args  1738) of vertex  1690 of type  _line is not of type  <type 'int'>
Args  1743) of vertex  1695 of type  _line is not of type  <type 'int'>
Args  1745) of vertex  1697 of type  _line is not of type  <type 'int'>
Args  1747) of vertex  1699 of type  _line is not of type  <type 'int'>

### p98

ERROR ^<S93.2(realisation=2019,length=1.2,type=FL,length_bourse=0.5,leaf_area_2019=22.17508,leaf_area_2019b=83.48928052,_line=344)
Args  343) of vertex  294 of type  _line is not of type  <type 'int'>
Args  447)""" of vertex  398 of type  _line is not of type  <type 'int'>
Args  1572)S446. of vertex  1524 of type  _line is not of type  <type 'int'>

### p109
Args  851)201 of vertex  803 of type  _line is not of type  <type 'int'>

TODO: Line 853: empty

### p113
Args  713)B38. of vertex  664 of type  _line is not of type  <type 'int'>

### p115
ERROR ^<C39(realisation=2018,length=15.1,type=VG,leaf_area_2018=190.7331,leaf_area_2018b=190.7331,_line=605)
Args  604) of vertex  549 of type  _line is not of type  <type 'int'>

### p126

Args  635) of vertex  587 of type  _line is not of type  <type 'int'>

### p127
Args  106)/22. of vertex  58 of type  _line is not of type  <type 'int'>

### p140
rgs  477)S103. of vertex  428 of type  _line is not of type  <type 'int'>

TODO: ERREUR Line 482 +S104
<C46+S104 ou +C46/S104

### p141
ERROR ^S56.1(realisation=2019,length=26.9,type=FL,leaf_area_2019=215.33371,leaf_area_2019b=215.33371,_line=287)
Args  286)^S56. of vertex  237 of type  _line is not of type  <type 'int'>
Args  1374)B70. of vertex  1324 of type  _line is not of type  <type 'int'>


------------------------

## p52
ln 58: -> *
Add has_date
