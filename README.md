# Evaluating the Resilience of AI Chatbots Against Prompt Injection Attacks

**Author:** Trilochan Adhikari
**Supervisor:** Dr Frank Jiang  
**Institution:** Deakin University  
**Unit:** SIT792 – Research Training and Project

## About This Research

This repository contains the source code, datasets, and experimental results used in the research project “Evaluating the Resilience of AI Chatbots Against Prompt Injection Attacks.”

The research evaluates the resilience of an LLM-based university student support chatbot against selected prompt injection attacks and examines the effectiveness of a prompt-based defence.

## Research Questions

1. How resilient is an LLM-based chatbot against different types of prompt injection
   attacks?
2. How does the success rate of prompt injection attacks vary across different attack
   techniques against the selected LLM-based chatbot?
3. To what extent do selected defence mechanisms improve the chatbot's resilience against
   prompt injection attacks?

## Experimental Design

The experiment used 20 unique prompt injection attacks across four different categories:

- Instruction Override
- Role Manipulation
- Prompt Extraction
- Obfuscated Injection

Each attack was repeated three times, producing 60 observations before defence implementation and 60 observations after defence implementation.

Attack outcomes were classified as Blocked, Partially Successful, or Successful. Strict Attack Success Rate (ASR) was calculated using fully successful attacks.

## Repository Contents

- Python scripts used to conduct and analyse the experiments.
- `data/` – Normal prompts and prompt injection attack datasets.
- `results/` – Experimental results and evaluated CSV files.

## Key Results

Before defence implementation, 53 of 60 attacks (88.33%) were blocked, 4 attacks (6.67%) were partially successful, and 3 attacks (5.00%) were successful, resulting in a strict ASR of 5.00%.

After defence implementation, 57 of 60 attacks (95.00%) were blocked, 3 attacks (5.00%) were partially successful, and no attacks were fully successful, reducing the strict ASR to 0.00%.

Normal utility remained at 100% (10/10 relevant responses) after the defence was implemented.

These results apply to the specific chatbot configuration, attack dataset, and experimental conditions used in this research.

## Security Note

API credentials and other sensitive authentication information are not included in this repository. The `.env` file containing the API key has been excluded from version control.

## Acknowledgement

This research was conducted under the supervision of **Dr Frank Jiang** at Deakin University. I would like to sincerely thank Dr Frank Jiang for his guidance, valuable feedback, and continuous support throughout this research project. His advice contributed to the development of the experimental approach and the overall completion of this research.

I would also like to acknowledge the SIT792: Research Training and Project teaching team, the School of Information Technology at Deakin University, and the Deakin University Library for the academic guidance, learning resources, and research support provided throughout this project.

## Academic Use

This repository accompanies the research thesis completed for SIT792: Research Training and Project at Deakin University and provides the experimental materials used in the study to support research transparency and reproducibility.
