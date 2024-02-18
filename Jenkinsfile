pipeline {
  agent {
      node {
          label 'ht28' 
        }
  }
  stages {
      stage("Stage 1") {
          steps {
              script {
              sh """
              #!/bin/bash
              docker compose build
              docker compose up
              """
              }
          }
      }
  }
}
