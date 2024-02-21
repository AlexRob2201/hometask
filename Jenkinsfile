pipeline {
  agent any
  stages {
      stage("Build and test") {
          steps {
              sh """
              #!/bin/bash
              sudo docker run -ti -p 3000:80 --rm node-app test
              """
              }
          }
      }
  }
}