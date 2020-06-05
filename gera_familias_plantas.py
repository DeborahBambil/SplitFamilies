#SCRIPT EM LINGUAGEM PYTHON PARA GERAR DIRETÓRIOS DE FAMÍLIAS DE MIRNAS

import re
import random
import sys
import os
import shutil


def gera_diretorios():
    
    os.mkdir("FAMILIAS_MENOR_3")
    arq = "saida_MIR_filtradas.fa"
    arquivo_saida = open("ID_MIRNAS", "w")

    letras = []
    l = []
    array_mirnas = []

    
    aux = 0
    contador_sequencias = 0
    familia = 0
    with open(arq) as arquivo:
        for line in arquivo:
            match = re.search( r'>[\w]+-([\w]+[\d]+)', line) 
            if(match):
                #CONTA QUANTAS SEQUENCIAS TEM
                contador_sequencias = contador_sequencias + 1
                id_mirna = match.group(1)
                if(id_mirna in l):
                    familia = familia +1
                else:
                    l.append(id_mirna)
                    #gera diretoio
                    os.mkdir(str(id_mirna))
                    arquivo_saida.write(id_mirna+"\n")
                    
                    
                    
    return contador_sequencias                
                    
            
def gera_familias(caminho,contador_sequencias):
    
    arq = "ID_MIRNAS"
    arquivo_saida_quantidade_sequencias = open("QUANTIDADE_SEQ", "w")
    flag = 0
    total_sequencias = 0
    contador_menores_3 = 0
    contador_total_familias = 0
    with open(arq) as arquivo_1:
        for line_arq in arquivo_1:
            contador_total_familias = contador_total_familias +1
            match = re.search( r'([\w]+[\d]+)', line_arq) 
            if(match):
                id_mirna = match.group(1)
                arquivo_saida = open(str(id_mirna)+"/familia_"+str(id_mirna)+"_mirnas.fa", "a")
                contador = 0
                with open("saida_MIR_filtradas.fa") as arquivo:
                    for line in arquivo:
                        if(flag == 1):
                            match1 = re.search( r'^(>)', line) 
                            if(match1):
                                flag = 0
                            
                            else:
                                arquivo_saida.write(line)
                        
                        match2 = re.search( r'>[\w]+-([\w]+[\d]+)', line) 
                        if(match2):
                            mirna = match2.group(1)
                            if(mirna == id_mirna):
                                #CONTA QUANTAS SEQUENCIAS TEM EM CASA FAMILIA
                                contador = contador+1
                                arquivo_saida.write(line)
                                flag = 1
                arquivo_saida_quantidade_sequencias.write(">"+id_mirna+" QUANTIDADE DE SEQUENCIAS: "+str(contador)+"\n")
                if(contador < 3):
                    shutil.move(str(caminho)+str(id_mirna), str(caminho)+"FAMILIAS_MENOR_3") 
                    contador_menores_3 = contador_menores_3 + 1
                
                total_sequencias = total_sequencias + contador
                
    arquivo_saida_quantidade_sequencias.write("QUANTIDADE TOTAL DE FAMILIAS: "+str(contador_total_familias)+"\n")
    aux = (contador_total_familias-contador_menores_3)
    arquivo_saida_quantidade_sequencias.write("QUANTIDADE TOTAL DE FAMILIAS COM 3 OU MAIS SEQUENCIAS: "+str(aux)+"\n")
    arquivo_saida_quantidade_sequencias.write("QUANTIDADE TOTAL DE FAMILIAS COM MENOS DE 3 SEQUENCIAS: "+str(contador_menores_3)+"\n")
    arquivo_saida_quantidade_sequencias.write("QUANTIDADE TOTAL DE SEQUENCIAS EM TODAS AS FAMILIAS: "+str(total_sequencias)+"\n")
    arquivo_saida_quantidade_sequencias.write("QUANTIDADE TOTAL DE SEQUENCIAS NO ARQUIVO DE MIRNAS: "+str(contador_sequencias)+"\n")
    
                                    
                                   
                                                
                                        

        

def main():
    
    
    
    #------------------------------------------------------------------------------------------------------------------------------------
    #ARQUIVOS RECEBIDOS COMO PARAMETRO
    #exemplo de caminho /home/Documentos/MIRELE/MIRNAS/
    caminho = sys.argv[1]
    #--------------------------------------------------------------------------------------------------------------------------------------
    
    finalizou = gera_diretorios()
    if(finalizou > 0):
        gera_familias(caminho,finalizou)


    
main()



