# Changeable variables
# k value
k = 5
# main project path
# For windows
path = 'D:\\Documents\\5. Summer 2022\\'
# For Linux
# path =


# Do not change below variables and functions
target_raw_path = path + 'target_raw\\'
target_k_path = path + 'target_' + str(k) + '\\'
features_path = path + 'features\\'
data_raw = 'data_raw.csv'
data_target = 'data_target.csv'
data_features = 'data_features.csv'
url_file = 'url_list.csv'
target_raw = 'target_raw.csv'
target_k = 'target_' + str(k) +'.csv'
features = 'features.csv'
statistics = 'data_statistics.xlsx'

def file(url):
    return str(url+'.csv')
