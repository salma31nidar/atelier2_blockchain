import random

# Fonction pour calculer le pgcd de deux nombres
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Fonction pour calculer l'inverse modulaire
def mod_inverse(e, phi):
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2, x1 = x1, x
        d, y1 = y1, y

    if temp_phi == 1:
        return d + phi

# Fonction pour générer des clés RSA
def generate_keys():
    p = 5  # petit premier pour l'exemple
    q = 11 # petit premier pour l'exemple
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choisir e tel que 1 < e < phi et gcd(e, phi) = 1
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Calculer d, l'inverse de e mod phi
    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

# Fonction de chiffrement
def encrypt(public_key, message, k):
    e, n = public_key
    m_prime = message + k
    c = pow(m_prime, e, n)
    return c

# Fonction de déchiffrement
def decrypt(private_key, ciphertext, k):
    d, n = private_key
    m_prime = pow(ciphertext, d, n)
    message = m_prime - k
    return message

# Test de l'algorithme RSA-SimpleMod
def test_rsa_simplemod():
    print("Génération des clés...")
    public_key, private_key = generate_keys()
    print("Clé publique:", public_key)
    print("Clé privée:", private_key)

    # Message à chiffrer
    message = 12
    # Constante secrète
    k = 4

    print("\nMessage original:", message)

    # Chiffrement
    ciphertext = encrypt(public_key, message, k)
    print("Message chiffré:", ciphertext)

    # Déchiffrement
    decrypted_message = decrypt(private_key, ciphertext, k)
    print("Message déchiffré:", decrypted_message)

# Appel de la fonction de test
test_rsa_simplemod()
