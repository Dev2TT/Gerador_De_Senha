from random import randint


class PasswordService:

    @staticmethod
    def create_password(senha:str):
        tamanho_senha=len(senha)
        list_letter=[]
        list_number=[]
        especiais=['!','@','#', '$', '%', '&', '*', '?', '_', '.']
        list_especial=[]

        for letra in senha:
            if(isinstance(letra) == str):
                for simbolo in especiais:
                    if letra == simbolo:
                        list_especial.append(letra)
                list_letter.append(letra)
            list_number.append(letra)
        
        list_letter={list_letter}
        list_number={list_number}
        list_especial={list_especial}
        
        tamanho_caracteres=[len(list_letter), len(list_number), len(list_especial)].sort()

        password=''

        for c in range(0,16):
            if tamanho_caracteres[0] == 0 or tamanho_caracteres[1] == 0 or tamanho_caracteres[2] == 0:
                aleatorio=randint(0,10)
                password+=str(aleatorio)
            if tamanho_caracteres[0] != 0:
                password+=list_letter[c]
            if tamanho_caracteres[1] != 0:
                password+=list_number[c]
            if tamanho_caracteres[2] !=0:
                password+=list_especial[c]
        
        
            
                

        
        

