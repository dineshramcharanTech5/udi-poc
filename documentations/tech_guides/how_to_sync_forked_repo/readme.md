# Steps to sync a forked repo with the original

#### Set the original repository as the upstream

1. First list the configured remote repository of your forked repo
``` 
$ git remote -v
> origin  https://github.com/ICTASL/udi-poc-mosip-config.git (fetch)
> origin  https://github.com/ICTASL/udi-poc-mosip-config.git (push)
```

you will get an output as above.

2. Configure the original repository as the upstream using below command
``` 
git remote add upstream https://github.com/mosip/mosip-config.git
``` 
3. Verify if the upstream is set correctly
```
$ git remote -v
> origin  https://github.com/ICTASL/udi-poc-mosip-config.git (fetch)
> origin  https://github.com/ICTASL/udi-poc-mosip-config.git (push)
> upstream        https://github.com/mosip/mosip-config.git (fetch)
> upstream        https://github.com/mosip/mosip-config.git (push)
```
#### Syncing the fork

4. Fetch the new branches and changes from the upstream repository.
```
git fetch upstream
```

5. Checkout to the default branch
```
git checkout master
```

6. Merge the changes from the upstream default branch
```
git merge upstream/master
```

7. Checkout to the branch that you fetched from the upstream and push it to the remote.
```
git checkout 1.1.5
git push origin
```

8. The branch will be visible in the remote repository.
