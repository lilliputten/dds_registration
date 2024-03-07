#!/bin/sh
# @desc Config variables (common version -- stored in repository)
# @changed 2024.02.21, 16:52

# NOTE: May be overrided by `config-local.sh`
# NOTE: Don't forget to update rules in `public-publish/.htaccess` and `public-publish/robots.txt` files if you changed branch from production to demo.

# NOTE: It's possible to incorporate current branch (`DIST_BRANCH`) into the build tag?
DIST_BRANCH="publish" # Production build -> html-app-build

# Use the repo from `.git/config`
DIST_REPO="git@github.com:lilliputten/dds-invoicing-app.git"
SRC_TAG_PREFIX="v" # "v" for default tags like "v.X.Y.Z"

PUBLISH_FOLDER="client.build" # "$DIST_BRANCH"
PUBLISH_TAG_ID="client.build" # "$DIST_BRANCH"

# Timezone for timestamps (GMT, Europe/Moscow, Asia/Bangkok, etc)
# NOTE: See duplications in 'config.js'
TIMEZONE="Asia/Bangkok"
