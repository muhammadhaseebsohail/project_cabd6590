Here is a comprehensive unit test for the DeploymentProcessConfig component using Jest and React Testing Library.

```jsx
import React from 'react';
import { render, cleanup } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import DeploymentProcessConfig from './DeploymentProcessConfig';

afterEach(cleanup);

describe('DeploymentProcessConfig component', () => {
  it('renders without crashing', () => {
    const { getByText } = render(<DeploymentProcessConfig task="Test Task" requirements={['Requirement 1', 'Requirement 2']} />);
    expect(getByText('Test Task')).toBeInTheDocument();
  });

  it('displays the correct task and requirements', () => {
    const { getByText } = render(<DeploymentProcessConfig task="Test Task" requirements={['Requirement 1', 'Requirement 2']} />);
    expect(getByText('Test Task')).toBeInTheDocument();
    expect(getByText('Requirement 1')).toBeInTheDocument();
    expect(getByText('Requirement 2')).toBeInTheDocument();
  });

  it('throws an error when no props are provided', () => {
    console.error = jest.fn(); // to hide the prop-types console.error in jest output
    expect(() => render(<DeploymentProcessConfig />)).toThrow();
  });

  it('throws an error when incorrect props types are provided', () => {
    console.error = jest.fn(); // to hide the prop-types console.error in jest output
    expect(() => render(<DeploymentProcessConfig task={123} requirements="not an array" />)).toThrow();
  });
});
```

In this test:

1. We first import the necessary libraries and the component we want to test.
2. We use `afterEach(cleanup)` to ensure that our tests do not affect each other.
3. We then describe a suite of tests for the `DeploymentProcessConfig` component.
4. The first test checks that the component renders without crashing when the correct props are provided.
5. The second test ensures that the component displays the correct task and requirements.
6. The third test checks that an error is thrown when no props are provided.
7. The last test checks that an error is thrown when the wrong types of props are provided. 

Please note that you should replace `'./DeploymentProcessConfig'` with the actual path to your `DeploymentProcessConfig` component.