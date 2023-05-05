const apiUrl = `${Cypress.env("apiUrl")}`

describe('Backend Test Spec', () => {
  it('should call ping', () => {
    cy.request({
      failOnStatusCode: false,
      method: 'GET',
      url: `${apiUrl}/ping`,
    }).then((response) => {
      expect(response.status).to.eq(200)
    })
  })
})

describe('Hardcoded Recommendation route', () => {
  it('returns the expected recommendations', () => {
    cy.request({
      method: 'GET',
      url: `${apiUrl}/rec?inputs=27&inputs=16.1&inputs=52&inputs=17.9&inputs=0&inputs=0.0&inputs=1&inputs=0&inputs=1&inputs=5&inputs=3`
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body).to.be.an('array');
      response.body.forEach(item => {
        expect(item).to.be.a('string');
      });
    });
  });
});

describe('Recommendation route with encoding', () => {
  it('returns the expected recommendations', () => {
    const inputs = [12.5, 16.1, 52, 17.9, 50, 0.0, 1, 1, 1, 5, 3];
    const queryString = inputs.map(input => `inputs=${input}`).join('&');
    cy.request({
      method: 'GET',
      url: `${apiUrl}/rec?${queryString}`
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body).to.be.an('array');
      response.body.forEach(item => {
        expect(item).to.be.a('string');
      });
    });
  });
});

describe('Errors for Recommendation route', () => {
  it('returns an error if the inputs are not provided', () => {
    cy.request({
      method: 'GET',
      url: `${apiUrl}/rec`,
      failOnStatusCode: false
    }).then((response) => {
      expect(response.status).to.eq(400);
      expect(response.body).to.eq('Invalid input data: expected 11 inputs');
    });
  });
});

describe('Errors for Recommendation route on param amounts', () => {
  it('returns an error if the inputs are not in the correct format', () => {
    cy.request({
      method: 'GET',
      url: `${apiUrl}/rec`,
      qs: {
        inputs: '12.5,16.1,52,17.9,0,0.0,true,true,true,5,3'
      },
      failOnStatusCode: false
    }).then((response) => {
      expect(response.status).to.eq(400);
      expect(response.body).to.eq('Invalid input data: expected 11 inputs');
    });
  });
});


describe('Errors on input to Recommendation route', () => {
  it('returns an error if the inputs contain non-numeric values', () => {
    const inputs = [12.5, 16.1, 'fifty-two', 17.9, 0, 0.0, true, true, true, 5, 3];
    const queryString = inputs.map(input => `inputs=${input}`).join('&');
    cy.request({
      method: 'GET',
      url: `${apiUrl}/rec?${queryString}`,
      failOnStatusCode: false
    }).then((response) => {
      expect(response.status).to.eq(400);
      expect(response.body).to.eq('Invalid input data: expected 11 inputs');
    });
  });
});