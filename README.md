azure-sample-application
========================

This is a small sample application using `flask` and deployed in azure
functions.

To deploy, follow this [tutorial].

To test, you can visit both `/` and `/MyFunction` endpoints to verify that it
is working.

The magic sauce that enables this is two parts:

1. extensions.http.routePrefix in host.json (removes the needed `/api`)
2. bindings[0].route in MyFunction/function.json (respond to all routes, not
   just /MyFunction)

[tutorial]: https://docs.microsoft.com/en-us/azure/developer/python/tutorial-vs-code-serverless-python-05
