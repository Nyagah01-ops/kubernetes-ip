Kubernetes Independent Project
This repository contains the code and configuration files for my Independent Project, which demonstrates a scalable and highly available web application deployed on a Kubernetes cluster.

Getting Started
To get started with the project, follow these steps:

Clone the repository: git clone https://github.com/Nyagah01-ops/kubernetes-ip-week5.git
Build the Docker image: docker build -t /Nyagah01-ops/my-app-image .
Push the Docker image to Docker Hub: docker push [your-username]/my-app-image
Apply the Kubernetes manifests: kubectl apply -f deployment.yaml
Expose the application to the internet: kubectl apply -f service.yaml
Live URL
The live URL for the application is: http://[insert-ip-address]:[insert-port]

Contributing
Contributions are welcome! Please submit a pull request with your changes and a brief description of what you've added.

License
This project is licensed under the MIT Licence

