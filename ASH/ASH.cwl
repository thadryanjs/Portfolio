#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: python3
arguments: ["run_ash.py"]
inputs:
  fasta1_flag:
    type: File
    inputBinding:
      position: 1
      prefix: --fasta1
  fasta2_flag:
    type: File
    inputBinding:
      position: 2
      prefix: --fasta2
  kmer_flag:
    type: int
    inputBinding:
      position: 3
      prefix: --kmer
outputs:
  example_out:
    type: File
    outputBinding:
      glob: hello.txt
