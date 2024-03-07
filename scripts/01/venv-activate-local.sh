#!/bin/sh
# @changed 2022.02.07, 20:40

# if uname | grep -q "CYGWIN"; then
#   # NOTE: Must be called directly: otherwise initalizing venv for current execution only.
#   # Use `call .venv/Scripts/activate.bat`
#   cmd /C "utils\\venv-activate-local.cmd"
#   # cmd /C ".\\.venv\\Scripts\\activate.bat"
# else
  source "./.venv/Scripts/activate"
# fi
