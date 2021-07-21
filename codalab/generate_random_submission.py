import random

random.seed(2021)

for setting in ['full', 'half', 'small', 'hard']:
    with open(f'convai2_{setting}.csv', 'w') as f:
        metrics = 'avoid_rep,enjoy,fluency,inquisitive,interest,listen,make_sense,persona_guess,reward,turing'
        f.write(f'model_name,{metrics}\n')
        metrics = metrics.split(',')
        for model_name in ['inquisitive_model_ct_setting10_better', 'greedy_model', 'repetition_model_settinginf', 'repetition_model_setting05', 'repetition_model_setting12', 'inquisitive_model_ct_setting07', 'interesting_nidf_model_bfw_setting_08', 'responsiveness_model_bfw_setting_00', 'inquisitive_model_ct_setting01', 'repetition_model_setting35_settinginf', 'interesting_nidf_model_ct_setting9', 'interesting_nidf_model_ct_setting2', 'responsiveness_model_bfw_setting_10', 'responsiveness_model_bfw_setting_minus_10', 'interesting_nidf_model_ct_setting7', 'interesting_nidf_model_bfw_setting_06', 'repetition_model_setting35', 'interesting_nidf_model_bfw_setting_minus_10', 'responsiveness_model_bfw_setting_05', 'inquisitive_model_ct_setting10', 'inquisitive_model_ct_setting04', 'interesting_nidf_model_ct_setting0', 'interesting_nidf_model_ct_setting4', 'interesting_nidf_model_bfw_setting_minus_04', 'inquisitive_model_ct_setting00', 'interesting_nidf_model_bfw_setting_04', 'responsiveness_model_bfw_setting_13', 'baseline_model']:
            scores = [random.random() for _ in range(len(metrics))]
            scores = ','.join(map(str, scores))
            f.write(f'{model_name},{scores}\n')
    with open(f'airdialogue_{setting}.csv', 'w') as f:
        metrics = 'flight_score,name_score,reward,status_score'
        f.write(f'model_name,{metrics}\n')
        metrics = metrics.split(',')
        for model_name in ['150K_w', '40K', '40K_w', '5K', '30K', '30K_w', '100K', '75K', '250K', '10K', '10K_w', '200K', '75K_w', '250K_w', 'full_w', '20K_w', '20K', '200K_w', '50K_w', '100K_w', '150K', '50K', 'full', '5K_w']:
            scores = [random.random() for _ in range(len(metrics))]
            scores = ','.join(map(str, scores))
            f.write(f'{model_name},{scores}\n')    