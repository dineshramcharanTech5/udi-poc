# Setting up Terraform to new Setup

##### 1. Execute the following commands to set the variables
&nbsp;
```javascript
export AWS_ACCESS_KEY_ID=AKIA3KJAXHURODMUGFX7^C
export AWS_SECRET_ACCESS_KEY=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
export TF_LOG=DEBUG
export TF_LOG_PATH=tf.log
```
##### 2. Edit the variables.tf file and add ```digitalid-lgcc``` as sandbox-name.
&nbsp;
Note that the above name is for tag purpose and it will create everything based on this name at aws. If you need a new set of vpc you can change this to another and create.
&nbsp;
##### 3. Run the following commands one after the other.
&nbsp;
```javascript
terraform init
terraform plan
terraform apply
```
&nbsp;

```terraform init ``` needs to be executed only once as this will prepare from scratch.

```terraform plan``` command would plan and let you know how many are getting ready to be created and changed.

Please note that ``` terraform apply``` would execute and create instances in aws credential provided above.

Once the above steps are completed few files will be generated. Please make sure those files are not deleted as if you need to change something existing file system you need those. If you are going to destroy everything in aws and rebuild then delete those files and follow the steps from above.