# comparative_genomics_protien

This script performs a homology search of proteins of interest within a target genome using HMMER and NCBI Entrez tools. The key steps include downloading protein HMM profiles and preparing the HMM search model, fetching protein sequences from NCBI using a BioSample or BioProject accession number, performing the homology search using hmmscan, and converting the output to a readable CSV file.

#Steps to download the HMM model of proteins of interest and creating the HMMdatabase with HMMER can be found in https://github.com/Pratimagtm/homologysearch_metagenomeseq

# Update input.json file with genomes information of interest, path to HMMdatabase and parameters for HMMER homology search.

regulatortohmm.py will use Bio.Entrez module from BioPython to fetch genomic data by BioSample or BioProject accession number, performs hommology search and writes the homologs in a output tab file.
tsvtocsv.py will Parse the Hmmer tblout output file to a structured CSV file.