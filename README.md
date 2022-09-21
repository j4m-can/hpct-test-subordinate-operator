# hpct-test-subordinate-operator

## Description

The subordinate operator is used to test and work with a `NodeCharm`-based
operator.

## Usage

To deploy:

```
juju deploy ./hpct-test-subordinate_ubuntu-22.04-amd64.charm
```

See hpct-test-node-operator for more.

## Relations

A "ready" relation is used where subordinate requires and the node
provides.

The "ready" relation uses the "ReadyUnitSuperInterface" which is available
in the default interface registry under "relation-subordinate-ready".

## Contributing

Please see the [Juju SDK docs](https://juju.is/docs/sdk) for guidelines
on enhancements to this charm following best practice guidelines, and
`CONTRIBUTING.md` for developer guidance.
