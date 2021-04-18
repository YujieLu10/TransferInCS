<!--
 * @Author: your name
 * @Date: 2021-03-20 17:46:11
 * @LastEditTime: 2021-04-18 22:38:42
 * @LastEditors: your name
 * @Description: In User Settings Edit
 * @FilePath: /TransferInCS/data_preprocess/pcs_data_script.md
-->
PCS_data_analysis_script
# grep_paperid
cat paperconferenceid.tsv | grep 1163450153 > CHI_paperids.tsv
cat paperconferenceid.tsv | grep 1195049314 > CSCW_paperids.tsv
cat paperconferenceid.tsv | grep 1166315290 > UIST_paperids.tsv
cat paperconferenceid.tsv | grep 2754292954 > IMCL_paperids.tsv
cat paperconferenceid.tsv | grep 1171345118 > UbiComp.tsv

# 第N列最大最小值
awk -F',' 'BEGIN{min=2015}{if($3<min){min=$3}}END{print min}' extracted_paperyear/paperyear_result_CHI.tsv
awk -F',' 'BEGIN{max=0}{if($3>max && $3!="year"){max=$3}}END{print max}' extracted_paperyear/paperyear_result_CHI.tsv

sort -t, -nk3 xxx.tsv
sort -nk2 year.tsv
sort -nk1 author
sort -nk2 paper_author

# 聚合
# cat papercitations_UBI.tsv | awk -F',' '{print $3}' | uniq -c

cat papercitations_UBI.tsv | awk -F',' '{a[$2]++}END{for(i in a){print i,a[i] | "sort -k 1"}}'

cat papercitations_UBI.tsv | awk -F',' '{a[$2]++}END{for(i in a){print i,a[i] | "sort -k 1"}}' > ubi.tsv
sort -rnk2 ubi.tsv > ubi_sort.tsv 

# sort
sort popular_transferred_paper_CHI.tsv -rn -t ',' -k 4 -k 3 > CHI.tsv
head -11 UBI.tsv | awk -F',' '{print $3}'
head -100 UBI.tsv | grep ,0 | awk -F',' '{print $2,$3}'

# duration
awk -F'\t' 'BEGIN{max=2021012000;min=2021011300}{if($2>=min && $2<=max){a[$1]=$2}}END{for(i in a){print i,a[i]}}' sorted_non_hit_user_request.txt > needed_non_hit_user_request.txt

awk -F'\t' 'BEGIN{max=2021012000;min=2021011300}{if($2>=min && $2<=max){a[$1]=$2}}END{for(i in a){print i,a[i]}}'

# 去重重复行
awk '!a[$0]++' top1000rongyao > uni_top1000rongyao

# 统计uniq单元的个数
awk -F',' '{print $5}' papercitationscience_result_CHI.tsv | sort | uniq -c
awk -F',' '{print $5}' papercitationscience_result_CHI.tsv | sort | uniq -c | wc -l
