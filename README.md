<!--
 * @Author: your name
 * @Date: 2021-04-18 22:44:31
 * @LastEditTime: 2021-04-20 00:19:25
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /TransferInCS/data_preprocess/README.md
-->

# data source
patent citation to science(pcs) V14: https://www.openicpsr.org/openicpsr/project/108362/version/V14/view
patentsview: https://patentsview.org/download/data-download-tables

# folder introduction
- data_preprocess
    - pcs_data_script : refer to grep_paperid section to extract paper_ids of the conferences you need to analyze
    - pcs_data_extraction : extract corresponding data from "patent citation to science"
    - author_information : construct all the author information (this would take a long time and take up large compute resources)
    - dblp_patentsview_data_join : join data from "dblp" and "patentsview"
    
- data_analysis
    - analysis : basic analysis of extracted data

- data : extracted data is under this directory
- analysis_result : analysis result is under this directory