def analizar_texto(frase: str) -> tuple[int, int]:
	
	
	vocales = "aáeéiíoóuúü"
	numvocales: int = 0
	
	for letra in frase.lower():
		if letra in vocales:
			numvocales += 1
	
	palabras: int = len(frase.split())
	

	return numvocales, palabras





def main():
	"función principal"
	frase: str = str(input("Escribe una frase, te diré sus vocales y cuantas palabras tiene: "))
	
	conversion: tuple[int, int] = analizar_texto(frase)
	
	
	print(f"Vocales: {conversion[0]} Palabras: {conversion[1]}" )

if __name__ == "__main__":
    main()