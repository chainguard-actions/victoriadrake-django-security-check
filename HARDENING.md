<!-- markdownlint-disable -->

# Hardening Report: victoriadrake--django-security-check/v1.1.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **victoriadrake--django-security-check/v1.1.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (b) violation: entrypoint.sh uses multiple unquoted shell variable expansions of workflow-controlled (untrusted) environment variables. The variables MANAGE_PATH and REQS are constructed from caller-supplied env vars APP_PATH and DEP_PATH (set by the calling workflow), and FAIL is derived from FAIL_LEVEL. These are used unquoted in shell commands such as `cd $REQS`, `cd $MANAGE_PATH`, `pip install -r $REQS`, and `--fail-level ${FAIL}`. An attacker controlling these env vars could inject shell metacharacters (e.g. spaces, semicolons, pipes) to execute arbitrary commands. All expansions of workflow-controllable variables must be double-quoted (e.g. `cd "$REQS"`, `cd "$MANAGE_PATH"`, `pip install -r "$REQS"`, `--fail-level "${FAIL}"`).

Offending lines:
- Line 9:  `echo -e "Path to manage.py set as: " $MANAGE_PATH`
- Line 10: `echo -e "Requirements path set as: " $REQS`
- Line 13: `cd $REQS`
- Line 14: `cd $MANAGE_PATH && ... --fail-level ${FAIL}`
- Line 17: `pip install -r $REQS`
- Line 18: `cd $MANAGE_PATH && ... --fail-level ${FAIL}`
- Line 22: `cd $MANAGE_PATH && ... --fail-level ${FAIL}`

Locations:

- `entrypoint.sh:9`
- `entrypoint.sh:10`
- `entrypoint.sh:13`
- `entrypoint.sh:14`
- `entrypoint.sh:17`
- `entrypoint.sh:18`
- `entrypoint.sh:22`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed all unquoted shell variable expansions in hardened/action/entrypoint.sh. Added double quotes around all expansions of workflow-controlled variables: $MANAGE_PATH (derived from APP_PATH), $REQS (derived from DEP_PATH), and ${FAIL} (derived from FAIL_LEVEL). This prevents shell metacharacter injection attacks where an attacker controlling these environment variables could inject arbitrary shell commands via spaces, semicolons, pipes, or other metacharacters.

