pipeline {
  agent any
  stages {
      stage("Stage 1") {
          steps {
              script {
              sh """
              #!/bin/bash
              ls -la ./
              """
              }
          }
      }
      stage("Stage 1") {
          steps {
              script {
              sh """
              #!/bin/bash
              echo "some text"
              exit 1
              """
              }
          }
      }
  }
}
