# --------------------------------------------
# SCRIPT DE DESPLIEGUE EN KUBERNETES (GitLab CI)
# --------------------------------------------
deploy-prod:
  stage: deploy
  image: alpine/k8s:1.25.0
  script:
    - echo "$KUBE_CONFIG" > kubeconfig.yaml
    - kubectl apply -f k8s/
      --kubeconfig=kubeconfig.yaml
      --namespace=mechbot-prod
  only:
    - main
  variables:
    KUBE_CONFIG: $KUBERNETES_CONFIG_PROD
