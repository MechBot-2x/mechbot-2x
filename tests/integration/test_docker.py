integration-test:
  name: Integration Suite
    eeds: quality-assurance
   runs-on: ubuntu-22.04
    services:
      postgres:
        image: postgres:14
        env:
          POSTGRES_PASSWORD: test
        ports:
          - 5432:5432
        options: --health-cmd pg_isready --health-interval 10s --health-timeout 5s --health-retries 5

    steps:
      - uses: actions/checkout@v4
      - run: |
          docker-compose -f docker-compose.test.yml up -d
          pytest tests/integration/
