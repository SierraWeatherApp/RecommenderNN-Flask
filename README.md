
## Contents

- [Backend service](app) - a Flask service with a `/ping` and a `/rec` endpoint, Rec expects 11 parameters, examples can be found under cypress tests.
- [E2E test suites](cypress/integration) - a backend and a frontend Cypress test suites. Extend with your tests.
- [Pipeline](.github/workflows/tests.yml) - a test Runner that executes the Cypress tests on push to a branch other than `master`/`main`.

## Tech Stack

### Backend

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)

### Misc

- Cypress
- GitHub Actions

## Getting started

Alternative route: The app contains a dockerfile, If you dont want to use docker you can use:

1. Make sure [`python3`](https://www.python.org/downloads/) and [`pip3`](https://pip.pypa.io/en/stable/installing/) are installed on your local env.

2. Make sure npm & node are configured on your local env. You can download those distributions for your platform [here](https://nodejs.org/en/download/)

3. Build your app.

```bash
npm install
npm run build
```

4. Start your app.

```bash
npm install
npm run start
```

5. Run the Cypress tests.

```bash
npm run test # run project tests under `cypress/integration`
```

---

Template by [DevSkills](https://devskills.co)
