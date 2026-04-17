# EDAM_ground_truth

Ground truth dataset of life sciences software, including 44 analyzed tools by experts. 
In total, 16 experts took part in the ground truth: 2 for Genetic Variant, 2 in Metagenomics, 3 in Phylogeny, 2 in
Single Cell, 3 in Systems Biology and 4 experts in Bio-imaging, which includes the fields of Microscopy
and Neuroimaging .
A LLM (DeepSeek V3.1) was used to annotate the ground-truth data, and these annotations were reviewed and validated by experts. Those selected by the experts were incorporated into the expert–LLM consensus.
The expert-LLM annotations from the tools are compared to those in [bio.tools registry](https://bio.tools/) using the [**EDAM ontology**](https://edamontology.org/page).
This ground truth are supported by the [ShareFAIR](https://projet.liris.cnrs.fr/sharefair/).

---

## Table of Contents
- [Installation](#installation)
- [Content and Usage](#content-and-usage)
- [License](#license)
- [Authors and Affiliations](#authors-and-affiliations)

---

## Installation

1. **Clone the EDAM_ground_truth repository**

```bash
git clone https://github.com/ulysseLeclanche/EDAM_ground_truth.git
```

```bash
cd EDAM_ground_truth
```

2. **All the packages used are listed in `environment.yml`; a Conda environment can be created**

```bash
conda env create -f environment.yml
```

```bash
conda activate EDAM_GT
```

## Content and Usage

This repository contains resources related to the EDAM ground truth dataset of life sciences software. 

### 1. **Ground-Truth Dataset**
   
#### 1.1. **Prompting Strategy**
  - [`Supplementary_material.pdf`](Supplementary_material.pdf)
    
Description of the prompt design and the example provided to experts for annotation. 
  - [`Prompt_examples_two_annotated_tools.txt`](Prompt_examples_two_annotated_tools.txt)  

  Example prompts used with the LLM (DeepSeek V3.1) to replicate expert annotation procedures.

#### 1.2. **List of software tools**
  - [`Tools_lists.csv`](Tools_lists.csv)  

  List of software tools included in the dataset, with links to their corresponding entries in [bio.tools](https://bio.tools/).

#### 1.3. **Raw free-text annotations from experts and DeepSeek**
- [`Raw_free_text_annotation/`](Raw_free_text_annotation/) (text and JSON formats)
  JSON files are generated using: [`Confusion_matrix_json.ipynb`](Confusion_matrix_json.ipynb).

#### 1.4 **Distribution of free-text annotations by type**
- [`Distribution_free_text_annotation/`](Distribution_free_text_annotation/)
  Free-text annotations by type : topic, operation, input/output data type, and input/output format generated with [`Distribution_free_text_annotation.ipynb`](Distribution_free_text_annotation.ipynb).

#### 1.5. **Ground-truth EDAM terms validated by expert**
- [`EDAM_terms_URI_ground_truth_validated.tsv`](EDAM_terms_URI_ground_truth_validated.tsv)  
  Contains the URIs of validated EDAM terms, their labels, and the associated free-text annotation proposals from experts. Each annotation is linked to one or more tools, within a domain and a category (topics, operations, format, or data).

### 2. **LLM vs Expert Annotation Analysis**

#### 2.1. **Metrics : Recall, Precision and F1 score**
  All metrics are calculated by comparing DeepSeek's proposals and the expert consensus against the LLM-Expert consensus.

  Metrics are computed using : [`Confusion_matrix_json.ipynb`](Confusion_matrix_json.ipynb) and figures with  [`Contribution_LLM_expert_Precision_recall_F1_figures.ipynb`](Contribution_LLM_expert_Precision_recall_F1_figures.ipynb).  
  Recall, Precision, and F1 score were calculated for all tools across each domain, as well as by annotation type.

#### 2.2. **Resources and plots**
  - All confusion matrix are inside :[`Confusion_matrix_free_text_annotation/`](Confusion_matrix_free_text_annotation/)   
  Confusion matrices contain : TP, FN, FP, recall, precision, F1 score, annotations retained or rejected and mixed annotations. 
  - [`plots/`](plots/) Figures for recall, precision, F1 score by domains and annotation types.

### 3. **Added Value of LLM and Expert Annotations**

#### 3.1 **Missing annotations in EDAM**
  Identification of free-text annotation found by experts/LLM but absent from EDAM ontology.  
  The notebook [`Contingency_table_annotation_consensus_mapped.ipynb`](Contingency_table_annotation_consensus_mapped.ipynb) calculates the contingency table for free-text annotations, regardless of whether they have been validated as EDAM annotations.

#### 3.2 **Contribution to bio.tools**
  Comparison between: Ground-truth validated annotations (expert + LLM consensus) and existing annotations in bio.tools using the notebook [`Contingency_table_Biotools_vs_ground_truth.ipynb`](Contingency_table_Biotools_vs_ground_truth.ipynb).
  Annotations inherited from the EDAM ontology based on direct annotations are calculated using [`edam_neighbors.py`](Contingency_table/edam_neighbors.py)

All notebooks and contingency tables are in the folder: [`Contingency_table/`](Contingency_table/)

## Authors and Affiliations:

**Authors:**  
Ulysse Le Clanche¹, Melvin Selim Atay², Elise Bannier²,³, Anaïs Baudot⁴,⁵, Lea Bellenger⁶, Alexandrina Bodrug⁶, Samuel Chaffron⁷, Eric Charpentier⁶, Erwan Corre⁸, Clémence Frioux⁹, Aurélie Lardenois¹⁰, Frédéric Lemoine¹¹, Camille Maumet², Cyril Noël¹², Perrine Paul-Gilloteaux¹³, Paul Simion¹⁴, Morgane Térézol⁴, Olivier Dameron¹, and Alban Gaignard⁶

**Affiliations:**  
1. Univ Rennes, Inria, CNRS, IRISA - UMR 6074, F-35000 Rennes, France
2. Univ Rennes, CNRS, Inria, Inserm, IRISA UMR 6074, EMPENN — ERL U 1228, F-35000 Rennes, France
3. CHU Rennes, Radiology Department, Rennes, France
4. Aix Marseille Université, INSERM, MMG, Marseille, France
5. CNRS, Marseille, France
6. Nantes Université, CNRS, INSERM, l'institut du thorax, F-44000 Nantes, France
7. Nantes Université, École Centrale Nantes, CNRS, LS2N, UMR 6004, F-44000 Nantes, France
8. ABiMS-IFB, Station Biologique de Roscoff, CNRS/Sorbonne Université, Roscoff, France
9. Inria, Univ. Bordeaux, INRAE, 33400, Talence, France
10. Institut National de Santé et de Recherche Médicale, U1085-Irset, Université de Rennes 1, F-35042 Rennes, France
11. Institut Pasteur, Université Paris Cité, Bioinformatics of Biostatistics Hub, F-75015 Paris, France
12. SeBiMER Service de Bioinformatique de l'Ifremer, Ifremer, IRSI, Plouzané, France
13. Nantes Université, CHU Nantes, CNRS, Inserm, BioCore, US16, SFR Bonamy, Nantes, France
14. EcoBio - Ecosystems, Biodiversity, Evolution, Université de Rennes 1, 35042 Rennes, France

## License

This project is licensed under the [MIT License](LICENSE).
