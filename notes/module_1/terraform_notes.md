# Module 1: Terraform, Infrastructure as Code (IaC)

Terraform is an open-source Infrastructure as Code (IaC) tool developed by HashiCorp. It simplifies the process of provisioning and managing infrastructure by allowing users to define infrastructure resources in a declarative configuration language.

## Key Concepts:

### 1. Declarative Configuration
Terraform uses a declarative syntax to describe the desired state of infrastructure. Users define resources and their configurations, and Terraform ensures the actual infrastructure aligns with this desired state.

### 2. Providers
Terraform supports various cloud providers (e.g., AWS, Azure, Google Cloud) and other infrastructure platforms. Providers define a set of resources that can be managed through Terraform.

### 3. State Management
Terraform maintains a state file that records the current state of the infrastructure. This helps Terraform understand changes and track relationships between resources.

### 4. Execution Plans
Before applying changes, Terraform generates an execution plan outlining the actions it will take to achieve the desired state. Users can review and approve these changes.

### 5. Immutable Infrastructure
Terraform promotes the concept of immutable infrastructure, creating new resources rather than modifying existing ones. This reduces configuration drift and ensures consistency.

## Workflow:

1. **Configuration:** Write Terraform configuration files (in HashiCorp Configuration Language - HCL) describing the desired infrastructure.

2. **Initialization:** Run `terraform init` to initialize the working directory and download necessary provider plugins.

3. **Planning:** Run `terraform plan` to create an execution plan, showing changes Terraform will make.

4. **Application:** Run `terraform apply` to apply changes and create/update infrastructure.

5. **Destroy:** Run `terraform destroy` to decommission and destroy resources.

Terraform simplifies infrastructure management, provides version control for infrastructure code, and enhances collaboration among development and operations teams. It is widely used for building scalable and reproducible infrastructure in cloud and hybrid cloud environments.

## Additional Information

It is important to obtain the .json credentials file in order to create resources on the desired cloud provider. This allows Terraform to leverage the services mentioned in the main.tf file.

``` bash
# Example for Google Cloud Platform

export GOOGLE_CREDENTIALS='path/to/json/credentials/file'
```
