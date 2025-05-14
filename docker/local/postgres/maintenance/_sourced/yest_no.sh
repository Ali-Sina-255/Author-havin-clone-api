#!/usr/bin/env bash

yes_no(){
    # Description: Prompt for confirmation. ${1} is the confirmation message.
    local arg1="${1}"
    local response
    read -r -p "${arg1} (y/[n])? " response
    
    if [[ "${response}" =~ ^[Yy]$ ]]; then
        exit 0  # User confirmed with 'y' or 'Y'
    else
        exit 1  # User confirmed with 'n' or any other response
    fi
}
