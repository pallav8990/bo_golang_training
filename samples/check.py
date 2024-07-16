from kubernetes import client, config

# Load kubeconfig
config.load_kube_config()

# Define the Kubernetes API client
v1 = client.CustomObjectsApi()

# Specify the namespace and the environment variable to update
namespace = 'cp-build'
env_var_name = 'YOUR_ENV_VAR_NAME'
env_var_value = 'NEW_VALUE'

# Get all Pipeline CRDs in the namespace
pipelines = v1.list_namespaced_custom_object(
    group='tekton.dev', 
    version='v1beta1', 
    namespace=namespace, 
    plural='pipelines'
)

# Iterate over each pipeline to update the environment variable
for pipeline in pipelines['items']:
    # Get the name of the pipeline
    pipeline_name = pipeline['metadata']['name']
    
    # Iterate over all tasks in the pipeline
    for task in pipeline['spec']['tasks']:
        # Check if env section exists, otherwise create it
        if 'env' not in task['taskSpec']['containers'][0]:
            task['taskSpec']['containers'][0]['env'] = []
        
        # Find and update the environment variable or add if it does not exist
        env_updated = False
        for env_var in task['taskSpec']['containers'][0]['env']:
            if env_var['name'] == env_var_name:
                env_var['value'] = env_var_value
                env_updated = True
                break
        
        if not env_updated:
            task['taskSpec']['containers'][0]['env'].append({
                'name': env_var_name,
                'value': env_var_value
            })
    
    # Update the pipeline with the new environment variable
    v1.replace_namespaced_custom_object(
        group='tekton.dev',
        version='v1beta1',
        namespace=namespace,
        plural='pipelines',
        name=pipeline_name,
        body=pipeline
    )

print(f"Updated environment variable '{env_var_name}' for all pipeline definitions in the '{namespace}' namespace.")
