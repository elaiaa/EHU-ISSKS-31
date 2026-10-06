from collections import Counter

# Frecuencias típicas del Euskera (orientativas):
# A, E, I, N, O, T, S, R, K, L, Z, U, D, B, G, M, P, H, F, X, J, Y, W, Q, V

def analyze_frequencies(text):
    # Filtrar solo caracteres alfabéticos
    letters = [char for char in text if char.isalpha()]
    total = len(letters)
    counter = Counter(letters)
    
    print("\n--- ANÁLISIS DE FRECUENCIAS EN EL CRIPTOGRAMA ---")
    print(f"Total de letras: {total}\n")
    print(f"{'Letra':<6} | {'Apariciones':<12} | {'Porcentaje':<10}")
    print("-" * 35)
    for char, count in counter.most_common():
        percentage = (count / total) * 100
        print(f"  {char:<4} | {count:<12} | {percentage:.2f}%")

def apply_mapping(ciphertext, mapping):
    result = []
    for char in ciphertext:
        if char in mapping:
            # Si se ha asignado un reemplazo, mostrarlo en MINÚSCULA para destacarlo
            result.append(mapping[char].lower())
        else:
            # Dejar en MAYÚSCULA los símbolos aún no descifrados
            result.append(char)
    return "".join(result)

def interactive_solver(ciphertext):
    mapping = {}
    
    while True:
        print("\n" + "="*60)
        print("TEXTO ACTUALMENTE DESCIFRADO (Minúsculas = reemplazadas | Mayúsculas = pendientes):")
        print("="*60)
        print(apply_mapping(ciphertext, mapping))
        print("="*60)
        
        print("\nOpciones:")
        print("1. Ver análisis de frecuencias de los caracteres no asignados")
        print("2. Agregar / Modificar sustitución (ejemplo: 'X' -> 'a')")
        print("3. Eliminar una sustitución")
        print("4. Salir")
        
        opt = input("\nSelecciona una opción (1-4): ").strip()
        
        if opt == '1':
            # Filtrar solo letras no asignadas aún
            unmapped = [c for c in ciphertext if c.isalpha() and c not in mapping]
            analyze_frequencies("".join(unmapped))
        elif opt == '2':
            src = input("Carácter cifrado (mayúscula): ").strip()
            dst = input("Reemplazar por letra real (minúscula): ").strip().lower()
            if len(src) == 1 and len(dst) == 1:
                mapping[src] = dst
            else:
                print("[!] Ingresa caracteres válidos.")
        elif opt == '3':
            src = input("Carácter cifrado a desvincular: ").strip()
            mapping.pop(src, None)
        elif opt == '4':
            print("\nMapeo final obtenido:", mapping)
            break

if __name__ == "__main__":
    ciphertext = (
        "JIYQ WQIEtYLP YtXLLW OPLP! CWXYM SPMQPLtP YEYQWtP CPOX PLZP SBPJPQX "
        "bPBQXWYtPQX bPtYPM. JYLYM bPW, XLPWM HYMCY PEQX PtYLPtJYM CP HPWJQWbYB "
        "WQIEtYLP; tRPBXPQ YtP tRPBXPQ, YtP «PISP, HPWJQWbYB!» XWFIPQ WJPM CWLP "
        "MPOIEW WbWBbWCY XEXPM. QPBY MPOIEWP YLY HPCP YJ CP BYFYM bYJPWM OPtPJQPtEIP, "
        "bPWMP, XLPWMCWQ YLY, JYMbPWt YZPQIZY OPJtYQ SPEPYLPM bWJQPLLP YZPM CWXtY "
        "HPWJQWbYBW, SPLtY FPLtJYP bPWZYMtJYM CWYM QXMSPWMWP bPQPLLPLW."
    )
    
    interactive_solver(ciphertext)
