# Split Families of Pre-miRNAs

**Author:** MIRELE CAROLINA SOUZA

## Purpose

The purpose of this tool is to select families of micro RNAs with a minimum number of sequences.

## Requirements

- **Python 3**

## Script

The script `gera_familias_plantas.py` generates the following outputs:

1. **Directories of the miRNA families** containing the FASTA files with the sequences.

2. **Directories with families** that have fewer than 3 sequences, located in the `FAMILIAS_MENOR_3` folder.

3. **miRNA Family ID File** (This may not be used, but the information is saved in a file called: `ID_MIRNAS`).

4. **File with the Quantity of Sequences** for each miRNA family, called `QUANTIDADE_SEQ`. This file contains all the information and counters at the end.

## Usage

Run the script by providing the path of the folder where it is located as a parameter in the terminal. For example:

If the script is inside the `MIRNAS` folder and the folder is located at `/home/Downloads/MIRNAS/`, the command in the terminal will be:

```bash
python3 gera_familias_plantas.py /home/Downloads/MIRNAS/
