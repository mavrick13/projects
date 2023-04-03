pipeline {
  agent any
  stages {
    stage('checkout code ') {
      steps {
        git(url: 'https://github.com/mavrick13/projects.git', branch: 'master', poll: true, credentialsId: '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')
      }
    }

    stage('docker') {
      steps {
        dockerNode(image: 'ubuntu')
      }
    }

  }
}