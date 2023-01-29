# -*- coding: utf-8 -*-


df2 = pd.read_csv('AnnoMI_dataset.csv')

pd.set_option('display.max_columns', None)
pd.set_option("display.max_colwidth", None)
pd.set_option('display.max_rows', None)

def rows_to_cols(row_val):
  contexted = []
  # number of turns - This could be treated as a hyperparameter.
  n = 7
  row_val.reset_index(inplace=True)
  #update the loop 3shan lw feeh 7aga el-length bta3ha 10 or less mayedrabsh
  for i in range(n, len(row_val['utterance_text'])):
    row = []
    # print('here')
    prev = i - 1 - n # we additionally substract 1, so row will contain current responce and 7 previous responces  
    for j in range(i, prev, -1):
      # print(row_val['utterance_text'])
      # print(row_val['transcript_id'])

      row.append(row_val['utterance_text'][j])
      # print('hi')
    contexted.append(row)  

  columns = ['response', 'context'] 
  columns = columns + ['context/'+str(i) for i in range(n-1)]
  df = pd.DataFrame.from_records(contexted, columns=columns)
  return df



#apply this function to each group
df2_grp = df2.groupby('transcript_id').apply(rows_to_cols)

df2_grp.shape

df2_grp.to_csv('AnnoMI_reshaped_for_DialoGPT_n=7.csv')

df2_grp.head()
