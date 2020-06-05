# Selection families of harpin 

Author: MIRELE CAROLINA SOUZA

The purpose of this tool is to select families of micro RNAs, with a minimum number of seque

Requirements run the tool:

python3

SCRIPT gera_familias_plantas.py GENERATES OUTPUTS:

1- THE DIRECTORIES OF THE MIRNAS FAMILIES CONTAINING THE FASTA ARCHIVE WITH THE SEQUENCES

2- DIRECTORIES WITH FAMILIES WITH LESS THAN 3 SEQUENCES ARE IN THE FAMILIAS_MENOR_3 FOLDER

3- MIRNAS FAMILY ID FILE (I may not even use this, but I saved this information in a file called: ID_MIRNAS)

3- FILE WITH THE QUANTITY OF SEQUENCES OF EACH FAMILY OF MIRNAS (called: QUANTIDADE_SEQ) at the end of this file are all the information and counters !!!

RUN:

SCRIPT (gera_familias_plantas.py) receives as a parameter in the terminal the path of the folder where it is located, example:

the script is inside the MIRNAS folder and the folder is at: /home/Downloads/MIRNAS/

then the execution in the terminal will be:

python3 cria_familias_plantas.py /home/Downloads/MIRNAS/
