def xor_cipher(message_bytes: bytes, key_bytes: bytes) -> bytes:
    # Alica XOR carácter a carácter repitiendo la clave si es necesario
    result = bytearray()
    key_len = len(key_bytes)
    for i, b in enumerate(message_bytes):
        result.append(b ^ key_bytes[i % key_len])
    return bytes(result)

def main():
    message_str = "GURE MEZUA HAU DA"
    key_str = "GAKO1234567890"

    # Convertir cadenas a bytes en codificación UTF-8
    message_bytes = message_str.encode('utf-8')
    key_bytes = key_str.encode('utf-8')

    # 1. Cifrar
    cryptogram_bytes = xor_cipher(message_bytes, key_bytes)

    # 2. Descifrar (Aspirando al mensaje original usando la misma clave)
    decrypted_bytes = xor_cipher(cryptogram_bytes, key_bytes)
    decrypted_str = decrypted_bytes.decode('utf-8')

    # Mostrar resultados
    print("=== CIFRADO DE FLUJO (XOR) ===")
    print(f"Mensaje Original : {message_str}")
    print(f"Clave Utilizada  : {key_str}")
    print(f"Criptograma (HEX): {cryptogram_bytes.hex().upper()}")
    print(f"Texto Descifrado : {decrypted_str}")

    # 3. Comprobación de integridad
    assert message_bytes == decrypted_bytes, "Error: El texto descifrado no coincide con el original."
    print("\n[+] Confirmación exitosa: El descifrado coincide exactamente con el texto original.")

if __name__ == "__main__":
    main()
