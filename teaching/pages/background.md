# Background

The starter exercise uses a deliberately small unicycle-style forward model so that the focus stays on the implementation and testing workflow.

For the example state derivative, the commanded forward speed is carried into the first component and the second component is preserved.
This gives you a compact target for practicing the complete edit, test, and verification loop.

## Suggested workflow

1. Read the function docstring and the public test together.
2. Identify the observable behavior required by the test.
3. Implement the smallest complete expression.
4. Run the targeted test.
5. Run the complete public and smoke test suite.

![A simple forward-motion diagram](assets/lab-diagram.svg)
