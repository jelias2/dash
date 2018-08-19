#!/usr/bin/env groovy
node('master') {

      stage ('Clone') {
      	checkout scm

      }

      withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'awscreds']]) {

        stage('Build and Push new image to ECR'){
              sh '$(aws ecr get-login --no-include-email --region us-west-2)'
              sh 'docker build -t dash .'
              sh 'docker tag dash:latest 772813348682.dkr.ecr.us-west-2.amazonaws.com/dash:latest'
              sh 'docker push 772813348682.dkr.ecr.us-west-2.amazonaws.com/dash:latest'

        }
         stage('Create Cluster'){
              sh 'aws ecs create-cluster --region us-west-2 --cluster-name dash-cluster'
          }

          stage('Create service'){
              sh """aws ecs create-service --cluster dash-cluster \
                    --region us-west-2 \
                    --service-name dash-service \
                    --task-definition dash_task_def:1 \
                    --desired-count 1 \
                    --launch-type "FARGATE" \
                    --network-configuration awsvpcConfiguration="{subnets=[subnet-d764cb9e],securityGroups=[sg-b3efdfcb],assignPublicIp="ENABLED"}" """

          }
      }
}
