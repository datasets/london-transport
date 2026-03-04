# Update Script Maintenance Report

Date: 2026-03-04

- Re-ran `scripts/london_public_transport_journeys.py` and refreshed:
  - `data/data/public-transport-journeys.csv`
  - `data/datapackage.json`
- Updated GitHub Actions automation at `.github/workflows/actions.yml`:
  - removed push/PR triggers, kept schedule + manual dispatch,
  - added explicit `permissions: contents: write`,
  - upgraded to `actions/checkout@v4` and `actions/setup-python@v5`,
  - simplified dependency/script steps for reliable CI execution.
