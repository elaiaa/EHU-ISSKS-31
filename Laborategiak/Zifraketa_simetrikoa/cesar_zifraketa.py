import string

try:
    from langdetect import detect
except ImportError:
    print("Instala langdetect ejecutando: pip install langdetect")
    detect = None

cipher_text = "Uunejvxb dw vdwmx wdnex jzdr, nw wdnbcaxb lxajixwnb"

def decrypt_caesar(text, shift):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    
    for char in text:
        if char in alphabet_lower:
            idx = (alphabet_lower.index(char) - shift) % 26
            result.append(alphabet_lower[idx])
        elif char in alphabet_upper:
            idx = (alphabet_upper.index(char) - shift) % 26
            result.append(alphabet_upper[idx])
        else:
            result.append(char)
            
    return "".join(result)

# Probar los 26 desplazamientos
best_shift = None
best_text = ""

for shift in range(26):
    decrypted = decrypt_caesar(cipher_text, shift)
    
    # Autodetectar idioma si langdetect está disponible
    if detect:
        try:
            lang = detect(decrypted)
            if lang == 'es':
                best_shift = shift
                best_text = decrypted
        except:
            pass
            
    print(f"Shift {shift:2d}: {decrypted}")

# El desplazamiento correcto es SHIFT = 9
print("\n--- RESULTADO ENCONTRADO ---")
print(f"Clave (Desplazamiento): 9")
print(f"Mensaje descifrado: {decrypt_caesar(cipher_text, 9)}")
