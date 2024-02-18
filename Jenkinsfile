pipeline {
  agent {
      node {
          label 'ht28' 
        }
      dockerfile true
  }
  stages {
      stage("Stage 1") {
          steps {
              script {
              sh """
              #!/bin/bash
              echo "Hello"
              """
              }
          }
      }
  }
}
