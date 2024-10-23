# Principe de l'algorithme RSA-SimpleMod

Le principe de base reste similaire à RSA, mais avec une petite variation : on ajoute simplement une constante secrète au moment du chiffrement pour introduire une légère variation dans le texte chiffré.

## Étapes de l'algorithme RSA-SimpleMod

### Génération des clés (comme dans RSA) :

1. Choisissez deux nombres premiers \( p \) et \( q \).
2. Calculez \( n = p \times q \).
3. Calculez \( \phi(n) = (p - 1) \times (q - 1) \).
4. Choisissez un entier \( e \), tel que \( \text{gcd}(e, \phi(n)) = 1 \).
5. Calculez \( d \), l'inverse de \( e \) modulo \( \phi(n) \).

- Clé publique : \( (e, n) \).
- Clé privée : \( (d, n) \).

### Chiffrement :

1. Choisissez un message \( m \) (avec \( 0 \leq m < n \)).
2. Ajoutez une petite constante secrète \( k \) au message : \( m' = m + k \).
3. Chiffrez avec la clé publique : 
   \[
   c = (m'^e) \mod n
   \]
   où \( c \) est le message chiffré.

### Déchiffrement :

1. Déchiffrez avec la clé privée : 
   \[
   m' = c^d \mod n
   \]
2. Soustrayez la constante secrète \( k \) pour retrouver le message original :
   \[
   m = m' - k
   \]
