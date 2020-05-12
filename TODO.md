# Tasks

## 1. Extract errors for code 

## 2. 
### Analysis at tree scale

•	apple_tree: Apple tree number
p52 -> 52
g.index(1)

•	trt: treatment or NCI category

•	NCI: Neighbourhood crowding index value
•	TSA_2018: Trunk section area: π*diameter_b_2018²/4 (cm²)
•	TSA_2019: Trunk section area: π*diameter_b²/4 (cm²)
•	L_shoot_V/F_2018/2019: Number of vegetative of floral long shoots (>=5cm) in 2018 and 2019
•	S_shoot_V/F_2018/2019: Number of vegetative of floral short shoots (<5cm) in 2018 and 2019
•	nb_V_2018/2019: Number of vegetative buds in 2018 and 2019
•	nb_F_2018/2019: Number of floral buds in 2018 and 2019
•	nb_L_2018/2019: Number of latent buds in 2018 and 2019
•	LA_2018/2019: Leaf area (cm²) in 2018 and 2019
•	Elongation : longueur du tronc (A1+A2+A3+dernier /S) / diamètre base  (A1)
•	Tapper : (diamètre base (A1) - diamètre sommet) / longueur total

L'information est dans la colonne "type" qui peut prendre 5 valeurs : VG, FL, BL, EX, NA

VG : bourgeon végétatif

FL : bourgeon florale

BL : bourgeon latent

EX : extinction

NA :  disparition du bourgeon pour des raisons inconnus (casse, phytophagie ou cas d'extinction dont je n'ai pas été témoin)

- trunk length
sum(trunk)

## 3. Branch scale 
### Questions

- BSA_2018/2019 : 
diameter	REAL
diameter_b	REAL												diameter_a	REAL
diameter_2018
diameter_b2018
diameter_a2018
 default : 0.3

Comment calculer diametre branche en 2019?

- B_dist:
    branch distance on the trunk (0 base of the tree 1 apex of the tree)

    Q: Distance topologique ou géométrique?
    R: Topologique
     
- B_lgth_2018/2019:
    branch length (cm) in 2018 (2017+2018) and 2019 (2017+2018+2019)

    Q: Comment calculer la longueur quand length n'est pas renseignée? 
    Quelle info pour 2019?
    
- L_shoot_V/F_2018/2019:
    Number of vegetative of floral long shoots (>=5cm) on the branch in 2018 and 2019
- S_shoot_V/F_2018/2019:
    Number of vegetative of floral short shoots (<5cm) on the branch in 2018 and 2019
- nb_V_2018/2019:
    Number of vegetative buds on the branch in 2018 and 2019
- nb_F_2018/2019:
    Number of floral buds on the branch in 2018 and 2019
- nb_L_2018/2019:
    Number of latent buds on the branch in 2018 and 2019
- LA_2018/2019:
    Leaf area (cm2) in 2018 and 2019
- Elongation :
    longueur de la branche / diametre base de la branche
- Tapper :
    (diametre base de la branche (2017 ou 2018) - diametre sommet de la branche(2019)) / longueur total de la branche
