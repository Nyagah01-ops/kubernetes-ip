Explanation of Objectives
Objective 1: Scalability
To achieve scalability, I used a Kubernetes Deployment to manage the rollout of new versions of the application. This allows me to easily scale the application up or down to meet changing traffic demands.

Objective 2: High Availability
To achieve high availability, I used a Kubernetes Service to expose the application to the internet. This allows me to route traffic to multiple pods, ensuring that the application remains available even if one pod fails.

Objective 3: Persistent Storage
To achieve persistent storage, I used a Kubernetes Persistent Volume to persist data even if the pods are restarted or deleted. This ensures that data is not lost in the event of a pod failure.

Objective 4: Exposing Pods
To expose the pods to the internet, I used a Kubernetes Service with a LoadBalancer. This allows me to route traffic to the pods using a single IP address.

Objective 5: Git Workflow
To manage changes to the project, I used a Git workflow that involves creating a new branch for each feature or bug fix, committing changes to the branch, pushing the branch to the remote repository, creating a pull request to merge the branch into the main branch, and reviewing and merging the pull request.

