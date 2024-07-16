from kubernetes import client, config
import yaml

# Load kubeconfig
config.load_kube_config()

# Define the CustomObjectsApi client
custom_objects_api = client.CustomObjectsApi()

# Namespace where your pipelines are located
namespace = 'your-namespace'

# Retrieve all Tekton pipelines in the specified namespace
pipelines = custom_objects_api.list_namespaced_custom_object(
    group="tekton.dev",
    version="v1beta1",
    namespace=namespace,
    plural="pipelines"
)

# Print the pipelines in YAML format
print(yaml.dump(pipelines, default_flow_style=False))
