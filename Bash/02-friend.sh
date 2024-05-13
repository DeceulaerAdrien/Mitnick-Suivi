#!/usr/bin/env sh

jokes_file="jokes.txt"

tell_joke() {
    joke=$(shuf -n 1 "$jokes_file")
    echo "$joke"
}

tell_time() {
    current_time=$(date +"%H:%M:%S")
    echo "Current time is $current_time"
}

calculate() {
    result=$(echo "$1" | bc)
    echo "$result"
}

interpret_input() {
    case $1 in

    "tell a joke")
        tell_joke
        ;;

    "what time is it")
        tell_time
        ;;

    "calculate"*)
        calculate "$(echo "$1" | cut -c11-)"
        ;;

    *)
        echo "Sorry, I don't understand that command."
        ;;

    esac
}

interactive_mode() {
    while true; do
        echo "You: \c"
        read -r input
        interpret_input "$input"
    done
}

non_interactive_mode() {
    interpret_input "$1"
}

if [ $# -eq 0 ]; then
    interactive_mode
else
    non_interactive_mode "$1"
fi
