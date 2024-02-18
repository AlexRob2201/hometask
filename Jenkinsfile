pipeline {
  agent any
  stages {
      stage("Stage 1") {
          steps {
              git branch: 'main',
              credentialsId: 'my-private-key',
              url: 'https://github.com/AlexRob2201/hometask.git'
              script {
            //   properties([
            //     parameters([
            //         choice(
            //                 choices: ['corm', 'igrashka', 'water'], 
            //                     name: 'PRODUCT'
            //                 ),
            //                 text(
            //                     defaultValue: '', 
            //                     name: 'PRICE'
            //                 )
            //     ])
            //   ])
              sh """
              #!/bin/bash
              #bash custom_test.sh ${params.PRODUCT} ${params.PRICE}
              docker-compose build
              mkdir -p coverage
              docker-compose up -d mysql
              docker-compose up app-coverage
              docker cp app-coverage:/workdir/htmlcov/index.html .
              cat index.html
              """
              }
              //publishHTML (target : [allowMissing: false,
              //alwaysLinkToLastBuild: true,
              //keepAll: true,
              //reportDir: './',
              //reportFiles: 'index.html',
              //reportName: 'My Reports',
              //reportTitles: 'The Report'])

          }
      }
  }
}
