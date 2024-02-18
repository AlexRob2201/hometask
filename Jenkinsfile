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
              echo "hello world"
              """
              }
          }
      }
  }
}
