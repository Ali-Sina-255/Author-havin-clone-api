#!/usr/bin/env bash

countdown() {
    declare desc='A simple countdown'
    local seconds="${1}"

    local end_time=$(( $(date +%s) + seconds ))

    while [ "$end_time" -ge "$(date +%s)" ]; do
        local remaining_time=$(( end_time - $(date +%s) ))
        local hrs=$(( remaining_time / 3600 ))
        local mins=$(( (remaining_time % 3600) / 60 ))
        local secs=$(( remaining_time % 60 ))

        printf "\r%02d:%02d:%02d" "$hrs" "$mins" "$secs"
        sleep 0.1
    done

    echo -e "\nCountdown finished!"
}

# Example usage
countdown 10
