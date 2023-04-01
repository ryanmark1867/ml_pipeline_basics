
project_id = 'first-project-ml-tabular'
region = 'us-central1'
dataset_id = '2901415472631119872'
dataset_path = 'projects/'+project_id+'/locations/'+region+'/datasets/'+dataset_id
print("dataset_path is: ",dataset_path)
ds = aiplatform.TabularDataset(dataset_path)
#ds = aiplatform.TabularDataset( 'projects/my-project/locations/us-central1/datasets/12345')