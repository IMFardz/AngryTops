training_dir = 'CheckPoints/training_5'

column_names = ["runNumber", "eventNumber", "weight", "jets_n", "bjets_n",
"lep.Px", "lep.Py", "lep.Pz", "lep.E", "met_met", "met_phi",
"jet0 P_x",  "jet0 P_y",  "jet0 P_z",  "jet0 E",  "jet0 M",  "jet0 BTag",
"jet1 P_x",  "jet1 P_y",  "jet1 P_z",  "jet1 E",  "jet1 M",  "jet1 BTag",
"jet2 P_x",  "jet2 P_y",  "jet2 P_z",  "jet2 E",  "jet2 M",  "jet2 BTag",
"jet3 P_x",  "jet3 P_y",  "jet3 P_z",  "jet3 E",  "jet3 M",  "jet3 BTag",
"jet4 P_x",  "jet4 P_y",  "jet4 P_z",  "jet4 E",  "jet4 M",  "jet4 BTag",
"target_W_had_Px", "target_W_had_Py", "target_W_had_Pz", "target_W_had_E", "target_W_had_M",
"target_W_lep_Px", "target_W_lep_Py", "target_W_lep_Pz", "target_W_lep_E", "target_W_lep_M",
"target_b_had_Px", "target_b_had_Py", "target_b_had_Pz", "target_b_had_E", "target_b_had_M",
"target_b_lep_Px", "target_b_lep_Py", "target_b_lep_Pz", "target_b_lep_E", "target_b_lep_M",
"target_t_had_Px", "target_t_had_Py", "target_t_had_Pz", "target_t_had_E", "target_t_had_M",
"target_t_lep_Px", "target_t_lep_Py", "target_t_lep_Pz", "target_t_lep_E", "target_t_lep_M"]


input_columns = [
"lep.Px", "lep.Py", "lep.Pz", "lep.E", "met_met", "met_phi",
"jet0 P_x",  "jet0 P_y",  "jet0 P_z",  "jet0 E",  "jet0 M",  "jet0 BTag",
"jet1 P_x",  "jet1 P_y",  "jet1 P_z",  "jet1 E",  "jet1 M",  "jet1 BTag",
"jet2 P_x",  "jet2 P_y",  "jet2 P_z",  "jet2 E",  "jet2 M",  "jet2 BTag",
"jet3 P_x",  "jet3 P_y",  "jet3 P_z",  "jet3 E",  "jet3 M",  "jet3 BTag",
"jet4 P_x",  "jet4 P_y",  "jet4 P_z",  "jet4 E",  "jet4 M",  "jet4 BTag",
]

output_columns = [
"target_W_had_Px", "target_W_had_Py", "target_W_had_Pz", "target_W_had_E",
"target_W_lep_Px", "target_W_lep_Py", "target_W_lep_Pz", "target_W_lep_E",
"target_b_had_Px", "target_b_had_Py", "target_b_had_Pz", "target_b_had_E",
"target_b_lep_Px", "target_b_lep_Py", "target_b_lep_Pz", "target_b_lep_E",
"target_t_had_Px", "target_t_had_Py", "target_t_had_Pz", "target_t_had_E",
"target_t_lep_Px", "target_t_lep_Py", "target_t_lep_Pz", "target_t_lep_E",
]

input_features_jets = [
"jet0 P_x",  "jet0 P_y",  "jet0 P_z",  "jet0 E",  "jet0 M",  "jet0 BTag",
"jet1 P_x",  "jet1 P_y",  "jet1 P_z",  "jet1 E",  "jet1 M",  "jet1 BTag",
"jet2 P_x",  "jet2 P_y",  "jet2 P_z",  "jet2 E",  "jet2 M",  "jet2 BTag",
"jet3 P_x",  "jet3 P_y",  "jet3 P_z",  "jet3 E",  "jet3 M",  "jet3 BTag",
"jet4 P_x",  "jet4 P_y",  "jet4 P_z",  "jet4 E",  "jet4 M",  "jet4 BTag",
]

input_features_lep = [
"lep.Px", "lep.Py", "lep.Pz", "lep.E", "met_met", "met_phi"
]

target_features_W_lep = [
"target_W_lep_Px", "target_W_lep_Py", "target_W_lep_Pz", "target_W_lep_E"
]

target_features_W_had = [
"target_W_had_Px", "target_W_had_Py", "target_W_had_Pz", "target_W_had_E"
]

target_features_b_had  = [
"target_b_had_Px", "target_b_had_Py", "target_b_had_Pz", "target_b_had_E"
]

target_features_b_lep  = [
"target_b_lep_Px", "target_b_lep_Py", "target_b_lep_Pz", "target_b_lep_E"
]

target_features_t_had  = [
"target_t_had_Px", "target_t_had_Py", "target_t_had_Pz", "target_t_had_E"
]

target_features_t_lep  = [
"target_t_lep_Px", "target_t_lep_Py", "target_t_lep_Pz", "target_t_lep_E"
]

features_event_info = [
    "jets_n", "bjets_n",
]


# output_columns = [
# "target_W_had_Px", "target_W_had_Py", "target_W_had_Pz", "target_W_had_E", "target_W_had_M",
# "target_W_lep_Px", "target_W_lep_Py", "target_W_lep_Pz", "target_W_lep_E", "target_W_lep_M",
# "target_b_had_Px", "target_b_had_Py", "target_b_had_Pz", "target_b_had_E", "target_b_had_M",
# "target_b_lep_Px", "target_b_lep_Py", "target_b_lep_Pz", "target_b_lep_E", "target_b_lep_M",
# "target_t_had_Px", "target_t_had_Py", "target_t_had_Pz", "target_t_had_E", "target_t_had_M",
# "target_t_lep_Px", "target_t_lep_Py", "target_t_lep_Pz", "target_t_lep_E", "target_t_lep_M"
# ]

# header = [
#     "runNumber", "eventNumber", "weight", "jets_n", "bjets_n",
#     "lep_px", "lep_py", "lep_pz", "lep_E", "met_met", "met_phi",
#     "j1_px", "j1_py", "j1_pz", "j1_E", "j1_m", "j1_mv2c10",
#     "j2_px", "j2_py", "j2_pz", "j2_E", "j2_m", "j2_mv2c10",
#     "j3_px", "j3_py", "j3_pz", "j3_E", "j3_m", "j3_mv2c10",
#     "j4_px", "j4_py", "j4_pz", "j4_E", "j4_m", "j4_mv2c10",
#     "j5_px", "j5_py", "j5_pz", "j5_E", "j5_m", "j5_mv2c10",
#     "W_had_px", "W_had_py", "W_had_pz", "W_had_E", "W_had_m",
#     "W_lep_px", "W_lep_py", "W_lep_pz", "W_lep_E", "W_lep_m",
#     "b_had_px", "b_had_py", "b_had_pz", "b_had_E", "b_had_m",
#     "b_lep_px", "b_lep_py", "b_lep_pz", "b_lep_E", "b_lep_m",
#     "t_had_px", "t_had_py", "t_had_pz", "t_had_E", "t_had_m",
#     "t_lep_px", "t_lep_py", "t_lep_pz", "t_lep_E", "t_lep_m",
# ]
#
# features_event_info = [
#     "runNumber", "eventNumber", "weight", "jets_n", "bjets_n",
# ]
