# https://just.systems/man/en/

# REQUIRES

find := require("find")
rm := require("rm")
uv := require("uv")

# SETTINGS

set dotenv-load := true

# VARIABLES

PACKAGE := "gentwriter"
REPOSITORY := "gentwriter"
SOURCES := "gentwriter"
TESTS := "tests"
EVALS := "evals"

# DEFAULTS

# display help information
default:
    @just --list

# IMPORTS

import 'tasks/agent.just'
import 'tasks/check.just'
import 'tasks/clean.just'
import 'tasks/doc.just'
import 'tasks/format.just'
import 'tasks/install.just'
import 'tasks/package.just'
