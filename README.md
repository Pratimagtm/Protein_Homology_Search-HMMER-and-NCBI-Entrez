# Protein_Homology_Search-HMMER-and-NCBI-Entrez

This script performs a homology search of proteins of interest within a target genome using HMMER and NCBI Entrez tools. The key steps include downloading protein HMM profiles and preparing the HMM search model, fetching protein sequences from NCBI using a BioSample or BioProject accession number, performing the homology search using hmmscan, and converting the output to a readable CSV file.

# Build HMM DB
Steps to download the HMM model of proteins of interest and create the HMM database with HMMER can be found in https://github.com/Pratimagtm/homologysearch_metagenomeseq

# Update input.json file 
Update the input file with the genomes' information of interest, the path to the HMM database, and parameters for the HMMER homology search.

# Steps
regulatortohmm.py will use Bio.Entrez module from BioPython to fetch genomic data by BioSample or BioProject accession number, performs homology search, and writes the homologs in an output tab file.
tsvtocsv.py will parse the Hmmer tblout output file to a structured CSV file.
